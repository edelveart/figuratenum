from typing import Iterator


def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, num):
        t *= i
    return t


def binomial_coefficient(n: int, k: int) -> int:
    return factorial_iter(n) / (factorial_iter(k) * factorial_iter(n - k))


def pentatope_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3)) // 24
        delta += 1


def hypertetrahedral_numbers() -> Iterator[int]:
    return pentatope_numbers()


def triangulotriangular_numbers() -> Iterator[int]:
    return pentatope_numbers()


def rising_factorial(n: int, k: int) -> int:
    t = 1
    for i in range(n, n + k - 1):
        t *= i
    return t


def k_dimensional_hypertetrahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, k) // factorial_iter(k)
        delta += 1


def biquadratic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 4
        delta += 1


def k_dimensional_hypercube_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** k
        delta += 1


def k_hypercube_numbers(k: int) -> Iterator[int]:
    return k_dimensional_hypercube_numbers(k)


def hyperoctahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1
