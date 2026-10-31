from collections.abc import Generator

from .plane_figuratenum import (
    _polygonal_incremental,
    polygonal, centered_square, diamond,
    centered_dodecagonal, star, centered_mgonal, _centered_mgonal_incremental,
    pronic, heteromecic, oblong,  polite,
    impolite, cross, aztec_diamond, polygram, _polygram_incremental,
    centered_star_polygonal, pentagram, gnomonic,
    truncated_triangular, _truncated_triangular_incremental, truncated_square, _truncated_square_incremental, truncated_pronic, _truncated_pronic_incremental,
    truncated_centered_pol, _truncated_centered_pol_incremental, truncated_centered_mgonal,
    truncated_centered_hexagonal, truncated_hex,
    generalized_mgonal, generalized_centered_pol, generalized_pronic
)

from .specific_plane_figuratenum import (
    # triangular, square, pentagonal,
    # hexagonal, heptagonal, octagonal,
    # nonagonal, decagonal, hendecagonal,
    # dodecagonal, tridecagonal, tetradecagonal,
    # pentadecagonal, hexadecagonal, heptadecagonal,
    # octadecagonal, nonadecagonal, icosagonal,
    # icosihenagonal, icosiheptagonal, icosidigonal,
    # icositrigonal, icositetragonal, icosipentagonal,
    # icosihexagonal,  icosioctagonal,
    # icosinonagonal, triacontagonal,

    centered_triangular,

    centered_pentagonal,
    centered_hexagonal,
    centered_heptagonal,
    centered_octagonal,
    centered_nonagonal,
    centered_decagonal,
    centered_hendecagonal,

    centered_tridecagonal,
    centered_tetradecagonal,
    centered_pentadecagonal,
    centered_hexadecagonal,
    centered_heptadecagonal,
    centered_octadecagonal,
    centered_nonadecagonal,
    centered_icosagonal,
    centered_icosihenagonal,
    centered_icosidigonal,
    centered_icositrigonal,
    centered_icositetragonal,
    centered_icosipentagonal,
    centered_icosihexagonal,
    centered_icosiheptagonal,
    centered_icosioctagonal,
    centered_icosinonagonal,
    centered_triacontagonal,


    truncated_centered_triangular,
    truncated_centered_square,
    truncated_centered_pentagonal,

    generalized_pentagonal,
    generalized_hexagonal
)


