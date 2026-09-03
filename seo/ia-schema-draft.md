# IA, internal links, schema — Dr Julia Nguyen, Wheelers Hill

**Audience:** Canine (patient copy) and Molar (build). This pack is IA, link graph, JSON-LD shapes, and on-page SEO specs. Not patient-facing prose.  
**Practice:** Premium private (not bulk-bill). One clinic, Wheelers Hill VIC 3150.  
**URL rule:** Procedure-led slugs. Local modifiers (Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley) live in schema, NAP, `areaServed`, title tags, and supporting copy — **not** in paths and **not** as suburb homepages at launch.  
**Placeholders for Molar:** `{{PRACTICE_NAME}}` · `{{URL}}` (origin, no trailing slash) · `{{PHONE}}` · `{{GEO}}` (GeoCoordinates object: `@type`, `latitude`, `longitude`). Street line is `{{STREET}}` if needed for NAP.  
**Volumes:** Do not invent or paste search volumes. Premolar merges Semrush later.  
**Competitive note (structure only):** Liberty = copy dedicated service URLs. Atlas = do not rely on bundling premium terms on the homepage. `wheelershilldental.com` already owns “dentist wheelers hill” — skip that as a year-one URL/KPI. Cost and super questions outrank suburb names; `/dental-implants-cost` is a first-class money page, not a blog.

---

## 1. Information architecture (launch)

Nine URLs. Header always exposes **Emergency** as a top-level item (not nested under Treatments). Treatments dropdown lists the six clinical URLs plus implant cost.

| URL | Template | One-line purpose |
|---|---|---|
| `/` | Home | Practice door: who we are, Wheelers Hill NAP, six clinical doors + emergency + implant-cost teaser. |
| `/implants` | Procedure (implants hub) | Own the implant conversation (single / multiple / vs full-arch). Hub for All-on-4 and cost. |
| `/all-on-4` | Procedure (implants spoke) | Full-arch / full-mouth rehab path. Not a homepage keyword dump. |
| `/invisalign` | Procedure (independent) | Aligners as its own product URL. Linked from home + cosmetic; not a cosmetic child in the URL tree. |
| `/veneers` | Procedure (cosmetic spoke) | Veneer procedure page. Parent internally is `/cosmetic`. |
| `/cosmetic` | Hub (cosmetic) | Category hub for veneers + whitening; also routes to Invisalign. Later: injectables mention only, no URL. |
| `/whitening` | Procedure (cosmetic spoke) | Whitening procedure page. Parent internally is `/cosmetic`. |
| `/emergency` | Procedure (acquisition) | Same-day / urgent dental. Fills chairs. Never buried in a treatments index. |
| `/dental-implants-cost` | Money page | Fee ranges, staging, super, Medicare-eligibility questions. First-class URL, not a blog post. |

### Chrome that may exist (Molar), not this SEO set

About, contact/book, policies, treatment-risks, new-patients, a general fees page if built. Those are site furniture. They must **not** steal the eight launch slugs or become extra procedure landings.

### What NOT to create at launch

- Suburb landings: `/dentist-wheelers-hill`, `/dentist-rowville`, `/dentist-glen-waverley`, `/dentist-mulgrave`, `/dentist-mount-waverley`, or any `/dentist-{suburb}/` farm.
- Suburb-in-slug procedure URLs (`/dental-implants-wheelers-hill`, etc.). Slugs stay as the table above.
- Skip locally: bulk-bill, kids / children’s dentist, wisdom teeth, hygienist / check-up-and-clean as ranking URLs.
- Injectables / anti-wrinkle / lip filler URLs (later offering).
- Blog, articles, reels, “smile gallery” as a nav destination.
- Standalone super URL, porcelain-vs-composite URL, smile-makeover URL — those intents sit on existing pages (cost, veneers, cosmetic).
- A thin `/services/` mega-index unless Molar needs it for nav; `/implants` and `/cosmetic` are the hubs.
- Product + AggregateRating / review-snippet schema on treatments.
- Speakable schema (skip).

---

## 2. Internal link graph

**Rules**

- Anchors are descriptive procedure phrases. Never “click here”, “learn more”, “read more” as the sole link text.
- One primary hub per cluster. Do not cross-link every page to every page.
- Emergency is in **header, footer, and homepage body**. Not only in a treatments dropdown.
- Cost ↔ implants ↔ All-on-4 is a closed triangle. Every one of those three links to the other two.
- Invisalign is relatively independent: inlinks from homepage + cosmetic (+ nav/footer). Optional vs-veneers on `/veneers` only.
- Cosmetic hub owns veneers and whitening. Implants hub owns All-on-4 and cost.

