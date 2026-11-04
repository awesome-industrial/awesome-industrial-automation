#!/usr/bin/env python3
"""Finds active GitHub projects on industrial topics that are not on the list yet, as markdown for a weekly issue.

    GITHUB_TOKEN=... python3 scripts/discover.py > candidates.md

A maintainer reviews the candidates; nothing is added automatically. Repositories in data/skip.txt (one
owner/repo per line) are never suggested again.
"""
import datetime
import json
import os
import pathlib
import time
import urllib.parse
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPICS = [
    "modbus", "opc-ua", "opcua", "plc", "scada", "hmi", "iec61131-3", "industrial-automation", "iiot",
    "industrial-iot", "industry-4-0", "sparkplug", "unified-namespace", "mes", "ethercat", "profinet", "bacnet",
    "ethernet-ip", "s7", "digital-twin", "predictive-maintenance",
]
MIN_STARS = 50
ACTIVE_DAYS = 120
LIMIT = 30


def search(query):
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
        {"q": query, "sort": "stars", "order": "desc", "per_page": 30})
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "User-Agent": "awesome-industrial-discover",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["items"]


def known():
    urls = set()
    for path in (ROOT / "data").glob("*.yml"):
        for s in yaml.safe_load(path.read_text(encoding="utf-8"))["sections"]:
            urls |= {e["url"].rstrip("/").lower() for e in s.get("items", [])}
    skip = ROOT / "data/skip.txt"
    if skip.exists():
        urls |= {f"https://github.com/{l.strip().lower()}" for l in skip.read_text().splitlines()
                 if l.strip() and not l.startswith("#")}
    return urls


def main():
    since = (datetime.date.today() - datetime.timedelta(days=ACTIVE_DAYS)).isoformat()
    seen, found = known(), {}
    for topic in TOPICS:
        for r in search(f"topic:{topic} stars:>={MIN_STARS} pushed:>={since} archived:false fork:false"):
            url = r["html_url"].lower()
            if url not in seen and url not in found:
                found[url] = r | {"topic": topic}
        time.sleep(2.5)  # the search API allows 30 requests a minute
    best = sorted(found.values(), key=lambda r: r["stargazers_count"], reverse=True)[:LIMIT]
    print(f"Active projects on industrial topics (at least {MIN_STARS} stars, pushed in the last {ACTIVE_DAYS} "
          "days) that are not on the list. Add the good ones with a pull request or a suggestion issue; add the "
          "rest to `data/skip.txt` so they are not proposed again.\n")
    print("| Project | Stars | Topic | Description |\n|---|---:|---|---|")
    for r in best:
        desc = (r["description"] or "").replace("|", "\\|")[:140]
        print(f"| [{r['full_name']}]({r['html_url']}) | {r['stargazers_count']} | {r['topic']} | {desc} |")
    if not best:
        print("| _Nothing new this week._ | | | |")


if __name__ == "__main__":
    main()
