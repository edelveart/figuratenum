from typing import Iterator


def m_pyramidal_numbers(m) -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def cubic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def tetrahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2)) // 6
        delta += 1


def octahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (2 * delta ** 2 + 1)) // 3
        delta += 1


def dodecahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (3 * delta - 1) * (3 * delta - 2)) // 2
        delta += 1


def icosahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (5 * delta ** 2 - 5 * delta + 2)) // 2
        delta += 1


def truncated_tetrahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 27 * delta + 10) * delta // 6
        delta += 1


def truncated_cubic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta - 2) ** 3 - ((8 * (delta - 1) * delta * (delta + 1)) // 6)
        delta += 1