```
                    HEADER / FOOTER
                    Emergency (always)
                           |
    HOME ---------------------------------------------
     |        |         |          |         |        |
 implants  all-on-4  cost     invisalign  cosmetic  emergency
     |        |         |          |         |
     +--------+---------+          |      veneers
     (triangle)                    |      whitening
                                   |
                              (from cosmetic)
```

### Global chrome (every page)

| Location | Required outlinks | Suggested anchors |
|---|---|---|
| Header | `/emergency` (top-level) | Emergency dentist |
| Header Treatments ▾ | `/implants`, `/all-on-4`, `/dental-implants-cost`, `/invisalign`, `/cosmetic`, `/veneers`, `/whitening` | Dental implants · All-on-4 · Dental implant cost · Invisalign · Cosmetic dentistry · Veneers · Teeth whitening |
| Logo | `/` | `{{PRACTICE_NAME}}` |
| Footer NAP | `/` + `/emergency` + implant triangle + `/invisalign` + `/cosmetic` | Same descriptive anchors. Address text is Wheelers Hill VIC 3150, not a link farm of five suburbs. |
| Footer service area line | Plain text, not URLs | Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley |

### Per URL

#### `/` homepage

| | Spec |
|---|---|
| **Required inlinks** | Logo + Home in nav/footer on every page. |
| **Required outlinks** | All eight launch URLs. Emergency in the first screen of doors, not last in a long grid. Implant-cost teaser is a real link, not “see fees” buried in About. |
| **Suggested anchors** | Dental implants · All-on-4 · Dental implant cost · Invisalign · Cosmetic dentistry · Veneers · Teeth whitening · Emergency dentist |
| **Do not** | Bundle all premium terms into one homepage H1 and skip dedicated URLs (Atlas pattern). |

#### `/implants` — implants hub

| | Spec |
|---|---|
| **Required inlinks** | `/` (“dental implants”); `/all-on-4` (“single and multiple dental implants”); `/dental-implants-cost` (“dental implants”); `/cosmetic` optional (“implants as an alternative”); header + footer. |
| **Required outlinks** | `/all-on-4`; `/dental-implants-cost`. Optional: `/emergency` if covering trauma/tooth loss. |
| **Suggested out anchors** | All-on-4 full-arch implants · Dental implant cost |
| **Hub job** | Parent of All-on-4 and cost. Breadcrumb parent for both. |

#### `/all-on-4` — implants spoke

| | Spec |
|---|---|
| **Required inlinks** | `/` (“All-on-4”); `/implants` (“All-on-4”); `/dental-implants-cost` (“All-on-4 cost / full-arch fees”); header + footer. |
| **Required outlinks** | `/implants`; `/dental-implants-cost`. |
| **Suggested out anchors** | Dental implants (single and multiple) · All-on-4 and implant fees |

#### `/dental-implants-cost` — money page

| | Spec |
|---|---|
| **Required inlinks** | `/` (“dental implant cost”); `/implants` (“implant fees / what implants cost”); `/all-on-4` (“All-on-4 cost”); header Treatments. |
| **Required outlinks** | `/implants`; `/all-on-4`. No third-wave super/blog URL. Super and Medicare FAQs stay on this page. |
| **Suggested out anchors** | Dental implants · All-on-4 |
| **Do not** | Relocate this to `/blog/...` or `/fees#implants`. It is a first-class URL. |

#### `/cosmetic` — cosmetic hub

| | Spec |
|---|---|
| **Required inlinks** | `/` (“cosmetic dentistry”); `/veneers` (“cosmetic dentistry”); `/whitening` (“cosmetic dentistry”); `/invisalign` (“cosmetic dentistry” in a related block, not as parent crumb); header + footer. |
| **Required outlinks** | `/veneers`; `/whitening`; `/invisalign`. Optional: `/implants` as full-mouth alternative. |
| **Suggested out anchors** | Veneers · Teeth whitening · Invisalign |
| **Hub job** | Parent of veneers and whitening only. Invisalign is linked, not nested. |

#### `/veneers` — cosmetic spoke

