from .instance_methods_figuratenum import InstanceMethodsFigurateNum

from .plane_figuratenum import (
    polygonal_numbers, centered_square_numbers, diamond_numbers,
    centered_dodecagonal_numbers, star_numbers, centered_mgonal_numbers,
    pronic_numbers, heteromecic_numbers, oblong_numbers,  polite_numbers,
    impolite_numbers, cross_numbers, aztec_diamond_numbers, polygram_numbers,
    centered_star_polygonal_numbers, pentagram_numbers, gnomic_numbers,
    truncated_triangular_numbers, truncated_square_numbers, truncated_pronic_numbers,
    truncated_centered_pol_numbers, truncated_centered_mgonal_numbers,
    truncated_centered_hexagonal_numbers, truncated_hex_numbers,
    generalized_mgonal_numbers, generalized_centered_pol_numbers, generalized_pronic_numbers
)

from .specific_plane_figuratenum import (
    triangular_numbers, square_numbers, pentagonal_numbers,
    hexagonal_numbers, heptagonal_numbers, octagonal_numbers,
    nonagonal_numbers, decagonal_numbers, hendecagonal_numbers,
    dodecagonal_numbers, tridecagonal_numbers, tetradecagonal_numbers,
    pentadecagonal_numbers, hexadecagonal_numbers, heptadecagonal_numbers,
    octadecagonal_numbers, nonadecagonal_numbers, icosagonal_numbers,
    icosihenagonal_numbers, icosiheptagonal_numbers, icosidigonal_numbers,
    icositrigonal_numbers, icositetragonal_numbers, icosipentagonal_numbers,
    icosihexagonal_numbers, centered_icosiheptagonal_numbers, icosioctagonal_numbers,
    icosinonagonal_numbers, triacontagonal_numbers
)


class PlaneFigurateNum(InstanceMethodsFigurateNum):

    @classmethod
    def polygonal_numbers(cls, k: int) -> "PlaneFigurateNum":
        return cls(polygonal_numbers(k))

    @classmethod
    def centered_square_numbers(cls) -> "PlaneFigurateNum":
        return cls(centered_square_numbers())

    @classmethod
    def diamond_numbers(cls) -> "PlaneFigurateNum":
        return cls(diamond_numbers())

    @classmethod
    def centered_dodecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(centered_dodecagonal_numbers())

    @classmethod
    def star_numbers(cls) -> "PlaneFigurateNum":
        return cls(star_numbers())

    @classmethod
    def centered_mgonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(centered_mgonal_numbers())

    @classmethod
    def pronic_numbers(cls) -> "PlaneFigurateNum":
        return cls(pronic_numbers())

    @classmethod
    def heteromecic_numbers(cls) -> "PlaneFigurateNum":
        return cls(heteromecic_numbers())

    @classmethod
    def oblong_numbers(cls) -> "PlaneFigurateNum":
        return cls(oblong_numbers())

    @classmethod
    def polite_numbers(cls) -> "PlaneFigurateNum":
        return cls(polite_numbers())

    @classmethod
    def impolite_numbers(cls) -> "PlaneFigurateNum":
        return cls(impolite_numbers())

    @classmethod
    def cross_numbers(cls) -> "PlaneFigurateNum":
        return cls(cross_numbers())

    @classmethod
    def aztec_diamond_numbers(cls) -> "PlaneFigurateNum":
        return cls(aztec_diamond_numbers())

    @classmethod
    def polygram_numbers(cls, m: int) -> "PlaneFigurateNum":
        return cls(polygram_numbers(m))

    @classmethod
    def centered_star_polygonal_numbers(cls, m: int) -> "PlaneFigurateNum":
        return cls(centered_star_polygonal_numbers(m))

    @classmethod
    def pentagram_numbers(cls) -> "PlaneFigurateNum":
        return cls(pentagram_numbers())

    @classmethod
    def gnomic_numbers(cls) -> "PlaneFigurateNum":
        return cls(gnomic_numbers())

    @classmethod
    def truncated_triangular_numbers(cls) -> "PlaneFigurateNum":
        return cls(truncated_triangular_numbers())

    @classmethod
    def truncated_square_numbers(cls) -> "PlaneFigurateNum":
        return cls(truncated_square_numbers())

    @classmethod
    def truncated_pronic_numbers(cls) -> "PlaneFigurateNum":
        return cls(truncated_pronic_numbers())

    @classmethod
    def truncated_centered_pol_numbers(cls, m: int) -> "PlaneFigurateNum":
        return cls(truncated_centered_pol_numbers(m))

    @classmethod
    def truncated_centered_mgonal_numbers(cls, m: int) -> "PlaneFigurateNum":
        return cls(truncated_centered_mgonal_numbers(m))

    @classmethod
    def truncated_centered_hexagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(truncated_centered_hexagonal_numbers())

    @classmethod
    def truncated_hex_numbers(cls) -> "PlaneFigurateNum":
        return cls(truncated_hex_numbers())

    @classmethod
    def generalized_mgonal_numbers(cls, m: int, start_num: int = 0) -> "PlaneFigurateNum":
        return cls(generalized_mgonal_numbers(m, start_num))

    @classmethod
    def generalized_centered_pol_numbers(cls, m: int, start_num: int = 0) -> "PlaneFigurateNum":
        return cls(generalized_centered_pol_numbers(m, start_num))

    @classmethod
    def generalized_pronic_numbers(cls, start_num: int = 0) -> "PlaneFigurateNum":
        return cls(generalized_pronic_numbers(start_num))

    # specific plane figuratenum

    @classmethod
    def triangular_numbers(cls) -> "PlaneFigurateNum":
        return cls(triangular_numbers())

    @classmethod
    def square_numbers(cls) -> "PlaneFigurateNum":
        return cls(square_numbers())

    @classmethod
    def pentagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(pentagonal_numbers())

    @classmethod
    def hexagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(hexagonal_numbers())

    @classmethod
    def heptagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(heptagonal_numbers())

    @classmethod
    def octagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(octagonal_numbers())

    @classmethod
    def nonagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(nonagonal_numbers())

    @classmethod
    def decagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(decagonal_numbers())

    @classmethod
    def hendecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(hendecagonal_numbers())

    @classmethod
    def dodecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(dodecagonal_numbers())

    @classmethod
    def tridecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(tridecagonal_numbers())

    @classmethod
    def tetradecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(tetradecagonal_numbers())

    @classmethod
    def pentadecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(pentadecagonal_numbers())

    @classmethod
    def hexadecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(hexadecagonal_numbers())

    @classmethod
    def heptadecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(heptadecagonal_numbers())

    @classmethod
    def octadecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(octadecagonal_numbers())

    @classmethod
    def nonadecagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(nonadecagonal_numbers())

    @classmethod
    def icosagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosagonal_numbers())

    @classmethod
    def icosihenagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosihenagonal_numbers())

    @classmethod
    def icosiheptagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosiheptagonal_numbers())

    @classmethod
    def icosidigonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosidigonal_numbers())

    @classmethod
    def icositrigonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icositrigonal_numbers())

    @classmethod
    def icositetragonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icositetragonal_numbers())

    @classmethod
    def icosipentagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosipentagonal_numbers())

    @classmethod
    def icosihexagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosihexagonal_numbers())

    @classmethod
    def centered_icosiheptagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(centered_icosiheptagonal_numbers())

    @classmethod
    def icosioctagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosioctagonal_numbers())

    @classmethod
    def icosinonagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(icosinonagonal_numbers())

    @classmethod
    def triacontagonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(triacontagonal_numbers())
