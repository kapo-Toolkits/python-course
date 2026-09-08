"""
kapo-mathtools ბიბლიოთეკის გამოყენების მაგალითები
"""

from kapo_mathtools import statistics, geometry, text_tools, converters

print("=" * 50)
print("სტატისტიკური გამოთვლები")
print("=" * 50)

# რიცხვების სია
numbers = [85, 90, 78, 92, 88, 76, 95, 89]

print(f"რიცხვები: {numbers}")
print(f"საშუალო: {statistics.mean(numbers):.2f}")
print(f"მედიანა: {statistics.median(numbers)}")
print(f"დისპერსია: {statistics.variance(numbers):.2f}")
print(f"სტანდარტული გადახრა: {statistics.std_dev(numbers):.2f}")

print("\n" + "=" * 50)
print("გეომეტრიული გამოთვლები")
print("=" * 50)

# წრის გამოთვლები
radius = 5
print(f"\nწრე რადიუსით {radius}:")
print(f"  ფართობი: {geometry.circle_area(radius):.2f}")
print(f"  გარშემოწერილობა: {geometry.circle_circumference(radius):.2f}")

# მართკუთხედის გამოთვლები
length, width = 10, 6
print(f"\nმართკუთხედი {length}x{width}:")
print(f"  ფართობი: {geometry.rectangle_area(length, width)}")
print(f"  პერიმეტრი: {geometry.rectangle_perimeter(length, width)}")

# სამკუთხედის გამოთვლები
base, height = 8, 5
print(f"\nსამკუთხედი (ფუძე={base}, სიმაღლე={height}):")
print(f"  ფართობი: {geometry.triangle_area(base, height)}")

print("\n" + "=" * 50)
print("ტექსტის დამუშავება")
print("=" * 50)

text = "Python Programming"
print(f"\nტექსტი: '{text}'")
print(f"  სიტყვების რაოდენობა: {text_tools.count_words(text)}")
print(f"  სიმბოლოების რაოდენობა (space-ების გარეშე): {text_tools.count_chars(text)}")
print(f"  სიმბოლოების რაოდენობა (space-ებით): {text_tools.count_chars(text, include_spaces=True)}")
print(f"  შებრუნებული: '{text_tools.reverse_text(text)}'")
print(f"  ხმოვანების რაოდენობა: {text_tools.count_vowels(text)}")

palindrome = "radar"
print(f"\n'{palindrome}' პალინდრომია? {text_tools.is_palindrome(palindrome)}")
print(f"'{text}' პალინდრომია? {text_tools.is_palindrome(text)}")

print("\n" + "=" * 50)
print("ერთეულების კონვერტაცია")
print("=" * 50)

print(f"\nტემპერატურა:")
print(f"  25°C = {converters.celsius_to_fahrenheit(25):.1f}°F")
print(f"  77°F = {converters.fahrenheit_to_celsius(77):.1f}°C")

print(f"\nმანძილი:")
print(f"  10 კმ = {converters.kilometers_to_miles(10):.2f} მილი")
print(f"  10 მილი = {converters.miles_to_kilometers(10):.2f} კმ")

print(f"\nწონა:")
print(f"  10 კგ = {converters.kilograms_to_pounds(10):.2f} ფუნტი")
print(f"  10 ფუნტი = {converters.pounds_to_kilograms(10):.2f} კგ")

print(f"\nსიგრძე:")
print(f"  10 მ = {converters.meters_to_feet(10):.2f} ფუტი")
print(f"  10 ფუტი = {converters.feet_to_meters(10):.2f} მ")