| | Spec |
|---|---|
| **Required inlinks** | `/` (“veneers”); `/cosmetic` (“veneers”); `/whitening` (“veneers”); optional `/invisalign` (“veneers” in vs-alternatives). |
| **Required outlinks** | `/cosmetic`; `/whitening`. Optional: `/invisalign` if covering alignment vs veneers. |
| **Suggested out anchors** | Cosmetic dentistry · Teeth whitening · Invisalign |

#### `/whitening` — cosmetic spoke

| | Spec |
|---|---|
| **Required inlinks** | `/` (“teeth whitening”); `/cosmetic` (“teeth whitening”); `/veneers` (“teeth whitening”). |
| **Required outlinks** | `/cosmetic`; `/veneers`. |
| **Suggested out anchors** | Cosmetic dentistry · Veneers |
| **Do not** | Bid/copy Glen Waverley-only whitening landings. Geo stays Wheelers Hill in title/schema. |

#### `/invisalign` — independent procedure

| | Spec |
|---|---|
| **Required inlinks** | `/` (“Invisalign”); `/cosmetic` (“Invisalign”); header + footer. Optional from `/veneers` (vs). |
| **Required outlinks** | `/cosmetic`. Optional: `/veneers` in vs-alternatives. |
| **Suggested out anchors** | Cosmetic dentistry · Veneers |
| **Breadcrumb** | Home → Invisalign (not Home → Cosmetic → Invisalign). |

#### `/emergency`

| | Spec |
|---|---|
| **Required inlinks** | **Header** (all pages); **footer** (all pages); **homepage body**. Optional from `/implants` (tooth loss / trauma). |
| **Required outlinks** | `/implants` if covering lost teeth. Book/call is the primary action; do not bury this URL under Treatments only. |
| **Suggested out anchors** | Dental implants |
| **Do not** | Leave emergency as homepage-only (Atlas / several locals). Needs its own URL **and** chrome. |

### Anchor bank (reuse these; do not improvise vague CTAs)

| Target | Preferred anchors (pick one per placement) |
|---|---|
| `/implants` | dental implants · single and multiple dental implants |
| `/all-on-4` | All-on-4 · All-on-4 full-arch implants |
| `/dental-implants-cost` | dental implant cost · implant fees · how much dental implants cost |
| `/invisalign` | Invisalign |
| `/veneers` | veneers · dental veneers · porcelain veneers |
| `/cosmetic` | cosmetic dentistry |
| `/whitening` | teeth whitening |
| `/emergency` | emergency dentist · emergency dental |

---

## 3. Schema.org JSON-LD

### Implementation rules (Molar)

- One `<script type="application/ld+json">` per page, `@graph` array.
- `Dentist` + `DentalClinic` on **every** page via a shared clinic node `@id`: `{{URL}}/#clinic`. Do not emit a second, conflicting NAP.
- Procedure pages add `MedicalProcedure` **and** `Service`. Money page adds `Service` only (cost is not a procedure).
- `FAQPage` on every URL that lists the FAQ questions in §4 (all eight plus home if home ships FAQs; home may omit FAQPage if it has no FAQ block).
- `BreadcrumbList` on all except `/`.
- **Speakable: skip.**
- No `Product`, no `AggregateRating`, no review nodes on treatments.
- `MedicalProcedure.name` must be exactly one of: `Dental Implant` · `All-on-4` · `Dental Veneer` · `Teeth Whitening` · `Invisalign` · `Emergency Dental` · `Cosmetic Dentistry`.
- `areaServed` is defined once on `#clinic` (and repeated on the page `Service` if present). Values: Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley, Melbourne VIC.

### Shared fragments (paste into every graph)

**Clinic node** (all pages)

```json
{
  "@type": ["Dentist", "DentalClinic"],
  "@id": "{{URL}}/#clinic",
  "name": "{{PRACTICE_NAME}}",
  "url": "{{URL}}",
  "telephone": "{{PHONE}}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{STREET}}",
    "addressLocality": "Wheelers Hill",
    "addressRegion": "VIC",
    "postalCode": "3150",
    "addressCountry": "AU"
  },
  "geo": {{GEO}},
  "areaServed": [
    { "@type": "City", "name": "Wheelers Hill" },
    { "@type": "City", "name": "Rowville" },
    { "@type": "City", "name": "Glen Waverley" },
    { "@type": "City", "name": "Mulgrave" },
    { "@type": "City", "name": "Mount Waverley" },
    { "@type": "City", "name": "Melbourne", "addressRegion": "VIC", "addressCountry": "AU" }
  ],
  "medicalSpecialty": "https://schema.org/Dentistry"
}
```

