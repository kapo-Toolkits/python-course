"""kapo-mathtools — ტესტები."""

import math

import pytest

from kapo_mathtools import __version__, converters, geometry, statistics, text_tools


def test_version():
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2


# ---------------------------------------------------------------- statistics

class TestStatistics:
    def test_mean(self):
        assert statistics.mean([1, 2, 3, 4, 5]) == 3.0
        assert statistics.mean([85, 90, 78, 92]) == 86.25
        assert statistics.mean([7]) == 7.0
        assert statistics.mean([-2, 2]) == 0.0

    def test_median_odd(self):
        assert statistics.median([1, 2, 3, 4, 5]) == 3
        assert statistics.median([5, 1, 3]) == 3       # დაუხარისხებელი

    def test_median_even(self):
        assert statistics.median([1, 2, 3, 4]) == 2.5

    def test_variance_and_std_dev(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        assert statistics.variance(data) == 4.0        # გენერალური (n-ზე)
        assert statistics.std_dev(data) == 2.0

    def test_std_dev_is_sqrt_of_variance(self):
        data = [85, 90, 78, 92, 88]
        assert statistics.std_dev(data) == pytest.approx(
            math.sqrt(statistics.variance(data))
        )

    @pytest.mark.parametrize("func", [
        statistics.mean, statistics.median,
        statistics.variance, statistics.std_dev,
    ])
    def test_empty_raises(self, func):
        with pytest.raises(ValueError):
            func([])


# ------------------------------------------------------------------ geometry

class TestGeometry:
    def test_circle(self):
        assert geometry.circle_area(5) == pytest.approx(math.pi * 25)
        assert geometry.circle_circumference(5) == pytest.approx(2 * math.pi * 5)
        assert geometry.circle_area(0) == 0

    def test_rectangle(self):
        assert geometry.rectangle_area(4, 6) == 24
        assert geometry.rectangle_perimeter(4, 6) == 20

    def test_triangle(self):
        assert geometry.triangle_area(10, 5) == 25.0

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            geometry.circle_area(-1)


# ---------------------------------------------------------------- text_tools

class TestTextTools:
    def test_count_words(self):
        assert text_tools.count_words("გამარჯობა მსოფლიო") == 2
        assert text_tools.count_words("ერთი  ორი   სამი") == 3   # მრავალი ჰარე
        assert text_tools.count_words("") == 0

    def test_count_chars(self):
        assert text_tools.count_chars("ab cd") == 4
        assert text_tools.count_chars("ab cd", include_spaces=True) == 5

    def test_reverse_text(self):
        assert text_tools.reverse_text("Python") == "nohtyP"
        assert text_tools.reverse_text("") == ""

    def test_is_palindrome(self):
        assert text_tools.is_palindrome("radar") is True
        assert text_tools.is_palindrome("A man a plan a canal Panama") is True
        assert text_tools.is_palindrome("python") is False

    def test_capitalize_words(self):
        assert text_tools.capitalize_words("hello world") == "Hello World"

    def test_count_vowels(self):
        assert text_tools.count_vowels("hello") == 2
        assert text_tools.count_vowels("HELLO") == 2       # რეგისტრი არ აქვს მნიშვნელობა
        assert text_tools.count_vowels("xyz") == 0


# ---------------------------------------------------------------- converters

class TestConverters:
    def test_temperature(self):
        assert converters.celsius_to_fahrenheit(0) == 32.0
        assert converters.celsius_to_fahrenheit(100) == 212.0
        assert converters.fahrenheit_to_celsius(32) == 0.0
        assert converters.fahrenheit_to_celsius(212) == pytest.approx(100.0)

    def test_temperature_round_trip(self):
        for c in (-40, 0, 25, 37, 100):
            back = converters.fahrenheit_to_celsius(
                converters.celsius_to_fahrenheit(c)
            )
            assert back == pytest.approx(c)

    @pytest.mark.parametrize("there,back,value", [
        (converters.kilometers_to_miles, converters.miles_to_kilometers, 10),
        (converters.kilograms_to_pounds, converters.pounds_to_kilograms, 70),
        (converters.meters_to_feet, converters.feet_to_meters, 100),
    ])
    def test_unit_round_trips(self, there, back, value):
        assert back(there(value)) == pytest.approx(value, rel=1e-4)

    def test_known_values(self):
        assert converters.kilometers_to_miles(10) == pytest.approx(6.21371)
        assert converters.meters_to_feet(10) == pytest.approx(32.8084)
