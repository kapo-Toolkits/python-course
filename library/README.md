# kapo-mathtools

**მარტივი მათემატიკური ხელსაწყოები Python-ისთვის.**
სასწავლო ბიბლიოთეკა ქართული დოკუმენტაციით, **გარე დამოკიდებულების გარეშე**.

**Simple math tools for Python.**
A small teaching library with bilingual documentation and **zero dependencies**.

```bash
pip install kapo-mathtools
```

```python
from kapo_mathtools import statistics, geometry, text_tools, converters

statistics.mean([85, 90, 78, 92])      # 86.25
geometry.circle_area(5)                # 78.53981633974483
text_tools.is_palindrome("radar")      # True
converters.celsius_to_fahrenheit(25)   # 77.0
```

მოითხოვს Python 3.9+ · Requires Python 3.9+

---

## `statistics` — სტატისტიკა / Statistics

| ფუნქცია / Function | აღწერა | Description |
|---|---|---|
| `mean(numbers)` | საშუალო არითმეტიკული | Arithmetic mean |
| `median(numbers)` | მედიანა | Median |
| `variance(numbers)` | დისპერსია | Variance |
| `std_dev(numbers)` | სტანდარტული გადახრა | Standard deviation |

```python
from kapo_mathtools import statistics

scores = [85, 90, 78, 92, 88]
statistics.mean(scores)      # 86.6
statistics.median(scores)    # 88
statistics.std_dev(scores)   # 4.882622246293481
```

ცარიელ სიაზე ისვრის `ValueError`-ს. `variance` და `std_dev` **გენერალურ ერთობლიობას**
ითვლის (გაყოფა `n`-ზე, არა `n-1`-ზე).

Raises `ValueError` on an empty list. `variance` and `std_dev` compute the
**population** statistics (divide by `n`, not `n-1`).

## `geometry` — გეომეტრია / Geometry

| ფუნქცია / Function | აღწერა | Description |
|---|---|---|
| `circle_area(radius)` | წრის ფართობი | Area of a circle |
| `circle_circumference(radius)` | წრეწირის სიგრძე | Circumference of a circle |
| `rectangle_area(length, width)` | მართკუთხედის ფართობი | Area of a rectangle |
| `rectangle_perimeter(length, width)` | მართკუთხედის პერიმეტრი | Perimeter of a rectangle |
| `triangle_area(base, height)` | სამკუთხედის ფართობი | Area of a triangle |

```python
from kapo_mathtools import geometry

geometry.circle_area(5)             # 78.53981633974483
geometry.rectangle_area(4, 6)       # 24
geometry.triangle_area(10, 5)       # 25.0
```

უარყოფით რადიუსზე ისვრის `ValueError`-ს. · Raises `ValueError` for a negative radius.

## `text_tools` — ტექსტი / Text

| ფუნქცია / Function | აღწერა | Description |
|---|---|---|
| `count_words(text)` | სიტყვების რაოდენობა | Word count |
| `count_chars(text, include_spaces=False)` | სიმბოლოების რაოდენობა | Character count |
| `reverse_text(text)` | ტექსტის შებრუნება | Reverse the text |
| `is_palindrome(text)` | პალინდრომია? | Is it a palindrome? |
| `capitalize_words(text)` | ყოველი სიტყვის პირველი ასო დიდი | Title-case the text |
| `count_vowels(text)` | ხმოვნების რაოდენობა | Vowel count |

```python
from kapo_mathtools import text_tools

text_tools.count_words("გამარჯობა მსოფლიო")               # 2
text_tools.is_palindrome("A man a plan a canal Panama")   # True
text_tools.reverse_text("Python")                         # 'nohtyP'
```

`is_palindrome` უგულებელყოფს ჰარეებს და რეგისტრს, პუნქტუაციას — არა.
`count_vowels` ითვლის მხოლოდ ინგლისურ ხმოვნებს (`aeiou`).

`is_palindrome` ignores spaces and letter case, but not punctuation.
`count_vowels` counts English vowels only (`aeiou`).

## `converters` — ერთეულების კონვერტაცია / Unit conversion

| ფუნქცია / Function | აღწერა | Description |
|---|---|---|
| `celsius_to_fahrenheit(c)` · `fahrenheit_to_celsius(f)` | ტემპერატურა | Temperature |
| `kilometers_to_miles(km)` · `miles_to_kilometers(mi)` | მანძილი | Distance |
| `kilograms_to_pounds(kg)` · `pounds_to_kilograms(lb)` | წონა | Weight |
| `meters_to_feet(m)` · `feet_to_meters(ft)` | სიგრძე | Length |

```python
from kapo_mathtools import converters

converters.celsius_to_fahrenheit(25)   # 77.0
converters.kilometers_to_miles(10)     # 6.21371
converters.kilograms_to_pounds(70)     # 154.3234
```

---

## დახმარება / Built-in help

ყველა ფუნქციას აქვს ქართული docstring მაგალითით.
Every function carries a docstring with a worked example.

```python
from kapo_mathtools import statistics

help(statistics.mean)
print(statistics.median.__doc__)
```

## ლიცენზია / License

MIT — see [`LICENSE`](LICENSE).

ბიბლიოთეკა შექმნილია სასწავლო კურსისთვის
**[პროგრამირების საწყისები (Python)](https://kapo-toolkits.github.io/python-course/)**.

Built for the open course *Programming Essentials (Python)* —
source in the [`library/`](https://github.com/kapo-Toolkits/python-course/tree/main/library)
folder of the course repository.
