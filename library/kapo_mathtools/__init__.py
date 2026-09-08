"""
Kapo MathTools — მარტივი მათემატიკური ხელსაწყოები Python-ისთვის.

სასწავლო დანიშნულების ბიბლიოთეკა: გარე დამოკიდებულების გარეშე,
ქართული დოკუმენტაციით.

    from kapo_mathtools import statistics, geometry, text_tools, converters

    statistics.mean([1, 2, 3])          # 2.0
    geometry.circle_area(5)             # 78.539...
    text_tools.is_palindrome("radar")   # True
    converters.celsius_to_fahrenheit(25)  # 77.0
"""

__version__ = "0.3.0"

from . import converters, geometry, statistics, text_tools

__all__ = ["statistics", "geometry", "text_tools", "converters", "__version__"]
