from math import comb as math_comb, factorial as math_factorial, prod as math_prod


def factorial_iter(num: int) -> int:
    """Simple factorial implementation for reference only."""
    t = 1
    for i in range(1, (num) + 1):
        t *= i
    return t


def binomial_coefficient_from_book(n: int, k: int) -> int:
    """Classic factorial-based version, slower, for reference only."""
    return factorial_iter(n) // (factorial_iter(k) * factorial_iter(n - k))


def factorial(num: int) -> int:
    """Optimized version using math.factorial for production"""
    return math_factorial(num)


def binomial_coefficient(n: int, k: int) -> int:
    """Optimized version using math.comb for production."""
    return math_comb(n, k)


def pseudo_rising_factorial_from_book(n: int, k: int) -> int:
    """Similar to the rising factorial but stops at n + k - 2 instead of n + k - 1.
    Provided for reference only.
    """
    t = 1
    for i in range(n, (n + k - 2) + 1):
        t *= i
    return t


def pseudo_rising_factorial(n: int, k: int) -> int:
    """Optimized version using math.prod for production"""
    return math_prod(range(n, n + k - 1))


def pseudo_pochhammer_function(n: int, k: int) -> int:
    return pseudo_rising_factorial(n, k)


def rising_factorial_from_book(n: int, k: int) -> int:
    """Classic rising factorial implementation. For reference only."""
    t = 1
    for i in range(n, (n + k - 1) + 1):
        t *= i
    return t


def rising_factorial(n: int, k: int) -> int:
    """Optimized version using math.prod for production"""
    return math_prod(range(n, n + k))


def helper_centered_hypertetrahedron(k: int, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return binomial_coefficient(k + 1, k)
    tau = 0
    for i in range(0, (k - 1) + 1):
        tau += (binomial_coefficient(k + 1, k - i) *
                binomial_coefficient(n - 2, i))
    return tau


def acc_helper_centered_hypertetrahedron(k: int, n: int) -> int:
    a = 0
    for j in range(1, (n) + 1):
        a += helper_centered_hypertetrahedron(k, j)
    return a


def helper_ext_int_double_sigma_from_book(k: int, n: int) -> int:
    """
    Original formula-based version from Figurate Numbers (2012).
    Kept for clarity and educational reference. Slower than the optimized version.
    """
    t = ((2 ** 1) * binomial_coefficient(k, 1) * binomial_coefficient(1, 0))
    if n == 1:
        return t + 1
    a = 0
    for j in range(1, (n - 1) + 1):
        for i in range(0, (k - 1) + 1):
            a += ((2 ** (1 + i)) * binomial_coefficient(k, 1 + i)
                  * binomial_coefficient(j, i))
    return 1 + t + a


def helper_ext_int_double_sigma(k: int, n: int) -> int:
    """
    Optimized implementation of 'helper_ext_int_double_sigma_from_book(k, n)'.
    Precomputes powers of two and binomial coefficients. Use in production.
    """
    if n == 1:
        return 2 * k + 1
    binom_k = [binomial_coefficient(k, 1 + i) for i in range(k)]
    powers_of_2 = [2 ** (1 + i) for i in range(k)]
    a = 0
    for j in range(1, n):
        for i in range(k):
            a += powers_of_2[i] * binom_k[i] * binomial_coefficient(j, i)
    return 2 * k + 1 + a