Do not invent `sameAs` social profiles or Wikidata IDs. Omit `priceRange` until fees copy exists.

`{{GEO}}` expands to:

```json
{ "@type": "GeoCoordinates", "latitude": "<lat>", "longitude": "<lng>" }
```

**WebPage shell** (swap `url`, `@id`, `name`, `description` per URL; `description` = meta description once Canine writes it)

```json
{
  "@type": "WebPage",
  "@id": "{{PAGE_URL}}#webpage",
  "url": "{{PAGE_URL}}",
  "name": "{{TITLE_TAG}}",
  "isPartOf": { "@id": "{{URL}}/#website" },
  "about": { "@id": "{{URL}}/#clinic" },
  "breadcrumb": { "@id": "{{PAGE_URL}}#breadcrumb" },
  "mainEntity": { "@id": "{{PAGE_URL}}#procedure" }
}
```

On `/dental-implants-cost`, `mainEntity` points at `#service` (and `#faq` may be listed in `hasPart` or as a second `mainEntity` — prefer `mainEntity` = `#faq` on the money page because the page’s job is questions + fees). On `/cosmetic`, `mainEntity` = `#procedure` (Cosmetic Dentistry). On `/`, omit `mainEntity` procedure; use `#clinic`.

**WebSite node** (home only, referenced by `isPartOf` elsewhere)

```json
{
  "@type": "WebSite",
  "@id": "{{URL}}/#website",
  "url": "{{URL}}",
  "name": "{{PRACTICE_NAME}}",
  "publisher": { "@id": "{{URL}}/#clinic" }
}
```

No `SearchAction`.

**BreadcrumbList** (all except home)

```json
{
  "@type": "BreadcrumbList",
  "@id": "{{PAGE_URL}}#breadcrumb",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{URL}}/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{CRUMB_NAME}}",
      "item": "{{PAGE_URL}}"
    }
  ]
}
```

Three-level crumbs (spokes under a hub):

```json
{
  "@type": "BreadcrumbList",
  "@id": "{{PAGE_URL}}#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "{{URL}}/" },
    { "@type": "ListItem", "position": 2, "name": "{{HUB_NAME}}", "item": "{{HUB_URL}}" },
    { "@type": "ListItem", "position": 3, "name": "{{CRUMB_NAME}}", "item": "{{PAGE_URL}}" }
  ]
}
```

| URL | Breadcrumb |
|---|---|
| `/implants` | Home → Dental implants |
| `/all-on-4` | Home → Dental implants → All-on-4 |
| `/dental-implants-cost` | Home → Dental implants → Dental implant cost |
| `/cosmetic` | Home → Cosmetic dentistry |
| `/veneers` | Home → Cosmetic dentistry → Veneers |
| `/whitening` | Home → Cosmetic dentistry → Teeth whitening |
| `/invisalign` | Home → Invisalign |
| `/emergency` | Home → Emergency dentist |

**MedicalProcedure + Service** (procedure pages)

```json
{
  "@type": "MedicalProcedure",
  "@id": "{{PAGE_URL}}#procedure",
  "name": "{{PROCEDURE_NAME}}",
  "procedureType": "https://schema.org/TherapeuticProcedure",
  "followup": "{{URL}}/#clinic"
}
```

```json
{
  "@type": "Service",
  "@id": "{{PAGE_URL}}#service",
  "name": "{{PROCEDURE_NAME}}",
  "serviceType": "{{PROCEDURE_NAME}}",
  "provider": { "@id": "{{URL}}/#clinic" },
  "areaServed": [
    { "@type": "City", "name": "Wheelers Hill" },
    { "@type": "City", "name": "Rowville" },
    { "@type": "City", "name": "Glen Waverley" },
    { "@type": "City", "name": "Mulgrave" },
    { "@type": "City", "name": "Mount Waverley" },
    { "@type": "City", "name": "Melbourne", "addressRegion": "VIC", "addressCountry": "AU" }
  ],
  "url": "{{PAGE_URL}}"
}
```

For surgical implant / All-on-4, Molar may set `procedureType` to `https://schema.org/SurgicalProcedure`. Whitening, veneers, Invisalign, cosmetic, emergency stay `TherapeuticProcedure`.

