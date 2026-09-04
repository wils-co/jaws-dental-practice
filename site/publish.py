#!/usr/bin/env python3
"""Publish the site to the vault preview copy — the ONLY sanctioned way.

    python3 site/publish.py            # publish
    python3 site/publish.py --check    # report drift, change nothing

Source of truth is site/pages/ in this repo. The vault copy exists so the
site is readable on the phone via Watchtower Library; it is build output,
not a place to edit. Every published file carries a GENERATED banner so any
agent that opens one sees that before touching it.

Background: on 2026-09-04 the two copies diverged across all 15 files
because two agents edited different copies on the same day. This script and
the banner exist to make that impossible to repeat by accident.
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
SRC = REPO / "pages"
DEST = Path.home() / "Dev/brain/03-Resources/topics/smiles-by-design"

# Inserted immediately AFTER the doctype, never before it: a comment ahead of
# the doctype is legal but risks quirks mode in older engines, and there is no
# reason to gamble the whole layout on it.
BANNER = (
    "<!-- GENERATED FILE — DO NOT EDIT.\n"
    "     Source: ~/Dev/Projects/jaws-dental-practice/site/pages/{name}\n"
    "     Publish with: python3 site/publish.py\n"
    "     Edits made here are destroyed on the next publish. -->\n"
)


def banner_for(name: str) -> str:
    return BANNER.format(name=name)


def inject_banner(text: str, name: str) -> str:
    """Place the banner just after the doctype declaration."""
    low = text.lstrip()
    if low[:9].lower() == "<!doctype":
        end = text.find(">", text.lower().find("<!doctype"))
        if end != -1:
            return text[:end + 1] + "\n" + banner_for(name) + text[end + 1:].lstrip("\n")
    return banner_for(name) + text


def strip_banner(text: str) -> str:
    """Remove a previously injected banner so comparisons are like-for-like."""
    i = text.find("<!-- GENERATED FILE")
    if i != -1:
        end = text.find("-->", i)
        if end != -1:
            return (text[:i] + text[end + 3:].lstrip("\n")).replace("\n\n", "\n", 1)
    return text


def iter_files():
    yield from sorted(SRC.glob("*.html"))
    for sub in ("css", "js"):
        yield from sorted((SRC / sub).glob("*"))


def rel(p: Path) -> Path:
    return p.relative_to(SRC)


def publish(check: bool) -> int:
    if not SRC.is_dir():
        print(f"error: source not found: {SRC}", file=sys.stderr)
        return 2

    changed, unchanged, edited_downstream = [], [], []

    for src in iter_files():
        r = rel(src)
        dst = DEST / r
        text = src.read_text(encoding="utf-8")
        out = inject_banner(text, r.name) if src.suffix == ".html" else text

        if dst.exists():
            current = dst.read_text(encoding="utf-8")
            if current == out:
                unchanged.append(r)
                continue
            # Did someone hand-edit the published copy? Compare bodies.
            if strip_banner(current) != text:
                edited_downstream.append(r)
        changed.append(r)

        if not check:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(out, encoding="utf-8")

    # icon sprite rides along untouched (no banner: it is not HTML)
    sprite = REPO / "components/icons/sprite.svg"
    if sprite.exists() and not check:
        (DEST / "icons").mkdir(parents=True, exist_ok=True)
        if not (DEST / "icons/sprite.svg").exists() or not filecmp.cmp(
            sprite, DEST / "icons/sprite.svg", shallow=False
        ):
            shutil.copy2(sprite, DEST / "icons/sprite.svg")

    verb = "would update" if check else "published"
    print(f"{verb}: {len(changed)}   unchanged: {len(unchanged)}")
    for r in changed:
        print(f"  {verb[:9]:>9}  {r}")

    if edited_downstream:
        print(
            f"\nWARNING: {len(edited_downstream)} published file(s) had been "
            "edited directly in the vault:"
        )
        for r in edited_downstream:
            print(f"  {r}")
        print(
            "Those edits are NOT in the repo. If they were wanted, recover them "
            f"from the brain repo's history before publishing:\n"
            f"  git -C ~/Dev/brain log -p -- 03-Resources/topics/smiles-by-design/"
        )
        if check:
            return 1

    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="report what would change; write nothing")
    raise SystemExit(publish(ap.parse_args().check))
