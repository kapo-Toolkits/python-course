"""მათემატიკური დამხმარე ფუნქციები.

დავალება #2-დან გადმოტანილი — ეს არის „მოდულად დაშლის“ არსი:
ფუნქციები იქ ცხოვრობენ, სადაც ისინი თემატურად ეკუთვნიან.
"""


def is_prime(n):
    """ამოწმებს, მარტივია თუ არა n.

        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True


def convert_temp(value, to="F"):
    """ცელსიუსს გარდაქმნის ფარენჰეიტში ("F") ან კელვინში ("K").

        >>> convert_temp(100)
        212.0
    """
    unit = to.upper()

    if unit == "F":
        return value * 9 / 5 + 32
    if unit == "K":
        return value + 273.15

    return None


def stats(*numbers):
    """აბრუნებს (min, max, sum, mean) ან None ცარიელ გამოძახებაზე.

        >>> stats(4, 8, 15, 16)
        (4, 16, 43, 10.75)
    """
    if not numbers:
        return None

    total = sum(numbers)
    return min(numbers), max(numbers), total, total / len(numbers)


# მოდულის საკუთარი ტესტ-ბლოკი: სრულდება მხოლოდ `python tools/mathtools.py`-ზე,
# იმპორტისას — არა.
if __name__ == "__main__":
    print("is_prime(17):", is_prime(17))
    print("is_prime(1): ", is_prime(1))
    print("convert_temp(100):", convert_temp(100))
    print("convert_temp(0, 'K'):", convert_temp(0, "K"))
    print("stats(4, 8, 15, 16):", stats(4, 8, 15, 16))
