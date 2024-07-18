from typing import Iterator, List
from .space_figuratenum import (
    m_pyramidal_numbers, cubic_numbers, tetrahedral_numbers,
    octahedral_numbers, dodecahedral_numbers, icosahedral_numbers,
    truncated_tetrahedral_numbers, truncated_cubic_numbers, truncated_octahedral_numbers,
    stella_octangula_numbers, centered_cube_numbers, rhombic_dodecahedral_numbers,
    hauy_rhombic_dodecahedral_numbers, centered_tetrahedron_numbers, centered_tetrahedral_numbers,
    centered_square_pyramid_numbers, centered_pyramid_numbers, centered_mgonal_pyramid_numbers,
    centered_octahedron_numbers, centered_icosahedron_numbers, centered_cuboctahedron_numbers,
    centered_dodecahedron_numbers, centered_truncated_tetrahedron_numbers, centered_truncated_cube_numbers,
    centered_truncated_octahedron_numbers, centered_mgonal_pyramidal_numbers, centered_hexagonal_pyramidal_numbers,
    hex_pyramidal_numbers,  hexagonal_prism_numbers, mgonal_prism_numbers, generalized_mgonal_pyramidal_numbers,
    generalized_cubic_numbers, generalized_octahedral_numbers, generalized_icosahedral_numbers,
    generalized_dodecahedral_numbers, generalized_centered_cube_numbers,
    generalized_centered_tetrahedron_numbers, generalized_centered_square_pyramid_numbers,
    generalized_rhombic_dodecahedral_numbers, generalized_centered_mgonal_pyramidal_numbers,
    generalized_mgonal_prism_numbers, generalized_hexagonal_prism_numbers
)


class SpaceFigurateNum:
    def __init__(self, generator: Iterator[int]):
        self.generator = generator

    def take(self, n: int) -> List[int]:
        result = []
        for _ in range(n):
            result.append(next(self.generator))
        return result

    @classmethod
    def m_pyramidal_numbers(cls, m: int) -> "SpaceFigurateNum":
        return cls(m_pyramidal_numbers(m))

    @classmethod
    def cubic_numbers(cls) -> "SpaceFigurateNum":
        return cls(cubic_numbers())

    @classmethod
    def tetrahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(tetrahedral_numbers())

    @classmethod
    def octahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(octahedral_numbers())

    @classmethod
    def dodecahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(dodecahedral_numbers())

    @classmethod
    def icosahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosahedral_numbers())

    @classmethod
    def truncated_tetrahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(truncated_tetrahedral_numbers())

    @classmethod
    def truncated_cubic_numbers(cls) -> "SpaceFigurateNum":
        return cls(truncated_cubic_numbers())

    @classmethod
    def truncated_octahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(truncated_octahedral_numbers())

    @classmethod
    def stella_octangula_numbers(cls) -> "SpaceFigurateNum":
        return cls(stella_octangula_numbers())

    @classmethod
    def centered_cube_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_cube_numbers())

    @classmethod
    def rhombic_dodecahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(rhombic_dodecahedral_numbers())

    @classmethod
    def hauy_rhombic_dodecahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(hauy_rhombic_dodecahedral_numbers())

    @classmethod
    def centered_tetrahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_tetrahedron_numbers())

    @classmethod
    def centered_tetrahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_tetrahedral_numbers())

    @classmethod
    def centered_square_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_square_pyramid_numbers())

    @classmethod
    def centered_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_pyramid_numbers())

    @classmethod
    def centered_mgonal_pyramid_numbers(cls, m: int) -> "SpaceFigurateNum":
        return cls(centered_mgonal_pyramid_numbers(m))

    @classmethod
    def centered_octahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_octahedron_numbers())

    @classmethod
    def centered_icosahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_icosahedron_numbers())

    @classmethod
    def centered_cuboctahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_cuboctahedron_numbers())

    @classmethod
    def centered_dodecahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_dodecahedron_numbers())

    @classmethod
    def centered_truncated_tetrahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_truncated_tetrahedron_numbers())

    @classmethod
    def centered_truncated_cube_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_truncated_cube_numbers())

    @classmethod
    def centered_truncated_octahedron_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_truncated_octahedron_numbers())

    @classmethod
    def centered_mgonal_pyramidal_numbers(cls, m: int) -> "SpaceFigurateNum":
        return cls(centered_mgonal_pyramidal_numbers(m))

    @classmethod
    def centered_hexagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_hexagonal_pyramidal_numbers())

    @classmethod
    def hex_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(hex_pyramidal_numbers())

    @classmethod
    def hexagonal_prism_numbers(cls) -> "SpaceFigurateNum":
        return cls(hexagonal_prism_numbers())

    @classmethod
    def mgonal_prism_numbers(cls, m: int) -> "SpaceFigurateNum":
        return cls(mgonal_prism_numbers(m))

    @classmethod
    def generalized_mgonal_pyramidal_numbers(cls, m: int) -> "SpaceFigurateNum":
        return cls(generalized_mgonal_pyramidal_numbers(m))

    @classmethod
    def generalized_cubic_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_cubic_numbers(start_num))

    @classmethod
    def generalized_octahedral_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_octahedral_numbers(start_num))

    @classmethod
    def generalized_icosahedral_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_icosahedral_numbers(start_num))

    @classmethod
    def generalized_dodecahedral_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_dodecahedral_numbers(start_num))

    @classmethod
    def generalized_centered_cube_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_centered_cube_numbers(start_num))

    @classmethod
    def generalized_centered_tetrahedron_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_centered_tetrahedron_numbers(start_num))

    @classmethod
    def generalized_centered_square_pyramid_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_centered_square_pyramid_numbers(start_num))

    @classmethod
    def generalized_rhombic_dodecahedral_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_rhombic_dodecahedral_numbers(start_num))

    @classmethod
    def generalized_centered_mgonal_pyramidal_numbers(cls, m: int, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_centered_mgonal_pyramidal_numbers(m, start_num))

    @classmethod
    def generalized_mgonal_prism_numbers(cls, m, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_mgonal_prism_numbers(m, start_num))

    @classmethod
    def generalized_hexagonal_prism_numbers(cls, start_num: int = 0) -> "SpaceFigurateNum":
        return cls(generalized_hexagonal_prism_numbers(start_num))
