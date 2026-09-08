"""
სტატისტიკური გამოთვლების მოდული
"""

def mean(numbers):
    """
    გამოთვლის რიცხვების საშუალო არითმეტიკულს.
    
    Args:
        numbers (list): რიცხვების სია
        
    Returns:
        float: საშუალო არითმეტიკული
        
    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი")
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    გამოთვლის რიცხვების მედიანას.
    
    Args:
        numbers (list): რიცხვების სია
        
    Returns:
        float: მედიანა
        
    Example:
        >>> median([1, 2, 3, 4, 5])
        3
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]


def variance(numbers):
    """
    გამოთვლის დისპერსიას.
    
    Args:
        numbers (list): რიცხვების სია
        
    Returns:
        float: დისპერსია
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი")
    
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def std_dev(numbers):
    """
    გამოთვლის სტანდარტულ გადახრას.
    
    Args:
        numbers (list): რიცხვების სია
        
    Returns:
        float: სტანდარტული გადახრა
    """
    return variance(numbers) ** 0.5
