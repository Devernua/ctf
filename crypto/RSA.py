from functools import reduce


def mul_inv(a, n):
    """
    Extended Euclidean algorithm for Modular multiplicative inverse

    :param a: digit
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
    :param pares: list of (c,n) where c is digit and n is prime
    :return: m**(len(pares)) where c = m mod n for each pares
    """

    sum = 0
    prod = reduce(lambda a, b: a * b, [i[1] for i in pares])

    for a_i, n_i in pares:
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod