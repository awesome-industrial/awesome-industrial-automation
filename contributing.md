# Contribution Guidelines

Thank you for helping. This list stays useful only while every entry is something an automation engineer would
actually recommend, so please read this before opening a pull request.

## What belongs here

- Software, libraries, standards, datasets and learning resources for industrial automation: PLCs, fieldbuses and
  industrial protocols, SCADA and HMI, edge and gateways, historians, MES, digital twins, industrial AI.
- Open source projects that are maintained, documented and usable today.
- Commercial products sparingly, as reference points next to the open source options. Mark them with
  `commercial: true`.

## What does not

- Projects with no release, no documentation or no activity for years (unless they are finished and still widely
  used).
- Blog posts that are mainly advertising, link farms, paywalled content without a free part.
- Your own project, unless it stands on its merits next to the others. Say in the pull request that it is yours.

## The quick way

[Open a suggestion](https://github.com/awesome-industrial/awesome-industrial-automation/issues/new?template=suggest.yml):
fill in the name, link, one-line description and section. A bot turns it into a pull request and tells you if
something needs fixing. A maintainer reviews and merges it.

## How to add an entry by hand

1. Find the right file in [data/](data/) and the right section.
2. Add the entry:

   ```yaml
   - name: Project Name
     url: https://github.com/owner/project
     description: What it does, in one plain sentence.
   ```

   The description starts with a capital letter, ends with a period, stays under 160 characters, does not repeat
   the name and avoids marketing words.
3. Run `python3 scripts/build.py` to regenerate `readme.md`, and commit both files.
4. One entry per pull request, with a short note on why it belongs.

## Checks

`scripts/build.py --check` validates every entry and `scripts/check_links.py` checks the links. Both run on every
pull request; the link check also runs weekly and opens an issue when a link breaks. Every Thursday a bot opens an
issue with active projects on industrial topics that are not on the list yet, for review.

## Is your project on the list?

You can show it with this badge:

```markdown
[![Mentioned in Awesome Industrial Automation](https://awesome.re/mentioned-badge.svg)](https://github.com/awesome-industrial/awesome-industrial-automation)
```

By contributing you agree to release your contribution under [CC0](license).
