from functools import reduce
import math


def mul_inv(a, n):
    """
    Extended Euclidean algorithm for Modular multiplicative inverse

    :param a: number
    :param n: prime
    :return: a**(-1) (mod(b))
    """

    b0 = n
    x0, x1 = 0, 1

    if n == 1:
        return 1

    while a > 1:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1


def chinese_remainder(pares):
    """
    Realise of Chinese remainder theorem

    :param pares: list of (c,n) where c is number and n is prime
    :return: m where c = m mod n for each pares
    """

    _sum = 0
    prod = reduce(lambda a, b: a * b, [i[1] for i in pares])

    for a_i, n_i in pares:
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod


def inv_pow(x, n):
    """
    Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.

    :return: x**(-n)
    """
    high = 1
    mid = 1

    while high ** n < x:
        high *= 2

    low = high // 2

    while low < high:
        mid = (low + high) // 2

        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid

    return mid + 1


def gcd(numbers):
    """
    Greatest common divisor

    :param numbers: list of numbers
    :return: greatest common divisor of numbers
    """
    return reduce(lambda a, b: math.gcd(a, b), numbers)
