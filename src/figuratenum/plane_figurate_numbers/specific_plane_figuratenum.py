from collections.abc import Generator
# specific cases of polygonal(m)


def triangular() -> Generator[int]:
    delta = 1
    while True:
        yield (delta ** 2 + delta) // 2
        delta += 1


def square() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 2) // 2
        delta += 1


def pentagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2 - delta) // 2
        delta += 1


def hexagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (4 * delta ** 2 - 2 * delta) // 2
        delta += 1


def heptagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 2 - 3 * delta) // 2
        delta += 1


def octagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (6 * delta ** 2 - 4 * delta) // 2
        delta += 1


def nonagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2 - 5 * delta) // 2
        delta += 1


def decagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (8 * delta ** 2 - 6 * delta) // 2
        delta += 1


def hendecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (9 * delta ** 2 - 7 * delta) // 2
        delta += 1


def dodecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (10 * delta ** 2 - 8 * delta) // 2
        delta += 1


def tridecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (11 * delta ** 2 - 9 * delta) // 2
        delta += 1


def tetradecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (12 * delta ** 2 - 10 * delta) // 2
        delta += 1


def pentadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (13 * delta ** 2 - 11 * delta) // 2
        delta += 1


def hexadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (14 * delta ** 2 - 12 * delta) // 2
        delta += 1


def heptadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (15 * delta ** 2 - 13 * delta) // 2
        delta += 1


def octadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (16 * delta ** 2 - 14 * delta) // 2
        delta += 1


def nonadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (17 * delta ** 2 - 15 * delta) // 2
        delta += 1


def icosagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (18 * delta ** 2 - 16 * delta) // 2
        delta += 1


def icosihenagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (19 * delta ** 2 - 17 * delta) // 2
        delta += 1


def icosidigonal() -> Generator[int]:
    delta = 1
    while True:
        yield (20 * delta ** 2 - 18 * delta) // 2
        delta += 1


def icositrigonal() -> Generator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 19 * delta) // 2
        delta += 1


def icositetragonal() -> Generator[int]:
    delta = 1
    while True:
        yield (22 * delta ** 2 - 20 * delta) // 2
        delta += 1


def icosipentagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 21 * delta) // 2
        delta += 1


def icosihexagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (24 * delta ** 2 - 22 * delta) // 2
        delta += 1


def icosiheptagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (25 * delta ** 2 - 23 * delta) // 2
        delta += 1


def icosioctagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (26 * delta ** 2 - 24 * delta) // 2
        delta += 1


def icosinonagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (27 * delta ** 2 - 25 * delta) // 2
        delta += 1


def triacontagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (28 * delta ** 2 - 26 * delta) // 2
        delta += 1


# specific cases of centered_mgonal(m)


def centered_triangular() -> Generator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2 - 3 * delta + 2) // 2
        delta += 1


def centered_pentagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 2 - 5 * delta + 2) // 2
        delta += 1


def centered_hexagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 3 * delta ** 2 - 3 * delta + 1
        delta += 1


def centered_heptagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2 - 7 * delta + 2) // 2
        delta += 1


def centered_octagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 4 * delta ** 2 - 4 * delta + 1
        delta += 1


def centered_nonagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (9 * delta ** 2 - 9 * delta + 2) // 2
        delta += 1


def centered_decagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 5 * delta ** 2 - 5 * delta + 1
        delta += 1


def centered_hendecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (11 * delta ** 2 - 11 * delta + 2) // 2
        delta += 1


def centered_tridecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (13 * delta ** 2 - 13 * delta + 2) // 2
        delta += 1


def centered_tetradecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 7 * delta ** 2 - 7 * delta + 1
        delta += 1


def centered_pentadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (15 * delta**2 - 15 * delta + 2) // 2
        delta += 1


def centered_hexadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 8 * delta ** 2 - 8 * delta + 1
        delta += 1


def centered_heptadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (17 * delta**2 - 17 * delta + 2) // 2
        delta += 1


def centered_octadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 9 * delta ** 2 - 9 * delta + 1
        delta += 1


def centered_nonadecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (19 * delta ** 2 - 19 * delta + 2) // 2
        delta += 1


def centered_icosagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 10 * delta ** 2 - 10 * delta + 1
        delta += 1


def centered_icosihenagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 21 * delta + 2) // 2
        delta += 1


def centered_icosidigonal() -> Generator[int]:
    delta = 1
    while True:
        yield 11 * delta ** 2 - 11 * delta + 1
        delta += 1


def centered_icositrigonal() -> Generator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 23 * delta + 2) // 2
        delta += 1


def centered_icositetragonal() -> Generator[int]:
    delta = 1
    while True:
        yield 12 * delta ** 2 - 12 * delta + 1
        delta += 1


def centered_icosipentagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (25 * delta ** 2 - 25 * delta + 2) // 2
        delta += 1


def centered_icosihexagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 13 * delta ** 2 - 13 * delta + 1
        delta += 1


def centered_icosiheptagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (27 * delta ** 2 - 27 * delta + 2) // 2
        delta += 1


def centered_icosioctagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 14 * delta ** 2 - 14 * delta + 1
        delta += 1


def centered_icosinonagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (29 * delta ** 2 - 29 * delta + 2) // 2
        delta += 1


def centered_triacontagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 15 * delta ** 2 - 15 * delta + 1
        delta += 1


# specific cases of truncated_centered_pol(m)

def truncated_centered_triangular() -> Generator[int]:
    delta = 1
    while True:
        yield (21 * delta ** 2 - 33 * delta) // 2 + 7
        delta += 1


def truncated_centered_square() -> Generator[int]:
    delta = 1
    while True:
        yield 14 * delta**2 - 22 * delta + 9
        delta += 1


def truncated_centered_pentagonal() -> Generator[int]:
    delta = 1
    while True:
        yield (35 * delta**2 - 55 * delta) // 2 + 11
        delta += 1


def generalized_pentagonal(start_num: int = 0) -> Generator[int]:
    m = 5
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1


def generalized_hexagonal(start_num: int = 0) -> Generator[int]:
    m = 6
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1
