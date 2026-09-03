# Icon system — Smiles by Design (Julia Nguyen, Wheelers Hill)

Medical-clean **line** icons. One style only. Colour comes from the parent, not from the file.

## System (do not fork)

Every standalone file and every `<symbol>` uses the same drawing surface:

| Attribute | Value |
|---|---|
| Size | 24×24 |
| `viewBox` | `0 0 24 24` |
| `fill` | `none` (the pin hole is the only tiny `currentColor` dot) |
| `stroke` | `currentColor` |
| `stroke-width` | `1.75` |
| `stroke-linecap` / `stroke-linejoin` | `round` |

Artwork sits inside a 20×20 inner box (2px inset on each side). No dual-tone, no filled shapes, no cartoon tooth-faces, no brand logos (including the official Invisalign mark).

This set is the only icon language on the launch site. **Do not mix with Font Awesome**, Heroicons, or a second stroke weight.

## Size

| Context | Rendered size |
|---|---|
| Default (nav, footer, inline, treatment body, chrome) | **24px** |
| Homepage demand-door grid (six doors) | **32px** |

Scale with `width` / `height` or CSS. Do not change `stroke-width` when scaling — 1.75 is authored for the 24 viewBox and should stay there.

## Colour

Icons inherit `color` via `currentColor`. Set colour on the parent (link, button, heading), not on the SVG.

**Do not recolour per service.** Emergency is not red, whitening is not gold, Invisalign is not teal. One ink, same as body text (or the chrome inverse on a dark bar).

## Usage

### Individual file (inline or `<img>`)

```html
<a href="/emergency" class="door">
  <img src="/icons/emergency.svg" width="32" height="32" alt="">
  Emergency dentist
</a>
```

Prefer inline SVG or the sprite so `currentColor` works. `<img>` cannot inherit text colour.

### Sprite

```html
<svg class="icon" width="24" height="24" aria-hidden="true">
  <use href="/icons/sprite.svg#icon-phone"></use>
</svg>
```

Symbol ids are `icon-{filename-without-svg}` (e.g. `icon-all-on-4`, `icon-dental-implants-cost`).

When using `<use>`, repeat the stroke system on the outer svg (some browsers do not copy presentation attributes off `<symbol>`):

```css
.icon {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.75;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.icon--door { width: 32px; height: 32px; }
```

The pin hole is a filled circle. If you set `fill: none` on `.icon`, keep pin as an inline file, or set `fill: currentColor` on that circle.

`chevron.svg` points **down**. Rotate the element for other directions (`-90deg` left, `90deg` right, `180deg` up). `arrow.svg` is a right-pointing shaft + head for text links.

`book.svg` is a **calendar** (Book an appointment), not an open book.

## Mapping

Premolar owns final slugs if they differ. Confirmed launch URLs from copy are marked.

### Treatments

| File | Metaphor | Where it goes |
|---|---|---|
| `emergency.svg` | Tooth + lightning | Homepage demand door (32px). Treatment page **`/emergency`**. |
| `checkup.svg` | Tooth + check | Homepage demand door (32px). Check-up and clean page (likely `/check-up-and-clean`). |
| `invisalign.svg` | Aligner tray (top view, not the trademark) | Homepage demand door (32px). Treatment page `/invisalign`. |
| `implants.svg` | Single fixture + crown | Homepage demand door (32px). Treatment page **`/dental-implants-wheelers-hill`**. |
| `all-on-4.svg` | Arch + four posts (distal angled) | Treatment page **`/all-on-4`**. Related link from implants. Not a homepage door. |
| `veneers.svg` | Tooth + facial shell | Homepage demand door (32px). Treatment page `/veneers`. |
| `whitening.svg` | Tooth + spark | Homepage demand door (32px). Treatment page `/whitening`. |
| `cosmetic.svg` | Smile arc | Cosmetic treatment page `/cosmetic`. Treatments hub. Not a homepage door. |
| `dental-implants-cost.svg` | Implant + price tag | **`/dental-implants-cost`**. Related from implants. Not a homepage door. |

Homepage six doors (32px): emergency, checkup, invisalign, implants, veneers, whitening.

Do **not** add kids, wisdom, hygienist, crowns, root canal, or anxious-patient icons to this folder. Those pages can wait; this set is launch only.

### Chrome

| File | Slot |
|---|---|
| `phone.svg` | Header and footer call control. Pairs with the practice number. |
| `book.svg` | Header and footer **Book** control (calendar). |
| `pin.svg` | Footer address / Wheelers Hill / contact. |
| `menu.svg` | Mobile nav open. |
| `close.svg` | Mobile nav close. |
| `chevron.svg` | Nav dropdown, accordion, select. |
| `arrow.svg` | Inline “view treatment” / text-link affordance. |

Header utilities stay **phone + Book** only. Do not invent extra chrome icons for enquire, download, or gallery.

## Do

- Use this set for every treatment door and every chrome control on launch.
- Keep `currentColor` and the 1.75 stroke.
- Scale 24 → 32 for the demand-door grid only.

## Don’t

- Don’t mix Font Awesome (or any second family) on the same page.
- Don’t recolour per service, hover-tint individual treatments, or add a fill dual-tone.
- Don’t swap `invisalign.svg` for Align Technology’s logo.
- Don’t draw cartoon teeth with faces, sparkles-as-eyes, or a dollar-face.
- Don’t add icons that are not in the table above.
