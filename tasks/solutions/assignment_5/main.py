"""დავალება #5 — მოდულები, პაკეტები და git (XV კვირა). სანიმუშო ამოხსნა.

პროგრამის შესვლის წერტილი. აქ ლოგიკა აღარაა — მხოლოდ პაკეტის
ფუნქციების გამოძახება. ეს არის „მოდულად დაშლის“ მიზანი.

გაშვება:  python main.py
"""

# 1. სტანდარტული ბიბლიოთეკა (ამ ფაილს არ სჭირდება)
# 2. მესამე მხარის პაკეტები (არ გვაქვს — გარე დამოკიდებულების გარეშე)
# 3. საკუთარი მოდულები
from tools import textutils
from tools.mathtools import convert_temp, is_prime, stats

TEXT = "პითონი მარტივი ენაა და პითონი პოპულარული ენაა."


def main():
    """ყველა მოდულის ერთი დემონსტრაცია."""
    primes = [n for n in range(1, 51) if is_prime(n)]
    print("მარტივი რიცხვები 1–50:")
    print(" ", primes)

    print("\nტემპერატურა:")
    print("  100°C =", convert_temp(100), "°F")
    print("  100°C =", convert_temp(100, "K"), "K")

    print("\nსტატისტიკა:")
    print(" ", stats(*primes))

    print("\nტექსტი:")
    print("  ხმოვნები:        ", textutils.count_vowels(TEXT))
    print("  უნიკალური სიტყვები:", textutils.unique_words(TEXT))
    print("  სიხშირე:         ", textutils.word_frequency(TEXT))


if __name__ == "__main__":
    main()
