# Handover: Smiles by Design / Toof-less → local CoS

**From:** Klud (Grok Bot chief of staff)  
**To:** Local CoS on the Mac Studio (Hermes)  
**Date:** 3 Sep 2026  
**Repo:** https://github.com/wils-co/jaws-dental-practice (private, `wils-co`)  
**Practice:** Smiles by Design — Dr Julia Nguyen — Wheelers Hill VIC 3150  

Wilson owns calls that stick. You execute the site on the Studio. Do **not** ping Grok Bot to build, PR, or drain usage. Klud sequences the Grok pod only if Wilson asks.

---

## 1. What you are taking over

A boutique cosmetic/reconstructive site, not a bulk-bill mill. Eight launch URLs already drafted as AHPRA-safe copy. Pour them into the **existing Studio shell**. Do not start a second stack. Do not mint a second repo. Ignore `wils-co/seo-primer`.

GitHub (`wils-co`) is the only shared bus. No Google Drive, no grok-inbox, no rclone, no GCS.

---

## 2. Roster (do not blur jobs)

| Name | Job | Does not |
|---|---|---|
| **Incisor** | Reception. Non-clinical: hours, parking, bookings. Test inbox `reception.dentalmail.test@gmail.com`. | Clinical advice, fees as diagnosis |
| **Canine** (label: Silver Tongue) | Original patient copy. Topics from other clinics, never scrape-and-republish. | SEO, HTML |
| **Premolar** | Keywords, slugs, schema, internal links. Semrush AU. | Long-form copy, site build |
| **Molar** | Assemble Canine copy + Premolar IA. One icon set. | Inventing clinical claims |
| **Klud** | Grok CoS. Sequences the pod when Wilson asks. | Building the live site |
| **Plumb'oor** | GitHub infra (token, permissions, hygiene). | Dental pages, merge of content |
| **You (local CoS)** | Studio checkout, preview, Julia’s 20% polish, merge, deploy. | Opening git for Julia |

Grok path if Wilson ever re-asks the cloud pod: Premolar locks slug/schema, then Canine writes, then Molar assembles. You review. Wilson merges. Plumb'oor is not a content hop.

---

## 3. Launch URLs (do not restart)

Polish what exists. Do not rewrite from scratch.

| Slug | H1 | Title tag | HTML on leftover branch? |
|---|---|---|---|
| `/implants` | Dental implants | Dental Implants Melbourne \| Smiles by Design | No — copy only |
| `/all-on-4` | All-on-4 dental implants | All-on-4 Dental Implants Melbourne \| Smiles by Design | No — copy only |
| `/invisalign` | Invisalign | Invisalign Melbourne \| Smiles by Design | No — copy only |
| `/veneers` | Porcelain and composite veneers | Porcelain & Composite Veneers Melbourne \| Smiles by Design | No — copy only |
| `/cosmetic` | Cosmetic dentistry | Cosmetic Dentistry Melbourne \| Smiles by Design | Yes |
| `/whitening` | Professional teeth whitening | Professional Teeth Whitening Melbourne \| Smiles by Design | Yes |
| `/emergency` | Emergency dentist | Emergency Dentist Melbourne \| Smiles by Design | Yes |
| `/dental-implants-cost` | Dental implants cost | Dental Implants Cost Australia \| Smiles by Design | No — copy only |

**Do not build:** bulk-bill, kids/CDBS, wisdom teeth, hygienist mill. No suburb-in-path slugs. No extra `/dental-implants-wheelers-hill`.

**Homepage (when you get to it):** Julia’s face, one phone, Book, demand doors (emergency, check-up, Invisalign, implants, veneers, whitening). `dentist wheelers hill` is NAP/GBP, not the product H1. wheelershilldental.com already owns that query.

**Wave 2 (not now):** one drive-time page each for Rowville, Glen Waverley, Mulgrave, Mount Waverley, linking **into** these eight. Do not clone 8×4.

---

## 4. Leftover GitHub branch (your call)

Branch: `toof-less/launch-pages`  
PR: **none** (stopped on purpose).  
Klud will not touch this branch.

**Keep it as a drop, or delete it and copy files locally.** On it today:

- `TOOF-LESS.md`
- `copy/` — all eight launch `.md` plus `00-ahpra-and-voice.md`
- `seo/LAUNCH-SEO-PACK.md`, `seo/ia-schema-draft.md`
- `site/pages/css/site.css`
- `site/components/icons/` (sprite + README)
- HTML: `cosmetic.html`, `whitening.html`, `emergency.html` only