Do not put a dollar `Offer` on MedicalProcedure. Guide fees belong in copy + FAQ answers, not as a Product SKU.

**FAQPage** (pages in §4 that ship an FAQ block)

```json
{
  "@type": "FAQPage",
  "@id": "{{PAGE_URL}}#faq",
  "url": "{{PAGE_URL}}",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{QUESTION}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER}}"
      }
    }
  ]
}
```

`{{ANSWER}}` is Canine’s FAQ answer (plain text, no HTML). Emit one `Question` per on-page FAQ. If a planned question is not yet answered, **omit it from JSON-LD** — do not ship empty answers.

### Per-template graphs

#### Home `/`

`@graph`: WebSite · Dentist/DentalClinic · WebPage (`mainEntity` = `#clinic`).  
No BreadcrumbList. No MedicalProcedure. No FAQPage unless a FAQ block ships.  
Optional: `hasOfferCatalog` ItemList of the eight service URLs pointing at each `#service` `@id`. Nice-to-have, not required for launch.

#### Procedure template  
`/implants` · `/all-on-4` · `/invisalign` · `/veneers` · `/whitening` · `/emergency` · `/cosmetic`

`@graph`: Dentist/DentalClinic (or `@id` reference only if Molar inlines the full node) · WebPage · MedicalProcedure · Service · BreadcrumbList · FAQPage.

| URL | `MedicalProcedure.name` / `Service.name` |
|---|---|
| `/implants` | Dental Implant |
| `/all-on-4` | All-on-4 |
| `/invisalign` | Invisalign |
| `/veneers` | Dental Veneer |
| `/whitening` | Teeth Whitening |
| `/emergency` | Emergency Dental |
| `/cosmetic` | Cosmetic Dentistry |

On `/implants`, `Service` may `isRelatedTo` `/all-on-4#service` and `/dental-implants-cost#service`. On `/cosmetic`, `isRelatedTo` veneers, whitening, Invisalign service ids.

#### Money template `/dental-implants-cost`

`@graph`: Dentist/DentalClinic · WebPage (`mainEntity` = `#faq`) · Service (`name`: `Dental Implant`, `url`: this page, `provider`: `#clinic`) · BreadcrumbList · FAQPage.

No MedicalProcedure on the cost page (the procedure lives on `/implants` and `/all-on-4`).  
Service here is the same type as implants so Google associates fees with the treatment, not a new invented “cost procedure”.

---

## 4. On-page SEO spec (Molar / Canine)

**Title pattern (all except home):** `{Procedure} | {{PRACTICE_NAME}} | Wheelers Hill`  
Target ≤60 characters. If the practice name blows the limit, shorten the practice token — never drop the procedure or Wheelers Hill.  
**Home title:** `{{PRACTICE_NAME}} | Dentist Wheelers Hill` is acceptable as a brand+NAP title; do not build a `/dentist-wheelers-hill` URL to match it.

**Meta description:** 150–160 characters. One procedure + one location (Wheelers Hill). Do not comma-stuff Rowville / Glen Waverley / Mulgrave / Mount Waverley into the meta. Nearby suburbs belong in body NAP / service-area sentence and schema.

**H1:** Procedure-led. One H1. Suburb may appear in a subline or first paragraph, not as “Dentist in Rowville, Glen Waverley, Mulgrave…” stacked in the H1 (Liberty geo-stack — do not copy).

**H2s below are SEO section labels only.** Canine writes the prose. Do not ship these labels as patient-facing marketing headlines if the voice guide wants plainer section names — keep the *intent* of each block.

**FAQ questions are capture targets**, not final wording. Canine may tighten. Answers must not promise outcomes, “pain-free”, or Medicare/super approval.

---

### `/` homepage

| Field | Spec |
|---|---|
| **H1** | Practice + what we do (implants, Invisalign, veneers, cosmetic). Not “Dentist Wheelers Hill” as the product. |
| **Title** | `{{PRACTICE_NAME}} \| Dentist Wheelers Hill` |
| **Meta** | 150–160c. Brand, Wheelers Hill, premium mix named once. |
| **H2 outline** | Dental implants · All-on-4 · Invisalign · Cosmetic dentistry (veneers + whitening) · Emergency dentist · Dental implant cost · Visit (NAP + service area as copy, not eight H2s) |
| **FAQ** | None required. If added, keep to hours/parking/how to book — not treatment encyclopaedia. |

### `/implants`

