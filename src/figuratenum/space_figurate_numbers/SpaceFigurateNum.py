from typing import Iterator

from .space_figuratenum import (
    m_pyramidal, cubic, tetrahedral,
    octahedral, dodecahedral, icosahedral,
    truncated_tetrahedral, truncated_cubic, truncated_octahedral,
    stella_octangula, centered_cube, rhombic_dodecahedral,
    hauy_rhombic_dodecahedral, centered_tetrahedron, centered_tetrahedral,
    centered_square_pyramid, centered_pyramid, centered_mgonal_pyramid,
    centered_octahedron, centered_icosahedron, centered_cuboctahedron,
    centered_dodecahedron, centered_truncated_tetrahedron, centered_truncated_cube,
    centered_truncated_octahedron, centered_mgonal_pyramidal, centered_hexagonal_pyramidal,
    hex_pyramidal,  hexagonal_prism, mgonal_prism, generalized_mgonal_pyramidal,
    generalized_cubic, generalized_octahedral, generalized_icosahedral,
    generalized_dodecahedral, generalized_centered_cube,
    generalized_centered_tetrahedron, generalized_centered_square_pyramid,
    generalized_rhombic_dodecahedral, generalized_centered_mgonal_pyramidal,
    generalized_mgonal_prism, generalized_hexagonal_prism
)

from .specific_space_figuratenum import (
    triangular_pyramidal, square_pyramidal, pyramidal, pentagonal_pyramidal,
    hexagonal_pyramidal, heptagonal_pyramidal, octagonal_pyramidal,
    nonagonal_pyramidal, decagonal_pyramidal, hendecagonal_pyramidal,
    dodecagonal_pyramidal, tridecagonal_pyramidal, tetradecagonal_pyramidal,
    pentadecagonal_pyramidal, hexadecagonal_pyramidal, heptadecagonal_pyramidal,
    octadecagonal_pyramidal, nonadecagonal_pyramidal, icosagonal_pyramidal,
    icosihenagonal_pyramidal, icosidigonal_pyramidal, icositrigonal_pyramidal,
    icositetragonal_pyramidal, icosipentagonal_pyramidal, icosihexagonal_pyramidal,
    icosiheptagonal_pyramidal, icosioctagonal_pyramidal,
    icosinonagonal_pyramidal, triacontagonal_pyramidal,
    triangular_tetrahedral, triangular_square_pyramidal, square_tetrahedral,
    square_square_pyramidal, tetrahedral_square_pyramidal,


    centered_pentagonal_pyramid, centered_hexagonal_pyramid,
    centered_heptagonal_pyramid, centered_octagonal_pyramid,

    centered_triangular_pyramidal, centered_square_pyramidal, centered_pentagonal_pyramidal,
    centered_heptagonal_pyramidal, centered_octagonal_pyramidal, centered_nonagonal_pyramidal,
    centered_decagonal_pyramidal, centered_hendecagonal_pyramidal, centered_dodecagonal_pyramidal,

    generalized_pentagonal_pyramidal,
    generalized_hexagonal_pyramidal
)


