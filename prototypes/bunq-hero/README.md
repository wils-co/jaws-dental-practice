# Bunq hero — agy

agy's night fluid WebGL hero. **Not the live site.** Chip on the page: **agy**.

Grok's own direction is `prototypes/grok-build/`.

Teardown: `~/Dev/brain/03-Resources/topics/bunqlabs-teardown.md`

## What it is

The teardown's 90/10: **one WebGL hero**, everything below is real HTML.

- Hero: three.js r169 ESM — curl-noise velocity + advected dye mist,
  headline refraction, 3k ceramic particles, idle sleep.
- Page: Direction C copy (AHPRA-safe), Instrument Serif + JetBrains Mono,
  film grain, Lenis, light→dark close.
- Stills in `media/` are AI-generated placeholders, watermark-cropped.

## Run

```
cd ~/Dev/Projects/jaws-dental-practice/prototypes/bunq-hero
python3 -m http.server 8898
# http://localhost:8898/
```

`file://` is fine for the DOM page. WebGL stills are not uploaded as
textures (they're `<img>`), so CORS is not an issue here.

## Publish

```
python3 prototypes/publish.py
python3 ~/Dev/Hermes/scripts/topics_catalog.py
```
