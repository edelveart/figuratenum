from typing import Iterator


def cuban_prime() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta + 1)**3 - delta**3
        delta += 1


def pell():
    pell_numbers = [0, 1]
    yield 0
    yield 1
    i = 2
    while True:
        next_val = 2 * pell_numbers[i - 1] + pell_numbers[i - 2]
        pell_numbers.append(next_val)
        yield next_val
        i += 1