**Missing on the branch:** HTML for implants, All-on-4, Invisalign, veneers, dental-implants-cost. `seo/semrush-keyword-brief.md` (numbers live in the pack; optional).

Assemble the five missing pages **locally from `copy/`**. Do not ask Grok to finish the dump.

Do not overwrite `BRIEF.md`, the spatial-planning PDF, or `practical-seo-guide.*` unless you mean to. BRIEF still says “JAWs Dental Practice” and mentions root canals — that is kickoff noise. Live name is **Smiles by Design**. Skip root canal as a launch page.

---

## 5. SEO / IA rules (Premolar pack)

Canonical: `seo/LAUNCH-SEO-PACK.md` and `seo/ia-schema-draft.md`.

- Titles use **Melbourne**. Wheelers Hill is NAP, schema `areaServed`, first paragraph — not H1, not slug.
- Emergency in header, footer, and homepage.
- Internal links: implants ↔ All-on-4 ↔ dental-implants-cost (triangle). Cosmetic hub → veneers, whitening, Invisalign. Invisalign crumb is Home → Invisalign (not nested under cosmetic).
- Schema: `Dentist` + `DentalClinic` on every page. Procedure pages get `MedicalProcedure` + `Service`. Cost page is Service + FAQPage, no MedicalProcedure. No Product, no AggregateRating, no dollar Offer on procedures.
- Do not title on the giant navigational heads (`invisalign` 27k, `teeth whitening` 22k DIY SERP). Those are secondaries.
- Beat Liberty on **dedicated service URLs**. Do not copy Atlas homepage bundling.

Reference sites for **layout/structure only**, never prose: dentalboutique.com.au, ebdg.com.au, libertydental.com.au.

---

## 6. AHPRA / voice (non-negotiable)

From `copy/00-ahpra-and-voice.md`:

**Never:** outcome testimonials (including Google quotes about results), “best” / leading / #1 / guaranteed / pain-free as a promise, before/after galleries, award walls, fake case counts, specialist titles Julia does not hold, in-house GA, CEREC, “15 dentists”, Product star ratings.

**Always:** risks and recovery on invasive/cosmetic pages; fees as a **guide**; “Julia will assess” not “you are a candidate”; honest in-house vs referred.

**Do not invent:** who places the implant, AHPRA number, phone, hours, booking product, or a house catchphrase. Do **not** lock “Your Teeth Have a Timeline” until Julia says it.

Still placeholders until Wilson/Julia supply them: phone, hours, AHPRA number, who places implants (Julia vs referred surgeon), guide fees, live booking.

---

## 7. Julia’s 20% (zero git friction)

Toof-less copy is ~80%. Julia supplies bedside manner on a phone preview.

- She never opens Git, terminal, or PR forms.
- Voice notes are welcome (WhatsApp/Telegram/voice memo). **You** transcribe and patch. Do not add Telegram as an inbox for Klud.
- Apply her notes on the draft branch, then Wilson merges.

---

## 8. Execute this (local)

1. Decide: keep `toof-less/launch-pages` as a drop, or delete it after copying files onto the Studio checkout.
2. Pour `copy/` + icons + CSS into the **existing shell** (whatever is already on the Studio). Do not start Astro vs HTML as a new project.
3. Build the five missing HTML pages from copy, same template as the three that already exist. Polish order: **implants and cost, then Invisalign and veneers, then the rest.**
4. Wire Premolar slugs, Melbourne titles, NAP/schema, implant triangle, cosmetic hub, Emergency in the header.
5. Leave TBD fields as obvious placeholders. Do not fake a phone number or AHPRA.
6. Preview for Julia. Ingest her 20%. Wilson merges to `main`. You deploy (Cloudflare Pages / Vercel / whatever the shell already uses).
7. Incisor / reception auto-reply is a **later** track. Not part of this site PR.

---

## 9. Do not

- Ask Grok Bot / Klud / Molar to open another PR or finish the HTML dump.
- Create `TASKS.md` theatre or “Toof-less take TASK-01”.
- Put working HTML in Drive.
- Scrape-and-republish competitor blogs.
- Ship kids, wisdom, hygienist, bulk-bill, or a suburb URL farm.
- Quote exact clinical prices as if they were a diagnosis.

---

## 10. Blockers that still need Wilson / Julia

- Phone, hours, AHPRA registration number  
- Who places implants / All-on-4 (in-house vs referred)  
- Guide fee ranges she will actually stand behind  
- Booking tool (Halaxy or other)  
- Julia photos for homepage  
- Confirm “Smiles by Design” is the locked trading name on the live domain  

When those land, patch placeholders. Do not block the rest of the assemble on them.
