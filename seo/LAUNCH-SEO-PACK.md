# Launch SEO pack — Dr Julia Nguyen, Wheelers Hill VIC 3150

**For:** Canine (copy) and Molar (build). Not patient-facing prose.  
**Owner:** Premolar. **Pull:** Semrush AU `phrase_these` 2 Sep 2026.  
**Canonical files:** this pack · `semrush-keyword-brief.md` (numbers) · `ia-schema-draft.md` (JSON-LD + full link graph).  
**Supersedes** the IA draft title pattern. Titles use the **Melbourne commercial layer**. Wheelers Hill lives in NAP, schema `areaServed`, first paragraph — not H1, not slug.

Practice: premium, not bulk-bill. Procedure-led. Skip: bulk-bill, kids, wisdom, hygienist. Later: injectables, suburb drive-time pages, blog.

---

## 1. Launch URLs (keyword map)

| Slug | Primary (vol / KD / intent) | H1 | Title tag |
|---|---|---|---|
| `/implants` | dental implants 8,100 / 34 / commercial | Dental implants | Dental Implants Melbourne \| {{PRACTICE_NAME}} |
| `/all-on-4` | all on 4 dental implants 2,900 / 18 / informational | All-on-4 dental implants | All-on-4 Dental Implants Melbourne \| {{PRACTICE_NAME}} |
| `/invisalign` | invisalign melbourne 2,400 / 16 / commercial | Invisalign | Invisalign Melbourne \| {{PRACTICE_NAME}} |
| `/veneers` | veneers melbourne 1,300 / 12 / commercial | Porcelain and composite veneers | Porcelain & Composite Veneers Melbourne \| {{PRACTICE_NAME}} |
| `/cosmetic` | cosmetic dentistry 4,400 / 50 / commercial | Cosmetic dentistry | Cosmetic Dentistry Melbourne \| {{PRACTICE_NAME}} |
| `/whitening` | teeth whitening melbourne 2,900 / 19 / commercial | Professional teeth whitening | Professional Teeth Whitening Melbourne \| {{PRACTICE_NAME}} |
| `/emergency` | emergency dentist 4,400 / 35 / commercial | Emergency dentist | Emergency Dentist Melbourne \| {{PRACTICE_NAME}} |
| `/dental-implants-cost` | dental implants cost 1,900 / **6** / informational | Dental implants cost | Dental Implants Cost Australia \| {{PRACTICE_NAME}} |
| `/` | dentist wheelers hill 590 / 26 — **schema/NAP only** | Practice + mix, not “Dentist Wheelers Hill” as the product | {{PRACTICE_NAME}} \| Dentist Wheelers Hill |

Do **not** title on: `invisalign` 27.1k (navigational), `veneers` 9.9k KD 47, `teeth whitening` 22.2k (DIY SERP). Those are secondaries. Cost questions stay **on the procedure URL** except implants, which get a dedicated money page.

**On-page capture (not extra URLs):** Invisalign cost 8,100; how much is invisalign 1,600; veneers cost 2,400; how much are dental implants 720; `can i use my super for dental implants` 260 KD 4. Exact `implants cost` is 20 — ignore Klud’s 720 as that phrase.

Local `procedure + wheelers hill` phrases (~930 combined) are national counts, KD ~6. Body/schema only. `dentist wheelers hill` is a homepage/GBP job; wheelershilldental.com already #1.

---

## 2. Internal links (required)

Header: **Emergency** top-level. Treatments: the six clinical URLs + implant cost. Footer: NAP Wheelers Hill VIC 3150 + service-area sentence (Rowville, Glen Waverley, Mulgrave, Mount Waverley) as **text**, not five suburb URLs.

```
HOME → implants, all-on-4, cost, invisalign, cosmetic, emergency, veneers, whitening
implants ↔ all-on-4 ↔ dental-implants-cost     (closed triangle)
cosmetic → veneers, whitening, invisalign        (hub; Invisalign not nested in crumbs)
veneers ↔ whitening ↔ cosmetic
invisalign crumb: Home → Invisalign
emergency: header + footer + homepage body
```

