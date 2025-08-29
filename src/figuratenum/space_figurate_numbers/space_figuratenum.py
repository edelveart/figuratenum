from collections.abc import Generator


def m_pyramidal(m) -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def cubic() -> Generator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def tetrahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2)) // 6
        delta += 1


def octahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (2 * delta ** 2 + 1)) // 3
        delta += 1


def dodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (3 * delta - 1) * (3 * delta - 2)) // 2
        delta += 1


def icosahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (5 * delta ** 2 - 5 * delta + 2)) // 2
        delta += 1


def truncated_tetrahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (23 * delta ** 2 - 27 * delta + 10) * delta // 6
        delta += 1


def truncated_cubic() -> Generator[int]:
    delta = 1
    while True:
        yield (3 * delta - 2) ** 3 - ((8 * (delta - 1) * delta * (delta + 1)) // 6)
        delta += 1


def truncated_octahedral() -> Generator[int]:
    delta = 1
    while True:
        yield 16 * delta ** 3 - 33 * delta ** 2 + 24 * delta - 6
        delta += 1


def stella_octangula() -> Generator[int]:
    delta = 1
    while True:
        yield delta * (2 * delta ** 2 - 1)
        delta += 1


def centered_cube() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def rhombic_dodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 1)
        delta += 1


def hauy_rhombic_dodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (8 * delta ** 2 - 14 * delta + 7)
        delta += 1


def centered_tetrahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 3)) // 3
        delta += 1


def centered_tetrahedral() -> Generator[int]:
    return centered_tetrahedron()


def centered_square_pyramid() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 2)) // 2
        delta += 1


def centered_pyramid() -> Generator[int]:
    return centered_square_pyramid()


def centered_mgonal_pyramid(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (m - 1) * ((delta - 1) * delta * (2 * delta - 1)) // 6 + (2 * delta - 1)
        delta += 1


def centered_octahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 3) // 3
        delta += 1


def centered_icosahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 3) // 3
        delta += 1


def centered_cuboctahedron() -> Generator[int]:
    return centered_icosahedron()


def centered_dodecahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def centered_truncated_tetrahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (7 * delta ** 2 - 7 * delta + 3) // 3
        delta += 1


def centered_truncated_cube() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (23 * delta ** 2 - 23 * delta + 3) // 3
        delta += 1


def centered_truncated_octahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 1)
        delta += 1


def centered_mgonal_pyramidal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def centered_hexagonal_pyramidal() -> Generator[int]:
    delta = 1
    while True:
        yield delta ** 3
        delta += 1


def hex_pyramidal() -> Generator[int]:
    return centered_hexagonal_pyramidal()


def hexagonal_prism() -> Generator[int]:
    delta = 1
    while True:
        yield delta * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def mgonal_prism(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield delta * (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_mgonal_pyramidal(m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def generalized_cubic(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** 3
        delta += 1


def generalized_octahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (2 * delta ** 2 + 1) * delta // 3
        delta += 1


def generalized_icosahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (5 * delta ** 2 - 5 * delta + 2) * delta // 2
        delta += 1


def generalized_dodecahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (9 * delta ** 2 - 9 * delta + 2) * delta // 2
        delta += 1


def generalized_centered_cube(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def generalized_centered_tetrahedron(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 3) // 3
        delta += 1


def generalized_centered_square_pyramid(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield ((2 * delta - 1) * (delta ** 2 - delta + 2)) // 2
        delta += 1


def generalized_rhombic_dodecahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** 4 - (delta - 1) ** 4
        delta += 1


def generalized_centered_mgonal_pyramidal(m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def generalized_mgonal_prism(m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta * (m * delta ** 2 - m * delta + 2) // 2
        delta += 1


def generalized_hexagonal_prism(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1
