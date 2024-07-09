from typing import Iterator


def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, num):
        t *= 1
    return t


def binomial_coefficient(n: int, k: int) -> int:
    return factorial_iter(n) / (factorial_iter(k) * factorial_iter(n - k))