Anchors (never “learn more”): dental implants · All-on-4 · dental implant cost · Invisalign · veneers · cosmetic dentistry · teeth whitening · emergency dentist.

---

## 3. Schema (Molar)

One `@graph` per page. Full JSON-LD in `ia-schema-draft.md`.

- Every page: `Dentist` + `DentalClinic` `@id` `{{URL}}/#clinic`. `areaServed`: Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley, Melbourne VIC.
- Procedure pages: `MedicalProcedure` + `Service`. Exact names: Dental Implant · All-on-4 · Dental Veneer · Teeth Whitening · Invisalign · Emergency Dental · Cosmetic Dentistry.
- `/dental-implants-cost`: Service + FAQPage, **no** MedicalProcedure.
- BreadcrumbList on all except home. FAQPage only where Canine has answers.
- Skip: Speakable, Product, AggregateRating, dollar Offer on procedures.

---

## 4. Who to beat

| Rival | Domain | Pattern | Our counter |
|---|---|---|---|
| **Liberty** | libertydental.com.au | Dedicated service URLs. Invisalign WH #1, porcelain veneers WH #1, implants WH #3 | Copy the **shape** (one clean slug per cluster). Do not copy doubled veneers URLs or suburb×service |
| Atlas | atlassmilesdental.com.au | Premium WH terms on the **homepage** | Dedicated URLs, not a mega-home |
| wheelershilldental.com | owns `dentist wheelers hill` #1 on `/` | Leave that KPI. Homepage NAP only |
| Rowville Dentists / Waverley Gardens | steal WH service SERPs from outside | Match service URLs, not their suburb farm |
| Dentist on Waverley | WH harvest, **zero Invisalign KWs** | Open gap on `/invisalign` |
| Waverley Park | no implants/Invisalign WH traffic | Gap |
| Star Smiles | brand homepage + 1 paid KW | Ignore |

Paid auction otherwise empty.

---

## 5. Canine: FAQ capture (schema these once answered)

**Implants / cost:** How much are dental implants? (720) · How much do dental implants cost? (590) · Can I use my super for dental implants? (260 KD 4) · Are dental implants covered by health insurance? (210) · How much are dental implants in Australia? (210) · How long do dental implants last? (390)

**All-on-4:** How much is All-on-4? (390) · What is All-on-4? (390) · How much does All-on-4 cost in Australia? (260) · All-on-4 vs single implants / dentures

**Invisalign (cost stays on this URL):** How much does Invisalign cost? (1,600) · How much is Invisalign? (1,600) · How long does Invisalign take? (320) · Invisalign vs braces (260)

**Veneers:** How much are veneers? (880) · How much do veneers cost in Australia? (390) · Porcelain vs composite · How long do veneers last? (480). Filter brick-veneer SERPs.

**Whitening:** In-clinic only. How much does teeth whitening cost? (590). Skip DIY (how to whiten teeth 1,600 KD 55).

**Emergency:** Hours, Sunday, visit cost (PAA ≤20 vol — still write them). Phone + NAP above the fold.

**Cosmetic:** Hub language; KD 50 means this page wins on internal links, not the national head.

No outcome promises. Super/Medicare = process and eligibility, not approval.

---

## 6. Molar checklist

- [ ] Slugs exact: `/all-on-4` not `allon4`; no suburb in path
- [ ] Emergency in header, footer, homepage
- [ ] Implant triangle + cosmetic hub as §2
- [ ] JSON-LD per `ia-schema-draft.md`
- [ ] No launch routes for injectables, suburbs, blog, bulk-bill, kids, wisdom, hygienist

Wave 2 (not now): dentist Rowville 880, Glen Waverley 720, Mulgrave 590, Mount Waverley 590. One drive-time page each, linking **into** these eight URLs — do not clone 8×4.
