"""
ტექსტის დამუშავების მოდული.
Text processing helpers.
"""


def count_words(text):
    """
    ითვლის სიტყვების რაოდენობას ტექსტში. სიტყვებს ჰარეები ჰყოფს.
    Return the number of words in the text, split on whitespace.

    Args / პარამეტრები:
        text (str): ტექსტი / the text

    Returns / აბრუნებს:
        int: სიტყვების რაოდენობა / the word count

    Example:
        >>> count_words("გამარჯობა მსოფლიო")
        2
        >>> count_words("")
        0
    """
    if not text:
        return 0
    return len(text.split())


def count_chars(text, include_spaces=False):
    """
    ითვლის სიმბოლოების რაოდენობას. ნაგულისხმევად ჰარეები არ ითვლება.
    Return the number of characters. Spaces are excluded by default.

    Args / პარამეტრები:
        text (str): ტექსტი / the text
        include_spaces (bool): დაითვალოს თუ არა ჰარეები / whether to count spaces

    Returns / აბრუნებს:
        int: სიმბოლოების რაოდენობა / the character count

    Example:
        >>> count_chars("Hello World")
        10
        >>> count_chars("Hello World", include_spaces=True)
        11
    """
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def reverse_text(text):
    """
    აბრუნებს ტექსტს შებრუნებული თანმიმდევრობით.
    Return the text with its characters in reverse order.

    Args / პარამეტრები:
        text (str): ტექსტი / the text

    Returns / აბრუნებს:
        str: შებრუნებული ტექსტი / the reversed text

    Example:
        >>> reverse_text("Python")
        'nohtyP'
    """
    return text[::-1]


def is_palindrome(text):
    """
    ამოწმებს, არის თუ არა ტექსტი პალინდრომი.
    Check whether the text is a palindrome.

    ჰარეებსა და რეგისტრს უგულებელყოფს, პუნქტუაციას — არა.
    Spaces and letter case are ignored; punctuation is not.

    Args / პარამეტრები:
        text (str): ტექსტი / the text

    Returns / აბრუნებს:
        bool: True თუ პალინდრომია / True if it is a palindrome

    Example:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("python")
        False
    """
    # ჰარეებს ვაშორებთ და რეგისტრს ვასწორებთ
    # strip spaces and normalise the case
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]


def capitalize_words(text):
    """
    ყოველი სიტყვის პირველ ასოს დიდად აქცევს.
    Return the text with the first letter of every word capitalised.

    Args / პარამეტრები:
        text (str): ტექსტი / the text

    Returns / აბრუნებს:
        str: დამუშავებული ტექსტი / the title-cased text

    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return text.title()


def count_vowels(text):
    """
    ითვლის ხმოვნების რაოდენობას. მხოლოდ ინგლისური ხმოვნები (aeiou).
    Return the number of vowels. English vowels only (aeiou).

    Args / პარამეტრები:
        text (str): ტექსტი / the text

    Returns / აბრუნებს:
        int: ხმოვნების რაოდენობა / the vowel count

    Example:
        >>> count_vowels("Hello World")
        3
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
