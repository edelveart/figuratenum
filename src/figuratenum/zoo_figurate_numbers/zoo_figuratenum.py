from typing import Iterator


def cuban_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta + 1)**3 - delta**3
        delta += 1
