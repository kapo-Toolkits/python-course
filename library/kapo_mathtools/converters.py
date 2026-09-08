"""
ერთეულების კონვერტაციის მოდული.
Unit conversion helpers.

გამოიყენება დამრგვალებული კოეფიციენტები (მაგ. 1 კმ = 0.621371 მილი),
ამიტომ იქით-უკან გადაყვანა უმნიშვნელო ცდომილებას იძლევა.
Rounded conversion factors are used (e.g. 1 km = 0.621371 mi), so a
round-trip conversion carries a small error.
"""


def celsius_to_fahrenheit(celsius):
    """
    ცელსიუსს გადაჰყავს ფარენჰეიტში: °F = °C · 9/5 + 32.
    Convert Celsius to Fahrenheit: °F = °C · 9/5 + 32.

    Args / პარამეტრები:
        celsius (float): ტემპერატურა ცელსიუსში / temperature in Celsius

    Returns / აბრუნებს:
        float: ტემპერატურა ფარენჰეიტში / temperature in Fahrenheit

    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    ფარენჰეიტს გადაჰყავს ცელსიუსში: °C = (°F − 32) · 5/9.
    Convert Fahrenheit to Celsius: °C = (°F − 32) · 5/9.

    Args / პარამეტრები:
        fahrenheit (float): ტემპერატურა ფარენჰეიტში / temperature in Fahrenheit

    Returns / აბრუნებს:
        float: ტემპერატურა ცელსიუსში / temperature in Celsius

    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5/9


def kilometers_to_miles(km):
    """
    კილომეტრს გადაჰყავს მილებში (1 კმ = 0.621371 მილი).
    Convert kilometres to miles (1 km = 0.621371 mi).

    Args / პარამეტრები:
        km (float): მანძილი კილომეტრებში / distance in kilometres

    Returns / აბრუნებს:
        float: მანძილი მილებში / distance in miles

    Example:
        >>> kilometers_to_miles(10)
        6.21371
    """
    return km * 0.621371


def miles_to_kilometers(miles):
    """
    მილს გადაჰყავს კილომეტრებში (1 მილი = 1.60934 კმ).
    Convert miles to kilometres (1 mi = 1.60934 km).

    Args / პარამეტრები:
        miles (float): მანძილი მილებში / distance in miles

    Returns / აბრუნებს:
        float: მანძილი კილომეტრებში / distance in kilometres

    Example:
        >>> miles_to_kilometers(10)
        16.0934
    """
    return miles * 1.60934


def kilograms_to_pounds(kg):
    """
    კილოგრამს გადაჰყავს ფუნტებში (1 კგ = 2.20462 ფუნტი).
    Convert kilograms to pounds (1 kg = 2.20462 lb).

    Args / პარამეტრები:
        kg (float): წონა კილოგრამებში / weight in kilograms

    Returns / აბრუნებს:
        float: წონა ფუნტებში / weight in pounds

    Example:
        >>> kilograms_to_pounds(10)
        22.0462
    """
    return kg * 2.20462


def pounds_to_kilograms(pounds):
    """
    ფუნტს გადაჰყავს კილოგრამებში (1 ფუნტი = 0.453592 კგ).
    Convert pounds to kilograms (1 lb = 0.453592 kg).

    Args / პარამეტრები:
        pounds (float): წონა ფუნტებში / weight in pounds

    Returns / აბრუნებს:
        float: წონა კილოგრამებში / weight in kilograms

    Example:
        >>> pounds_to_kilograms(10)
        4.53592
    """
    return pounds * 0.453592


def meters_to_feet(meters):
    """
    მეტრს გადაჰყავს ფუტებში (1 მ = 3.28084 ფუტი).
    Convert metres to feet (1 m = 3.28084 ft).

    Args / პარამეტრები:
        meters (float): სიგრძე მეტრებში / length in metres

    Returns / აბრუნებს:
        float: სიგრძე ფუტებში / length in feet

    Example:
        >>> meters_to_feet(10)
        32.8084
    """
    return meters * 3.28084


def feet_to_meters(feet):
    """
    ფუტს გადაჰყავს მეტრებში (1 ფუტი = 0.3048 მ).
    Convert feet to metres (1 ft = 0.3048 m).

    Args / პარამეტრები:
        feet (float): სიგრძე ფუტებში / length in feet

    Returns / აბრუნებს:
        float: სიგრძე მეტრებში / length in metres

    Example:
        >>> feet_to_meters(10)
        3.048
    """
    return feet * 0.3048
