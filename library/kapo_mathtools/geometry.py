"""
გეომეტრიული გამოთვლების მოდული
"""
import math


def circle_area(radius):
    """
    გამოთვლის წრის ფართობს.
    
    Args:
        radius (float): რადიუსი
        
    Returns:
        float: ფართობი
        
    Example:
        >>> circle_area(5)
        78.53981633974483
    """
    if radius < 0:
        raise ValueError("რადიუსი უნდა იყოს დადებითი")
    return math.pi * radius ** 2


def circle_circumference(radius):
    """
    გამოთვლის წრის გარშემოწერილობას.
    
    Args:
        radius (float): რადიუსი
        
    Returns:
        float: გარშემოწერილობა
    """
    if radius < 0:
        raise ValueError("რადიუსი უნდა იყოს დადებითი")
    return 2 * math.pi * radius


def rectangle_area(length, width):
    """
    გამოთვლის მართკუთხედის ფართობს.
    
    Args:
        length (float): სიგრძე
        width (float): სიგანე
        
    Returns:
        float: ფართობი
        
    Example:
        >>> rectangle_area(4, 6)
        24
    """
    if length < 0 or width < 0:
        raise ValueError("გვერდები უნდა იყოს დადებითი")
    return length * width


def rectangle_perimeter(length, width):
    """
    გამოთვლის მართკუთხედის პერიმეტრს.
    
    Args:
        length (float): სიგრძე
        width (float): სიგანე
        
    Returns:
        float: პერიმეტრი
    """
    if length < 0 or width < 0:
        raise ValueError("გვერდები უნდა იყოს დადებითი")
    return 2 * (length + width)


def triangle_area(base, height):
    """
    გამოთვლის სამკუთხედის ფართობს.
    
    Args:
        base (float): ფუძე
        height (float): სიმაღლე
        
    Returns:
        float: ფართობი
    """
    if base < 0 or height < 0:
        raise ValueError("პარამეტრები უნდა იყოს დადებითი")
    return 0.5 * base * height
