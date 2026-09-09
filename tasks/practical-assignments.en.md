[ქართული](practical-assignments.md) · **English**

# Practical assignments — 5 × 8 points = 40 points

**Course:** Introduction to Programming (Python)
**Format:** individually, during the practical session, in the computer lab.

> The point distribution is a recommendation — adjust it freely to your own course rules.

> Reference solutions and marking notes: [`solutions/`](solutions/) (Georgian only)

## Marking criteria (per assignment, max 8 points)

| Points | Criterion |
|---|---|
| **3.0** | Amount of work completed — the assignment is finished in full and the intended result is achieved |
| **2.0** | Ability to work independently — completed unaided, within the allotted time |
| **3.0** | Applying theory in practice — the approach (the sequence of steps) is correct, the rules are respected, no mechanical errors |
| **0** | The assignment was not done / one of the criteria scored 0 |

> ⚠ If any single criterion scores 0, the whole assignment scores 0.

---

## Assignment #1 — Conditions (Week III)

*Prerequisite: lectures 01–03*

1. **Even/odd + sign.** The user enters an integer. Print whether it is even or odd, and whether it is positive, negative or zero.
2. **Largest of three.** Find the largest of three numbers — without the built-in `max()`.
3. **Grade converter.** A score of 0–100 → a letter grade A/B/C/D/E/F. Print a message for an invalid score.
4. **Ticket price.** Age < 6 — free; 6–17 — 50% off; 18–64 — full price; ≥ 65 — 30% off.

**What is assessed:** correct use of `int(input(...))`, the order of `if/elif/else`, indentation.

---

## Assignment #2 — Functions (Week VI)

*Prerequisite: lectures 04–06*

1. **`is_prime(n)`** — returns `True`/`False`. Use it in a loop to print the primes between 1 and 50.
2. **`convert_temp(value, to="F")`** — with a default parameter: °C → °F or °C → K.
3. **`stats(*numbers)`** — returns the minimum, maximum, sum and mean (several values at once).
4. **`count_vowels(text)`** — counts vowels. Add a docstring and check it with `help()`.

**What is assessed:** every function must `return`, not `print`. A function must work correctly for a range of arguments — including edge cases (0, 1, a negative number, an empty string).

---

## Assignment #3 — Sets and dictionaries (Week XI)

*Prerequisite: lectures 07–11*

1. **Unique words.** Extract the unique words from a text with a `set`; print them sorted alphabetically.
2. **Comparing two groups.** From two sets: the students in both, only in the first, only in the second.
3. **Word frequency.** Use a dictionary to count every word in a text; print the 5 most frequent.
4. **Phone book.** With a menu: add, look up (with `get`), delete, list all. Store the data in a file.
5. **Gradebook.** A list of dictionaries (name + 3 scores). Print an aligned table sorted by the average.

**What is assessed:** using `get()` instead of `[]`, iterating with `items()`, `encoding="utf-8"`.

---

## Assignment #4 — Iterators (Week XIII)

*Prerequisite: lectures 12–13*

1. **`iter`/`next` by hand.** Walk a list with `while True`, `next()` and by catching `StopIteration`.
2. **A generator `even_numbers(limit)`** — returns even numbers with `yield`. Compare it with the list version of the same logic using `sys.getsizeof()`.
3. **A Fibonacci generator** — infinite; take the first 15 terms with `itertools.islice`.
4. **A file pipeline.** Three generators: read lines → filter → transform. Chain them together.
5. **An explanation.** Write it as a comment: how do `[x for x in ...]` and `(x for x in ...)` differ?

**What is assessed:** correct use of `yield`, `try/except StopIteration`, the memory-comparison numbers.

---

## Assignment #5 — Modules and git (Week XV)

*Prerequisite: lectures 14–15*

1. **Split into modules.** Break up your previous assignment: `tools/mathtools.py`, `tools/textutils.py`, `main.py`.
2. **`__init__.py`** — make it a package and use `from tools.mathtools import ...`.
3. **`if __name__ == "__main__":`** — give every module its own test block.
4. **git** — `git init` → `.gitignore` → at least 3 meaningful commits.
5. **Publish** — push it to GitHub and add a `README.md` describing the project.

**Bonus:** run `ruff check .` and fix every warning before you commit.

**What is assessed:** the package structure, correct imports, meaningful commit messages, `__pycache__/` and `.venv/` in `.gitignore`.