| Field | Spec |
|---|---|
| **H1** | Dental implants |
| **Title** | `Dental Implants \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Implants + Wheelers Hill. Point to cost/super as a reason to open the page, not a second URL in the meta. |
| **H2 outline** | What dental implants are · Single vs multiple vs full-arch · Who it may suit · Process · Timeline · Cost, staging, super (teaser → `/dental-implants-cost`) · Implants vs dentures, bridges, All-on-4 · Risks · FAQs · Related |
| **FAQs to capture** | How much do dental implants cost? · Can I use super for dental implants? · Does Medicare cover dental implants? · How long do implants take? · Implant vs denture vs bridge · Single implant vs All-on-4 |

### `/all-on-4`

| Field | Spec |
|---|---|
| **H1** | All-on-4 |
| **Title** | `All-on-4 \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. All-on-4 / full-arch + Wheelers Hill. Cost intent allowed. |
| **H2 outline** | What All-on-4 is · Full-mouth rehab / who it may suit · Process · Timeline · Cost and super (link to `/dental-implants-cost`) · All-on-4 vs single implants vs dentures · Risks · FAQs · Related |
| **FAQs to capture** | How much does All-on-4 cost? · Can I use super for All-on-4 / full-mouth implants? · Does Medicare cover All-on-4? · How long does All-on-4 take? · All-on-4 vs single implants · All-on-4 vs dentures |

### `/invisalign`

| Field | Spec |
|---|---|
| **H1** | Invisalign |
| **Title** | `Invisalign \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Invisalign + Wheelers Hill. Cost intent allowed. |
| **H2 outline** | What Invisalign is · Who it may suit · Process · Timeline / wear · Cost (on-page guide + consult; no separate Invisalign-cost URL at launch) · Invisalign vs braces vs veneers · Risks / retention · FAQs · Related (`/cosmetic`, optional `/veneers`) |
| **FAQs to capture** | How much does Invisalign cost? · Does Medicare or extras cover Invisalign? · Can I use super for Invisalign? · How long does Invisalign take? · Invisalign vs braces · Invisalign vs veneers |

### `/veneers`

| Field | Spec |
|---|---|
| **H1** | Dental veneers |
| **Title** | `Dental Veneers \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Veneers + Wheelers Hill. Porcelain may appear; do not split composite to its own URL. |
| **H2 outline** | What veneers are · Porcelain vs composite (same URL) · Who it may suit · Process · Timeline · Cost · Veneers vs Invisalign vs whitening vs crowns · Risks (incl. irreversibility) · FAQs · Related |
| **FAQs to capture** | How much do veneers cost? · Does Medicare cover veneers? · Can I use super for veneers? · How long do veneers take? · Veneers vs Invisalign · Porcelain vs composite veneers |

### `/cosmetic`

| Field | Spec |
|---|---|
| **H1** | Cosmetic dentistry |
| **Title** | `Cosmetic Dentistry \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Cosmetic dentistry + Wheelers Hill. Name veneers / whitening / Invisalign as the mix, not injectables. |
| **H2 outline** | What cosmetic dentistry covers here · Veneers · Teeth whitening · Invisalign (route, not nested) · Smile design / makeover as a planning idea, not a URL · Cost (consult; link implant cost only if full-mouth) · FAQs · Related spokes |
| **FAQs to capture** | How much does cosmetic dentistry cost? · Does Medicare cover cosmetic dentistry? · Can I use super for cosmetic work? · How long does a smile makeover take? · Veneers vs Invisalign vs whitening — which first? |
| **Later-only line** | Injectables: one sentence “not offered yet” max. No H2, no URL, no schema name. |

### `/whitening`

| Field | Spec |
|---|---|
| **H1** | Teeth whitening |
| **Title** | `Teeth Whitening \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Whitening + Wheelers Hill. Do not geo-target Glen Waverley in title. |
| **H2 outline** | What in-chair / take-home whitening is · Who it may suit · Process · Timeline / how long it lasts (range, not a promise) · Cost · Whitening vs veneers · Risks / sensitivity · FAQs · Related |
| **FAQs to capture** | How much does teeth whitening cost? · Does Medicare cover whitening? · How long does whitening last? · Whitening vs veneers · Can I whiten crowns or veneers? |

### `/emergency`

