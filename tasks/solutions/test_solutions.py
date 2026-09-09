"""ამოხსნების შემოწმება — რომ ისინი მართლა მუშაობდეს.

ეს ფაილი კურსის მასალა არ არის; ის მხოლოდ იმას იცავს, რომ ამ საქაღალდეში
გამოქვეყნებული სანიმუშო ამოხსნები დროთა განმავლობაში არ გაფუჭდეს.

გაშვება (pytest არ სჭირდება):
    python test_solutions.py

pytest-ითაც მუშაობს, doctest-ებთან ერთად:
    pytest --doctest-modules
"""

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import assignment_2 as a2          # noqa: E402
import assignment_3 as a3          # noqa: E402
import assignment_4 as a4          # noqa: E402


# ─────────────────────────────────────────────────────────────
# დავალება #1 — ინტერაქციულია, ამიტომ ცალკე პროცესად ვუშვებთ
# ─────────────────────────────────────────────────────────────
def test_assignment_1():
    """ექვსი პასუხი: რიცხვი · სამი რიცხვი · ქულა · ასაკი."""
    result = subprocess.run(
        [sys.executable, str(HERE / "assignment_1.py")],
        input="7\n3\n9\n5\n85\n70\n",
        capture_output=True, text=True, encoding="utf-8", timeout=30,
    )
    assert result.returncode == 0, result.stderr
    out = result.stdout

    assert "კენტი, დადებითი" in out
    assert "უდიდესი: 9" in out
    assert "B — ძალიან კარგი" in out
    assert "14.00" in out                     # 70 წელი → 20 * 0.7


# ─────────────────────────────────────────────────────────────
# დავალება #2
# ─────────────────────────────────────────────────────────────
def test_is_prime():
    assert [n for n in range(1, 20) if a2.is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]
    assert a2.is_prime(0) is False
    assert a2.is_prime(1) is False
    assert a2.is_prime(2) is True             # კიდურა შემთხვევა
    assert a2.is_prime(-7) is False


def test_convert_temp():
    assert a2.convert_temp(100) == 212.0
    assert a2.convert_temp(-40) == -40.0      # ერთადერთი წერტილი, სადაც ემთხვევა
    assert a2.convert_temp(0, "K") == 273.15
    assert a2.convert_temp(0, "k") == 273.15  # რეგისტრი მნიშვნელობა არ უნდა ჰქონდეს
    assert a2.convert_temp(0, "X") is None


def test_stats():
    assert a2.stats(4, 8, 15, 16) == (4, 16, 43, 10.75)
    assert a2.stats(5) == (5, 5, 5, 5.0)
    assert a2.stats() is None                 # კიდურა შემთხვევა


def test_count_vowels():
    assert a2.count_vowels("Hello World") == 3
    assert a2.count_vowels("") == 0
    assert a2.count_vowels("პითონი") == 3
    assert a2.count_vowels("bcdfg") == 0


# ─────────────────────────────────────────────────────────────
# დავალება #3
# ─────────────────────────────────────────────────────────────
def test_unique_words():
    assert a3.unique_words("ენა, ენა და ენა!") == ["და", "ენა"]
    assert a3.unique_words("") == []
    assert a3.unique_words("The the THE") == ["the"]


def test_compare_groups():
    both, only_a, only_b = a3.compare_groups({"ა", "ბ", "გ"}, {"ბ", "გ", "დ"})
    assert both == ["ბ", "გ"]
    assert only_a == ["ა"]
    assert only_b == ["დ"]


def test_word_frequency():
    counts = a3.word_frequency("ენა ენა და ენა, კი")
    assert counts["ენა"] == 3
    assert counts["და"] == 1
    assert a3.top_words(counts, 2) == [("ენა", 3), ("და", 1)]


def test_phonebook_roundtrip():
    """ჩაწერა → წაკითხვა დროებით ფაილში, ქართული სახელებით."""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "phones.txt"
        a3.save_phones({"ანა ბერიძე": "555-11-22", "ბექა": "555-33-44"}, path)
        loaded = a3.load_phones(path)
        missing = a3.load_phones(Path(tmp) / "არაა.txt")

    assert loaded == {"ანა ბერიძე": "555-11-22", "ბექა": "555-33-44"}
    assert missing == {}          # არარსებული ფაილი შეცდომა არაა


