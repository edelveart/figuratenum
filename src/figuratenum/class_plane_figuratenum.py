from typing import Iterator, List
from plane_figuratenum import (
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


class PlaneFigurateNum:
    def __init__(self, generator: Iterator[int]):
        self.generator = generator

    def take(self, n: int) -> List[int]:
        result = []
        for _ in range(n):
            result.append(next(self.generator))
        return result

    @classmethod
    def polygonal_numbers(cls) -> "PlaneFigurateNum":
        return cls(polygonal_numbers())

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
