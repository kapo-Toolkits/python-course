"""დავალება #3 — set და dict (XI კვირა). სანიმუშო ამოხსნა.

წინაპირობა: ლექციები 07–11.
სატელეფონო წიგნაკის მენიუ ინტერაქციულია, ამიტომ მისი ლოგიკა ცალკე
ფუნქციებადაა გატანილი — ასე ის შემოწმებადია მენიუს გაშვების გარეშე.

გაშვება:  python assignment_3.py          — 1–3 და 5 დავალება
          python assignment_3.py phones   — სატელეფონო წიგნაკის მენიუ
"""

import sys
from pathlib import Path

TEXT = (
    "პითონი მარტივი ენაა და პითონი პოპულარული ენაა. "
    "ენა მარტივია, ენა კითხვადია, პითონი კი ყველგან გვხვდება."
)

PHONE_FILE = Path(__file__).with_name("phonebook.txt")


# ─────────────────────────────────────────────────────────────
# 1. უნიკალური სიტყვები
# ─────────────────────────────────────────────────────────────
def unique_words(text):
    """აბრუნებს ტექსტის უნიკალურ სიტყვებს ანბანურად დახარისხებულს.

    პუნქტუაცია ცალკე სიტყვად რომ არ ჩაითვალოს, ვასუფთავებთ.

        >>> unique_words("ენა, ენა და ენა!")
        ['და', 'ენა']
    """
    words = set()

    for raw in text.lower().split():
        word = raw.strip(".,!?;:„“\"'()")
        if word:                       # ცარიელი არ დაემატოს
            words.add(word)

    return sorted(words)


# ─────────────────────────────────────────────────────────────
# 2. ორი ჯგუფის შედარება
# ─────────────────────────────────────────────────────────────
def compare_groups(group_a, group_b):
    """აბრუნებს (საერთო, მხოლოდ_პირველში, მხოლოდ_მეორეში).

        >>> compare_groups({"ანა", "ბექა"}, {"ბექა", "გიო"})
        (['ბექა'], ['ანა'], ['გიო'])
    """
    return (
        sorted(group_a & group_b),     # თანაკვეთა
        sorted(group_a - group_b),      # სხვაობა
        sorted(group_b - group_a),
    )


# ─────────────────────────────────────────────────────────────
# 3. სიტყვების სიხშირე
# ─────────────────────────────────────────────────────────────
def word_frequency(text):
    """აბრუნებს ლექსიკონს {სიტყვა: რაოდენობა}.

        >>> word_frequency("ენა ენა და")["ენა"]
        2
    """
    counts = {}

    for raw in text.lower().split():
        word = raw.strip(".,!?;:„“\"'()")
        if not word:
            continue
        # get() ჩავარდნის ნაცვლად ნაგულისხმევს აბრუნებს — KeyError არ გვექნება
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_words(counts, n=5):
    """აბრუნებს n ყველაზე ხშირ სიტყვას — სიხშირით კლებადად.

    თანაბარი სიხშირისას ანბანური რიგი ინახება: `-count` კლებადია,
    `word` კი ზრდადი, ამიტომ შედეგი ყოველთვის ერთი და იგივეა.
    """
    ordered = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ordered[:n]


# ─────────────────────────────────────────────────────────────
# 4. სატელეფონო წიგნაკი
# ─────────────────────────────────────────────────────────────
def load_phones(path=PHONE_FILE):
    """კითხულობს წიგნაკს ფაილიდან. ფაილის არარსებობა შეცდომა არაა."""
    phones = {}

    if not path.exists():
        return phones

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, _, number = line.partition(",")
            phones[name.strip()] = number.strip()

    return phones


def save_phones(phones, path=PHONE_FILE):
    """ჩაწერს წიგნაკს ფაილში. encoding="utf-8" ქართული სახელებისთვის."""
    with open(path, "w", encoding="utf-8") as f:
        for name, number in sorted(phones.items()):
            f.write(f"{name},{number}\n")


def phone_menu():                      # pragma: no cover — ინტერაქციული
    """მარტივი ტექსტური მენიუ."""
    phones = load_phones()

    while True:
        print("\n1 დამატება · 2 ძებნა · 3 წაშლა · 4 სია · 0 გასვლა")
        choice = input("არჩევანი: ").strip()

        if choice == "1":
            name = input("სახელი: ").strip()
            phones[name] = input("ნომერი: ").strip()
            save_phones(phones)
            print("დამატებულია.")

        elif choice == "2":
            name = input("სახელი: ").strip()
            # get() — [] KeyError-ს ისვრის, get() კი None-ს აბრუნებს
            number = phones.get(name)
            print(f"{name}: {number}" if number else "ვერ მოიძებნა.")

        elif choice == "3":
            name = input("სახელი: ").strip()
            if phones.pop(name, None) is None:
                print("ვერ მოიძებნა.")
            else:
                save_phones(phones)
                print("წაშლილია.")

        elif choice == "4":
            if not phones:
                print("წიგნაკი ცარიელია.")
            for name, number in sorted(phones.items()):
                print(f"  {name:<15} {number}")

        elif choice == "0":
            break

        else:
            print("ასეთი პუნქტი არ არის.")


