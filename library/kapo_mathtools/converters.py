"""
ერთეულების კონვერტაციის მოდული
"""


def celsius_to_fahrenheit(celsius):
    """
    ცელსიუსი გადაჰყავს ფარენჰეიტად.
    
    Args:
        celsius (float): ტემპერატურა ცელსიუსში
        
    Returns:
        float: ტემპერატურა ფარენჰეიტში
        
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    ფარენჰეიტი გადაჰყავს ცელსიუსად.
    
    Args:
        fahrenheit (float): ტემპერატურა ფარენჰეიტში
        
    Returns:
        float: ტემპერატურა ცელსიუსში
        
    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5/9


def kilometers_to_miles(km):
    """
    კილომეტრი გადაჰყავს მილად.
    
    Args:
        km (float): მანძილი კილომეტრებში
        
    Returns:
        float: მანძილი მილებში
        
    Example:
        >>> kilometers_to_miles(10)
        6.213711922373339
    """
    return km * 0.621371


def miles_to_kilometers(miles):
    """
    მილი გადაჰყავს კილომეტრად.
    
    Args:
        miles (float): მანძილი მილებში
        
    Returns:
        float: მანძილი კილომეტრებში
        
    Example:
        >>> miles_to_kilometers(10)
        16.0934
    """
    return miles * 1.60934


def kilograms_to_pounds(kg):
    """
    კილოგრამი გადაჰყავს ფუნტად.
    
    Args:
        kg (float): წონა კილოგრამებში
        
    Returns:
        float: წონა ფუნტებში
        
    Example:
        >>> kilograms_to_pounds(10)
        22.046226218487757
    """
    return kg * 2.20462


def pounds_to_kilograms(pounds):
    """
    ფუნტი გადაჰყავს კილოგრამად.
    
    Args:
        pounds (float): წონა ფუნტებში
        
    Returns:
        float: წონა კილოგრამებში
        
    Example:
        >>> pounds_to_kilograms(10)
        4.535923700000001
    """
    return pounds * 0.453592


def meters_to_feet(meters):
    """
    მეტრი გადაჰყავს ფუტად.
    
    Args:
        meters (float): სიგრძე მეტრებში
        
    Returns:
        float: სიგრძე ფუტებში
        
    Example:
        >>> meters_to_feet(10)
        32.8084
    """
    return meters * 3.28084


def feet_to_meters(feet):
    """
    ფუტი გადაჰყავს მეტრად.
    
    Args:
        feet (float): სიგრძე ფუტებში
        
    Returns:
        float: სიგრძე მეტრებში
        
    Example:
        >>> feet_to_meters(10)
        3.048
    """
    return feet * 0.3048
