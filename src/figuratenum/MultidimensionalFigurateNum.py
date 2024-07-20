from .TakeMethods import TakeMethods

from .multidimensional_figuratenum import (
    pentatope_numbers, hypertetrahedral_numbers, triangulotriangular_numbers, k_hypertetrahedron_numbers,
    regular_k_polytopic_numbers, figurate_numbers_of_order_k, k_dimensional_hypertetrahedron_numbers,
    biquadratic_numbers, k_dimensional_hypercube_numbers, k_hypercube_numbers, hyperoctahedral_numbers,
    hexadecachoron_numbers, four_cross_polytope_numbers, four_orthoplex_numbers, hypericosahedral_numbers,
    tetraplex_numbers, polytetrahedron_numbers, hexacosichoron_numbers, hyperdodecahedral_numbers,
    hecatonicosachoron_numbers, dodecaplex_numbers, polydodecahedron_numbers, polyoctahedral_numbers,
    icositetrachoron_numbers, octaplex_numbers, hyperdiamond_numbers,  k_dimensional_hyperoctahedron_numbers,
    k_cross_polytope_numbers, four_dimensional_mgonal_pyramidal_numbers, mgonal_pyramidal_numbers_of_the_second_order,
    k_dimensional_mgonal_pyramidal_numbers, mgonal_pyramidal_numbers_of_the_k_2_th_order,
    centered_biquadratic_numbers, k_dimensional_centered_hypercube_numbers, centered_polytope_numbers,
    k_dimensional_centered_hypertetrahedron_numbers, centered_hyperoctahedral_numbers, orthoplex_numbers,
    nexus_numbers, k_dimensional_centered_hyperoctahedron_numbers,

    generalized_pentatope_numbers, generalized_k_dimensional_hypertetrahedron_numbers,
    generalized_biquadratic_numbers, generalized_k_dimensional_hypercube_numbers, generalized_hyperoctahedral_numbers,
    generalized_k_dimensional_hyperoctahedron_numbers, generalized_hyperdodecahedral_numbers,
    generalized_hypericosahedral_numbers, generalized_polyoctahedral_numbers,
    generalized_k_dimensional_mgonal_pyramidal_numbers, generalized_k_dimensional_centered_hypercube_numbers,
    generalized_nexus_numbers
)

from .specific_multidimensional_figuratenum import (
    five_dimensional_hypertetrahedron_numbers, six_dimensional_hypertetrahedron_numbers,

    five_dimensional_hypercube_numbers, six_dimensional_hypercube_numbers,

    four_dimensional_hyperoctahedron_numbers, five_dimensional_hyperoctahedron_numbers,
    six_dimensional_hyperoctahedron_numbers, seven_dimensional_hyperoctahedron_numbers,
    eight_dimensional_hyperoctahedron_numbers, nine_dimensional_hyperoctahedron_numbers,
    ten_dimensional_hyperoctahedron_numbers,

    four_dimensional_square_pyramidal_numbers, four_dimensional_pentagonal_pyramidal_numbers,
    four_dimensional_hexagonal_pyramidal_numbers, four_dimensional_heptagonal_pyramidal_numbers,
    four_dimensional_octagonal_pyramidal_numbers, four_dimensional_nonagonal_pyramidal_numbers,
    four_dimensional_decagonal_pyramidal_numbers, four_dimensional_hendecagonal_pyramidal_numbers,
    four_dimensional_dodecagonal_pyramidal_numbers,

    five_dimensional_mgonal_pyramidal_numbers, five_dimensional_square_pyramidal_numbers,
    five_dimensional_pentagonal_pyramidal_numbers, five_dimensional_hexagonal_pyramidal_numbers,
    five_dimensional_heptagonal_pyramidal_numbers, five_dimensional_octagonal_pyramidal_numbers,
    six_dimensional_mgonal_pyramidal_numbers, six_dimensional_square_pyramidal_numbers,
    six_dimensional_pentagonal_pyramidal_numbers, six_dimensional_hexagonal_pyramidal_numbers,
    six_dimensional_heptagonal_pyramidal_numbers, six_dimensional_octagonal_pyramidal_numbers,

    five_dimensional_centered_hypercube_numbers,
    six_dimensional_centered_hypercube_numbers,

    five_dimensional_centered_hypertetrahedron_numbers,
    six_dimensional_centered_hypertetrahedron_numbers,

    five_dimensional_centered_hyperoctahedron_numbers,
    six_dimensional_centered_hyperoctahedron_numbers
)


