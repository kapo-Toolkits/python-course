"""
სტატისტიკური გამოთვლების მოდული.
Statistical calculations.

შენიშვნა: `variance` და `std_dev` გენერალურ ერთობლიობას ითვლის (გაყოფა n-ზე).
Note: `variance` and `std_dev` compute population statistics (divide by n).
"""


def mean(numbers):
    """
    გამოთვლის რიცხვების საშუალო არითმეტიკულს.
    Return the arithmetic mean of the numbers.

    Args / პარამეტრები:
        numbers (list): რიცხვების სია / list of numbers

    Returns / აბრუნებს:
        float: საშუალო არითმეტიკული / the arithmetic mean

    Raises / ისვრის:
        ValueError: თუ სია ცარიელია / if the list is empty

    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი / list must not be empty")
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    გამოთვლის რიცხვების მედიანას — შუა მნიშვნელობას დახარისხების შემდეგ.
    Return the median: the middle value once the numbers are sorted.

    ლუწი რაოდენობისას აბრუნებს ორი შუა რიცხვის საშუალოს.
    For an even count, returns the mean of the two middle values.

    Args / პარამეტრები:
        numbers (list): რიცხვების სია / list of numbers

    Returns / აბრუნებს:
        float: მედიანა / the median

    Raises / ისვრის:
        ValueError: თუ სია ცარიელია / if the list is empty

    Example:
        >>> median([1, 2, 3, 4, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი / list must not be empty")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]


def variance(numbers):
    """
    გამოთვლის დისპერსიას — საშუალოდან გადახრების კვადრატების საშუალოს.
    Return the population variance: the mean of the squared deviations.

    Args / პარამეტრები:
        numbers (list): რიცხვების სია / list of numbers

    Returns / აბრუნებს:
        float: დისპერსია / the variance

    Raises / ისვრის:
        ValueError: თუ სია ცარიელია / if the list is empty

    Example:
        >>> variance([2, 4, 4, 4, 5, 5, 7, 9])
        4.0
    """
    if not numbers:
        raise ValueError("სია არ უნდა იყოს ცარიელი / list must not be empty")

    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def std_dev(numbers):
    """
    გამოთვლის სტანდარტულ გადახრას — დისპერსიის კვადრატულ ფესვს.
    Return the population standard deviation: the square root of the variance.

    Args / პარამეტრები:
        numbers (list): რიცხვების სია / list of numbers

    Returns / აბრუნებს:
        float: სტანდარტული გადახრა / the standard deviation

    Raises / ისვრის:
        ValueError: თუ სია ცარიელია / if the list is empty

    Example:
        >>> std_dev([2, 4, 4, 4, 5, 5, 7, 9])
        2.0
    """
    return variance(numbers) ** 0.5
