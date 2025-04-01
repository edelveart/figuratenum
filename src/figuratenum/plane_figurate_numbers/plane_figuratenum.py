from math import log2, floor
from typing import Iterator


def polygonal(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield ((m - 2) * delta ** 2 - (m - 4) * delta) // 2
        delta += 1


def centered_square() -> Iterator[int]:
    delta = 1
    while True:
        yield 2 * delta ** 2 - 2 * delta + 1
        delta += 1


def diamond() -> Iterator[int]:
    return centered_square()


def centered_dodecagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 6 * delta ** 2 - 6 * delta + 1
        delta += 1


def star() -> Iterator[int]:
    return centered_dodecagonal()


def centered_mgonal(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def pronic() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1)
        delta += 1


def heteromecic() -> Iterator[int]:
    return pronic()


def oblong() -> Iterator[int]:
    return pronic()


def polite() -> Iterator[int]:
    delta = 1
    while True:
        yield delta + floor(log2(delta + log2(delta)))
        delta += 1


def impolite() -> Iterator[int]:
    delta = 1
    while True:
        yield 2 ** delta
        delta += 1


def cross() -> Iterator[int]:
    delta = 1
    while True:
        yield 4 * delta - 3
        delta += 1


def aztec_diamond() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta) * (delta + 1)
        delta += 1


def polygram(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield m * delta ** 2 - m * delta + 1
        delta += 1


def centered_star_polygonal(m: int) -> Iterator[int]:
    return polygram(m)


def pentagram() -> Iterator[int]:
    delta = 1
    while True:
        yield 5 * delta ** 2 - 5 * delta + 1
        delta += 1


def gnomic() -> Iterator[int]:
    delta = 1
    while True:
        yield 2 * delta - 1
        delta += 1


def truncated_triangular() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2) - (3 * delta) + 1
        delta += 1


def truncated_square() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2) - (10 * delta) + 4
        delta += 1


def truncated_pronic() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2) - (7 * delta) + 2
        delta += 1


def truncated_centered_pol(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield 1 + (m * (7 * delta ** 2 - 11 * delta + 4)) // 2
        delta += 1


def truncated_centered_mgonal(m: int) -> Iterator[int]:
    return truncated_centered_pol(m)


def truncated_centered_hexagonal() -> Iterator[int]:
    delta = 1
    while True:
        yield 21 * delta ** 2 - 33 * delta + 13
        delta += 1


def truncated_hex() -> Iterator[int]:
    return truncated_centered_hexagonal()


def generalized_mgonal(m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1


def generalized_centered_pol(m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_pronic(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta * (delta + 1)
        delta += 1
