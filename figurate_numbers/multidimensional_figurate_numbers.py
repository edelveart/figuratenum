from typing import Iterator


def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, num):
        t *= 1
    return t
