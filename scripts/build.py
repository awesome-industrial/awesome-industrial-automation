#!/usr/bin/env python3
"""Builds readme.md from data/*.yml.

Every entry lives in a category file under data/; readme.md is generated and never edited by hand.

    python3 scripts/build.py          # write readme.md
    python3 scripts/build.py --check  # fail if readme.md is out of date or an entry breaks a rule
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README = ROOT / "readme.md"

ENTRY_KEYS = {"name", "url", "description", "commercial"}


def fail(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def anchor(title):
    """GitHub's heading anchor."""
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def check_entry(where, e, seen):
    if not isinstance(e, dict) or not {"name", "url", "description"} <= set(e):
        fail(f"{where}: an entry needs name, url and description: {e}")
    extra = set(e) - ENTRY_KEYS
    if extra:
        fail(f"{where} / {e['name']}: unknown keys {sorted(extra)}")
    url, desc = e["url"], e["description"]
    if not url.startswith("https://"):
        fail(f"{where} / {e['name']}: url must start with https://")
    key = url.rstrip("/").lower()
    if key in seen:
        fail(f"{where} / {e['name']}: duplicate of {seen[key]}")
    seen[key] = f"{where} / {e['name']}"
    if not desc[:1].isupper() or not desc.endswith("."):
        fail(f"{where} / {e['name']}: description must start with a capital letter and end with a period")
    if len(desc) > 160:
        fail(f"{where} / {e['name']}: description is longer than 160 characters")
    if re.search(r"\b(awesome|best|leading|world-class|revolutionary)\b", desc, re.I):
        fail(f"{where} / {e['name']}: description uses a marketing word")
    if desc.lower().startswith(e["name"].lower()):
        fail(f"{where} / {e['name']}: description repeats the name")


def load():
    cats, seen = [], {}
    for path in sorted(DATA.glob("*.yml")):
        c = yaml.safe_load(path.read_text(encoding="utf-8"))
        for k in ("title", "order", "sections"):
            if k not in c:
                fail(f"{path.name}: missing '{k}'")
        for s in c["sections"]:
            where = f"{path.name} / {s['title']}"
            for e in s.get("items", []):
                check_entry(where, e, seen)
            s["items"] = sorted(s.get("items", []), key=lambda e: e["name"].lower())
        cats.append(c)
    return sorted(cats, key=lambda c: c["order"]), len(seen)


def render(cats):
    head = (ROOT / "templates/head.md").read_text(encoding="utf-8").rstrip()
    foot = (ROOT / "templates/foot.md").read_text(encoding="utf-8").rstrip()
    out = [head, "", "## Contents", ""]
    for c in cats:
        out.append(f"- [{c['title']}](#{anchor(c['title'])})")
        for s in c["sections"]:
            if s["title"] != c["title"]:
                out.append(f"\t- [{s['title']}](#{anchor(s['title'])})")
    for c in cats:
        out += ["", f"## {c['title']}"]
        if c.get("description"):
            out += ["", f"_{c['description']}_"]
        for s in c["sections"]:
            if s["title"] != c["title"]:
                out += ["", f"### {s['title']}"]
            if s.get("description"):
                out += ["", f"_{s['description']}_"]
            out.append("")
            for e in s["items"]:
                mark = " `Commercial`" if e.get("commercial") else ""
                out.append(f"- [{e['name']}]({e['url']}){mark} - {e['description']}")
    out += ["", foot, ""]
    return "\n".join(out)


def main():
    cats, count = load()
    text = render(cats)
    if "--check" in sys.argv:
        if README.read_text(encoding="utf-8") != text:
            fail("readme.md is out of date; run python3 scripts/build.py")
        print(f"ok: {count} entries in {len(cats)} categories")
        return
    README.write_text(text, encoding="utf-8")
    print(f"readme.md: {count} entries in {len(cats)} categories")


if __name__ == "__main__":
    main()
