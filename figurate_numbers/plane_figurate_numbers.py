from math import log2, floor
from typing import Iterator


def polygonal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield ((m - 2) * delta ** 2 - (m - 4) * delta) // 2
        delta += 1


def centered_mgonal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def pronic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * delta + 1
        delta += 1


def heteromecic_numbers() -> Iterator[int]:
    return pronic_numbers()


def oblong_numbers() -> Iterator[int]:
    return pronic_numbers()


def polite_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta + floor(log2(delta + log2(delta)))
        delta += 1


def impolite_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield 2 ** delta
        delta += 1


def cross_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield 4 * delta - 3
        delta += 1


def aztec_diamond_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta) * (delta + 1)
        delta += 1


def polygram_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield m * delta ** 2 - m * delta + 1
        delta += 1


def pentagram_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield 5 * delta ** 2 - 5 * delta + 1
        delta += 1


def centered_star_polygonal_numbers(m: int) -> Iterator[int]:
    return polygram_numbers(m)


def gnomic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield 2 * delta - 1
        delta += 1


def truncated_triangular_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2) - (3 * delta) + 1
        delta += 1


def truncated_square_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2) - (10 * delta) + 4
        delta += 1
