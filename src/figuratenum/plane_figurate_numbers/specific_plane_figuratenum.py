from typing import Iterator

# specific cases of polygonal(m)


def triangular() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta ** 2 + delta) // 2
        delta += 1


def square() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 2) // 2
        delta += 1


def pentagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2 - delta) // 2
        delta += 1


def hexagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (4 * delta ** 2 - 2 * delta) // 2
        delta += 1


def heptagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 2 - 3 * delta) // 2
        delta += 1


def octagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (6 * delta ** 2 - 4 * delta) // 2
        delta += 1


def nonagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2 - 5 * delta) // 2
        delta += 1


def decagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (8 * delta ** 2 - 6 * delta) // 2
        delta += 1


def hendecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (9 * delta ** 2 - 7 * delta) // 2
        delta += 1


def dodecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (10 * delta ** 2 - 8 * delta) // 2
        delta += 1


def tridecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (11 * delta ** 2 - 9 * delta) // 2
        delta += 1


def tetradecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (12 * delta ** 2 - 10 * delta) // 2
        delta += 1


def pentadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (13 * delta ** 2 - 11 * delta) // 2
        delta += 1


def hexadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (14 * delta ** 2 - 12 * delta) // 2
        delta += 1


def heptadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (15 * delta ** 2 - 13 * delta) // 2
        delta += 1


def octadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (16 * delta ** 2 - 14 * delta) // 2
        delta += 1


def nonadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (17 * delta ** 2 - 15 * delta) // 2
        delta += 1


def icosagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (18 * delta ** 2 - 16 * delta) // 2
        delta += 1


def icosihenagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (19 * delta ** 2 - 17 * delta) // 2
        delta += 1


def icosidigonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (20 * delta ** 2 - 18 * delta) // 2
        delta += 1


def icositrigonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 19 * delta) // 2
        delta += 1


def icositetragonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (22 * delta ** 2 - 20 * delta) // 2
        delta += 1


def icosipentagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 21 * delta) // 2
        delta += 1


def icosihexagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (24 * delta ** 2 - 22 * delta) // 2
        delta += 1


def icosiheptagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (25 * delta ** 2 - 23 * delta) // 2
        delta += 1


def icosioctagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (26 * delta ** 2 - 24 * delta) // 2
        delta += 1


def icosinonagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (27 * delta ** 2 - 25 * delta) // 2
        delta += 1


def triacontagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (28 * delta ** 2 - 26 * delta) // 2
        delta += 1


# specific cases of centered_mgonal(m)


def centered_triangular() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2 - 3 * delta + 2) // 2
        delta += 1


def centered_pentagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 2 - 5 * delta + 2) // 2
        delta += 1


def centered_hexagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 3 * delta ** 2 - 3 * delta + 1
        delta += 1


def centered_heptagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2 - 7 * delta + 2) // 2
        delta += 1


def centered_octagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 4 * delta ** 2 - 4 * delta + 1
        delta += 1


def centered_nonagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (9 * delta ** 2 - 9 * delta + 2) // 2
        delta += 1


def centered_decagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 5 * delta ** 2 - 5 * delta + 1
        delta += 1


def centered_hendecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (11 * delta ** 2 - 11 * delta + 2) // 2
        delta += 1


def centered_tridecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (13 * delta ** 2 - 13 * delta + 2) // 2
        delta += 1


def centered_tetradecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 7 * delta ** 2 - 7 * delta + 1
        delta += 1


def centered_pentadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (15 * delta**2 - 15 * delta + 2) // 2
        delta += 1


def centered_hexadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 8 * delta ** 2 - 8 * delta + 1
        delta += 1


def centered_heptadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (17 * delta**2 - 17 * delta + 2) // 2
        delta += 1


def centered_octadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 9 * delta ** 2 - 9 * delta + 1
        delta += 1


def centered_nonadecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (19 * delta ** 2 - 19 * delta + 2) // 2
        delta += 1


def centered_icosagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 10 * delta ** 2 - 10 * delta + 1
        delta += 1


def centered_icosihenagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 21 * delta + 2) // 2
        delta += 1


def centered_icosidigonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 11 * delta ** 2 - 11 * delta + 1
        delta += 1


def centered_icositrigonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 23 * delta + 2) // 2
        delta += 1


def centered_icositetragonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 12 * delta ** 2 - 12 * delta + 1
        delta += 1


def centered_icosipentagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (25 * delta ** 2 - 25 * delta + 2) // 2
        delta += 1


def centered_icosihexagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 13 * delta ** 2 - 13 * delta + 1
        delta += 1


def centered_icosiheptagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (27 * delta ** 2 - 27 * delta + 2) // 2
        delta += 1


def centered_icosioctagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 14 * delta ** 2 - 14 * delta + 1
        delta += 1


def centered_icosinonagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (29 * delta ** 2 - 29 * delta + 2) // 2
        delta += 1


def centered_triacontagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 15 * delta ** 2 - 15 * delta + 1
        delta += 1


# specific cases of truncated_centered_pol(m)

def truncated_centered_triangular() -> Iterator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 33 * delta) // 2 + 7
        delta += 1


def truncated_centered_square() -> Iterator[int]:
    delta = 1
    while True:
        yield 14 * delta**2 - 22 * delta + 9
        delta += 1


def truncated_centered_pentagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield (35 * delta**2 - 55 * delta) // 2 + 11
        delta += 1


def generalized_pentagonal(start_num: int = 0) -> Iterator[int]:
    m = 5
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1


def generalized_hexagonal(start_num: int = 0) -> Iterator[int]:
    m = 6
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1