def test_gradebook_sorted_by_average():
    table = a3.gradebook(a3.STUDENTS)
    lines = table.splitlines()[2:]                        # სათაური და ხაზი გამოვტოვოთ
    averages = [float(line.split()[-1]) for line in lines]
    assert averages == sorted(averages, reverse=True)
    assert "გიორგი ნოზაძე" in lines[0]                    # ყველაზე მაღალი საშუალო


# ─────────────────────────────────────────────────────────────
# დავალება #4
# ─────────────────────────────────────────────────────────────
def test_manual_walk():
    assert a4.manual_walk([10, 20, 30]) == [10, 20, 30]
    assert a4.manual_walk([]) == []
    assert a4.manual_walk("აბგ") == ["ა", "ბ", "გ"]


def test_even_numbers_is_a_generator():
    gen = a4.even_numbers(10)
    assert hasattr(gen, "__next__"), "yield-ის ნაცვლად სია დაბრუნდა"
    assert list(gen) == [0, 2, 4, 6, 8]
    assert list(gen) == [], "იტერატორი ერთჯერადია"


def test_memory_comparison():
    gen_size, list_size = a4.memory_comparison(100_000)
    assert gen_size < 1000                    # გენერატორი მუდმივი ზომისაა
    assert list_size > 100 * gen_size         # სია რამდენიმე რიგით დიდია


def test_fibonacci():
    import itertools
    assert list(itertools.islice(a4.fibonacci(), 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_pipeline():
    with tempfile.TemporaryDirectory() as tmp:
        log = a4.make_sample_log(Path(tmp) / "test.log")
        messages = list(a4.error_messages(log))

    assert messages == ["ბაზასთან კავშირი გაწყდა", "ავტორიზაცია ვერ მოხერხდა"]


# ─────────────────────────────────────────────────────────────
# დავალება #5 — პაკეტი
# ─────────────────────────────────────────────────────────────
def test_assignment_5_package():
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=str(HERE / "assignment_5"),
        capture_output=True, text=True, encoding="utf-8", timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert "მარტივი რიცხვები" in result.stdout


def test_assignment_5_module_blocks():
    """თითოეული მოდული დამოუკიდებლადაც უნდა გაეშვას."""
    for module in ["tools/mathtools.py", "tools/textutils.py"]:
        result = subprocess.run(
            [sys.executable, module],
            cwd=str(HERE / "assignment_5"),
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        assert result.returncode == 0, f"{module}: {result.stderr}"
        assert result.stdout.strip(), f"{module}-ს ტესტ-ბლოკი არაფერს ბეჭდავს"


def test_assignment_5_gitignore():
    text = (HERE / "assignment_5" / ".gitignore").read_text(encoding="utf-8")
    assert "__pycache__/" in text
    assert ".venv/" in text


# ─────────────────────────────────────────────────────────────
# docstring-ების მაგალითებიც ნამდვილი უნდა იყოს
# ─────────────────────────────────────────────────────────────
def test_doctests():
    """ყველა `>>>` მაგალითი ნამდვილად უნდა მუშაობდეს."""
    import doctest
    import importlib

    sys.path.insert(0, str(HERE / "assignment_5"))
    attempted = failed = 0

    for name in ["assignment_2", "assignment_3", "assignment_4",
                 "tools.mathtools", "tools.textutils"]:
        result = doctest.testmod(importlib.import_module(name), verbose=False)
        attempted += result.attempted
        failed += result.failed

    assert attempted > 20, f"მხოლოდ {attempted} doctest მოიძებნა"
    assert failed == 0, f"{failed} doctest ვერ გავიდა"


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    tests = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]

    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ok   {name}")
        except AssertionError as error:
            failed += 1
            print(f"  FAIL {name}: {error}")

    print(f"\n{len(tests) - failed}/{len(tests)} ტესტი გაიარა")
    sys.exit(1 if failed else 0)
