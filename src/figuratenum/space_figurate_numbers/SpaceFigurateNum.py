from collections.abc import Generator


from .space_figuratenum import (
    m_pyramidal, _m_pyramidal_incremental, _cubic_incremental, _tetrahedral_incremental,
    _octahedral_incremental, _dodecahedral_incremental,  _icosahedral_incremental,
    _truncated_tetrahedral_incremental, _truncated_cubic_incremental, _truncated_octahedral_incremental,
    _stella_octangula_incremental, _centered_cube_incremental, _rhombic_dodecahedral_incremental,
    _hauy_rhombic_dodecahedral_incremental, _centered_tetrahedron_incremental,  _centered_mgonal_pyramid_incremental, _mgonal_prism_incremental,
    centered_square_pyramid,
    _centered_octahedron_incremental, _centered_icosahedron_incremental,
    _centered_dodecahedron_incremental, centered_truncated_tetrahedron, _centered_truncated_cube_incremental,  centered_truncated_cube, _centered_truncated_tetrahedron_incremental,  centered_truncated_octahedron,
    _centered_truncated_octahedron_incremental, centered_mgonal_pyramidal, _centered_mgonal_pyramidal_incremental,
    hexagonal_prism, mgonal_prism, generalized_mgonal_pyramidal,
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

    def m_pyramidal(self, m: int) -> Generator[int]:
        return _m_pyramidal_incremental(m)

    def cubic(self) -> Generator[int]:
        return _cubic_incremental()

    def tetrahedral(self) -> Generator[int]:
        return _tetrahedral_incremental()

    def octahedral(self) -> Generator[int]:
        return _octahedral_incremental()

    def dodecahedral(self) -> Generator[int]:
        return _dodecahedral_incremental()

    def icosahedral(self) -> Generator[int]:
        return _icosahedral_incremental()

    def truncated_tetrahedral(self) -> Generator[int]:
        return _truncated_tetrahedral_incremental()

    def truncated_cubic(self) -> Generator[int]:
        return _truncated_cubic_incremental()

    def truncated_octahedral(self) -> Generator[int]:
        return _truncated_octahedral_incremental()

    def stella_octangula(self) -> Generator[int]:
        return _stella_octangula_incremental()

    def centered_cube(self) -> Generator[int]:
        return _centered_cube_incremental()

    def rhombic_dodecahedral(self) -> Generator[int]:
        return _rhombic_dodecahedral_incremental()

    def hauy_rhombic_dodecahedral(self) -> Generator[int]:
        return _hauy_rhombic_dodecahedral_incremental()

    def centered_tetrahedron(self) -> Generator[int]:
        return _centered_tetrahedron_incremental()
    centered_tetrahedral = centered_tetrahedron

    def centered_square_pyramid(self) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(4)
    centered_pyramid = centered_square_pyramid

    def centered_mgonal_pyramid(self, m: int) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(m)

    def centered_octahedron(self) -> Generator[int]:
        return _centered_octahedron_incremental()

    def centered_icosahedron(self) -> Generator[int]:
        return _centered_icosahedron_incremental()
    centered_cuboctahedron = centered_icosahedron

    def centered_dodecahedron(self) -> Generator[int]:
        return _centered_dodecahedron_incremental()

    def centered_truncated_tetrahedron(self) -> Generator[int]:
        return _centered_truncated_tetrahedron_incremental()

    def centered_truncated_cube(self) -> Generator[int]:
        return _centered_truncated_cube_incremental()

    def centered_truncated_octahedron(self) -> Generator[int]:
        return _centered_truncated_octahedron_incremental()

    def centered_mgonal_pyramidal(self, m: int) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(m)

    def centered_hexagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(6)
    hex_pyramidal = centered_hexagonal_pyramidal

    def hexagonal_prism(self) -> Generator[int]:
        return _mgonal_prism_incremental(6)

    def mgonal_prism(self, m: int) -> Generator[int]:
        return _mgonal_prism_incremental(m)

    def generalized_mgonal_pyramidal(self, m: int, start_num) -> Generator[int]:
        return generalized_mgonal_pyramidal(m, start_num)

    def generalized_cubic(self, start_num: int = 0) -> Generator[int]:
        return generalized_cubic(start_num)

    def generalized_octahedral(self, start_num: int = 0) -> Generator[int]:
        return generalized_octahedral(start_num)

    def generalized_icosahedral(self, start_num: int = 0) -> Generator[int]:
        return generalized_icosahedral(start_num)

    def generalized_dodecahedral(self, start_num: int = 0) -> Generator[int]:
        return generalized_dodecahedral(start_num)

    def generalized_centered_cube(self, start_num: int = 0) -> Generator[int]:
        return generalized_centered_cube(start_num)

    def generalized_centered_tetrahedron(self, start_num: int = 0) -> Generator[int]:
        return generalized_centered_tetrahedron(start_num)

    def generalized_centered_square_pyramid(self, start_num: int = 0) -> Generator[int]:
        return generalized_centered_square_pyramid(start_num)

    def generalized_rhombic_dodecahedral(self, start_num: int = 0) -> Generator[int]:
        return generalized_rhombic_dodecahedral(start_num)

    def generalized_centered_mgonal_pyramidal(self, m: int, start_num: int = 0) -> Generator[int]:
        return generalized_centered_mgonal_pyramidal(m, start_num)

    def generalized_mgonal_prism(self, m, start_num: int = 0) -> Generator[int]:
        return generalized_mgonal_prism(m, start_num)

    def generalized_hexagonal_prism(self, start_num: int = 0) -> Generator[int]:
        return generalized_hexagonal_prism(start_num)

    # specific space figuratenum

    def triangular_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(3)

    def square_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(4)
    pyramidal = square_pyramidal

    def pentagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(5)

    def hexagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(6)

    def heptagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(7)

    def octagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(8)

    def nonagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(9)

    def decagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(10)

    def hendecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(11)

    def dodecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(12)

    def tridecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(13)

    def tetradecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(14)

    def pentadecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(15)

    def hexadecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(16)

    def heptadecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(17)

    def octadecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(18)

    def nonadecagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(19)

    def icosagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(20)

    def icosihenagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(21)

    def icosidigonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(22)

    def icositrigonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(23)

    def icositetragonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(24)

    def icosipentagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(25)

    def icosihexagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(26)

    def icosiheptagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(27)

    def icosioctagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(28)

    def icosinonagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(29)

    def triacontagonal_pyramidal(self) -> Generator[int]:
        return _m_pyramidal_incremental(30)

    def triangular_tetrahedral(self) -> Generator[int]:
        return triangular_tetrahedral()

    def triangular_square_pyramidal(self) -> Generator[int]:
        return triangular_square_pyramidal()

    def square_tetrahedral(self) -> Generator[int]:
        return square_tetrahedral()

    def square_square_pyramidal(self) -> Generator[int]:
        return square_square_pyramidal()

    def tetrahedral_square_pyramidal(self) -> Generator[int]:
        return tetrahedral_square_pyramidal()

    def centered_pentagonal_pyramid(self) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(5)

    def centered_hexagonal_pyramid(self) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(6)

    def centered_heptagonal_pyramid(self) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(7)

    def centered_octagonal_pyramid(self) -> Generator[int]:
        return _centered_mgonal_pyramid_incremental(8)

    def centered_triangular_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(3)

    def centered_square_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(4)

    def centered_pentagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(5)

    def centered_heptagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(7)

    def centered_octagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(8)

    def centered_nonagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(9)

    def centered_decagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(10)

    def centered_hendecagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(11)

    def centered_dodecagonal_pyramidal(self) -> Generator[int]:
        return _centered_mgonal_pyramidal_incremental(12)

    def generalized_pentagonal_pyramidal(self) -> Generator[int]:
        return generalized_pentagonal_pyramidal()

    def generalized_hexagonal_pyramidal(self) -> Generator[int]:
        return generalized_hexagonal_pyramidal()
