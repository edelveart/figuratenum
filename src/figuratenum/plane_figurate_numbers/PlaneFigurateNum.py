from collections.abc import Generator

from .plane_figuratenum import (
    polygonal, centered_square, diamond,
    centered_dodecagonal, star, centered_mgonal,
    pronic, heteromecic, oblong,  polite,
    impolite, cross, aztec_diamond, polygram,
    centered_star_polygonal, pentagram, gnomic,
    truncated_triangular, truncated_square, truncated_pronic,
    truncated_centered_pol, truncated_centered_mgonal,
    truncated_centered_hexagonal, truncated_hex,
    generalized_mgonal, generalized_centered_pol, generalized_pronic
)

from .specific_plane_figuratenum import (
    triangular, square, pentagonal,
    hexagonal, heptagonal, octagonal,
    nonagonal, decagonal, hendecagonal,
    dodecagonal, tridecagonal, tetradecagonal,
    pentadecagonal, hexadecagonal, heptadecagonal,
    octadecagonal, nonadecagonal, icosagonal,
    icosihenagonal, icosiheptagonal, icosidigonal,
    icositrigonal, icositetragonal, icosipentagonal,
    icosihexagonal,  icosioctagonal,
    icosinonagonal, triacontagonal,

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
        return polygonal(m)

    def centered_square(self) -> Generator[int]:
        return centered_square()

    def diamond(self) -> Generator[int]:
        return diamond()

    def centered_dodecagonal(self) -> Generator[int]:
        return centered_dodecagonal()

    def star(self) -> Generator[int]:
        return star()

    def centered_mgonal(self, m: int) -> Generator[int]:
        return centered_mgonal(m)

    def pronic(self) -> Generator[int]:
        return pronic()

    def heteromecic(self) -> Generator[int]:
        return heteromecic()

    def oblong(self) -> Generator[int]:
        return oblong()

    def polite(self) -> Generator[int]:
        return polite()

    def impolite(self) -> Generator[int]:
        return impolite()

    def cross(self) -> Generator[int]:
        return cross()

    def aztec_diamond(self) -> Generator[int]:
        return aztec_diamond()

    def polygram(self, m: int) -> Generator[int]:
        return polygram(m)

    def centered_star_polygonal(self, m: int) -> Generator[int]:
        return centered_star_polygonal(m)

    def pentagram(self) -> Generator[int]:
        return pentagram()

    def gnomic(self) -> Generator[int]:
        return gnomic()

    def truncated_triangular(self) -> Generator[int]:
        return truncated_triangular()

    def truncated_square(self) -> Generator[int]:
        return truncated_square()

    def truncated_pronic(self) -> Generator[int]:
        return truncated_pronic()

    def truncated_centered_pol(self, m: int) -> Generator[int]:
        return truncated_centered_pol(m)

    def truncated_centered_mgonal(self, m: int) -> Generator[int]:
        return truncated_centered_mgonal(m)

    def truncated_centered_hexagonal(self) -> Generator[int]:
        return truncated_centered_hexagonal()

    def truncated_hex(self) -> Generator[int]:
        return truncated_hex()

    def generalized_mgonal(self, m: int, start_num: int = 0) -> Generator[int]:
        return generalized_mgonal(m, start_num)

    def generalized_centered_pol(self, m: int, start_num: int = 0) -> Generator[int]:
        return generalized_centered_pol(m, start_num)

    def generalized_pronic(self, start_num: int = 0) -> Generator[int]:
        return generalized_pronic(start_num)

    # specific plane figuratenum

    def triangular(self) -> Generator[int]:
        return triangular()

    def square(self) -> Generator[int]:
        return square()

    def pentagonal(self) -> Generator[int]:
        return pentagonal()

    def hexagonal(self) -> Generator[int]:
        return hexagonal()

    def heptagonal(self) -> Generator[int]:
        return heptagonal()

    def octagonal(self) -> Generator[int]:
        return octagonal()

    def nonagonal(self) -> Generator[int]:
        return nonagonal()

    def decagonal(self) -> Generator[int]:
        return decagonal()

    def hendecagonal(self) -> Generator[int]:
        return hendecagonal()

    def dodecagonal(self) -> Generator[int]:
        return dodecagonal()

    def tridecagonal(self) -> Generator[int]:
        return tridecagonal()

    def tetradecagonal(self) -> Generator[int]:
        return tetradecagonal()

    def pentadecagonal(self) -> Generator[int]:
        return pentadecagonal()

    def hexadecagonal(self) -> Generator[int]:
        return hexadecagonal()

    def heptadecagonal(self) -> Generator[int]:
        return heptadecagonal()

    def octadecagonal(self) -> Generator[int]:
        return octadecagonal()

    def nonadecagonal(self) -> Generator[int]:
        return nonadecagonal()

    def icosagonal(self) -> Generator[int]:
        return icosagonal()

    def icosihenagonal(self) -> Generator[int]:
        return icosihenagonal()

    def icosiheptagonal(self) -> Generator[int]:
        return icosiheptagonal()

    def icosidigonal(self) -> Generator[int]:
        return icosidigonal()

    def icositrigonal(self) -> Generator[int]:
        return icositrigonal()

    def icositetragonal(self) -> Generator[int]:
        return icositetragonal()

    def icosipentagonal(self) -> Generator[int]:
        return icosipentagonal()

    def icosihexagonal(self) -> Generator[int]:
        return icosihexagonal()

    def icosioctagonal(self) -> Generator[int]:
        return icosioctagonal()

    def icosinonagonal(self) -> Generator[int]:
        return icosinonagonal()

    def triacontagonal(self) -> Generator[int]:
        return triacontagonal()

    def centered_triangular(self) -> Generator[int]:
        return centered_triangular()

    def centered_pentagonal(self) -> Generator[int]:
        return centered_pentagonal()

    def centered_hexagonal(self) -> Generator[int]:
        return centered_hexagonal()

    def centered_heptagonal(self) -> Generator[int]:
        return centered_heptagonal()

    def centered_octagonal(self) -> Generator[int]:
        return centered_octagonal()

    def centered_nonagonal(self) -> Generator[int]:
        return centered_nonagonal()

    def centered_decagonal(self) -> Generator[int]:
        return centered_decagonal()

    def centered_hendecagonal(self) -> Generator[int]:
        return centered_hendecagonal()

    def centered_tridecagonal(self) -> Generator[int]:
        return centered_tridecagonal()

    def centered_tetradecagonal(self) -> Generator[int]:
        return centered_tetradecagonal()

    def centered_pentadecagonal(self) -> Generator[int]:
        return centered_pentadecagonal()

    def centered_hexadecagonal(self) -> Generator[int]:
        return centered_hexadecagonal()

    def centered_heptadecagonal(self) -> Generator[int]:
        return centered_heptadecagonal()

    def centered_octadecagonal(self) -> Generator[int]:
        return centered_octadecagonal()

    def centered_nonadecagonal(self) -> Generator[int]:
        return centered_nonadecagonal()

    def centered_icosagonal(self) -> Generator[int]:
        return centered_icosagonal()

    def centered_icosihenagonal(self) -> Generator[int]:
        return centered_icosihenagonal()

    def centered_icosidigonal(self) -> Generator[int]:
        return centered_icosidigonal()

    def centered_icositrigonal(self) -> Generator[int]:
        return centered_icositrigonal()

    def centered_icositetragonal(self) -> Generator[int]:
        return centered_icositetragonal()

    def centered_icosipentagonal(self) -> Generator[int]:
        return centered_icosipentagonal()

    def centered_icosihexagonal(self) -> Generator[int]:
        return centered_icosihexagonal()

    def centered_icosiheptagonal(self) -> Generator[int]:
        return centered_icosiheptagonal()

    def centered_icosioctagonal(self) -> Generator[int]:
        return centered_icosioctagonal()

    def centered_icosinonagonal(self) -> Generator[int]:
        return centered_icosinonagonal()

    def centered_triacontagonal(self) -> Generator[int]:
        return centered_triacontagonal()

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
