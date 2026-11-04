#!/usr/bin/env python3
"""Checks every entry in data/*.yml: the link answers, and a GitHub repository is neither archived nor abandoned.

    GITHUB_TOKEN=... python3 scripts/check_links.py [data/file.yml ...]

Exits 1 when a link is broken or a repository is archived; repositories with no push for two years are reported as
stale but do not fail the run (a finished library can be quiet and still good).
"""
import concurrent.futures
import datetime
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKEN = os.environ.get("GITHUB_TOKEN", "")
UA = "Mozilla/5.0 (compatible; awesome-industrial link check)"
STALE = datetime.timedelta(days=730)
REPO = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)/?$")


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status, r.read()


def check(e):
    url = e["url"]
    m = REPO.match(url)
    try:
        if m:
            h = {"Accept": "application/vnd.github+json"}
            if TOKEN:
                h["Authorization"] = f"Bearer {TOKEN}"
            _, body = get(f"https://api.github.com/repos/{m[1]}/{m[2]}", h)
            r = json.loads(body)
            if r["html_url"].lower() != url.rstrip("/").lower():
                return "moved", f"now {r['html_url']}"
            if r["archived"]:
                return "archived", ""
            pushed = datetime.datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00"))
            if datetime.datetime.now(datetime.timezone.utc) - pushed > STALE:
                return "stale", f"last push {pushed:%Y-%m-%d}"
            return "ok", f"{r['stargazers_count']} stars"
        status, _ = get(url)
        return ("ok" if status < 400 else "broken"), str(status)
    except urllib.error.HTTPError as err:
        # Some sites refuse robots; 403/429 are reported, not failed.
        return ("blocked" if err.code in (403, 429) else "broken"), str(err.code)
    except Exception as err:  # noqa: BLE001 - any network failure is a finding
        return "broken", type(err).__name__


def main():
    files = [pathlib.Path(p) for p in sys.argv[1:]] or sorted((ROOT / "data").glob("*.yml"))
    entries = []
    for f in files:
        for s in yaml.safe_load(f.read_text(encoding="utf-8"))["sections"]:
            entries += [(f.name, e) for e in s.get("items", [])]
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        results = list(pool.map(lambda fe: (fe, check(fe[1])), entries))
    bad = 0
    for (fname, e), (state, info) in results:
        if state != "ok":
            print(f"{state:9} {fname} / {e['name']}: {e['url']} {info}")
            bad += state in ("broken", "archived", "moved")
    print(f"{len(entries)} links, {bad} failing")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
