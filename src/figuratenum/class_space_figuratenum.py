from typing import List
from array import array

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

from .specific_space_figuratenum import (
    triangular_pyramidal_numbers, square_pyramidal_numbers, pyramidal_numbers, pentagonal_pyramidal_numbers,
    hexagonal_pyramidal_numbers, heptagonal_pyramidal_numbers, octagonal_pyramidal_numbers,
    nonagonal_pyramidal_numbers, decagonal_pyramidal_numbers, hendecagonal_pyramidal_numbers,
    dodecagonal_pyramidal_numbers, tridecagonal_pyramidal_numbers, tetradecagonal_pyramidal_numbers,
    pentadecagonal_pyramidal_numbers, hexadecagonal_pyramidal_numbers, heptadecagonal_pyramidal_numbers,
    octadecagonal_pyramidal_numbers, nonadecagonal_pyramidal_numbers, icosagonal_pyramidal_numbers,
    icosihenagonal_pyramidal_numbers, icosidigonal_pyramidal_numbers, icositrigonal_pyramidal_numbers,
    icositetragonal_pyramidal_numbers, icosipentagonal_pyramidal_numbers, icosihexagonal_pyramidal_numbers,
    icosiheptagonal_pyramidal_numbers, icosioctagonal_pyramidal_numbers,
    icosinonagonal_pyramidal_numbers, triacontagonal_pyramidal_numbers,
    triangular_tetrahedral_numbers, triangular_square_pyramidal_numbers, square_tetrahedral_numbers,
    square_square_pyramidal_numbers, tetrahedral_square_pyramidal_numbers,


    centered_pentagonal_pyramid_numbers, centered_hexagonal_pyramid_numbers,
    centered_heptagonal_pyramid_numbers, centered_octagonal_pyramid_numbers,

    centered_triangular_pyramidal_numbers, centered_square_pyramidal_numbers, centered_pentagonal_pyramidal_numbers,
    centered_heptagonal_pyramidal_numbers, centered_octagonal_pyramidal_numbers, centered_nonagonal_pyramidal_numbers,
    centered_decagonal_pyramidal_numbers, centered_hendecagonal_pyramidal_numbers, centered_dodecagonal_pyramidal_numbers

)


class SpaceFigurateNum():

    def take_to_list(self, n: int) -> List[int]:
        """
        Takes the first n generated numbers from the sequence and returns them as a list.
        Args:
            n (int): Number of elements to take.
        Returns:
            list: List of the first n generated numbers.
        """
        seq_num = []
        for _ in range(n):
            seq_num.append(next(self.generator))
        return seq_num

    def take_to_array(self, n: int) -> array:
        """
        Takes the first n generated numbers from the sequence and returns them as an.
        Args:
            n (int): Number of elements to take.
        Returns:
            list: List of the first n generated numbers.
        """
        seq_num = array("i", [])
        for _ in range(n):
            seq_num.append(next(self.generator))
        return seq_num

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

    # specific space figuratenum

    @classmethod
    def triangular_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(triangular_pyramidal_numbers())

    @classmethod
    def square_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(square_pyramidal_numbers())

    @classmethod
    def pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(pyramidal_numbers())

    @classmethod
    def pentagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(pentagonal_pyramidal_numbers())

    @classmethod
    def hexagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(hexagonal_pyramidal_numbers())

    @classmethod
    def heptagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(heptagonal_pyramidal_numbers())

    @classmethod
    def octagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(octagonal_pyramidal_numbers())

    @classmethod
    def nonagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(nonagonal_pyramidal_numbers())

    @classmethod
    def decagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(decagonal_pyramidal_numbers())

    @classmethod
    def hendecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(hendecagonal_pyramidal_numbers())

    @classmethod
    def dodecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(dodecagonal_pyramidal_numbers())

    @classmethod
    def tridecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(tridecagonal_pyramidal_numbers())

    @classmethod
    def tetradecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(tetradecagonal_pyramidal_numbers())

    @classmethod
    def pentadecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(pentadecagonal_pyramidal_numbers())

    @classmethod
    def hexadecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(hexadecagonal_pyramidal_numbers())

    @classmethod
    def heptadecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(heptadecagonal_pyramidal_numbers())

    @classmethod
    def octadecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(octadecagonal_pyramidal_numbers())

    @classmethod
    def nonadecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(nonadecagonal_pyramidal_numbers())

    @classmethod
    def icosagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosagonal_pyramidal_numbers())

    @classmethod
    def icosihenagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosihenagonal_pyramidal_numbers())

    @classmethod
    def icosidigonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosidigonal_pyramidal_numbers())

    @classmethod
    def icositrigonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icositrigonal_pyramidal_numbers())

    @classmethod
    def icositetragonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icositetragonal_pyramidal_numbers())

    @classmethod
    def icosipentagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosipentagonal_pyramidal_numbers())

    @classmethod
    def icosihexagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosihexagonal_pyramidal_numbers())

    @classmethod
    def icosiheptagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosiheptagonal_pyramidal_numbers())

    @classmethod
    def icosioctagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosioctagonal_pyramidal_numbers())

    @classmethod
    def icosinonagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(icosinonagonal_pyramidal_numbers())

    @classmethod
    def triacontagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(triacontagonal_pyramidal_numbers())

    @classmethod
    def triangular_tetrahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(triangular_tetrahedral_numbers())

    @classmethod
    def triangular_square_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(triangular_square_pyramidal_numbers())

    @classmethod
    def square_tetrahedral_numbers(cls) -> "SpaceFigurateNum":
        return cls(square_tetrahedral_numbers())

    @classmethod
    def square_square_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(square_square_pyramidal_numbers())

    @classmethod
    def tetrahedral_square_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(tetrahedral_square_pyramidal_numbers())

    @classmethod
    def centered_pentagonal_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_pentagonal_pyramid_numbers())

    @classmethod
    def centered_hexagonal_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_hexagonal_pyramid_numbers())

    @classmethod
    def centered_heptagonal_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_heptagonal_pyramid_numbers())

    @classmethod
    def centered_octagonal_pyramid_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_octagonal_pyramid_numbers())

    @classmethod
    def centered_triangular_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_triangular_pyramidal_numbers())

    @classmethod
    def centered_square_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_square_pyramidal_numbers())

    @classmethod
    def centered_pentagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_pentagonal_pyramidal_numbers())

    @classmethod
    def centered_heptagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_heptagonal_pyramidal_numbers())

    @classmethod
    def centered_octagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_octagonal_pyramidal_numbers())

    @classmethod
    def centered_nonagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_nonagonal_pyramidal_numbers())

    @classmethod
    def centered_decagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_decagonal_pyramidal_numbers())

    @classmethod
    def centered_hendecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_hendecagonal_pyramidal_numbers())

    @classmethod
    def centered_dodecagonal_pyramidal_numbers(cls) -> "SpaceFigurateNum":
        return cls(centered_dodecagonal_pyramidal_numbers())
