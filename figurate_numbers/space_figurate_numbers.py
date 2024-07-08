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
