from typing import Iterator


def m_pyramidal(m) -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def cubic() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def tetrahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2)) // 6
        delta += 1


def octahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (2 * delta ** 2 + 1)) // 3
        delta += 1


def dodecahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (3 * delta - 1) * (3 * delta - 2)) // 2
        delta += 1


def icosahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (5 * delta ** 2 - 5 * delta + 2)) // 2
        delta += 1


def truncated_tetrahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 27 * delta + 10) * delta // 6
        delta += 1


def truncated_cubic() -> Iterator[int]:
    delta = 1
    while True:
        yield (3 * delta - 2) ** 3 - ((8 * (delta - 1) * delta * (delta + 1)) // 6)
        delta += 1


def truncated_octahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield 16 * delta ** 3 - 33 * delta ** 2 + 24 * delta - 6
        delta += 1


def stella_octangula() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (2 * delta ** 2 - 1)
        delta += 1


def centered_cube() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def rhombic_dodecahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 1)
        delta += 1


def hauy_rhombic_dodecahedral() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (8 * delta ** 2 - 14 * delta + 7)
        delta += 1


def centered_tetrahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 3)) // 3
        delta += 1


def centered_tetrahedral() -> Iterator[int]:
    return centered_tetrahedron()


def centered_square_pyramid() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 2)) // 2
        delta += 1


def centered_pyramid() -> Iterator[int]:
    return centered_square_pyramid()


def centered_mgonal_pyramid(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m - 1) * ((delta - 1) * delta * (2 * delta - 1)) // 6 + (2 * delta - 1)
        delta += 1


def centered_octahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 3) // 3
        delta += 1


def centered_icosahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 3) // 3
        delta += 1


def centered_cuboctahedron() -> Iterator[int]:
    return centered_icosahedron()


def centered_dodecahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def centered_truncated_tetrahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (7 * delta ** 2 - 7 * delta + 3) // 3
        delta += 1


def centered_truncated_cube() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (23 * delta ** 2 - 23 * delta + 3) // 3
        delta += 1


def centered_truncated_octahedron() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 1)
        delta += 1


def centered_mgonal_pyramidal(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def centered_hexagonal_pyramidal() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def hex_pyramidal() -> Iterator[int]:
    return centered_hexagonal_pyramidal()


def hexagonal_prism() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def mgonal_prism(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_mgonal_pyramidal(m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def generalized_cubic(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** 3
        delta += 1


def generalized_octahedral(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (2 * delta ** 2 + 1) * delta // 3
        delta += 1


def generalized_icosahedral(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (5 * delta ** 2 - 5 * delta + 2) * delta // 2
        delta += 1


def generalized_dodecahedral(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (9 * delta ** 2 - 9 * delta + 2) * delta // 2
        delta += 1


def generalized_centered_cube(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def generalized_centered_tetrahedron(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 3) // 3
        delta += 1


def generalized_centered_square_pyramid(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield ((2 * delta - 1) * (delta ** 2 - delta + 2)) // 2
        delta += 1


def generalized_rhombic_dodecahedral(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** 4 - (delta - 1) ** 4
        delta += 1


def generalized_centered_mgonal_pyramidal(m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def generalized_mgonal_prism(m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta * (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_hexagonal_prism(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1
