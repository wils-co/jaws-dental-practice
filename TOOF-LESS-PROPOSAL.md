---
source: agy (gemini-3.1-pro-high)
created: 2026-09-03
updated: 2026-09-03
status: proposal-for-review
reviewer: Klud (Grok Bot Chief of Staff)
project: jaws-dental-practice (Smiles by Design)
domain: business / health-marketing
tags: [toof-less, grok-bot, klud, julia-dental, ahpra, seo, workflow, proposal]
---

# Toof-less Dental Pod — Architecture & Publishing Pipeline Proposal

**Target Practice:** Smiles by Design (Dr. Julia Nguyen — Wheelers Hill VIC 3150)  
**Primary Repo:** `github.com/wils-co/jaws-dental-practice` (private)  
**Review Plane:** Watchtower Library (`dental-shelf.html` via `[Dental]` button)  
**Intended Reviewer:** Klud (Chief of Staff, Grok Bot)

---

## 1. Executive Summary

This proposal establishes the collaboration structure between **Toof-less** (the Grok Bot dental pod running in the xAI cloud / mobile app) and the **Local Stack** (Hermes on the Mac Studio M3 Ultra).

### Core Operating Principles
1. **Single Git Backbone:** Everything lives in `github.com/wils-co/jaws-dental-practice`. *Not a second repo. Not Google Drive.*
2. **Asymmetric Collaboration:** Grok Bot produces in the cloud; Local Hermes maintains infrastructure and merges on the Studio.
3. **The 80/20 Rule:** Toof-less produces the first 80% (SEO, structure, clinical facts, AHPRA safety); **Dr. Julia Nguyen provides the final 20% (authentic human bedside manner, empathy, clinical philosophy)**.
4. **Zero Doctor Friction:** Dr. Julia Nguyen never touches Git, terminal commands, or PR forms. Review happens via mobile staging preview and quick voice notes.

---

## 2. Pod Roster (Anterior to Posterior)

```
ANTERIOR (Front)                                             POSTERIOR (Back)
┌─────────────┐    ┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   INCISOR   │    │ CANINE (Silver) │    │   PREMOLAR   │    │    MOLAR    │
│  Reception  │    │  AHPRA-Safe     │    │   SEO & IA   │    │  Site Build │
│ Non-clinical│    │  Original Copy  │    │  Semrush/Vol │    │  Assembly   │
└─────────────┘    └────────┬────────┘    └──────┬───────┘    └──────▲──────┘
                            │                    │                   │
                            └─────────►  ◄───────┘                   │
                                         │                           │
                                         └───────────────────────────┘
                                                Hands off to Molar
```

| Role | Tooth | Responsibility | Hard Guardrails |
|---|---|---|---|
| **Incisor** | Front Incisor | Reception & inquiry triage. Fast, warm responses regarding clinic hours, location, parking, and consult booking funnel. | **Strictly non-clinical.** Never quotes exact treatment prices or answers medical questions. |
| **Canine** *(Silver Tongue)* | Eyetooth | Original patient-facing clinical copy. Translates complex procedures into clear, comforting prose. | **AHPRA s133 compliant.** No testimonials, no before/after guarantees. Researches topics from peers; **never scrapes-and-republishes**. |
| **Premolar** | Bicuspid | SEO & Information Architecture. Keyword intent, Semrush search volumes, slug architecture, Dentist JSON-LD schema, internal links. | Does not write long-form prose. Does not assemble HTML/code. |
| **Molar** | Grinder / Back | Site assembly. Takes Canine’s prose + Premolar’s IA and builds clean, responsive page templates. | Single unified icon set. Melbourne title tags. Wheelers Hill in NAP/Schema only (maintains geographic reach). |
| **Klud** | Chief of Staff | Sequences the pod. Decides which page to build next, monitors blockers, and hands completed batches to Plumb\'oor. | Manages pod throughput. Ensures Canine and Premolar complete before Molar builds. |
| **Plumb\'oor** | GitHub Infra | Repo governance (`wils-co`). Manages branch rules, GitHub PATs, CI checks, and PR formatting. | Keeps Git hygiene pristine. Enforces `.gitignore`. |
| **Local Hermes** | Studio Engine | Local Mac Studio agent. Runs local models (Qwen for reception), pulls PRs, checks local diffs, and manages production deploys. | Reviews PRs locally before Wilson approves merge to `main`. |

---

## 3. The 8 Launch URLs (Anti-Commodity Focus)

Smiles by Design is deliberately positioned as a **boutique cosmetic and reconstructive practice**, not a high-turnover insurance mill.

### The Launch Scope
1. `/implants` — Single & multiple tooth titanium restorations.
2. `/all-on-4` — Full-arch permanent fixed rehabilitation.
3. `/invisalign` — Clear aligner orthodontics for adult professionals.
4. `/veneers` — Handcrafted porcelain & composite smile makeovers.
5. `/cosmetic` — Full-mouth aesthetic rehabilitation.
6. `/whitening` — In-chair clinical & take-home professional whitening.
7. `/emergency` — High-intent triage for pain relief & broken teeth.
8. `/dental-implants-cost` — Transparent fee ranges, financing options, and phased treatment plans.

### Deliberate Exclusions (Do Not Build)
- ❌ **No Bulk-Bill pages** (conflicts with boutique positioning).
- ❌ **No Child Dental Benefits (CDBS) / pediatric content**.
- ❌ **No wisdom tooth extraction commodity factory**.
- ❌ **No routine hygienist churn mill**.

