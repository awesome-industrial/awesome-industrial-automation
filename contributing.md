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

## How to add an entry

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
pull request; the link check also runs weekly.

By contributing you agree to release your contribution under [CC0](license).