class PlaneFigurateNum:

    def polygonal(self, m: int) -> Generator[int]:
        return _polygonal_incremental(m)

    def centered_mgonal(self, m: int) -> Generator[int]:
        return _centered_mgonal_incremental(m)

    def pronic(self) -> Generator[int]:
        return pronic()
    heteromecic = pronic
    oblong = pronic

    def polite(self) -> Generator[int]:
        return polite()

    def impolite(self) -> Generator[int]:
        return impolite()

    def cross(self) -> Generator[int]:
        return cross()

    def aztec_diamond(self) -> Generator[int]:
        return aztec_diamond()

    def polygram(self, m: int) -> Generator[int]:
        return _polygram_incremental(m)
    centered_star_polygonal = polygram

    def pentagram(self) -> Generator[int]:
        return _polygram_incremental(5)

    def gnomonic(self) -> Generator[int]:
        return gnomonic()

    def truncated_triangular(self) -> Generator[int]:
        return _truncated_triangular_incremental()

    def truncated_square(self) -> Generator[int]:
        return _truncated_square_incremental()

    def truncated_pronic(self) -> Generator[int]:
        return _truncated_pronic_incremental()

    def truncated_centered_pol(self, m: int) -> Generator[int]:
        return _truncated_centered_pol_incremental(m)
    truncated_centered_mgonal = truncated_centered_pol

    def truncated_centered_hexagonal(self) -> Generator[int]:
        return _truncated_centered_pol_incremental(6)
    truncated_hex = truncated_centered_hexagonal

    def generalized_mgonal(self, m: int, start_num: int = 0) -> Generator[int]:
        return generalized_mgonal(m, start_num)

    def generalized_centered_pol(self, m: int, start_num: int = 0) -> Generator[int]:
        return generalized_centered_pol(m, start_num)

    def generalized_pronic(self, start_num: int = 0) -> Generator[int]:
        return generalized_pronic(start_num)

    # specific plane figuratenum

    def triangular(self) -> Generator[int]:
        return _polygonal_incremental(3)

    def square(self) -> Generator[int]:
        return _polygonal_incremental(4)

    def pentagonal(self) -> Generator[int]:
        return _polygonal_incremental(5)

    def hexagonal(self) -> Generator[int]:
        return _polygonal_incremental(6)

    def heptagonal(self) -> Generator[int]:
        return _polygonal_incremental(7)

    def octagonal(self) -> Generator[int]:
        return _polygonal_incremental(8)

    def nonagonal(self) -> Generator[int]:
        return _polygonal_incremental(9)

    def decagonal(self) -> Generator[int]:
        return _polygonal_incremental(10)

    def hendecagonal(self) -> Generator[int]:
        return _polygonal_incremental(11)

    def dodecagonal(self) -> Generator[int]:
        return _polygonal_incremental(12)

    def tridecagonal(self) -> Generator[int]:
        return _polygonal_incremental(13)

    def tetradecagonal(self) -> Generator[int]:
        return _polygonal_incremental(14)

    def pentadecagonal(self) -> Generator[int]:
        return _polygonal_incremental(15)

    def hexadecagonal(self) -> Generator[int]:
        return _polygonal_incremental(16)

    def heptadecagonal(self) -> Generator[int]:
        return _polygonal_incremental(17)

    def octadecagonal(self) -> Generator[int]:
        return _polygonal_incremental(18)

    def nonadecagonal(self) -> Generator[int]:
        return _polygonal_incremental(19)

    def icosagonal(self) -> Generator[int]:
        return _polygonal_incremental(20)

    def icosihenagonal(self) -> Generator[int]:
        return _polygonal_incremental(21)

    def icosidigonal(self) -> Generator[int]:
        return _polygonal_incremental(22)

    def icositrigonal(self) -> Generator[int]:
        return _polygonal_incremental(23)

    def icositetragonal(self) -> Generator[int]:
        return _polygonal_incremental(24)

    def icosipentagonal(self) -> Generator[int]:
        return _polygonal_incremental(25)

    def icosihexagonal(self) -> Generator[int]:
        return _polygonal_incremental(26)

    def icosiheptagonal(self) -> Generator[int]:
        return _polygonal_incremental(27)

    def icosioctagonal(self) -> Generator[int]:
        return _polygonal_incremental(28)

    def icosinonagonal(self) -> Generator[int]:
        return _polygonal_incremental(29)

    def triacontagonal(self) -> Generator[int]:
        return _polygonal_incremental(30)

    # Centered
    def centered_triangular(self) -> Generator[int]:
        return _centered_mgonal_incremental(3)

    def centered_square(self) -> Generator[int]:
        return _centered_mgonal_incremental(4)
    diamond = centered_square

    def centered_pentagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(5)

    def centered_hexagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(6)

    def centered_heptagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(7)

    def centered_octagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(8)

    def centered_nonagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(9)

    def centered_decagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(10)

    def centered_hendecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(11)

    def centered_dodecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(12)
    star = centered_dodecagonal

    def centered_tridecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(13)

    def centered_tetradecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(14)

    def centered_pentadecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(15)

    def centered_hexadecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(16)

    def centered_heptadecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(17)

    def centered_octadecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(18)

    def centered_nonadecagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(19)

    def centered_icosagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(20)

    def centered_icosihenagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(21)

    def centered_icosidigonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(22)

    def centered_icositrigonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(23)

    def centered_icositetragonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(24)

    def centered_icosipentagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(25)

    def centered_icosihexagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(26)

    def centered_icosiheptagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(27)

    def centered_icosioctagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(28)

    def centered_icosinonagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(29)

    def centered_triacontagonal(self) -> Generator[int]:
        return _centered_mgonal_incremental(30)

    def truncated_centered_triangular(self) -> Generator[int]:
        return truncated_centered_triangular()

    def truncated_centered_square(self) -> Generator[int]:
        return truncated_centered_square()

    def truncated_centered_pentagonal(self) -> Generator[int]:
        return truncated_centered_pentagonal()

    def generalized_pentagonal(self) -> Generator[int]:
        return generalized_pentagonal()

    def generalized_hexagonal(self) -> Generator[int]:
        return generalized_hexagonal()
