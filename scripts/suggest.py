#!/usr/bin/env python3
"""Turns a "Suggest a resource" issue into an entry in data/*.yml.

The issue body (GitHub issue form markdown) comes in ISSUE_BODY. On success the entry is inserted at the end of its
section, readme.md is rebuilt and the entry's name is printed; on failure the reason is printed to stderr and the
script exits 1. The text is never executed or interpolated into a shell: it is parsed here and written as YAML.
"""
import json
import os
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def fields(body):
    """Issue form markdown: '### Label' followed by the answer."""
    out, label = {}, None
    for line in body.replace("\r\n", "\n").split("\n"):
        m = re.match(r"^### (.+)$", line)
        if m:
            label = m[1].strip()
            out[label] = []
        elif label:
            out[label].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def scalar(value):
    """A plain YAML scalar when it reads back unchanged, otherwise a JSON (= YAML) quoted string."""
    try:
        if yaml.safe_load(f"k: {value}") == {"k": value}:
            return value
    except yaml.YAMLError:
        pass
    return json.dumps(value, ensure_ascii=False)


def main():
    f = fields(os.environ.get("ISSUE_BODY", ""))
    name, url, desc = f.get("Name", ""), f.get("Link", ""), f.get("Description", "")
    place = f.get("Section", "")
    commercial = "- [x]" in f.get("Commercial", "").lower()
    if not name or not url or not desc or "/" not in place:
        fail("The form is missing the name, link, description or section.")
    if len(name) > 80 or "\n" in name or "\n" in desc or "\n" in url:
        fail("Name, link and description must each be a single line.")
    url = url.strip("<> ")
    if not re.match(r"^https://[^\s]+$", url):
        fail("The link must be a single https:// URL.")
    category, section = (p.strip() for p in place.split("/", 1))

    for path in sorted((ROOT / "data").glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data["title"] != category:
            continue
        lines = path.read_text(encoding="utf-8").split("\n")
        try:
            start = lines.index(f"  - title: {section}")
        except ValueError:
            fail(f"Section '{section}' was not found in {category}.")
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("  - title:")), len(lines))
        while end > start and not lines[end - 1].strip():
            end -= 1
        block = [f"      - name: {scalar(name)}", f"        url: {url}", f"        description: {scalar(desc)}"]
        if commercial:
            block.append("        commercial: true")
        lines[end:end] = block
        path.write_text("\n".join(lines), encoding="utf-8")
        built = subprocess.run([sys.executable, str(ROOT / "scripts/build.py")], capture_output=True, text=True)
        if built.returncode:
            fail(built.stderr.strip().removeprefix("error: "))
        print(name)
        return
    fail(f"Category '{category}' was not found.")


if __name__ == "__main__":
    main()
