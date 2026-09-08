"""
ტექსტის დამუშავების მოდული
"""


def count_words(text):
    """
    ითვლის სიტყვების რაოდენობას ტექსტში.
    
    Args:
        text (str): ტექსტი
        
    Returns:
        int: სიტყვების რაოდენობა
        
    Example:
        >>> count_words("გამარჯობა მსოფლიო")
        2
    """
    if not text:
        return 0
    return len(text.split())


def count_chars(text, include_spaces=False):
    """
    ითვლის სიმბოლოების რაოდენობას.
    
    Args:
        text (str): ტექსტი
        include_spaces (bool): დაითვალოს თუ არა space-ები
        
    Returns:
        int: სიმბოლოების რაოდენობა
        
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
    ტექსტის შებრუნება.
    
    Args:
        text (str): ტექსტი
        
    Returns:
        str: შებრუნებული ტექსტი
        
    Example:
        >>> reverse_text("Python")
        'nohtyP'
    """
    return text[::-1]


def is_palindrome(text):
    """
    ამოწმებს არის თუ არა ტექსტი პალინდრომი.
    
    Args:
        text (str): ტექსტი
        
    Returns:
        bool: True თუ პალინდრომია
        
    Example:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("python")
        False
    """
    # ვშორავთ space-ებს და გადავიყვანთ lowercase-ში
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]


def capitalize_words(text):
    """
    ყველა სიტყვის პირველი ასო დიდი ხდება.
    
    Args:
        text (str): ტექსტი
        
    Returns:
        str: დამუშავებული ტექსტი
        
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return text.title()


def count_vowels(text):
    """
    ითვლის ხმოვანების რაოდენობას (ინგლისური).
    
    Args:
        text (str): ტექსტი
        
    Returns:
        int: ხმოვანების რაოდენობა
        
    Example:
        >>> count_vowels("Hello World")
        3
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
