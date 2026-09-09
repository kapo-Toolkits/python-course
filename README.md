# პროგრამირების საწყისები (Python) — სალექციო პრეზენტაციები

ღია სასწავლო მასალა — 15-კვირიანი შესავალი კურსის 16 პრეზენტაცია
(15 კვირა + სამუშაო გარემოს მომზადების ცალკე დეკი).

სრულად **ორენოვანია** — ქართული და English. ენა გადაირთვება <kbd>L</kbd> კლავიშით
ან HUD-ის ღილაკით და ინახება ბრაუზერში.

---

## სტრუქტურა

```
python-course/
├── index.html                    ← სასტარტო გვერდი
├── assets/
│   ├── deck.css                  ← მთელი დიზაინი (ფერები :root-ში)
│   └── deck.js                   ← ნავიგაცია, თემა, სინტაქსის ხაზგასმა
├── lectures/
│   ├── L00-setup.html            გარემო: Python + VS Code + დანამატები
│   ├── L01-intro.html            I     შესავალი
│   ├── L02-types.html            II    ტიპები და ცვლადები
│   ├── L03-conditions.html       III   პირობები          + გამეორება + დავალება #1
│   ├── L04-loops.html            IV    ციკლები
│   ├── L05-builtins.html         V     ჩაშენებული, math, random  + გამეორება
│   ├── L06-functions.html        VI    ფუნქციები          + დავალება #2
│   ├── L07-strings.html          VII   სტრიქონები        + გამეორება
│   ├── L08-midterm.html          VIII  შუალედური — სრული გამეორება (20 კითხვა)
│   ├── L09-files.html            IX    ფაილები
│   ├── L10-lists.html            X     სიები და tuple
│   ├── L11-set-dict.html         XI    set და dict        + გამეორება + დავალება #3
│   ├── L12-exceptions.html       XII   შეცდომები
│   ├── L13-iterators.html        XIII  იტერატორები       + გამეორება + დავალება #4
│   ├── L14-pep8-pypi.html        XIV   PEP 8 და PyPI
│   └── L15-modules-git.html      XV    მოდულები და git    + გამეორება + დავალება #5
├── tasks/
│   └── practical-assignments.md  ← ხუთივე პრაქტიკული დავალება ერთად (დასარიგებლად)
└── library/                      ← kapo-mathtools — PyPI პაკეტი (pip install kapo-mathtools)
    ├── kapo_mathtools/           statistics · geometry · text_tools · converters
    ├── tests/
    ├── examples/demo.py
    └── pyproject.toml
```

---

## კლავიატურა

| კლავიში | მოქმედება |
|---|---|
| `→` `←` `Space` `PgUp` `PgDn` | ნავიგაცია |
| `Home` `End` | პირველი / ბოლო სლაიდი |
| `O` | სლაიდების სია (გადახტომა) |
| `N` | **ლექტორის ჩანაწერები** — მხოლოდ შენთვის ხილული მინიშნებები |
| `L` | ენა: ქართული / English (ინახება) |
| `D` | ღია / მუქი თემა (ინახება) |
| `F` | სრული ეკრანი |
| `P` | ბეჭდვა → PDF |

მობილურზე / ტაბლეტზე — გადაფურცვლა (swipe).
URL-ის ბოლოს `#7` პირდაპირ მე-7 სლაიდზე გადადის — მოსახერხებელია ბმულის გასაზიარებლად.

---

## ლიცენზია

იხ. [`LICENSE`](LICENSE):

- **ძრავი** (`assets/deck.css`, `assets/deck.js`) — **MIT**
- **სალექციო შინაარსი** (`lectures/`, `tasks/`, `index.html`) — **CC BY 4.0**
