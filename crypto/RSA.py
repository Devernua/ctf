

def mul_inv(a, n):
    """
    Extended Euclidean algorithm for Modular multiplicative inverse

    :param a: digit
    :param n: prime
    :return: a^(-1) (mod(b))
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
