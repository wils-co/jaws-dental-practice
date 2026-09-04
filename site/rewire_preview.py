#!/usr/bin/env python3
"""Unify chrome + relative links on the 14-page static site."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/Users/wilsco/Dev/brain/03-Resources/topics/smiles-by-design")

LINKS = [
    ('href="/dental-implants-cost"', 'href="dental-implants-cost.html"'),
    ('href="/treatment-risks"', 'href="treatment-risks.html"'),
    ('href="/new-patients"', 'href="new-patients.html"'),
    ('href="/implants"', 'href="implants.html"'),
    ('href="/all-on-4"', 'href="all-on-4.html"'),
    ('href="/invisalign"', 'href="invisalign.html"'),
    ('href="/cosmetic"', 'href="cosmetic.html"'),
    ('href="/veneers"', 'href="veneers.html"'),
    ('href="/whitening"', 'href="whitening.html"'),
    ('href="/emergency"', 'href="emergency.html"'),
    ('href="/contact"', 'href="contact.html"'),
    ('href="/about"', 'href="about.html"'),
    ('href="/fees"', 'href="fees.html"'),
    ('href="/"', 'href="index.html"'),
]

CURRENT = {
    "index.html": "index.html",
    "about.html": "about.html",
    "new-patients.html": "new-patients.html",
    "fees.html": "fees.html",
    "contact.html": "contact.html",
    "treatment-risks.html": "treatment-risks.html",
    "implants.html": "implants.html",
    "all-on-4.html": "all-on-4.html",
    "dental-implants-cost.html": "dental-implants-cost.html",
    "invisalign.html": "invisalign.html",
    "cosmetic.html": "cosmetic.html",
    "veneers.html": "veneers.html",
    "whitening.html": "whitening.html",
    "emergency.html": "emergency.html",
}


def mark(href: str, page: str) -> str:
    cls = ' aria-current="page"' if href == page else ""
    return cls


def header(page: str) -> str:
    book = "#book" if page == "contact.html" else "contact.html#book"
    home_cur = mark("index.html", page)
    em_cur = mark("emergency.html", page)
    np_cur = mark("new-patients.html", page)
    fees_cur = mark("fees.html", page)
    about_cur = mark("about.html", page)
    contact_cur = mark("contact.html", page)

    def t(href: str, label: str) -> str:
        cur = mark(href, page)
        return f'            <a href="{href}"{cur}>{label}</a>'

    return f'''<header class="site-header">
    <div class="site-header__inner wrap">
      <a class="wordmark" href="index.html"{home_cur}>Smiles by Design</a>
      <nav class="site-nav" aria-label="Primary">
        <details class="nav-treatments">
          <summary>Treatments</summary>
          <div class="nav-treatments__panel">
{t("implants.html", "Dental implants")}
{t("all-on-4.html", "All-on-4")}
{t("dental-implants-cost.html", "Implant cost")}
{t("invisalign.html", "Invisalign")}
{t("cosmetic.html", "Cosmetic dentistry")}
{t("veneers.html", "Veneers")}
{t("whitening.html", "Teeth whitening")}
          </div>
        </details>
        <a href="emergency.html"{em_cur}>Emergency</a>
        <a href="new-patients.html"{np_cur}>New patients</a>
        <a href="fees.html"{fees_cur}>Fees</a>
        <a href="about.html"{about_cur}>About</a>
        <a href="contact.html"{contact_cur}>Contact</a>
      </nav>
      <div class="header-cta">
        <a class="header-phone" href="tel:">Call [phone]</a>
        <a class="btn btn--small" href="{book}">Book</a>
      </div>
      <details class="nav-menu">
        <summary>Menu</summary>
        <div class="nav-menu__panel">
          <a class="header-phone" href="tel:">Call [phone]</a>
{t("emergency.html", "Emergency dentist")}
{t("implants.html", "Dental implants")}
{t("all-on-4.html", "All-on-4")}
{t("dental-implants-cost.html", "Implant cost")}
{t("invisalign.html", "Invisalign")}
{t("cosmetic.html", "Cosmetic dentistry")}
{t("veneers.html", "Veneers")}
{t("whitening.html", "Teeth whitening")}
{t("new-patients.html", "New patients")}
{t("fees.html", "Fees")}
{t("about.html", "About")}
{t("contact.html", "Contact")}
{t("treatment-risks.html", "Treatment risks")}
          <a class="btn btn--small" href="{book}" style="margin:0.5rem 0.7rem;">Book an assessment</a>
        </div>
      </details>
    </div>
  </header>'''


def footer(page: str) -> str:
    book = "#book" if page == "contact.html" else "contact.html#book"
    return f'''<footer class="site-footer">
    <div class="wrap site-footer__inner">
      <div>
        <p><strong>Smiles by Design</strong> · Dr Julia Nguyen</p>
        <p>Wheelers Hill VIC 3150</p>
        <p>Catchment: Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley.</p>
        <p><a href="emergency.html">Emergency dentist</a> · <a href="treatment-risks.html">Treatment risks</a> · <a href="contact.html">Contact</a> · <a href="fees.html">Fees</a></p>
      </div>
      <div class="footer-cta">
        <p><a href="implants.html">implants</a> · <a href="all-on-4.html">All-on-4</a> · <a href="dental-implants-cost.html">implant cost</a> · <a href="invisalign.html">Invisalign</a> · <a href="cosmetic.html">cosmetic</a> · <a href="veneers.html">veneers</a> · <a href="whitening.html">whitening</a></p>
        <p><a class="btn" href="{book}">Book an assessment</a> <a class="btn btn--ghost" href="tel:">Call [phone]</a></p>
      </div>
    </div>
  </footer>'''


def sticky(page: str) -> str:
    book = "#book" if page == "contact.html" else "contact.html#book"
    return f'''<aside class="mobile-sticky-bar" aria-label="Quick Actions">
    <a class="btn btn--ghost" href="tel:">Call [phone]</a>
    <a class="btn" href="{book}">Book</a>
  </aside>'''


def rewire(path: Path) -> None:
    page = path.name
    text = path.read_text()
    text, n1 = re.subn(
        r'<header class="site-header">.*?</header>',
        header(page),
        text,
        count=1,
        flags=re.S,
    )
    text, n2 = re.subn(
        r'<footer class="site-footer">.*?</footer>',
        footer(page),
        text,
        count=1,
        flags=re.S,
    )
    text, n3 = re.subn(
        r'<aside class="mobile-sticky-bar".*?</aside>',
        sticky(page),
        text,
        count=1,
        flags=re.S,
    )
    for src, dst in LINKS:
        text = text.replace(src, dst)
    if page != "contact.html":
        text = text.replace('href="#book"', 'href="contact.html#book"')
    path.write_text(text)
    print(f"{page:28} header={n1} footer={n2} sticky={n3}")


def main() -> None:
    files = sorted(ROOT.glob("*.html"))
    for f in files:
        rewire(f)


if __name__ == "__main__":
    main()
