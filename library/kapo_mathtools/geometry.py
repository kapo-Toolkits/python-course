"""
გეომეტრიული გამოთვლების მოდული.
Geometric calculations.
"""

import math


def circle_area(radius):
    """
    გამოთვლის წრის ფართობს: π · r².
    Return the area of a circle: π · r².

    Args / პარამეტრები:
        radius (float): რადიუსი / the radius

    Returns / აბრუნებს:
        float: ფართობი / the area

    Raises / ისვრის:
        ValueError: თუ რადიუსი უარყოფითია / if the radius is negative

    Example:
        >>> circle_area(5)
        78.53981633974483
    """
    if radius < 0:
        raise ValueError("რადიუსი უნდა იყოს დადებითი / radius must not be negative")
    return math.pi * radius ** 2


def circle_circumference(radius):
    """
    გამოთვლის წრეწირის სიგრძეს: 2 · π · r.
    Return the circumference of a circle: 2 · π · r.

    Args / პარამეტრები:
        radius (float): რადიუსი / the radius

    Returns / აბრუნებს:
        float: წრეწირის სიგრძე / the circumference

    Raises / ისვრის:
        ValueError: თუ რადიუსი უარყოფითია / if the radius is negative

    Example:
        >>> circle_circumference(5)
        31.41592653589793
    """
    if radius < 0:
        raise ValueError("რადიუსი უნდა იყოს დადებითი / radius must not be negative")
    return 2 * math.pi * radius


def rectangle_area(length, width):
    """
    გამოთვლის მართკუთხედის ფართობს: სიგრძე · სიგანე.
    Return the area of a rectangle: length · width.

    Args / პარამეტრები:
        length (float): სიგრძე / the length
        width (float): სიგანე / the width

    Returns / აბრუნებს:
        float: ფართობი / the area

    Raises / ისვრის:
        ValueError: თუ გვერდი უარყოფითია / if a side is negative

    Example:
        >>> rectangle_area(4, 6)
        24
    """
    if length < 0 or width < 0:
        raise ValueError("გვერდები უნდა იყოს დადებითი / sides must not be negative")
    return length * width


def rectangle_perimeter(length, width):
    """
    გამოთვლის მართკუთხედის პერიმეტრს: 2 · (სიგრძე + სიგანე).
    Return the perimeter of a rectangle: 2 · (length + width).

    Args / პარამეტრები:
        length (float): სიგრძე / the length
        width (float): სიგანე / the width

    Returns / აბრუნებს:
        float: პერიმეტრი / the perimeter

    Raises / ისვრის:
        ValueError: თუ გვერდი უარყოფითია / if a side is negative

    Example:
        >>> rectangle_perimeter(4, 6)
        20
    """
    if length < 0 or width < 0:
        raise ValueError("გვერდები უნდა იყოს დადებითი / sides must not be negative")
    return 2 * (length + width)


def triangle_area(base, height):
    """
    გამოთვლის სამკუთხედის ფართობს: ½ · ფუძე · სიმაღლე.
    Return the area of a triangle: ½ · base · height.

    Args / პარამეტრები:
        base (float): ფუძე / the base
        height (float): სიმაღლე / the height

    Returns / აბრუნებს:
        float: ფართობი / the area

    Raises / ისვრის:
        ValueError: თუ პარამეტრი უარყოფითია / if an argument is negative

    Example:
        >>> triangle_area(10, 5)
        25.0
    """
    if base < 0 or height < 0:
        raise ValueError(
            "პარამეტრები უნდა იყოს დადებითი / arguments must not be negative"
        )
    return 0.5 * base * height
