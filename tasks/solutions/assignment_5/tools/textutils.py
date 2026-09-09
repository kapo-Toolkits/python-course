"""ტექსტის დამუშავების დამხმარე ფუნქციები.

დავალებები #2 და #3-დან გადმოტანილი.
"""

VOWELS = "aeiouAEIOU" + "აეიოუ"
PUNCTUATION = ".,!?;:„“\"'()"


def clean_word(raw):
    """აშორებს პუნქტუაციას და აქცევს პატარა ასოებად.

        >>> clean_word("ენაა.")
        'ენაა'
    """
    return raw.strip(PUNCTUATION).lower()


def count_vowels(text):
    """ითვლის ხმოვნებს (ლათინური და ქართული).

        >>> count_vowels("Hello")
        2
        >>> count_vowels("")
        0
    """
    count = 0

    for char in text:
        if char in VOWELS:
            count += 1

    return count


def unique_words(text):
    """აბრუნებს უნიკალურ სიტყვებს ანბანურად დახარისხებულს.

        >>> unique_words("ენა, ენა და ენა!")
        ['და', 'ენა']
    """
    words = set()

    for raw in text.split():
        word = clean_word(raw)
        if word:
            words.add(word)

    return sorted(words)


def word_frequency(text):
    """აბრუნებს ლექსიკონს {სიტყვა: რაოდენობა}.

        >>> word_frequency("ენა ენა და")["ენა"]
        2
    """
    counts = {}

    for raw in text.split():
        word = clean_word(raw)
        if word:
            counts[word] = counts.get(word, 0) + 1

    return counts


if __name__ == "__main__":
    sample = "ენა მარტივია, ენა კითხვადია და ენა პოპულარულია."
    print("count_vowels:", count_vowels(sample))
    print("unique_words:", unique_words(sample))
    print("word_frequency:", word_frequency(sample))
