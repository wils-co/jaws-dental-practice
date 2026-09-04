# Smiles by Design — jaws-dental-practice

Private repo for Dr Julia Nguyen's practice site (Wheelers Hill VIC 3150).

## Source of truth

**This repo owns everything that ships.** The Obsidian vault owns research
and context. Nothing is stored in both places — if it lives here, the vault
gets a link, not a copy.

| Artefact | Home |
| --- | --- |
| Site (HTML/CSS/JS) | `site/pages/` — **here** |
| Page copy, AHPRA + voice rules | `copy/` — **here** |
| Keyword pack, IA, schema | `seo/` — **here** |
| Build + publish scripts | `site/` — **here** |
| Project hub, status, why-decisions | `~/Dev/brain/01-Projects/jaws-dental-practice/BRIEF.md` |
| Commissioned reports, competitor audits, PDFs | `~/Dev/brain/03-Resources/topics/` |

## Publishing the phone preview

The vault copy at `03-Resources/topics/smiles-by-design/` is **generated
output**, read on the phone via Watchtower Library. Never edit it directly —
every file carries a GENERATED banner saying so.

```bash
python3 site/publish.py --check   # report drift, change nothing
python3 site/publish.py           # regenerate the vault copy
```

`--check` exits non-zero and names the files if someone has hand-edited the
published copy, so divergence is caught before it is overwritten.

## Working rules

1. **Edit `site/pages/`, never the vault copy.** One directory, one truth.
2. **One agent at a time on the site.** Two hands on two copies is what caused
   the 2026-09-04 divergence across all 15 files.
3. **Land work through this repo.** GitHub (`wils-co`) is the only shared bus —
   no Drive, no rclone, no inbox hops.
4. **Merge to `main` when a direction is settled.** Wilson's call. The Hermes
   review gate in `TOOF-LESS.md` came from the Grok pod's handover and is
   stood down while this is a repo of one — reinstate it when other people
   depend on `main`.
5. **AHPRA rules are non-negotiable** — `copy/00-ahpra-and-voice.md`.
   No testimonials, no before/after galleries, no "best"/"guaranteed"/
   "pain-free", no unregistered specialist titles.
6. **Do not invent placeholders.** Phone, hours, AHPRA number, fees and who
   places implants stay as tokens until Julia confirms them.

Field guide: `practical-seo-guide.html`. Workstream map and roles: `TOOF-LESS.md`.
