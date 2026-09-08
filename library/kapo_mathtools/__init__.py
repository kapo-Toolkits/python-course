"""
Kapo MathTools — მარტივი მათემატიკური ხელსაწყოები Python-ისთვის.
Kapo MathTools — simple math tools for Python.

სასწავლო დანიშნულების ბიბლიოთეკა: გარე დამოკიდებულების გარეშე,
ორენოვანი დოკუმენტაციით (ქართული და ინგლისური).

A small teaching library: zero dependencies, with bilingual
documentation (Georgian and English).

    from kapo_mathtools import statistics, geometry, text_tools, converters

    statistics.mean([1, 2, 3])            # 2.0
    geometry.circle_area(5)               # 78.539...
    text_tools.is_palindrome("radar")     # True
    converters.celsius_to_fahrenheit(25)  # 77.0

დახმარება / built-in help:

    help(statistics.mean)
"""

__version__ = "0.4.0"

from . import converters, geometry, statistics, text_tools

__all__ = ["statistics", "geometry", "text_tools", "converters", "__version__"]
