# Direction C — the WebGL hybrid

A one-page design exploration. **Not the live site.** `noindex`.

Answers one question: can we get [bunqlabs.com](https://www.bunqlabs.com/)'s
polish without its architecture?

Teardown that prompted this: `~/Dev/brain/03-Resources/topics/bunqlabs-teardown.md`

## v2 — "stop hedging" (2026-09-09)

v1 was too restrained: type on a gradient, nothing to look at. Julia's verdict
was "too boring" and it was correct. v2 keeps exactly one rule from v1 — **all
type stays crawlable HTML** — and pushes everything else.

**The stage.** A 340vh pinned section driving one scroll value, `p`, through
three scenes:

| `p` | State | Ground |
| --- | --- | --- |
| 0.00–0.30 | `arc.jpg` assembled from ~69k particles | near-black |
| 0.30–0.70 | the field disperses and drifts | warms to slate |
| 0.70–1.00 | `porcelain.jpg` re-forms | back to deep |

That is BUNQ's mountain→point-cloud move and their light→dark inversion, done
with two JPEGs and no model pipeline. 61 fps at 2× DPR.

## The thesis

BUNQ renders every glyph into a WebGL canvas and leaves six lines of
`visually-hidden` HTML for Google. Direction C inverts that relationship:

| | BUNQ | Direction C |
| --- | --- | --- |
| Type | **inside** the canvas (MSDF atlases) | **on top of** the canvas (real HTML) |
| Crawlable words | ~30 | ~484 |
| Canvas scope | whole site, all 5 scenes | the stage only, decorative |
| Payload | 7.6MB / 50 requests | 310KB, one file |
| Script fails | blank page | page unaffected |

The canvas is decoration. Delete the script tags and the page still reads,
still ranks, still converts.

## Borrowed from BUNQ

Light→dark inversion as the scroll device (here: dark hero → warm page →
dark close), film grain over everything, fluid `clamp()` type with no
breakpoint jumps, four hand-tuned cubic-beziers instead of `ease-in-out`,
Lenis smooth scroll, and a cursor-reactive light field — their dye/pressure
fluid sim reduced to the one effect that earns its place.

**Not** borrowed: MSDF text, Draco GLBs, KTX2 bakes, scroll snapping, ambient
audio, lil-gui, the 7.6MB.

## Palette and type

Palette is **Direction A's own** (sage / forest / terracotta) so this reads as
the same practice in a different register, not a different brand.

Type is Instrument Serif + Inter Tight + JetBrains Mono. **Instrument Serif is
standing in for Larken Light**, the commercial face BUNQ uses (~A$60–100,
Ellen Luff). Swap one line — `--font-display` — to trial the real thing.

## Motion contract

Inherited from Direction B, non-negotiable:

- Base stylesheet never hides content.
- Hidden-initial-state is scoped to `html.motion-on`, which JS applies.
- Blocked or failed script → fully readable static page.
- WebGL absent or failed → hero falls back to a CSS gradient, no gap.
- `prefers-reduced-motion` disables the lot.
- Emergency strip never moves.

## Verified

Headless Chrome (ANGLE/Metal), from `file://`, zero console errors:

| Config | Particles | Photographs | h1 | Words |
| --- | --- | --- | --- | --- |
| Desktop + WebGL | live, 61 fps @2× DPR | in canvas | visible | 556 |
| `prefers-reduced-motion` | off | as `<img>` | visible | 555 |
| **JS disabled** (crawler) | off | as `<img>` | visible | 555 |
| Mobile 390×844 | live, ~20k | in canvas | visible | 553 |

Mobile now gets a real, lighter version (~20k particles) rather than nothing —
v1 switched the canvas off below 768px, which is very likely what made it look
flat on a phone.

The canvas stops rendering when the stage scrolls out of view or the tab hides.

## Three bugs worth remembering

1. **Dispersion must be measured in grid spacings, not world units.** At this
   grid one spacing is ~0.019 world units, so a "gentle" 0.3 push scatters
   particles ~15 cells and turns the photograph into static.
2. **Circles on a square grid cover only ~79%.** Points have to overlap
   (×1.5 of spacing) or the gaps read as noise, not as an image.
3. **`file://` blocks WebGL texture uploads** from separate image files — CORS
   taints the canvas. A `media/` folder silently dropped the whole stage to the
   `<img>` fallback when opened from disk, which is exactly how the vault
   Library opens it. The photographs are inlined as data URIs, read back out of
   the page's own `<img>` elements so the bytes exist once.

## Copy

Lifted from Julia-approved pages. No new clinical claims, no testimonials, no
superlatives, no counters, no before/after. Rules: `copy/00-ahpra-and-voice.md`.

Placeholders that still need real values: phone number, booking URL, practice
hours, AHPRA registration number, and the treatment card links.

## Two CDN gotchas worth knowing

1. **three.js has no UMD build since r150.** `three.min.js` 404s on every CDN.
   It is ESM-only — `three.module.min.js` via `import()`.
2. **Lenis is not on cdnjs at all.** It is on jsdelivr.

Both are pinned. For production, self-host rather than hotlink.

## Images

`media/` holds the full-resolution sources. They are **AI-generated
placeholders**, not practice photography, and the page says so on screen — the
Grok watermarks have been cropped off. Downscaled copies are inlined into
`index.html`; the folder is source material, not a runtime dependency.

## Run it

Open `index.html` directly — no build step, no server, no dependencies.
