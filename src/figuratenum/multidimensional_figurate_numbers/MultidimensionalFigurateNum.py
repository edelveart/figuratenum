from typing import Iterator

from .multidimensional_figuratenum import (
    pentatope, hypertetrahedral, triangulotriangular, k_hypertetrahedron,
    regular_k_polytopic, figurate_of_order_k, k_dimensional_hypertetrahedron,
    biquadratic, k_dimensional_hypercube, k_hypercube, hyperoctahedral,
    hexadecachoron, four_cross_polytope, four_orthoplex, hypericosahedral,
    tetraplex, polytetrahedron, hexacosichoron, hyperdodecahedral,
    hecatonicosachoron, dodecaplex, polydodecahedron, polyoctahedral,
    icositetrachoron, octaplex, hyperdiamond,  k_dimensional_hyperoctahedron,
    k_cross_polytope, four_dimensional_mgonal_pyramidal, mgonal_pyramidal_of_the_second_order,
    k_dimensional_mgonal_pyramidal, mgonal_pyramidal_of_the_k_2_th_order,
    centered_biquadratic, k_dimensional_centered_hypercube, centered_polytope,
    k_dimensional_centered_hypertetrahedron, centered_hyperoctahedral, orthoplex,
    nexus, k_dimensional_centered_hyperoctahedron,

    generalized_pentatope, generalized_k_dimensional_hypertetrahedron,
    generalized_biquadratic, generalized_k_dimensional_hypercube, generalized_hyperoctahedral,
    generalized_k_dimensional_hyperoctahedron, generalized_hyperdodecahedral,
    generalized_hypericosahedral, generalized_polyoctahedral,
    generalized_k_dimensional_mgonal_pyramidal, generalized_k_dimensional_centered_hypercube,
    generalized_nexus
)

from .specific_multidimensional_figuratenum import (
    five_dimensional_hypertetrahedron, six_dimensional_hypertetrahedron,

    five_dimensional_hypercube, six_dimensional_hypercube,

    four_dimensional_hyperoctahedron, five_dimensional_hyperoctahedron,
    six_dimensional_hyperoctahedron, seven_dimensional_hyperoctahedron,
    eight_dimensional_hyperoctahedron, nine_dimensional_hyperoctahedron,
    ten_dimensional_hyperoctahedron,

    four_dimensional_square_pyramidal, four_dimensional_pentagonal_pyramidal,
    four_dimensional_hexagonal_pyramidal, four_dimensional_heptagonal_pyramidal,
    four_dimensional_octagonal_pyramidal, four_dimensional_nonagonal_pyramidal,
    four_dimensional_decagonal_pyramidal, four_dimensional_hendecagonal_pyramidal,
    four_dimensional_dodecagonal_pyramidal,

    five_dimensional_mgonal_pyramidal, five_dimensional_square_pyramidal,
    five_dimensional_pentagonal_pyramidal, five_dimensional_hexagonal_pyramidal,
    five_dimensional_heptagonal_pyramidal, five_dimensional_octagonal_pyramidal,
    six_dimensional_mgonal_pyramidal, six_dimensional_square_pyramidal,
    six_dimensional_pentagonal_pyramidal, six_dimensional_hexagonal_pyramidal,
    six_dimensional_heptagonal_pyramidal, six_dimensional_octagonal_pyramidal,

    five_dimensional_centered_hypercube,
    six_dimensional_centered_hypercube,

    five_dimensional_centered_hypertetrahedron,
    six_dimensional_centered_hypertetrahedron,

    five_dimensional_centered_hyperoctahedron,
    six_dimensional_centered_hyperoctahedron
)


