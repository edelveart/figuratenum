from typing import Iterator

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
    icosihexagonal, centered_icosiheptagonal, icosioctagonal,
    icosinonagonal, triacontagonal,

    truncated_centered_triangular,
    truncated_centered_square,
    truncated_centered_pentagonal,

    generalized_pentagonal,
    generalized_hexagonal
)


class PlaneFigurateNum:

    def polygonal(self, m: int) -> Iterator[int]:
        return polygonal(m)

    def centered_square(self) -> Iterator[int]:
        return centered_square()

    def diamond(self) -> Iterator[int]:
        return diamond()

    def centered_dodecagonal(self) -> Iterator[int]:
        return centered_dodecagonal()

    def star(self) -> Iterator[int]:
        return star()

    def centered_mgonal(self, m: int) -> Iterator[int]:
        return centered_mgonal(m)

    def pronic(self) -> Iterator[int]:
        return pronic()

    def heteromecic(self) -> Iterator[int]:
        return heteromecic()

    def oblong(self) -> Iterator[int]:
        return oblong()

    def polite(self) -> Iterator[int]:
        return polite()

    def impolite(self) -> Iterator[int]:
        return impolite()

    def cross(self) -> Iterator[int]:
        return cross()

    def aztec_diamond(self) -> Iterator[int]:
        return aztec_diamond()

    def polygram(self, m: int) -> Iterator[int]:
        return polygram(m)

    def centered_star_polygonal(self, m: int) -> Iterator[int]:
        return centered_star_polygonal(m)

    def pentagram(self) -> Iterator[int]:
        return pentagram()

    def gnomic(self) -> Iterator[int]:
        return gnomic()

    def truncated_triangular(self) -> Iterator[int]:
        return truncated_triangular()

    def truncated_square(self) -> Iterator[int]:
        return truncated_square()

    def truncated_pronic(self) -> Iterator[int]:
        return truncated_pronic()

    def truncated_centered_pol(self, m: int) -> Iterator[int]:
        return truncated_centered_pol(m)

    def truncated_centered_mgonal(self, m: int) -> Iterator[int]:
        return truncated_centered_mgonal(m)

    def truncated_centered_hexagonal(self) -> Iterator[int]:
        return truncated_centered_hexagonal()

    def truncated_hex(self) -> Iterator[int]:
        return truncated_hex()

    def generalized_mgonal(self, m: int, start_num: int = 0) -> Iterator[int]:
        return generalized_mgonal(m, start_num)

    def generalized_centered_pol(self, m: int, start_num: int = 0) -> Iterator[int]:
        return generalized_centered_pol(m, start_num)

    def generalized_pronic(self, start_num: int = 0) -> Iterator[int]:
        return generalized_pronic(start_num)

    # specific plane figuratenum

    def triangular(self) -> Iterator[int]:
        return triangular()

    def square(self) -> Iterator[int]:
        return square()

    def pentagonal(self) -> Iterator[int]:
        return pentagonal()

    def hexagonal(self) -> Iterator[int]:
        return hexagonal()

    def heptagonal(self) -> Iterator[int]:
        return heptagonal()

    def octagonal(self) -> Iterator[int]:
        return octagonal()

    def nonagonal(self) -> Iterator[int]:
        return nonagonal()

    def decagonal(self) -> Iterator[int]:
        return decagonal()

    def hendecagonal(self) -> Iterator[int]:
        return hendecagonal()

    def dodecagonal(self) -> Iterator[int]:
        return dodecagonal()

    def tridecagonal(self) -> Iterator[int]:
        return tridecagonal()

    def tetradecagonal(self) -> Iterator[int]:
        return tetradecagonal()

    def pentadecagonal(self) -> Iterator[int]:
        return pentadecagonal()

    def hexadecagonal(self) -> Iterator[int]:
        return hexadecagonal()

    def heptadecagonal(self) -> Iterator[int]:
        return heptadecagonal()

    def octadecagonal(self) -> Iterator[int]:
        return octadecagonal()

    def nonadecagonal(self) -> Iterator[int]:
        return nonadecagonal()

    def icosagonal(self) -> Iterator[int]:
        return icosagonal()

    def icosihenagonal(self) -> Iterator[int]:
        return icosihenagonal()

    def icosiheptagonal(self) -> Iterator[int]:
        return icosiheptagonal()

    def icosidigonal(self) -> Iterator[int]:
        return icosidigonal()

    def icositrigonal(self) -> Iterator[int]:
        return icositrigonal()

    def icositetragonal(self) -> Iterator[int]:
        return icositetragonal()

    def icosipentagonal(self) -> Iterator[int]:
        return icosipentagonal()

    def icosihexagonal(self) -> Iterator[int]:
        return icosihexagonal()

    def centered_icosiheptagonal(self) -> Iterator[int]:
        return centered_icosiheptagonal()

    def icosioctagonal(self) -> Iterator[int]:
        return icosioctagonal()

    def icosinonagonal(self) -> Iterator[int]:
        return icosinonagonal()

    def triacontagonal(self) -> Iterator[int]:
        return triacontagonal()

    def truncated_centered_triangular(self) -> Iterator[int]:
        return truncated_centered_triangular()

    def truncated_centered_square(self) -> Iterator[int]:
        return truncated_centered_square()

    def truncated_centered_pentagonal(self) -> Iterator[int]:
        return truncated_centered_pentagonal()

    def generalized_pentagonal(self) -> Iterator[int]:
        return generalized_pentagonal()

    def generalized_hexagonal(self) -> Iterator[int]:
        return generalized_hexagonal()