| Field | Spec |
|---|---|
| **H1** | Emergency dentist |
| **Title** | `Emergency Dentist \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Emergency dental + Wheelers Hill. Call/NAP in the body, not stuffed into meta. |
| **H2 outline** | What counts as emergency dental here · When to call · What happens on the day · After-hours / limits (honest; do not invent 24/7) · Cost of emergency visits · Tooth loss and implants (link `/implants`) · FAQs |
| **FAQs to capture** | How much is an emergency dentist visit? · Do I need a referral? · Does Medicare cover emergency dental? · Can extras / health funds be used? · What if a tooth is knocked out? (route to implants, not a new URL) |

### `/dental-implants-cost`

| Field | Spec |
|---|---|
| **H1** | Dental implants cost |
| **Title** | `Dental Implants Cost \| {{PRACTICE_NAME}} \| Wheelers Hill` |
| **Meta** | 150–160c. Cost + Wheelers Hill / Melbourne-intent is fine in body; title stays this pattern. |
| **H2 outline** | Guide fees (ranges, not a quote) · What the fee includes / staging · Single vs multiple vs All-on-4 fees · Superannuation early release · Medicare and extras · Payment plans / health funds · Timeline vs cost · FAQs · Links to `/implants` and `/all-on-4` |
| **FAQs to capture** | How much are dental implants? · How much do dental implants cost in Melbourne? · Can I use my super for dental implants? · Does Medicare cover dental implants? · Why do implant fees vary? · All-on-4 cost vs single implants · Do health funds cover implants? |
| **Note** | This page is the money URL for the implant cluster. Do not also write a blog post targeting the same questions at launch. |

---

## 5. Launch vs later

| Now (this pack) | Explicitly later |
|---|---|
| `/` + eight slugs in §1 | **Injectables** (URL, H2, schema, ads). At most a “not offered yet” line on `/cosmetic`. |
| Procedure-led paths; Wheelers Hill in title, NAP, schema | **Suburb landings** as honest drive-time pages: `/dentist-rowville`, `/dentist-glen-waverley`, `/dentist-mulgrave`, `/dentist-mount-waverley`. Not doorway spam; not launch. |
| Nearby suburbs in `areaServed`, footer text, supporting copy | **Blog / education** (cost, vs, recovery posts). Implant cost is already a page — do not duplicate it as a post. |
| Cosmetic hub + implants hub + emergency chrome | Porcelain-only URL, composite-only URL, smile-makeover URL, super-only URL |
| Skip: bulk-bill, kids, wisdom, hygienist ranking URLs | Revisit those only if the mix changes |
| Skip: “dentist Wheelers Hill” as a year-one URL/KPI | Maps/GBP still name Wheelers Hill; that is not a web page |

**Second-wave suburb pages (when built):** one clinic, drive-time copy, link **into** the eight procedure URLs. Do not clone eight procedure pages × four suburbs.

---

## Build checklist (Molar)

- [ ] Routes match the eight slugs exactly (hyphens, no suburb in path, `all-on-4` not `all-on-four` / `allon4`)
- [ ] Header: Emergency top-level; Treatments dropdown lists all clinical URLs + `/dental-implants-cost`
- [ ] Footer: NAP (Wheelers Hill VIC 3150) + service-area sentence + popular-treatment links using the anchor bank
- [ ] Homepage body links all eight URLs
- [ ] Implant triangle: each of `/implants`, `/all-on-4`, `/dental-implants-cost` links to the other two
- [ ] Cosmetic hub links veneers, whitening, Invisalign; spokes link back to hub
- [ ] Invisalign breadcrumb is Home → Invisalign
- [ ] JSON-LD `@graph` per template; clinic `@id` stable; procedure names exact
- [ ] FAQPage only where FAQ answers exist
- [ ] No Speakable, no Product, no AggregateRating
- [ ] `areaServed` lists Wheelers Hill, Rowville, Glen Waverley, Mulgrave, Mount Waverley, Melbourne VIC
- [ ] No launch routes for injectables, suburbs, blog, bulk-bill, kids, wisdom, hygienist

## Copy checklist (Canine)

- [ ] Fill H1s, titles, metas to the patterns in §4 (no patient-facing draft in this pack)
- [ ] FAQ answers for every question that will be schema’d
- [ ] One service-area sentence naming the five suburbs + Melbourne — supporting copy, not H1
- [ ] Cost/super/Medicare language is eligibility-and-process, not approval promises
- [ ] No outcome testimonials, no “best/only/guaranteed”, no weekly-from SKU in H1
