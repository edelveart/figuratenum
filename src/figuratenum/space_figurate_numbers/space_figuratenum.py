from collections.abc import Generator


def _cubic_generator(a: int, b: int, c: int, d: int) -> Generator[int, None, None]:
    while True:
        yield a
        a += b
        b += c
        c += d


def _cubic_incremental() -> Generator[int]:
    return _cubic_generator(1, 7, 12, 6)


def _tetrahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 3, 3, 1)


def _octahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 5, 8, 4)


def _dodecahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 19, 45, 27)


def _icosahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 11, 25, 15)


def m_pyramidal(m) -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * ((m - 2) * delta - m + 5)) // 6
        delta += 1


def _m_pyramidal_incremental(m: int) -> Generator[int]:
    a = 1
    b = m
    c = 2 * m - 3
    d = m - 2

    while True:
        yield a
        a += b
        b += c
        c += d


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


def _truncated_tetrahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 15, 37, 23)


def truncated_cubic() -> Generator[int]:
    delta = 1
    while True:
        # yield (3 * delta - 2) ** 3 - ((8 * (delta - 1) * delta * (delta + 1)) // 6) # alternative via C(3n-2)-8S_3^3(n-1)
        yield (77 * delta**3 - 162 * delta**2 + 112 * delta - 24) // 3
        delta += 1


def _truncated_cubic_incremental() -> Generator[int]:
    return _cubic_generator(1, 55, 200, 154)


def truncated_octahedral() -> Generator[int]:
    delta = 1
    while True:
        yield 16 * delta ** 3 - 33 * delta ** 2 + 24 * delta - 6
        delta += 1


def _truncated_octahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 37, 126, 96)


def stella_octangula() -> Generator[int]:
    delta = 1
    while True:
        yield delta * (2 * delta ** 2 - 1)
        delta += 1


def _stella_octangula_incremental() -> Generator[int]:
    return _cubic_generator(1, 13, 24, 12)


def centered_cube() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (delta ** 2 - delta + 1)
        delta += 1


def _centered_cube_incremental() -> Generator[int]:
    return _cubic_generator(1, 8, 18, 12)


def rhombic_dodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 1)
        delta += 1


def _rhombic_dodecahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 14, 36, 24)


def hauy_rhombic_dodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (8 * delta ** 2 - 14 * delta + 7)
        delta += 1


def _hauy_rhombic_dodecahedral_incremental() -> Generator[int]:
    return _cubic_generator(1, 32, 120, 96)


def centered_tetrahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * ((delta ** 2 - delta + 3)) // 3
        delta += 1


def _centered_tetrahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 4, 6, 4)


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
        yield (2 * delta - 1) * ((m - 1) * delta**2 - (m - 1) * delta + 6) // 6
        delta += 1


def _centered_mgonal_pyramid_incremental(m: int) -> Generator[int]:
    a = 1
    b = m + 1
    c = 3 * (m - 1)
    d = 2 * (m - 1)

    while True:
        yield a
        a += b
        b += c
        c += d


def centered_octahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (2 * delta ** 2 - 2 * delta + 3) // 3
        delta += 1


def _centered_octahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 6, 12, 8)


def centered_icosahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 3) // 3
        delta += 1


def _centered_icosahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 12, 30, 20)


def centered_cuboctahedron() -> Generator[int]:
    return centered_icosahedron()


def centered_dodecahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (3 * delta ** 2 - 3 * delta + 1)
        delta += 1


def _centered_dodecahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 20, 54, 36)


def centered_truncated_tetrahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (7 * delta ** 2 - 7 * delta + 3) // 3
        delta += 1


def _centered_truncated_tetrahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 16, 42, 28)


def centered_truncated_cube() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (23 * delta ** 2 - 23 * delta + 3) // 3
        delta += 1


def _centered_truncated_cube_incremental() -> Generator[int]:
    return _cubic_generator(1, 48, 138, 92)


def centered_truncated_octahedron() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta - 1) * (5 * delta ** 2 - 5 * delta + 1)
        delta += 1


def _centered_truncated_octahedron_incremental() -> Generator[int]:
    return _cubic_generator(1, 32, 90, 60)


def centered_mgonal_pyramidal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (m * delta ** 3 + delta * (6 - m)) // 6
        delta += 1


def _centered_mgonal_pyramidal_incremental(m: int) -> Generator[int]:
    a = 1
    b = m + 1
    c = 2 * m
    d = m

    while True:
        yield a
        a += b
        b += c
        c += d


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


def _mgonal_prism_incremental(m: int) -> Generator[int]:
    a = 1
    b = 2 * m + 1
    c = 5 * m
    d = 3 * m

    while True:
        yield a
        a += b
        b += c
        c += d


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
