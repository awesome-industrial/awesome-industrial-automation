#!/usr/bin/env python3
"""Builds the website from data/*.yml into site/: a home page with every entry and a filter, one page per category
and one per section, plus sitemap.xml and robots.txt. Plain HTML and CSS, no build tools.

    python3 scripts/site.py   # SITE_URL overrides the address the pages are served from
"""
import datetime
import html
import json
import os
import pathlib
import shutil

from build import anchor, load

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
SITE = os.environ.get("SITE_URL", "https://awesome-industrial.github.io/awesome-industrial-automation").rstrip("/")
REPO = "https://github.com/awesome-industrial/awesome-industrial-automation"
SUGGEST = f"{REPO}/issues/new?template=suggest.yml"
NAME = "Awesome Industrial Automation"
e = html.escape

CSS = """
:root{--bg:#fbfbf9;--fg:#1d211f;--mute:#5d6661;--line:#dfe3e0;--card:#fff;--accent:#a63d30;--chip:#eef1ef}
@media (prefers-color-scheme:dark){:root{--bg:#141716;--fg:#e8ebe9;--mute:#9aa49f;--line:#2c322f;--card:#1b1f1d;--accent:#f2a091;--chip:#232826}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:2px}
.wrap{max-width:62rem;margin:0 auto;padding:0 1rem}
header{border-bottom:1px solid var(--line);padding:1.1rem 0}header .wrap{display:flex;gap:1rem;align-items:center;justify-content:space-between;flex-wrap:wrap}
.brand{font-weight:700;color:var(--fg);text-decoration:none}.cta{display:inline-block;padding:.45rem .9rem;border:1px solid var(--accent);border-radius:6px;text-decoration:none;font-weight:600}
h1{font-size:clamp(1.7rem,4vw,2.4rem);line-height:1.15;margin:2.2rem 0 .6rem}h2{margin:2.4rem 0 .4rem;font-size:1.45rem}h3{margin:1.8rem 0 .3rem;font-size:1.12rem}
.lead{color:var(--mute);max-width:46rem}.crumbs{font-size:.9rem;color:var(--mute);margin-top:1.4rem}
nav.toc{display:flex;flex-wrap:wrap;gap:.4rem;margin:1.2rem 0}nav.toc a{background:var(--chip);border-radius:99px;padding:.25rem .7rem;text-decoration:none;color:var(--fg);font-size:.92rem}
ul.items{list-style:none;padding:0;margin:.6rem 0;display:grid;gap:.5rem}
ul.items li{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:.7rem .9rem}
ul.items .n{font-weight:650}ul.items p{margin:.2rem 0 0;color:var(--mute);font-size:.95rem}
.tag{font-size:.75rem;border:1px solid var(--line);border-radius:4px;padding:0 .35rem;margin-left:.4rem;color:var(--mute)}
input[type=search]{width:100%;padding:.7rem .9rem;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);font-size:1rem;margin:1rem 0 .4rem}
footer{border-top:1px solid var(--line);margin-top:3.5rem;padding:1.6rem 0;color:var(--mute);font-size:.92rem}
"""

FILTER = """<script>
const q=document.getElementById('q');q&&q.addEventListener('input',()=>{const t=q.value.trim().toLowerCase();
document.querySelectorAll('ul.items li').forEach(li=>{li.hidden=t&&!li.textContent.toLowerCase().includes(t)});
document.querySelectorAll('section.s').forEach(s=>{s.hidden=t&&!s.querySelector('li:not([hidden])')})});
</script>"""


def items_html(items):
    out = ['<ul class="items">']
    for i in items:
        tag = '<span class="tag">Commercial</span>' if i.get("commercial") else ""
        out.append(f'<li><a class="n" href="{e(i["url"])}">{e(i["name"])}</a>{tag}<p>{e(i["description"])}</p></li>')
    out.append("</ul>")
    return "\n".join(out)


