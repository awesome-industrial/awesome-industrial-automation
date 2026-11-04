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
        c["slug"] = path.stem
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


def suggest_form(cats):
    """The "Suggest a resource" issue form; its section list follows the data, and scripts/suggest.py reads it back."""
    places = [f"{c['title']} / {s['title']}" for c in cats for s in c["sections"]]
    form = {
        "name": "Suggest a resource",
        "description": "Propose a project, tool or resource. A bot turns the suggestion into a pull request.",
        "title": "Suggest: ",
        "labels": ["suggestion"],
        "body": [
            {"type": "markdown", "attributes": {"value": "Thanks! Please read the [contribution guidelines](https://github.com/awesome-industrial/awesome-industrial-automation/blob/main/contributing.md) first. One resource per issue."}},
            {"type": "input", "id": "name", "attributes": {"label": "Name", "placeholder": "pymodbus"}, "validations": {"required": True}},
            {"type": "input", "id": "url", "attributes": {"label": "Link", "placeholder": "https://github.com/owner/project"}, "validations": {"required": True}},
            {"type": "input", "id": "description", "attributes": {"label": "Description", "description": "One plain sentence: starts with a capital letter, ends with a period, under 160 characters, does not repeat the name, no marketing words."}, "validations": {"required": True}},
            {"type": "dropdown", "id": "section", "attributes": {"label": "Section", "options": places}, "validations": {"required": True}},
            {"type": "checkboxes", "id": "commercial", "attributes": {"label": "Commercial", "options": [{"label": "Commercial product (not open source)"}]}},
            {"type": "textarea", "id": "why", "attributes": {"label": "Why it belongs", "description": "Who uses it, and is it yours?"}},
        ],
    }
    return "# Generated by scripts/build.py from data/*.yml.\n" + yaml.safe_dump(form, sort_keys=False, allow_unicode=True, width=1000)


FORM = ROOT / ".github/ISSUE_TEMPLATE/suggest.yml"


def main():
    cats, count = load()
    outputs = {README: render(cats), FORM: suggest_form(cats)}
    if "--check" in sys.argv:
        for path, text in outputs.items():
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                fail(f"{path.relative_to(ROOT)} is out of date; run python3 scripts/build.py")
        print(f"ok: {count} entries in {len(cats)} categories")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"readme.md: {count} entries in {len(cats)} categories")


if __name__ == "__main__":
    main()