class MultidimensionalFigurateNum:

    def pentatope(self) -> Iterator[int]:
        return pentatope()

    def hypertetrahedral(self) -> Iterator[int]:
        return hypertetrahedral()

    def pentachoron(self) -> Iterator[int]:
        return hypertetrahedral()

    def cell_5(self) -> Iterator[int]:
        return hypertetrahedral()

    def triangulotriangular(self) -> Iterator[int]:
        return triangulotriangular()

    def k_hypertetrahedron(self, k: int) -> Iterator[int]:
        return k_hypertetrahedron(k)

    def regular_k_polytopic(self, k: int) -> Iterator[int]:
        return regular_k_polytopic(k)

    def figurate_of_order_k(self, k: int) -> Iterator[int]:
        return figurate_of_order_k(k)

    def k_dimensional_hypertetrahedron(self, k: int) -> Iterator[int]:
        return k_dimensional_hypertetrahedron(k)

    def biquadratic(self) -> Iterator[int]:
        return biquadratic()

    def hypercube(self) -> Iterator[int]:
        return biquadratic()

    def cell_8(self) -> Iterator[int]:
        return biquadratic()

    def octachoron(self) -> Iterator[int]:
        return biquadratic()

    def k_dimensional_hypercube(self, k: int) -> Iterator[int]:
        return k_dimensional_hypercube(k)

    def k_hypercube(self, k: int) -> Iterator[int]:
        return k_hypercube(k)

    def tesseract(self) -> Iterator[int]:
        return k_dimensional_hypercube(4)

    def hyperoctahedral(self) -> Iterator[int]:
        return hyperoctahedral()

    def hexadecachoron(self) -> Iterator[int]:
        return hexadecachoron()

    def cell_16(self) -> Iterator[int]:
        return hyperoctahedral()

    def four_cross_polytope(self) -> Iterator[int]:
        return four_cross_polytope()

    def four_orthoplex(self) -> Iterator[int]:
        return four_orthoplex()

    def hypericosahedral(self) -> Iterator[int]:
        return hypericosahedral()

    def tetraplex(self) -> Iterator[int]:
        return tetraplex()

    def polytetrahedron(self) -> Iterator[int]:
        return polytetrahedron()

    def hexacosichoron(self) -> Iterator[int]:
        return hexacosichoron()

    def hyperdodecahedral(self) -> Iterator[int]:
        return hyperdodecahedral()

    def hecatonicosachoron(self) -> Iterator[int]:
        return hecatonicosachoron()

    def dodecaplex(self) -> Iterator[int]:
        return dodecaplex()

    def polydodecahedron(self) -> Iterator[int]:
        return polydodecahedron()

    def polyoctahedral(self) -> Iterator[int]:
        return polyoctahedral()

    def icositetrachoron(self) -> Iterator[int]:
        return icositetrachoron()

    def octaplex(self) -> Iterator[int]:
        return octaplex()

    def hyperdiamond(self) -> Iterator[int]:
        return hyperdiamond()

    def k_dimensional_hyperoctahedron(self, k: int) -> Iterator[int]:
        return k_dimensional_hyperoctahedron(k)

    def k_cross_polytope(self, k: int) -> Iterator[int]:
        return k_cross_polytope(k)

    def four_dimensional_mgonal_pyramidal(self, m: int) -> Iterator[int]:
        return four_dimensional_mgonal_pyramidal(m)

    def mgonal_pyramidal_of_the_second_order(self, m: int) -> Iterator[int]:
        return mgonal_pyramidal_of_the_second_order(m)

    def k_dimensional_mgonal_pyramidal(self, k: int, m: int) -> Iterator[int]:
        return k_dimensional_mgonal_pyramidal(k, m)

    def mgonal_pyramidal_of_the_k_2_th_order(self, k: int, m: int) -> Iterator[int]:
        return mgonal_pyramidal_of_the_k_2_th_order(k, m)

    def centered_biquadratic(self) -> Iterator[int]:
        return centered_biquadratic()

    def k_dimensional_centered_hypercube(self, k: int) -> Iterator[int]:
        return k_dimensional_centered_hypercube(k)

    def centered_polytope(self) -> Iterator[int]:
        return centered_polytope()

    def k_dimensional_centered_hypertetrahedron(self, k: int) -> Iterator[int]:
        return k_dimensional_centered_hypertetrahedron(k)

    def centered_hyperoctahedral(self) -> Iterator[int]:
        return centered_hyperoctahedral()

    def orthoplex(self) -> Iterator[int]:
        return orthoplex()

    def nexus(self) -> Iterator[int]:
        return nexus()

    def k_dimensional_centered_hyperoctahedron(self, k: int) -> Iterator[int]:
        return k_dimensional_centered_hyperoctahedron(k)

    def generalized_pentatope(self, start_num: int = 0) -> Iterator[int]:
        return generalized_pentatope(start_num)

    def generalized_k_dimensional_hypertetrahedron(self, k: int = 5, start_num: int = 0) -> Iterator[int]:
        return generalized_k_dimensional_hypertetrahedron(k, start_num)

    def generalized_biquadratic(self, start_num: int = 0) -> Iterator[int]:
        return generalized_biquadratic(start_num)

    def generalized_k_dimensional_hypercube(self, k: int = 5, start_num: int = 0) -> Iterator[int]:
        return generalized_k_dimensional_hypercube(k, start_num)

    def generalized_hyperoctahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_hyperoctahedral(start_num)

    def generalized_k_dimensional_hyperoctahedron(self, k: int = 5, start_num: int = 0) -> Iterator[int]:
        return generalized_k_dimensional_hyperoctahedron(k, start_num)

    def generalized_hyperdodecahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_hyperdodecahedral(start_num)

    def generalized_hypericosahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_hypericosahedral(start_num)

    def generalized_polyoctahedral(self, start_num: int = 0) -> Iterator[int]:
        return generalized_polyoctahedral(start_num)

    def generalized_k_dimensional_mgonal_pyramidal(self, k: int, m: int, start_num: int = 0) -> Iterator[int]:
        return generalized_k_dimensional_mgonal_pyramidal(k, m, start_num)

    def generalized_k_dimensional_centered_hypercube(self, k: int, start_num: int = 0) -> Iterator[int]:
        return generalized_k_dimensional_centered_hypercube(k, start_num)

    def generalized_nexus(self, k: int, start_num: int = 0) -> Iterator[int]:
        return generalized_nexus(k, start_num)

    # specific multidimensional figuratenum

    def five_dimensional_hypertetrahedron(self):
        return five_dimensional_hypertetrahedron()

    def six_dimensional_hypertetrahedron(self):
        return six_dimensional_hypertetrahedron()

    def five_dimensional_hypercube(self):
        return five_dimensional_hypercube()

    def six_dimensional_hypercube(self):
        return six_dimensional_hypercube()

    def four_dimensional_hyperoctahedron(self):
        return four_dimensional_hyperoctahedron()

    def five_dimensional_hyperoctahedron(self):
        return five_dimensional_hyperoctahedron()

    def six_dimensional_hyperoctahedron(self):
        return six_dimensional_hyperoctahedron()

    def seven_dimensional_hyperoctahedron(self):
        return seven_dimensional_hyperoctahedron()

    def eight_dimensional_hyperoctahedron(self):
        return eight_dimensional_hyperoctahedron()

    def nine_dimensional_hyperoctahedron(self):
        return nine_dimensional_hyperoctahedron()

    def ten_dimensional_hyperoctahedron(self):
        return ten_dimensional_hyperoctahedron()

    def four_dimensional_square_pyramidal(self):
        return four_dimensional_square_pyramidal()

    def four_dimensional_pentagonal_pyramidal(self):
        return four_dimensional_pentagonal_pyramidal()

    def four_dimensional_hexagonal_pyramidal(self):
        return four_dimensional_hexagonal_pyramidal()

    def four_dimensional_heptagonal_pyramidal(self):
        return four_dimensional_heptagonal_pyramidal()

    def four_dimensional_octagonal_pyramidal(self):
        return four_dimensional_octagonal_pyramidal()

    def four_dimensional_nonagonal_pyramidal(self):
        return four_dimensional_nonagonal_pyramidal()

    def four_dimensional_decagonal_pyramidal(self):
        return four_dimensional_decagonal_pyramidal()

    def four_dimensional_hendecagonal_pyramidal(self):
        return four_dimensional_hendecagonal_pyramidal()

    def four_dimensional_dodecagonal_pyramidal(self):
        return four_dimensional_dodecagonal_pyramidal()

    def five_dimensional_mgonal_pyramidal(self, m: int):
        return five_dimensional_mgonal_pyramidal(m)

    def five_dimensional_square_pyramidal(self):
        return five_dimensional_square_pyramidal()

    def five_dimensional_pentagonal_pyramidal(self):
        return five_dimensional_pentagonal_pyramidal()

    def five_dimensional_hexagonal_pyramidal(self):
        return five_dimensional_hexagonal_pyramidal()

    def five_dimensional_heptagonal_pyramidal(self):
        return five_dimensional_heptagonal_pyramidal()

    def five_dimensional_octagonal_pyramidal(self):
        return five_dimensional_octagonal_pyramidal()

    def six_dimensional_mgonal_pyramidal(self, m: int):
        return six_dimensional_mgonal_pyramidal(m)

    def six_dimensional_square_pyramidal(self):
        return six_dimensional_square_pyramidal()

    def six_dimensional_pentagonal_pyramidal(self):
        return six_dimensional_pentagonal_pyramidal()

    def six_dimensional_hexagonal_pyramidal(self):
        return six_dimensional_hexagonal_pyramidal()

    def six_dimensional_heptagonal_pyramidal(self):
        return six_dimensional_heptagonal_pyramidal()

    def six_dimensional_octagonal_pyramidal(self):
        return six_dimensional_octagonal_pyramidal()

    def five_dimensional_centered_hypercube(self):
        return five_dimensional_centered_hypercube()

    def six_dimensional_centered_hypercube(self):
        return six_dimensional_centered_hypercube()

    def five_dimensional_centered_hypertetrahedron(self):
        return five_dimensional_centered_hypertetrahedron()

    def six_dimensional_centered_hypertetrahedron(self):
        return six_dimensional_centered_hypertetrahedron()

    def five_dimensional_centered_hyperoctahedron(self):
        return five_dimensional_centered_hyperoctahedron()

    def six_dimensional_centered_hyperoctahedron(self):
        return six_dimensional_centered_hyperoctahedron()
