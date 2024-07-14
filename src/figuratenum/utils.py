def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, (num) + 1):
        t *= i
    return t


def binomial_coefficient(n: int, k: int) -> int:
    return factorial_iter(n) // (factorial_iter(k) * factorial_iter(n - k))


def pseudo_rising_factorial(n: int, k: int) -> int:
    t = 1
    for i in range(n, (n + k - 2) + 1):
        t *= i
    return t


def pseudo_pochhammer_function(n: int, k: int) -> int:
    return pseudo_rising_factorial(n, k)


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


def helper_ext_int_double_sigma(k: int, n: int) -> int:
    t = ((2 ** 1) * binomial_coefficient(k, 1) * binomial_coefficient(1, 0))
    if n == 1:
        return t + 1
    a = 0
    for j in range(1, (n - 1) + 1):
        for i in range(0, (k - 1) + 1):
            a += ((2 ** (1 + i)) * binomial_coefficient(k, 1 + i)
                  * binomial_coefficient(j, i))
    return 1 + t + a
