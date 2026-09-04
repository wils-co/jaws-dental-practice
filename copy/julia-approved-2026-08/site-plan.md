# Site plan — drjuliadentist.com.au
Dr Julia Nguyen · 9 Aug 2026

---

## What this site is, and is not

**Is:** a clinician's professional profile and a serious patient-education library, under her own name, on a domain she owns.

**Is not:** a practice site. No booking engine, no "become my patient", no service-area pages, no offers. She is an associate at two practices she does not own, with a 5km/12-month restraint at BCDC, and she has kept her ownership plans private.

Every page must pass one test: **would she be comfortable if Andrea Manley or Dina Liosis read it?** Assume they will.

The practice layer gets added later, on a domain that by then has years of content and search history behind it.

---

## Pages

### 1. Home
Who she is, what she does, and a way into the education content. Not a sales page.

Above the fold: her name, "general dentist", the one-liner, the headshot. Below: three or four entry points into the education modules, and a short route to *How I work*.

No stock photography anywhere on this site. Ever.

### 2. About
The approved bio verbatim (`bio-FINAL.md`), plus the credentials block: degrees, AHPRA number, and the CPD list. The CPD list does the work that "committed to excellence" fails to do — it is long, dated, and checkable.

### 3. How I work
**The page that makes this site different from every other dentist's.** It carries the material she cut from the bio, where it has room to be shown rather than claimed:

- **You will hear the cost in the surgery, not at the front desk.** With the number of appointments and how long treatment takes — the part people underestimate.
- **"We'll keep an eye on it" usually means nothing.** Teeth change by fractions of a millimetre. Nobody can hold that across six months. She scans and compares.
- **The long explanation or the short one.** Whichever the patient wants.
- **She will say when something is not worth doing.** Not every tooth needs saving; some treatment costs more than the problem.

Written as description of practice, never as a comparative claim about other dentists. The point is always about the tooth or the method, never the operator.

### 4. Education library
The interactive modules. The reason anyone links to, returns to, or finds this site. See build order below.

### 5. What things cost
Indicative ranges and appointment lengths. This page is what makes *How I work* provable rather than another unverifiable claim — and almost nobody in Australian dentistry publishes it.

Ranges, not fixed prices, with a plain note that the number depends on the case. Item numbers where useful. Typical health fund gap explained without quoting rebate figures — she has already established, in her own patient contracts, that specifying rebates creates liability and the claiming responsibility sits with the patient.

**If this page is not built, the cost sentences on *How I work* must be cut.**

### 6. Where I practise
Rye Family Dental and Blackburn Clinic Dental Centre, with their contact details and their booking links.

This page is what makes the whole site safe. It is not a funnel away from her employers — it sends patients *to* them. A personal site that routes work to Rye and BCDC is a gift to both, and it is the honest answer to the only question a patient will have after reading the education content.

### 7. Contact
Minimal. Professional enquiries only. No patient booking form — booking happens at whichever practice they choose on the page above.

---

## Build order for the modules

Criteria: buildable with no photography, no patient data, and no long lead time; demonstrates how she thinks; cannot be copied by a competitor.

### First — "Should this tooth be saved?"
An interactive walk through the reasoning: what is left of the tooth, what is holding it, what it is doing in the mouth, what the alternatives cost in money and time.

Best first build because it needs **no assets at all** — no scans, no photographs, no illustration. Pure logic, which she already has and most dentists have never written down. It also carries *not every tooth needs saving*, which is the most counter-intuitive and most linkable thing on the site.

**Framing is non-negotiable:** it ends in *"here is what a dentist is weighing"*, never a diagnosis or a recommendation. Explicit, prominent statement that it is general information and not personal advice.

### Second — the wear time-lapse
Two scans of the same mouth months apart, overlaid, change visible. This is the flagship — her argument, her technology, and nothing like it exists on an Australian dental site.

**Start the clock now.** It needs a first scan today and a second in six months. Use a typodont or a consenting volunteer — never patient scans from Rye or BCDC, which are those practices' and those patients' data.

### Third — what waiting costs
Filling, crown, root canal and crown, implant. Money and time, side by side, as a problem progresses. Reuses the pricing page data, so it costs little once that page exists.

### Later
Cracked tooth explorer (needs illustration). A rotatable 3D scan from a typodont. "Why your dentist might say no" — patients know about informed consent; almost none know it runs both ways. Frame as *I will not take your money for something that will break*, never doctor-knows-best.

---

## Stack

**Astro + Tailwind, hosted on Cloudflare Pages, source in a private git repo.** Three.js for anything 3D; plain JS islands for the rest.

Chosen for the endgame, not for elegance: she wants Claude Code and agents running marketing against this. That needs a repository of plain text files an agent can read, edit and commit. WordPress adds a database, a plugin surface and a security chore; Wix and Squarespace cannot host a 3D scan viewer and no agent can touch them.

Free to host at this scale.

---

## Sequence

**Now — hers, blocking everything**
- Buy `drjuliadentist.com.au` in her own name and ABN (55639292199). Auto-renew, domain lock, two years. Add `drjulia.dental` and `drjulianguyen.com.au` as redirects.
- Book a headshot. One session, clean background. No AI images — the site's entire argument is about reducing what a patient takes on faith.
- Read the BCDC restraint and non-solicitation clauses before anything goes live.

**Then — build**
1. Repo, deploy pipeline, and a holding page on the live domain. Getting the domain indexed early is free and compounds.
2. About and Home, from the approved bio.
3. How I work, and What things cost — these two ship together or not at all.
4. Where I practise.
5. First module: *Should this tooth be saved?*

**Then — distribution**
- Google Search Console, sitemap, and a manual geotarget if any non-`.com.au` domain is ever made canonical.
- LinkedIn rewritten from the approved short bio, so both platforms say the same thing in the same voice.
- Only once there is something worth maintaining: the agent layer, working against `voice-guide.md`.

---

## Not yet

Booking. Patient reviews or testimonials — banned outright under s133 regardless. Before-and-after imagery — heavily conditioned, and unnecessary when the education content does more work. Service-area or suburb pages. Anything about practice ownership, catchments or business models. Mint Scan, which stays quiet until she has her own practice to run it in.
