# Toof-less — Smiles by Design launch

Workstream map for Dr Julia Nguyen / Smiles by Design (Wheelers Hill VIC 3150).

| Role | Owner | This PR |
|---|---|---|
| **Incisor** | Reception / practice ops | Phone, hours, AHPRA number, fees, in-house vs referred — still TBD |
| **Canine** | Copy | `copy/` — AHPRA-safe treatment copy for the eight launch pages |
| **Premolar** | SEO | `seo/` — keyword pack, Semrush brief, IA/schema draft |
| **Molar** | Site | `site/` — eight HTML pages, CSS, icon sprite |
| **Klud** | Sequences | Follow-up sequences after these URLs exist (not in this PR) |
| **Plumb'oor** | GitHub infra | This repo, branch, PR |
| **Hermes** | Local review | Reviews PRs before merge |
| **Wilson** | Merge | Merges to `main` after Hermes sign-off |

Do not merge until Hermes has reviewed.

## Launch slugs

Melbourne titles. Wheelers Hill lives in NAP and schema `areaServed` only — not in H1 or slug.

| Path | Title pattern |
|---|---|---|
| `/implants` | Dental Implants Melbourne |
| `/all-on-4` | All-on-4 Dental Implants Melbourne |
| `/invisalign` | Invisalign Melbourne |
| `/veneers` | Porcelain & Composite Veneers Melbourne |
| `/cosmetic` | Cosmetic Dentistry Melbourne |
| `/whitening` | Professional Teeth Whitening Melbourne |
| `/emergency` | Emergency Dentist Melbourne |
| `/dental-implants-cost` | Dental Implants Cost Australia |

No kids, wisdom, hygienist, bulk-bill, or root-canal pages at launch.

## Placeholders (still TBD)

Do not invent values. Replace only when Incisor confirms:

- Phone number
- Opening hours (including weekend / emergency)
- AHPRA registration number
- Fees (guides only, after examination)
- In-house vs referred for implants, All-on-4, Invisalign, and any surgical placement
- Practice legal name vs trading name where they differ
- Street address (suburb/postcode Wheelers Hill VIC 3150 is known)

Copy and HTML currently use `[phone]`, `{{URL}}`, and similar tokens.

## AHPRA

- No testimonials (including Google quotes about clinical results)
- No “best”, leading, #1, world-class, luxury, guaranteed, pain-free as a promise
- No before/after galleries that imply a typical result
- No specialist titles unless registered; no unconfirmed kit or team
- Risks and recovery on every cosmetic or invasive page
- Suitability is “Julia will assess”, not “you are a candidate”
