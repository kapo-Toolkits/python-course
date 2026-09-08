# kapo-mathtools

მარტივი მათემატიკური ხელსაწყოები Python-ისთვის. სასწავლო დანიშნულების
ბიბლიოთეკა ქართული დოკუმენტაციით, **გარე დამოკიდებულების გარეშე**.

```bash
pip install kapo-mathtools
```

```python
from kapo_mathtools import statistics, geometry, text_tools, converters

print(statistics.mean([85, 90, 78, 92]))      # 86.25
print(geometry.circle_area(5))                # 78.53981633974483
print(text_tools.is_palindrome("radar"))      # True
print(converters.celsius_to_fahrenheit(25))   # 77.0
```

---

## `statistics` — სტატისტიკა

| ფუნქცია | აღწერა |
|---|---|
| `mean(numbers)` | საშუალო არითმეტიკული |
| `median(numbers)` | მედიანა |
| `variance(numbers)` | დისპერსია |
| `std_dev(numbers)` | სტანდარტული გადახრა |

```python
from kapo_mathtools import statistics

scores = [85, 90, 78, 92, 88]
statistics.mean(scores)      # 86.6
statistics.median(scores)    # 88
statistics.std_dev(scores)   # 4.882622246293481
```

ცარიელ სიაზე ისვრის `ValueError`-ს.
`variance` და `std_dev` **გენერალურ ერთობლიობას** ითვლის (გაყოფა `n`-ზე, არა `n-1`-ზე).

## `geometry` — გეომეტრია

| ფუნქცია | აღწერა |
|---|---|
| `circle_area(radius)` | წრის ფართობი |
| `circle_circumference(radius)` | წრეწირის სიგრძე |
| `rectangle_area(length, width)` | მართკუთხედის ფართობი |
| `rectangle_perimeter(length, width)` | მართკუთხედის პერიმეტრი |
| `triangle_area(base, height)` | სამკუთხედის ფართობი |

```python
from kapo_mathtools import geometry

geometry.circle_area(5)             # 78.53981633974483
geometry.rectangle_area(4, 6)       # 24
geometry.triangle_area(10, 5)       # 25.0
```

## `text_tools` — ტექსტი

| ფუნქცია | აღწერა |
|---|---|
| `count_words(text)` | სიტყვების რაოდენობა |
| `count_chars(text, include_spaces=False)` | სიმბოლოების რაოდენობა |
| `reverse_text(text)` | ტექსტის შებრუნება |
| `is_palindrome(text)` | პალინდრომია? (ჰარეებს უგულებელყოფს, პუნქტუაციას — არა) |
| `capitalize_words(text)` | ყოველი სიტყვის პირველი ასო დიდი |
| `count_vowels(text)` | ხმოვნების რაოდენობა (ინგლისური `aeiou`) |

```python
from kapo_mathtools import text_tools

text_tools.count_words("გამარჯობა მსოფლიო")   # 2
text_tools.is_palindrome("A man a plan a canal Panama")  # True
text_tools.reverse_text("Python")             # 'nohtyP'
```

## `converters` — ერთეულების კონვერტაცია

| ფუნქცია | აღწერა |
|---|---|
| `celsius_to_fahrenheit(celsius)` · `fahrenheit_to_celsius(fahrenheit)` | ტემპერატურა |
| `kilometers_to_miles(km)` · `miles_to_kilometers(miles)` | მანძილი |
| `kilograms_to_pounds(kg)` · `pounds_to_kilograms(pounds)` | წონა |
| `meters_to_feet(meters)` · `feet_to_meters(feet)` | სიგრძე |

```python
from kapo_mathtools import converters

converters.celsius_to_fahrenheit(25)   # 77.0
converters.kilometers_to_miles(10)     # 6.21371
converters.kilograms_to_pounds(70)     # 154.3234
```

---

## დახმარება პირდაპირ Python-ში

ყველა ფუნქციას აქვს ქართული docstring მაგალითით:

```python
from kapo_mathtools import statistics

help(statistics.mean)
print(statistics.median.__doc__)
```

## ლიცენზია

MIT — იხ. [`LICENSE`](LICENSE).

ბიბლიოთეკა შექმნილია სასწავლო კურსისთვის
**[პროგრამირების საწყისები (Python)](https://kapo-toolkits.github.io/python-course/)**.