---

## 4. The 80 / 20 Editorial Pipeline (Julia\'s Clinical Voice)

High-ticket elective dentistry is sold on **empathy and clinician trust**. Pure AI copy sounds like a sterile agency brochure; clinical jargon scares patients away.

```
  [Grok Bot App]
   ├── Premolar  ──► Keyword volume & Schema IA
   ├── Canine    ──► 80% AHPRA-safe clinical draft
   └── Molar     ──► Assembles page staging preview
         │
         ▼ (opens PR: toof-less/<slug>)
  [GitHub: wils-co/jaws-dental-practice]
         │
         ▼ (stages preview)
  [Watchtower / Staging Preview]
         │
         ▼
  ╔═══════════════════════════════════════════════════╗
  ║       DR. JULIA NGUYEN CLINICAL POLISH (20%)      ║
  ║  • Reads 80% draft on mobile (3 mins)             ║
  ║  • Sends 30-sec voice note or quick text edit     ║
  ║  • Injects warmth, bedside manner, & philosophy   ║
  ║  • Anchors signature "Your Teeth Have a Timeline" ║
  ╚═══════════════════════════════════════════════════╝
         │
         ▼
  [Local Hermes / Wilson Ingests & Merges PR]
         │
         ▼ (auto-deploy via Cloudflare Pages / Vercel)
  [LIVE PRODUCTION WEBSITE: Smiles by Design]
```

### How Dr. Julia Reviews Without Friction
- **Zero Git / No Terminal:** Dr. Julia reviews rendered preview cards on her phone via Watchtower Library.
- **The Voice Memo Protocol:** Julia sends a 30-second Telegram or WhatsApp voice note between patients:
  > *"On the Veneers page, under \'Does it hurt?\', remove that mention of \'Hollywood smiles\'—we design natural Melbourne smiles. And mention that we use the Wand computerised numbing so patients don\'t feel the sting."*
- **Hermes / Grok applies the edit:** Local Hermes updates the draft branch, verifies tone, and merges the PR.

---

## 5. Repository Structure (`wils-co/jaws-dental-practice`)

```
jaws-dental-practice/
├── README.md               # Pod overview & quickstart
├── BRIEF.md                # Project SSOT (synced with Second Brain)
├── TOOF-LESS.md            # The pod system prompt & operational rules
├── TASKS.md                # Klud\'s sequencing pipeline (8 launch URLs)
├── .gitignore              # Strict barrier (.env, 05-Personal/, OS junk)
│
├── copy/                   # CANINE (Silver Tongue)
│   ├── implants.md         # AHPRA-safe markdown copy drafts
│   ├── all-on-4.md
│   ├── invisalign.md
│   ├── veneers.md
│   ├── cosmetic.md
│   ├── whitening.md
│   ├── emergency.md
│   └── dental-implants-cost.md
│
├── seo/                    # PREMOLAR
│   ├── keyword-maps/       # Target keywords, intent, Semrush volumes
│   ├── schema/             # JSON-LD Dentist schema (Wheelers Hill NAP)
│   └── sitemap.md          # 8 core URL hierarchy & internal linking map
│
├── site/                   # MOLAR
│   ├── pages/              # Canine copy + Premolar IA assembled into HTML
│   └── components/         # Unified icon set, header/footer, styles
│
├── reception/              # INCISOR
│   ├── triage-rules.md     # Non-clinical email boundaries (hours, parking, booking)
│   └── canned-replies/     # Pre-approved reception templates
│
└── docs/                   # REFERENCE (Public-safe planning)
    ├── spatial-planning/   # AusHFG room schedule & catchment summaries
    └── vendor-audits/      # GDW vendor teardown & build vs buy
```

---

## 6. Grok Bot App ↔ GitHub Interaction Protocol

### Step 1: Task Assignment
Wilson or Local Hermes creates a task in `TASKS.md` or as a GitHub Issue:
```markdown
### [TASK-01] Veneers Launch Page
- Status: Ready for Canine & Premolar
- Target: /veneers
- Focus: Porcelain vs composite, natural aesthetic, zero pain guarantee prohibition.
```

### Step 2: Toof-less Execution (Grok Bot App)
1. You ping Grok Bot: *"Toof-less, take TASK-01 (Veneers)"*.
2. **Klud** sequences:
   - Premolar creates `seo/keyword-maps/veneers.md`.
   - Canine writes `copy/veneers.md`.
   - Molar compiles `site/pages/veneers.html`.
3. Toof-less branches: `toof-less/veneers`.
4. Pushes and opens a GitHub Pull Request with a checklist.

### Step 3: Local Review & Publish
1. Local Hermes pulls the PR, tests the preview in Watchtower.
2. Dr. Julia reviews on phone, provides her 20% voice polish.
3. Wilson merges the PR (`gh pr merge`).
4. Site auto-deploys to production.

---

## 7. Questions for Klud (Chief of Staff Review)

Please review this proposal and provide sign-off on:
1. **Pod sequencing:** Does Klud prefer running Canine and Premolar in parallel before Molar, or Premolar first for keyword targeting?
2. **Launch sequence:** Should we tackle the 8 URLs in priority order (e.g. Veneers & Implants first, Emergency & Whitening second)?
3. **Format preference:** Does Molar prefer assembling flat HTML5 components first, or targeting an Astro content collection?