def page(path, title, description, body, crumbs=(), items=()):
    url = f"{SITE}/{path}"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "url": url,
          "description": description, "isPartOf": {"@type": "WebSite", "name": NAME, "url": f"{SITE}/"}}
    if items:
        ld["mainEntity"] = {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
            {"@type": "ListItem", "position": n, "name": i["name"], "url": i["url"]} for n, i in enumerate(items, 1)]}
    trail = " / ".join([f'<a href="{SITE}/">{NAME}</a>'] + [f'<a href="{SITE}/{p}">{e(t)}</a>' for t, p in crumbs])
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}"><meta property="og:type" content="website">
<style>{CSS}</style><script type="application/ld+json">{json.dumps(ld)}</script></head>
<body><header><div class="wrap"><a class="brand" href="{SITE}/">{NAME}</a>
<span><a href="{REPO}">GitHub</a> &nbsp; <a class="cta" href="{SUGGEST}">Suggest a resource</a></span></div></header>
<main class="wrap">{'<p class="crumbs">' + trail + '</p>' if crumbs else ''}{body}</main>
<footer><div class="wrap">A curated, community-maintained list. Entries are open source unless marked Commercial.
<a href="{REPO}/blob/main/contributing.md">Contribute</a> &middot; <a href="{REPO}">Source on GitHub</a> &middot; CC0.<br>
Maintained by <a href="https://proxus.io/">Proxus</a> and contributors.</div></footer>{FILTER}</body></html>
"""
    target = OUT / path / "index.html" if path else OUT / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding="utf-8")
    return url


def names(items, n=4):
    shown = [i["name"] for i in items[:n]]
    return ", ".join(shown) + (" and more" if len(items) > n else "")


def main():
    cats, count = load()
    if OUT.exists():
        shutil.rmtree(OUT)
    urls = []

    # Home: every entry, filterable.
    toc = "".join(f'<a href="{SITE}/{c["slug"]}/">{e(c["title"])}</a>' for c in cats)
    body = [f"<h1>{NAME}</h1><p class=\"lead\">Open source software, protocols, standards and learning resources for "
            "industrial automation: PLCs and fieldbuses, SCADA and HMI, edge and IIoT, historians, MES and industrial "
            f"AI. {count} curated entries.</p>",
            '<input id="q" type="search" placeholder="Filter, e.g. modbus, python, historian" aria-label="Filter the list">',
            f'<nav class="toc">{toc}</nav>']
    for c in cats:
        body.append(f'<section class="s"><h2 id="{anchor(c["title"])}"><a href="{SITE}/{c["slug"]}/">{e(c["title"])}</a></h2>')
        for s in c["sections"]:
            if s["title"] != c["title"]:
                body.append(f'<section class="s"><h3 id="{anchor(s["title"])}">{e(s["title"])}</h3>')
            body.append(items_html(s["items"]))
            if s["title"] != c["title"]:
                body.append("</section>")
        body.append("</section>")
    urls.append(page("", f"{NAME}: open source tools for PLC, SCADA, IIoT and Industry 4.0",
                     f"{count} curated open source tools and resources for industrial automation: Modbus and OPC UA "
                     "libraries, PLC programming, SCADA, edge gateways, historians, MES and industrial AI.", "\n".join(body)))

    for c in cats:
        every = [i for s in c["sections"] for i in s["items"]]
        body = [f"<h1>{e(c['title'])}</h1><p class=\"lead\">{e(c.get('description', ''))} {len(every)} curated entries.</p>"]
        multi = [s for s in c["sections"] if s["title"] != c["title"]]
        if multi:
            body.append('<nav class="toc">' + "".join(
                f'<a href="{SITE}/{c["slug"]}/{anchor(s["title"])}/">{e(s["title"])}</a>' for s in multi) + "</nav>")
        for s in c["sections"]:
            if s["title"] != c["title"]:
                body.append(f'<h2 id="{anchor(s["title"])}"><a href="{SITE}/{c["slug"]}/{anchor(s["title"])}/">{e(s["title"])}</a></h2>')
            body.append(items_html(s["items"]))
        urls.append(page(f"{c['slug']}/", f"{c['title']} for industrial automation | {NAME}",
                         f"{len(every)} curated {c['title'].lower()} resources: {names(every)}.", "\n".join(body),
                         items=every))
        for s in multi:
            slug = f"{c['slug']}/{anchor(s['title'])}/"
            body = (f"<h1>{e(s['title'])}</h1><p class=\"lead\">Open source {e(s['title'])} projects and resources for "
                    f"industrial automation, curated and checked weekly. {len(s['items'])} entries.</p>" + items_html(s["items"])
                    + f'<p>Missing something? <a href="{SUGGEST}">Suggest a resource</a>.</p>')
            urls.append(page(slug, f"{s['title']}: open source tools and resources | {NAME}",
                             f"{len(s['items'])} curated {s['title']} projects and resources: {names(s['items'])}.",
                             body, crumbs=[(c["title"], f"{c['slug']}/")], items=s["items"]))

    today = datetime.date.today().isoformat()
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
                                     + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"site/: {len(urls)} pages, {count} entries")


if __name__ == "__main__":
    main()
