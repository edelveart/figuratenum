from typing import Iterator

# specific cases of m_pyramidal_numbers(m)


def triangular_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2)) // 6
        delta += 1


def square_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (2 * delta + 1)) // 6
        delta += 1


def pyramidal_numbers() -> Iterator[int]:
    return square_pyramidal_numbers()


def pentagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (delta + 1) // 2
        delta += 1


def hexagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (4 * delta - 1) // 6
        delta += 1


def heptagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (5 * delta - 2) // 6
        delta += 1


def octagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (6 * delta - 3) // 6
        delta += 1


def nonagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (7 * delta - 4) // 6
        delta += 1


def decagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (8 * delta - 5) // 6
        delta += 1


def hendecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (9 * delta - 6) // 6
        delta += 1


def dodecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (10 * delta - 7) // 6
        delta += 1


def tridecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (11 * delta - 8) // 6
        delta += 1


def tetradecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (12 * delta - 9) // 6
        delta += 1


def pentadecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (13 * delta - 10) // 6
        delta += 1


def hexadecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (14 * delta - 11) // 6
        delta += 1


def heptadecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (15 * delta - 12) // 6
        delta += 1


def octadecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (16 * delta - 13) // 6
        delta += 1


def nonadecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (17 * delta - 14) // 6
        delta += 1


def icosagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (18 * delta - 15) // 6
        delta += 1


def icosihenagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (19 * delta - 16) // 6
        delta += 1


def icosidigonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (20 * delta - 17) // 6
        delta += 1


def icositrigonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (21 * delta - 18) // 6
        delta += 1


def icositetragonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (22 * delta - 19) // 6
        delta += 1


def icosipentagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (23 * delta - 20) // 6
        delta += 1


def icosihexagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (24 * delta - 21) // 6
        delta += 1


def icosiheptagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (25 * delta - 22) // 6
        delta += 1


def icosioctagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (26 * delta - 23) // 6
        delta += 1


def icosinonagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (27 * delta - 24) // 6
        delta += 1


def triacontagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1) * (28 * delta - 25) // 6
        delta += 1
