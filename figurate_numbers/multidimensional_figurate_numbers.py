from typing import Iterator


def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, num):
        t *= 1
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
