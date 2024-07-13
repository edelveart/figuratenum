from typing import Iterator

# specific cases of polygonal_numbers(m)


def triangular_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta ** 2 + delta) // 2
        delta += 1


def square_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 2) // 2
        delta += 1


def pentagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2 - delta) // 2
        delta += 1


def hexagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (4 * delta ** 2 - 2 * delta) // 2
        delta += 1


def heptagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 2 - 3 * delta) // 2
        delta += 1


def octagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (6 * delta ** 2 - 4 * delta) // 2
        delta += 1


def nonagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2 - 5 * delta) // 2
        delta += 1


def decagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (8 * delta ** 2 - 6 * delta) // 2
        delta += 1


def hendecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (9 * delta ** 2 - 7 * delta) // 2
        delta += 1


def dodecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (10 * delta ** 2 - 8 * delta) // 2
        delta += 1


def tridecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (11 * delta ** 2 - 9 * delta) // 2
        delta += 1


def tetradecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (12 * delta ** 2 - 10 * delta) // 2
        delta += 1


def pentadecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (13 * delta ** 2 - 11 * delta) // 2
        delta += 1


def hexadecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (14 * delta ** 2 - 12 * delta) // 2
        delta += 1


def heptadecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (15 * delta ** 2 - 13 * delta) // 2
        delta += 1


def octadecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (16 * delta ** 2 - 14 * delta) // 2
        delta += 1


def nonadecagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (17 * delta ** 2 - 15 * delta) // 2
        delta += 1


def icosagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (18 * delta ** 2 - 16 * delta) // 2
        delta += 1


def icosihenagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (19 * delta ** 2 - 17 * delta) // 2
        delta += 1


def icosidigonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (20 * delta ** 2 - 18 * delta) // 2
        delta += 1


def icositrigonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 19 * delta) // 2
        delta += 1


def icositetragonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (22 * delta ** 2 - 20 * delta) // 2
        delta += 1


def icosipentagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 21 * delta) // 2
        delta += 1


def icosihexagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (24 * delta ** 2 - 22 * delta) // 2
        delta += 1


def icosiheptagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (25 * delta ** 2 - 23 * delta) // 2
        delta += 1


def icosioctagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (26 * delta ** 2 - 24 * delta) // 2
        delta += 1


def icosinonagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (27 * delta ** 2 - 25 * delta) // 2
        delta += 1


def triacontagonal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (28 * delta ** 2 - 26 * delta) // 2
        delta += 1