class SpaceFigurateNum:

    def m_pyramidal(self, m: int) -> Iterator[int]:
        return m_pyramidal(m)

    def cubic(self) -> Iterator[int]:
        return cubic()

    def tetrahedral(self) -> Iterator[int]:
        return tetrahedral()

    def octahedral(self) -> Iterator[int]:
        return octahedral()

    def dodecahedral(self) -> Iterator[int]:
        return dodecahedral()

    def icosahedral(self) -> Iterator[int]:
        return icosahedral()

    def truncated_tetrahedral(self) -> Iterator[int]:
        return truncated_tetrahedral()

    def truncated_cubic(self) -> Iterator[int]:
        return truncated_cubic()

    def truncated_octahedral(self) -> Iterator[int]:
        return truncated_octahedral()

    def stella_octangula(self) -> Iterator[int]:
        return stella_octangula()

    def centered_cube(self) -> Iterator[int]:
        return centered_cube()

    def rhombic_dodecahedral(self) -> Iterator[int]:
        return rhombic_dodecahedral()

    def hauy_rhombic_dodecahedral(self) -> Iterator[int]:
        return hauy_rhombic_dodecahedral()

    def centered_tetrahedron(self) -> Iterator[int]:
        return centered_tetrahedron()

    def centered_tetrahedral(self) -> Iterator[int]:
        return centered_tetrahedral()

    def centered_square_pyramid(self) -> Iterator[int]:
        return centered_square_pyramid()

    def centered_pyramid(self) -> Iterator[int]:
        return centered_pyramid()

    def centered_mgonal_pyramid(self, m: int) -> Iterator[int]:
        return centered_mgonal_pyramid(m)

    def centered_octahedron(self) -> Iterator[int]:
        return centered_octahedron()

    def centered_icosahedron(self) -> Iterator[int]:
        return centered_icosahedron()

    def centered_cuboctahedron(self) -> Iterator[int]:
        return centered_cuboctahedron()

    def centered_dodecahedron(self) -> Iterator[int]:
        return centered_dodecahedron()

    def centered_truncated_tetrahedron(self) -> Iterator[int]:
        return centered_truncated_tetrahedron()

    def centered_truncated_cube(self) -> Iterator[int]:
        return centered_truncated_cube()

    def centered_truncated_octahedron(self) -> Iterator[int]:
        return centered_truncated_octahedron()

    def centered_mgonal_pyramidal(self, m: int) -> Iterator[int]:
        return centered_mgonal_pyramidal(m)

    def centered_hexagonal_pyramidal(self) -> Iterator[int]:
        return centered_hexagonal_pyramidal()

    def hex_pyramidal(self) -> Iterator[int]:
        return hex_pyramidal()

    def hexagonal_prism(self) -> Iterator[int]:
        return hexagonal_prism()

    def mgonal_prism(self, m: int) -> Iterator[int]:
        return mgonal_prism(m)

    def generalized_mgonal_pyramidal(self, m: int, start_num) -> Iterator[int]:
        return generalized_mgonal_pyramidal(m, start_num)

    def generalized_cubic(self, start_num: int = 0) -> Iterator[int]:
        return generalized_cubic(start_num)

    def generalized_octahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_octahedral(start_num)

    def generalized_icosahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_icosahedral(start_num)

    def generalized_dodecahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_dodecahedral(start_num)

    def generalized_centered_cube(self, start_num: int = 0) -> Iterator[int]:
        return generalized_centered_cube(start_num)

    def generalized_centered_tetrahedron(self, start_num: int = 0) -> Iterator[int]:
        return generalized_centered_tetrahedron(start_num)

    def generalized_centered_square_pyramid(self, start_num: int = 0) -> Iterator[int]:
        return generalized_centered_square_pyramid(start_num)

    def generalized_rhombic_dodecahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_rhombic_dodecahedral(start_num)

    def generalized_centered_mgonal_pyramidal(self, m: int, start_num: int = 0) -> Iterator[int]:
        return generalized_centered_mgonal_pyramidal(m, start_num)

    def generalized_mgonal_prism(self, m, start_num: int = 0) -> Iterator[int]:
        return generalized_mgonal_prism(m, start_num)

    def generalized_hexagonal_prism(self, start_num: int = 0) -> Iterator[int]:
        return generalized_hexagonal_prism(start_num)

    # specific space figuratenum

    def triangular_pyramidal(self) -> Iterator[int]:
        return triangular_pyramidal()

    def square_pyramidal(self) -> Iterator[int]:
        return square_pyramidal()

    def pyramidal(self) -> Iterator[int]:
        return pyramidal()

    def pentagonal_pyramidal(self) -> Iterator[int]:
        return pentagonal_pyramidal()

    def hexagonal_pyramidal(self) -> Iterator[int]:
        return hexagonal_pyramidal()

    def heptagonal_pyramidal(self) -> Iterator[int]:
        return heptagonal_pyramidal()

    def octagonal_pyramidal(self) -> Iterator[int]:
        return octagonal_pyramidal()

    def nonagonal_pyramidal(self) -> Iterator[int]:
        return nonagonal_pyramidal()

    def decagonal_pyramidal(self) -> Iterator[int]:
        return decagonal_pyramidal()

    def hendecagonal_pyramidal(self) -> Iterator[int]:
        return hendecagonal_pyramidal()

    def dodecagonal_pyramidal(self) -> Iterator[int]:
        return dodecagonal_pyramidal()

    def tridecagonal_pyramidal(self) -> Iterator[int]:
        return tridecagonal_pyramidal()

    def tetradecagonal_pyramidal(self) -> Iterator[int]:
        return tetradecagonal_pyramidal()

    def pentadecagonal_pyramidal(self) -> Iterator[int]:
        return pentadecagonal_pyramidal()

    def hexadecagonal_pyramidal(self) -> Iterator[int]:
        return hexadecagonal_pyramidal()

    def heptadecagonal_pyramidal(self) -> Iterator[int]:
        return heptadecagonal_pyramidal()

    def octadecagonal_pyramidal(self) -> Iterator[int]:
        return octadecagonal_pyramidal()

    def nonadecagonal_pyramidal(self) -> Iterator[int]:
        return nonadecagonal_pyramidal()

    def icosagonal_pyramidal(self) -> Iterator[int]:
        return icosagonal_pyramidal()

    def icosihenagonal_pyramidal(self) -> Iterator[int]:
        return icosihenagonal_pyramidal()

    def icosidigonal_pyramidal(self) -> Iterator[int]:
        return icosidigonal_pyramidal()

    def icositrigonal_pyramidal(self) -> Iterator[int]:
        return icositrigonal_pyramidal()

    def icositetragonal_pyramidal(self) -> Iterator[int]:
        return icositetragonal_pyramidal()

    def icosipentagonal_pyramidal(self) -> Iterator[int]:
        return icosipentagonal_pyramidal()

    def icosihexagonal_pyramidal(self) -> Iterator[int]:
        return icosihexagonal_pyramidal()

    def icosiheptagonal_pyramidal(self) -> Iterator[int]:
        return icosiheptagonal_pyramidal()

    def icosioctagonal_pyramidal(self) -> Iterator[int]:
        return icosioctagonal_pyramidal()

    def icosinonagonal_pyramidal(self) -> Iterator[int]:
        return icosinonagonal_pyramidal()

    def triacontagonal_pyramidal(self) -> Iterator[int]:
        return triacontagonal_pyramidal()

    def triangular_tetrahedral(self) -> Iterator[int]:
        return triangular_tetrahedral()

    def triangular_square_pyramidal(self) -> Iterator[int]:
        return triangular_square_pyramidal()

    def square_tetrahedral(self) -> Iterator[int]:
        return square_tetrahedral()

    def square_square_pyramidal(self) -> Iterator[int]:
        return square_square_pyramidal()

    def tetrahedral_square_pyramidal(self) -> Iterator[int]:
        return tetrahedral_square_pyramidal()

    def centered_pentagonal_pyramid(self) -> Iterator[int]:
        return centered_pentagonal_pyramid()

    def centered_hexagonal_pyramid(self) -> Iterator[int]:
        return centered_hexagonal_pyramid()

    def centered_heptagonal_pyramid(self) -> Iterator[int]:
        return centered_heptagonal_pyramid()

    def centered_octagonal_pyramid(self) -> Iterator[int]:
        return centered_octagonal_pyramid()

    def centered_triangular_pyramidal(self) -> Iterator[int]:
        return centered_triangular_pyramidal()

    def centered_square_pyramidal(self) -> Iterator[int]:
        return centered_square_pyramidal()

    def centered_pentagonal_pyramidal(self) -> Iterator[int]:
        return centered_pentagonal_pyramidal()

    def centered_heptagonal_pyramidal(self) -> Iterator[int]:
        return centered_heptagonal_pyramidal()

    def centered_octagonal_pyramidal(self) -> Iterator[int]:
        return centered_octagonal_pyramidal()

    def centered_nonagonal_pyramidal(self) -> Iterator[int]:
        return centered_nonagonal_pyramidal()

    def centered_decagonal_pyramidal(self) -> Iterator[int]:
        return centered_decagonal_pyramidal()

    def centered_hendecagonal_pyramidal(self) -> Iterator[int]:
        return centered_hendecagonal_pyramidal()

    def centered_dodecagonal_pyramidal(self) -> Iterator[int]:
        return centered_dodecagonal_pyramidal()

    def generalized_pentagonal_pyramidal(self) -> Iterator[int]:
        return generalized_pentagonal_pyramidal()

    def generalized_hexagonal_pyramidal(self) -> Iterator[int]:
        return generalized_hexagonal_pyramidal()
