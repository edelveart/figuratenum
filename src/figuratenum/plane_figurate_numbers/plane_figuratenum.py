from math import log2, floor
from collections.abc import Generator


def _linear_generator(a, b) -> Generator[int]:
    while True:
        yield a
        a += b


def _quadratic_generator(a, b, c) -> Generator[int]:
    while True:
        yield a
        a += b
        b += c


def _polygonal_incremental(m: int) -> Generator[int]:
    a = 1
    b = m - 1
    c = m - 2

    while True:
        yield a
        a += b
        b += c


def polygonal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield ((m - 2) * delta ** 2 - (m - 4) * delta) // 2
        delta += 1


def centered_square() -> Generator[int]:
    delta = 1
    while True:
        yield 2 * delta ** 2 - 2 * delta + 1
        delta += 1


def diamond() -> Generator[int]:
    return centered_square()


def centered_dodecagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 6 * delta ** 2 - 6 * delta + 1
        delta += 1


def star() -> Generator[int]:
    return centered_dodecagonal()


def centered_mgonal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def _centered_mgonal_incremental(m: int) -> Generator[int]:
    a = 1
    b = m
    c = m

    while True:
        yield a
        a += b
        b += c


def pronic() -> Generator[int]:
    delta = 1
    while True:
        yield delta * (delta + 1)
        delta += 1


def _pronic_incremental() -> Generator[int]:
    return _quadratic_generator(2, 4, 2)


def heteromecic() -> Generator[int]:
    return _pronic_incremental()


def oblong() -> Generator[int]:
    return _pronic_incremental()


def polite() -> Generator[int]:
    delta = 1
    while True:
        yield delta + floor(log2(delta + log2(delta)))
        delta += 1


def impolite() -> Generator[int]:
    delta = 1
    while True:
        yield 2 ** delta
        delta += 1


def _impolite_incremental() -> Generator[int]:
    a = 2
    while True:
        yield a
        a *= 2


def cross() -> Generator[int]:
    delta = 1
    while True:
        yield 4 * delta - 3
        delta += 1


def _cross_incremental():
    return _linear_generator(1, 4)


def aztec_diamond() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta) * (delta + 1)
        delta += 1


def _aztec_diamond_incremental() -> Generator[int]:
    return _quadratic_generator(4, 8, 4)


def polygram(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield m * delta ** 2 - m * delta + 1
        delta += 1


def _polygram_incremental(m: int):
    a = 1
    b = 2 * m
    c = 2 * m

    while True:
        yield a
        a += b
        b += c


def centered_star_polygonal(m: int) -> Generator[int]:
    return _polygram_incremental(m)


def pentagram() -> Generator[int]:
    delta = 1
    while True:
        yield 5 * delta ** 2 - 5 * delta + 1
        delta += 1


def gnomonic() -> Generator[int]:
    delta = 1
    while True:
        yield 2 * delta - 1
        delta += 1


def _gnomonic_incremental() -> Generator[int]:
    return _linear_generator(1, 2)


def truncated_triangular() -> Generator[int]:
    delta = 1
    while True:
        yield (3 * delta ** 2) - (3 * delta) + 1
        delta += 1


def _truncated_triangular_incremental() -> Generator[int]:
    return _quadratic_generator(1, 6, 6)


def truncated_square() -> Generator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2) - (10 * delta) + 4
        delta += 1


def _truncated_square_incremental() -> Generator[int]:
    return _quadratic_generator(1, 11, 14)


def truncated_pronic() -> Generator[int]:
    delta = 1
    while True:
        yield (7 * delta ** 2) - (7 * delta) + 2
        delta += 1


def _truncated_pronic_incremental() -> Generator[int]:
    return _quadratic_generator(2, 14, 14)


def truncated_centered_pol(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield 1 + (m * (7 * delta ** 2 - 11 * delta + 4)) // 2
        delta += 1


def _truncated_centered_pol_incremental(m: int) -> Generator[int]:
    a = 1
    b = 5 * m
    c = 7 * m
    while True:
        yield a
        a += b
        b += c


def truncated_centered_mgonal(m: int) -> Generator[int]:
    return truncated_centered_pol(m)


def truncated_centered_hexagonal() -> Generator[int]:
    delta = 1
    while True:
        yield 21 * delta ** 2 - 33 * delta + 13
        delta += 1


def truncated_hex() -> Generator[int]:
    return truncated_centered_hexagonal()


def generalized_mgonal(m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta * ((m - 2) * delta - m + 4)) // 2
        delta += 1


def generalized_centered_pol(m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_pronic(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta * (delta + 1)
        delta += 1
