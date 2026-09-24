#!/usr/bin/env python3
"""Publish design-direction prototypes to the vault Library copy.

    python3 prototypes/publish.py            # publish
    python3 prototypes/publish.py --check    # report drift, change nothing

Source of truth is prototypes/<name>/index.html in this repo. The vault copy
exists so the prototype is reachable from Watchtower Library on the phone; it
is build output, not a place to edit. Every published file carries a GENERATED
banner so any agent that opens one sees that before touching it.

Same contract as site/publish.py — see that file for the 2026-09-04 divergence
that made these scripts necessary.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
TOPICS = Path.home() / "Dev/brain/03-Resources/topics"

# prototype dir name -> published vault filename
PROTOTYPES = {
    "direction-c-hybrid": "smiles-by-design-direction-c.html",
    "bunq-hero": "bunq-dental-hero.html",
    "grok-build": "smiles-by-design-grok-build.html",
}

# Optional sidecar media folders copied next to the HTML so relative
# `media/` paths keep working from the Library (file:// and Watchtower).
MEDIA = {
    "bunq-hero": "bunq-hero-media",
    "grok-build": "grok-build-media",
}

BANNER = (
    "<!-- GENERATED FILE — DO NOT EDIT.\n"
    "     Source: ~/Dev/Projects/jaws-dental-practice/prototypes/{name}/index.html\n"
    "     Republish with: python3 prototypes/publish.py\n"
    "     Then refresh the Library: python3 ~/Dev/Hermes/scripts/topics_catalog.py\n"
    "     Edits made here are destroyed on the next publish. -->\n"
)

DOCTYPE = re.compile(r"\s*<!DOCTYPE[^>]*>\n?", re.I)


def render(src: Path, name: str) -> str:
    """Return source HTML with the GENERATED banner injected after the doctype.

    After the doctype, never before it: a comment ahead of the doctype is legal
    but risks quirks mode in older engines.
    """
    text = src.read_text(encoding="utf-8")
    m = DOCTYPE.match(text)
    if not m:
        raise SystemExit(f"{src}: no doctype found; refusing to publish")
    html = text[: m.end()] + BANNER.format(name=name) + text[m.end() :]
    media_name = MEDIA.get(name)
    if media_name:
        html = html.replace('src="media/', f'src="{media_name}/')
    return html


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit non-zero; change nothing")
    args = ap.parse_args()

    drift, published = [], []
    for name, out_name in PROTOTYPES.items():
        src = REPO / name / "index.html"
        if not src.exists():
            raise SystemExit(f"missing source: {src}")
        dest = TOPICS / out_name
        want = render(src, name)

        if args.check:
            have = dest.read_text(encoding="utf-8") if dest.exists() else None
            if have != want:
                drift.append(out_name if dest.exists() else f"{out_name} (missing)")
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(want, encoding="utf-8")
        published.append(f"{name}/index.html -> {out_name}")
        media_name = MEDIA.get(name)
        if media_name:
            media_src = src.parent / "media"
            media_dest = TOPICS / media_name
            if media_src.is_dir():
                if media_dest.exists():
                    shutil.rmtree(media_dest)
                shutil.copytree(media_src, media_dest)
                published.append(f"{name}/media/ -> {media_name}/")

    if args.check:
        if drift:
            print("DRIFT — vault copy differs from repo source:")
            for d in drift:
                print(f"  {d}")
            print("\nRun: python3 prototypes/publish.py")
            return 1
        print("clean — vault copy matches repo source")
        return 0

    for line in published:
        print(f"published {line}")
    print("\nNow refresh the Library:")
    print("  python3 ~/Dev/Hermes/scripts/topics_catalog.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
