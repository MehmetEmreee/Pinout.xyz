# Gemstone Pinout

Gemstone Pinout is an interactive GPIO and expansion-header reference for the
T3 Gemstone O1 development board. It documents the physical 40-pin header,
compatibility GPIO numbers, power rails and supported peripheral interfaces in
English and Turkish.

The site is derived from the open-source [Pinout.xyz](https://pinout.xyz/)
project. Its presentation and static-site generator are reused under the
[Creative Commons Attribution-ShareAlike 4.0 International
License](https://creativecommons.org/licenses/by-sa/4.0/). T3 Gemstone board
data is cross-checked against the [official T3 Gemstone
documentation](https://docs.t3gemstone.org/en/boards/o1/introduction).

## What the site guarantees

- The diagram follows the physical T3-GEM-O1 40-pin header orientation.
- GPIO values are compatibility numbers, not native AM67A controller/line IDs.
- Peripheral pages document Gemstone-specific Linux and device-tree behavior.
- Raspberry Pi HATs are not assumed compatible merely because the connector
  fits. The catalogue publishes only reviewed `verified` or `conditional`
  boards.
- Unverified Raspberry Pi alternate pin functions are intentionally omitted.

## Local development

Create a virtual environment, install the dependencies and build the site:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pinoutxyz build en tr --site --strict
.venv/bin/python -m http.server 8765 --directory output/site
```

Then open <http://127.0.0.1:8765/>. The Turkish version is available at
<http://127.0.0.1:8765/tr/>.

Useful checks:

```bash
.venv/bin/python -m pinoutxyz translations check en tr
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q pinoutxyz
git diff --check
```

## Adding a compatible board

Copy `draft/overlay/template.md`, complete its metadata and add a transparent
top-down PNG under `draft/boards/`. Every submission must include one of these
review states:

- `verified`: electrical, pin, device-tree and driver compatibility confirmed.
- `conditional`: usable only with documented setup or limitations.
- `incompatible`: recorded as rejected and not published in the catalogue.

Validate and preview a draft with:

```bash
python3 -m pinoutxyz boards check my-board
python3 -m pinoutxyz boards publish my-board
python3 -m pinoutxyz build en tr --site --strict
```

Return it to the draft area after review with:

```bash
python3 -m pinoutxyz boards unpublish my-board
```

## Content layout

- `src/en/template/pinout.yaml`: authoritative T3-GEM-O1 header mapping.
- `src/*/overlay/`: interface documentation and reviewed add-on boards.
- `common/`: shared HTML templates.
- `resources/`: stylesheets, scripts and board artwork.
- `site.yaml`: enabled languages and board identity.

## Attribution and licensing

The Pinout.xyz project and generator were created and maintained by its
upstream contributors, including
[@Gadgetoid](https://github.com/Gadgetoid) and
[@RogueM](https://github.com/RogueM). The site footer retains visible upstream
attribution.

Unless a file states otherwise, inherited Pinout.xyz content and modifications
remain available under CC BY-SA 4.0. Product images and third-party marks may
have separate terms; consult their respective owners before reuse.