# ─────────────────────────────────────────────────────────────
# 5. უწყისი
# ─────────────────────────────────────────────────────────────
STUDENTS = [
    {"name": "ანა ბერიძე", "scores": [88, 92, 79]},
    {"name": "ბექა ლომიძე", "scores": [65, 71, 68]},
    {"name": "გიორგი ნოზაძე", "scores": [95, 90, 98]},
    {"name": "დავით კვარაცხელია", "scores": [55, 61, 49]},
]


def gradebook(students):
    """აბრუნებს უწყისს ტექსტად — საშუალოთი კლებადად დახარისხებულს."""
    rows = sorted(
        students,
        key=lambda s: sum(s["scores"]) / len(s["scores"]),
        reverse=True,
    )

    # :<20 და :>6 — გასწორება, რომ სვეტები ერთმანეთის ქვეშ დადგეს
    lines = [f"{'სახელი':<20}{'ქულები':>14}{'საშუალო':>10}"]
    lines.append("-" * 44)

    for student in rows:
        scores = student["scores"]
        average = sum(scores) / len(scores)
        printed = " ".join(f"{s:>3}" for s in scores)
        lines.append(f"{student['name']:<20}{printed:>14}{average:>10.2f}")

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "phones":
        phone_menu()
        sys.exit()

    print("1) უნიკალური სიტყვები:")
    print("  ", unique_words(TEXT))

    group_1 = {"ანა", "ბექა", "გიორგი", "დავითი"}
    group_2 = {"ბექა", "დავითი", "ელენე"}
    both, only_1, only_2 = compare_groups(group_1, group_2)
    print("\n2) ორივეში:", both)
    print("   მხოლოდ I ჯგუფში:", only_1)
    print("   მხოლოდ II ჯგუფში:", only_2)

    print("\n3) 5 ყველაზე ხშირი სიტყვა:")
    for word, count in top_words(word_frequency(TEXT)):
        print(f"   {word:<12} {count}")

    print("\n5) უწყისი:")
    print(gradebook(STUDENTS))

    print("\n(სატელეფონო წიგნაკი: python assignment_3.py phones)")


# ═════════════════════════════════════════════════════════════
# შემფასებლისთვის — ტიპური შეცდომები ამ დავალებაში
# ═════════════════════════════════════════════════════════════
#
# 1) `set()`-ის ნაცვლად `{}` — ცარიელი ლექსიკონი მიიღება, არა სიმრავლე.
#    შემდეგ `.add()` → AttributeError. ეს კლასიკური ხაფანგია (ლექცია 11).
#
# 2) პუნქტუაციის გაუსუფთავებლობა: "ენაა." და "ენაა" ორ სხვადასხვა
#    სიტყვად ჩაითვლება და სიხშირე არასწორია. `.strip(...)` ან `replace`.
#    ასევე `.lower()`-ის დავიწყება — ლათინურ ტექსტზე "The" ≠ "the".
#
# 3) სიხშირისთვის `counts[word] += 1` პირდაპირ → KeyError პირველივე
#    სიტყვაზე. სწორია `get(word, 0) + 1` ან წინასწარი `if word not in counts`.
#    `collections.Counter` კურსში გავლილი არაა — თუ იპოვა და გამოიყენა,
#    ბონუსია; მაგრამ სთხოვე ხელით ვარიანტიც ახსნას.
#
# 4) დახარისხება სიხშირით: `sorted(counts)` მხოლოდ გასაღებებს ალაგებს.
#    საჭიროა `counts.items()` + `key=`. `reverse=True`-ს დავიწყება ხშირია.
#
# 5) ფაილი `encoding="utf-8"`-ის გარეშე — Windows-ზე ქართული სახელები
#    UnicodeDecodeError-ს ან „ჯართს“ იძლევა. ეს პირდაპირ შემოწმებადია.
#
# 6) ძებნისას `phones[name]` `get()`-ის ნაცვლად → KeyError არარსებულ
#    სახელზე. დავალების პირობაში `get` პირდაპირ მოთხოვნილია.
#
# 7) უწყისში გასწორება ჰარეებით ხელით (`name + "    "`) — მუშაობს
#    მხოლოდ ერთი სიგრძის სახელებზე. `f"{name:<20}"` სწორი პასუხია.
