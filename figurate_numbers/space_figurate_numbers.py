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


def truncated_octahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield 16 * delta ** 3 - 33 * delta ** 2 + 24 * delta - 6
        delta += 1


def stella_octangula_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (2 * delta**2 - 1)
        delta += 1


def centered_cube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def rhombic_dodecahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 1)
        delta += 1


def hauy_rhombic_dodecahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (8 * delta ** 2 - 14 * delta + 7)
        delta += 1


def centered_tetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 3)) // 3
        delta += 1


def centered_tetrahedral_numbers() -> Iterator[int]:
    return centered_tetrahedron_numbers()


def centered_square_pyramid_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 2)) // 2
        delta += 1


def centered_pyramid_numbers() -> Iterator[int]:
    return centered_square_pyramid_numbers()


def centered_mgonal_pyramid_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m - 1) * ((delta - 1) * delta * (2 * delta - 1)) // 6 + (2 * delta - 1)
        delta += 1


def centered_octahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta**2 - 2 * delta + 3) // 3
        delta += 1


def centered_icosahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 3) // 3
        delta += 1


def centered_cuboctahedron_numbers() -> Iterator[int]:
    return centered_icosahedron_numbers()


def centered_dodecahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def centered_truncated_tetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (7 * delta ** 2 - 7 * delta + 3) // 3
        delta += 1


def centered_truncated_cube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (23 * delta**2 - 23 * delta + 3) // 3
        delta += 1


def centered_truncated_octahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 1)
        delta += 1


def centered_mgonal_pyramidal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def centered_hexagonal_pyramidal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def hex_pyramidal_numbers(m: int) -> Iterator[int]:
    return centered_hexagonal_pyramidal_numbers(m)


def hexagonal_prism_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def mgonal_prism_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (m * delta**2 - m * delta + 2) // 2
        delta += 1