class MultidimensionalFigurateNum(TakeMethods):

    @classmethod
    def pentatope_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(pentatope_numbers())

    @classmethod
    def hypertetrahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hypertetrahedral_numbers())

    @classmethod
    def triangulotriangular_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(triangulotriangular_numbers())

    @classmethod
    def k_hypertetrahedron_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_hypertetrahedron_numbers(k))

    @classmethod
    def regular_k_polytopic_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(regular_k_polytopic_numbers(k))

    @classmethod
    def figurate_numbers_of_order_k(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(figurate_numbers_of_order_k(k))

    @classmethod
    def k_dimensional_hypertetrahedron_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_hypertetrahedron_numbers(k))

    @classmethod
    def biquadratic_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(biquadratic_numbers())

    @classmethod
    def k_dimensional_hypercube_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_hypercube_numbers())

    @classmethod
    def k_hypercube_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(k_hypercube_numbers())

    @classmethod
    def hyperoctahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hyperoctahedral_numbers())

    @classmethod
    def hexadecachoron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hexadecachoron_numbers())

    @classmethod
    def four_cross_polytope_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(four_cross_polytope_numbers())

    @classmethod
    def four_orthoplex_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(four_orthoplex_numbers())

    @classmethod
    def hypericosahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hypericosahedral_numbers())

    @classmethod
    def tetraplex_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(tetraplex_numbers())

    @classmethod
    def polytetrahedron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(polytetrahedron_numbers())

    @classmethod
    def hexacosichoron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hexacosichoron_numbers())

    @classmethod
    def hyperdodecahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hyperdodecahedral_numbers())

    @classmethod
    def hecatonicosachoron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hecatonicosachoron_numbers())

    @classmethod
    def dodecaplex_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(dodecaplex_numbers())

    @classmethod
    def polydodecahedron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(polydodecahedron_numbers())

    @classmethod
    def polyoctahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(polyoctahedral_numbers())

    @classmethod
    def icositetrachoron_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(icositetrachoron_numbers())

    @classmethod
    def octaplex_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(octaplex_numbers())

    @classmethod
    def hyperdiamond_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(hyperdiamond_numbers())

    @classmethod
    def k_dimensional_hyperoctahedron_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_hyperoctahedron_numbers(k))

    @classmethod
    def k_cross_polytope_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_cross_polytope_numbers(k))

    @classmethod
    def four_dimensional_mgonal_pyramidal_numbers(cls, m: int) -> "MultidimensionalFigurateNum":
        return cls(four_dimensional_mgonal_pyramidal_numbers(m))

    @classmethod
    def mgonal_pyramidal_numbers_of_the_second_order(cls, m: int) -> "MultidimensionalFigurateNum":
        return cls(mgonal_pyramidal_numbers_of_the_second_order(m))

    @classmethod
    def k_dimensional_mgonal_pyramidal_numbers(cls, k: int, m: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_mgonal_pyramidal_numbers(k, m))

    @classmethod
    def mgonal_pyramidal_numbers_of_the_k_2_th_order(cls, k: int, m: int) -> "MultidimensionalFigurateNum":
        return cls(mgonal_pyramidal_numbers_of_the_k_2_th_order(k, m))

    @classmethod
    def centered_biquadratic_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(centered_biquadratic_numbers())

    @classmethod
    def k_dimensional_centered_hypercube_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_centered_hypercube_numbers(k))

    @classmethod
    def centered_polytope_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(centered_polytope_numbers())

    @classmethod
    def k_dimensional_centered_hypertetrahedron_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_centered_hypertetrahedron_numbers(k))

    @classmethod
    def centered_hyperoctahedral_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(centered_hyperoctahedral_numbers())

    @classmethod
    def orthoplex_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(orthoplex_numbers())

    @classmethod
    def nexus_numbers(cls) -> "MultidimensionalFigurateNum":
        return cls(nexus_numbers())

    @classmethod
    def k_dimensional_centered_hyperoctahedron_numbers(cls, k: int) -> "MultidimensionalFigurateNum":
        return cls(k_dimensional_centered_hyperoctahedron_numbers(k))

    @classmethod
    def generalized_pentatope_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_pentatope_numbers(start_num))

    @classmethod
    def generalized_k_dimensional_hypertetrahedron_numbers(cls, k: int = 5, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_k_dimensional_hypertetrahedron_numbers(k, start_num))

    @classmethod
    def generalized_biquadratic_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_biquadratic_numbers(start_num))

    @classmethod
    def generalized_k_dimensional_hypercube_numbers(cls, k: int = 5, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_k_dimensional_hypercube_numbers(k, start_num))

    @classmethod
    def generalized_hyperoctahedral_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_hyperoctahedral_numbers(start_num))

    @classmethod
    def generalized_k_dimensional_hyperoctahedron_numbers(cls, k: int = 5, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_k_dimensional_hyperoctahedron_numbers(k, start_num))

    @classmethod
    def generalized_hyperdodecahedral_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_hyperdodecahedral_numbers(start_num))

    @classmethod
    def generalized_hypericosahedral_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_hypericosahedral_numbers(start_num))

    @classmethod
    def generalized_polyoctahedral_numbers(cls, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_polyoctahedral_numbers(start_num))

    @classmethod
    def generalized_k_dimensional_mgonal_pyramidal_numbers(cls, k: int, m: int, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_k_dimensional_mgonal_pyramidal_numbers(k, m, start_num))

    @classmethod
    def generalized_k_dimensional_centered_hypercube_numbers(cls, k: int, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_k_dimensional_centered_hypercube_numbers(k, start_num))

    @classmethod
    def generalized_nexus_numbers(cls, k: int, start_num: int = 0) -> "MultidimensionalFigurateNum":
        return cls(generalized_nexus_numbers(k, start_num))

    # specific multidimensional figuratenum

    @classmethod
    def five_dimensional_hypertetrahedron_numbers(cls):
        return cls(five_dimensional_hypertetrahedron_numbers())

    @classmethod
    def six_dimensional_hypertetrahedron_numbers(cls):
        return cls(six_dimensional_hypertetrahedron_numbers())

    @classmethod
    def five_dimensional_hypercube_numbers(cls):
        return cls(five_dimensional_hypercube_numbers())

    @classmethod
    def six_dimensional_hypercube_numbers(cls):
        return cls(six_dimensional_hypercube_numbers())

    @classmethod
    def four_dimensional_hyperoctahedron_numbers(cls):
        return cls(four_dimensional_hyperoctahedron_numbers())

    @classmethod
    def five_dimensional_hyperoctahedron_numbers(cls):
        return cls(five_dimensional_hyperoctahedron_numbers())

    @classmethod
    def six_dimensional_hyperoctahedron_numbers(cls):
        return cls(six_dimensional_hyperoctahedron_numbers())

    @classmethod
    def seven_dimensional_hyperoctahedron_numbers(cls):
        return cls(seven_dimensional_hyperoctahedron_numbers())

    @classmethod
    def eight_dimensional_hyperoctahedron_numbers(cls):
        return cls(eight_dimensional_hyperoctahedron_numbers())

    @classmethod
    def nine_dimensional_hyperoctahedron_numbers(cls):
        return cls(nine_dimensional_hyperoctahedron_numbers())

    @classmethod
    def ten_dimensional_hyperoctahedron_numbers(cls):
        return cls(ten_dimensional_hyperoctahedron_numbers())

    @classmethod
    def four_dimensional_square_pyramidal_numbers(cls):
        return cls(four_dimensional_square_pyramidal_numbers())

    @classmethod
    def four_dimensional_pentagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_pentagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_hexagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_hexagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_heptagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_heptagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_octagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_octagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_nonagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_nonagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_decagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_decagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_hendecagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_hendecagonal_pyramidal_numbers())

    @classmethod
    def four_dimensional_dodecagonal_pyramidal_numbers(cls):
        return cls(four_dimensional_dodecagonal_pyramidal_numbers())

    @classmethod
    def five_dimensional_mgonal_pyramidal_numbers(cls, m: int):
        return cls(five_dimensional_mgonal_pyramidal_numbers(m))

    @classmethod
    def five_dimensional_square_pyramidal_numbers(cls):
        return cls(five_dimensional_square_pyramidal_numbers())

    @classmethod
    def five_dimensional_pentagonal_pyramidal_numbers(cls):
        return cls(five_dimensional_pentagonal_pyramidal_numbers())

    @classmethod
    def five_dimensional_hexagonal_pyramidal_numbers(cls):
        return cls(five_dimensional_hexagonal_pyramidal_numbers())

    @classmethod
    def five_dimensional_heptagonal_pyramidal_numbers(cls):
        return cls(five_dimensional_heptagonal_pyramidal_numbers())

    @classmethod
    def five_dimensional_octagonal_pyramidal_numbers(cls):
        return cls(five_dimensional_octagonal_pyramidal_numbers())

    @classmethod
    def six_dimensional_mgonal_pyramidal_numbers(cls, m: int):
        return cls(six_dimensional_mgonal_pyramidal_numbers(m))

    @classmethod
    def six_dimensional_square_pyramidal_numbers(cls):
        return cls(six_dimensional_square_pyramidal_numbers())

    @classmethod
    def six_dimensional_pentagonal_pyramidal_numbers(cls):
        return cls(six_dimensional_pentagonal_pyramidal_numbers())

    @classmethod
    def six_dimensional_hexagonal_pyramidal_numbers(cls):
        return cls(six_dimensional_hexagonal_pyramidal_numbers())

    @classmethod
    def six_dimensional_heptagonal_pyramidal_numbers(cls):
        return cls(six_dimensional_heptagonal_pyramidal_numbers())

    @classmethod
    def six_dimensional_octagonal_pyramidal_numbers(cls):
        return cls(six_dimensional_octagonal_pyramidal_numbers())

    @classmethod
    def five_dimensional_centered_hypercube_numbers(cls):
        return cls(five_dimensional_centered_hypercube_numbers())

    @classmethod
    def six_dimensional_centered_hypercube_numbers(cls):
        return cls(six_dimensional_centered_hypercube_numbers())

    @classmethod
    def five_dimensional_centered_hypertetrahedron_numbers(cls):
        return cls(five_dimensional_centered_hypertetrahedron_numbers())

    @classmethod
    def six_dimensional_centered_hypertetrahedron_numbers(cls):
        return cls(six_dimensional_centered_hypertetrahedron_numbers())

    @classmethod
    def five_dimensional_centered_hyperoctahedron_numbers(cls):
        return cls(five_dimensional_centered_hyperoctahedron_numbers())

    @classmethod
    def six_dimensional_centered_hyperoctahedron_numbers(cls):
        return cls(six_dimensional_centered_hyperoctahedron_numbers())
