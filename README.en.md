[ქართული](README.md) · **English**

# Introduction to Programming (Python) — lecture slide decks

Open educational material — 16 decks for a 15-week introductory course
(15 weeks plus a separate deck on setting up the working environment).

**Live:** https://kapo-toolkits.github.io/python-course/

Fully **bilingual** — Georgian and English. Switch the language with the <kbd>L</kbd>
key or the HUD button; the choice is remembered in the browser.

---

## Structure

```
python-course/
├── index.html                    ← the start page
├── assets/
│   ├── deck.css                  ← the entire design (colors live in :root)
│   └── deck.js                   ← navigation, theme, syntax highlighting
├── lectures/
│   ├── L00-setup.html            environment: Python + VS Code + extensions
│   ├── L01-intro.html            I     introduction
│   ├── L02-types.html            II    types and variables
│   ├── L03-conditions.html       III   conditions       + review + assignment #1
│   ├── L04-loops.html            IV    loops
│   ├── L05-builtins.html         V     built-ins, math, random  + review
│   ├── L06-functions.html        VI    functions        + assignment #2
│   ├── L07-strings.html          VII   strings          + review
│   ├── L08-midterm.html          VIII  midterm — full review (20 questions)
│   ├── L09-files.html            IX    files
│   ├── L10-lists.html            X     lists and tuples
│   ├── L11-set-dict.html         XI    sets and dicts   + review + assignment #3
│   ├── L12-exceptions.html       XII   errors
│   ├── L13-iterators.html        XIII  iterators        + review + assignment #4
│   ├── L14-pep8-pypi.html        XIV   PEP 8 and PyPI
│   └── L15-modules-git.html      XV    modules and git  + review + assignment #5
├── tasks/
│   ├── practical-assignments.en.md   ← all five practical assignments (to hand out)
│   ├── practical-assignments.md      the same, in Georgian
│   └── solutions/                ← reference solutions + common mistakes (Georgian only)
└── library/                      ← kapo-mathtools — a PyPI package (pip install kapo-mathtools)
    ├── kapo_mathtools/           statistics · geometry · text_tools · converters
    ├── tests/
    ├── examples/demo.py
    └── pyproject.toml
```

No dependencies, no build step, no CDN. Open any `.html` file straight in a
browser — from a web server or from `file://`, online or offline.

---

## Keyboard

| Key | Action |
|---|---|
| `→` `←` `Space` `PgUp` `PgDn` | navigate |
| `Home` `End` | first / last slide |
| `O` | slide outline (jump to one) |
| `N` | **lecturer's notes** — hints visible only to you |
| `S` | **presenter view** — a second window: current + next slide, note, timer |
| `L` | language: Georgian / English (remembered) |
| `D` | light / dark theme (remembered) |
| `F` | fullscreen |
| `P` | print → PDF |

On a phone or tablet — swipe.
A `#7` at the end of the URL jumps straight to slide 7 — handy for sharing a link;
`#7p` opens that same slide directly in the presenter view.

### Presenter view

<kbd>S</kbd> opens a second window showing the **current** slide, the **next** one,
this slide's note and a lecture timer (alongside the clock). The two windows stay
in sync — navigation, language and theme change in both at once.

Move the main window to the projector and put it fullscreen with <kbd>F</kbd>;
leave the presenter window on your laptop. The sync uses `postMessage`, so it
works from `file://` too — no server required.

---

## License

See [`LICENSE`](LICENSE):

- **The engine** (`assets/deck.css`, `assets/deck.js`) — **MIT**
- **The course content** (`lectures/`, `tasks/`, `index.html`) — **CC BY 4.0**
