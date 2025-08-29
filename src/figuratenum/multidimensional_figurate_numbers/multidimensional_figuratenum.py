from collections.abc import Generator
from ..utils import (
    factorial_iter, binomial_coefficient, pseudo_rising_factorial,
    pseudo_pochhammer_function, rising_factorial,
    acc_helper_centered_hypertetrahedron,
    helper_ext_int_double_sigma
)


def pentatope() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3)) // 24
        delta += 1


def hypertetrahedral() -> Generator[int]:
    return pentatope()


def triangulotriangular() -> Generator[int]:
    return pentatope()


def k_dimensional_hypertetrahedron(k: int) -> Generator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, k) // factorial_iter(k)
        delta += 1


def k_hypertetrahedron(k: int) -> Generator[int]:
    return k_dimensional_hypertetrahedron(k)


def regular_k_polytopic(k: int) -> Generator[int]:
    return k_dimensional_hypertetrahedron(k)


def figurate_of_order_k(k: int) -> Generator[int]:
    return k_dimensional_hypertetrahedron(k)


def biquadratic() -> Generator[int]:
    delta = 1
    while True:
        yield delta ** 4
        delta += 1


def k_dimensional_hypercube(k: int) -> Generator[int]:
    delta = 1
    while True:
        yield delta ** k
        delta += 1


def k_hypercube(k: int) -> Generator[int]:
    return k_dimensional_hypercube(k)


def hyperoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1


def hexadecachoron() -> Generator[int]:
    return hyperoctahedral()


def four_cross_polytope() -> Generator[int]:
    return hyperoctahedral()


def four_orthoplex() -> Generator[int]:
    return hyperoctahedral()


def hypericosahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (145 * delta ** 3 - 280 * delta ** 2 + 179 * delta - 38)) // 6
        delta += 1


def tetraplex() -> Generator[int]:
    return hypericosahedral()


def polytetrahedron() -> Generator[int]:
    return hypericosahedral()


def hexacosichoron() -> Generator[int]:
    return hypericosahedral()


def hyperdodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (261 * delta ** 3 - 504 * delta ** 2 + 283 * delta - 38)) // 2
        delta += 1


def hecatonicosachoron() -> Generator[int]:
    return hyperdodecahedral()


def dodecaplex() -> Generator[int]:
    return hyperdodecahedral()


def polydodecahedron() -> Generator[int]:
    return hyperdodecahedral()


def polyoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (3 * delta ** 2 - 4 * delta + 2)
        delta += 1


def icositetrachoron() -> Generator[int]:
    return polyoctahedral()


def octaplex() -> Generator[int]:
    return polyoctahedral()


def hyperdiamond() -> Generator[int]:
    return polyoctahedral()


def k_dimensional_hyperoctahedron(k: int) -> Generator[int]:
    delta = 1
    while True:
        a = 0
        for i in range(0, (k - 1) + 1):
            a += (binomial_coefficient(k - 1, i) *
                  (rising_factorial(delta - i, k) // factorial_iter(k)))
        yield a
        delta += 1


def k_cross_polytope(k: int) -> Generator[int]:
    return k_dimensional_hyperoctahedron(k)


def four_dimensional_mgonal_pyramidal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((m - 2) * delta - m + 6)) // 24
        delta += 1


def mgonal_pyramidal_of_the_second_order(m: int) -> Generator[int]:
    return four_dimensional_mgonal_pyramidal(m)


def k_dimensional_mgonal_pyramidal(k: int, m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def mgonal_pyramidal_of_the_k_2_th_order(k: int, m: int) -> Generator[int]:
    return k_dimensional_mgonal_pyramidal(k, m)


def centered_biquadratic() -> Generator[int]:
    delta = 1
    a = 0
    while True:
        a += delta ** 4 - (delta - 2) ** 4
        yield a + 1
        delta += 1


def k_dimensional_centered_hypercube(k: int) -> Generator[int]:
    delta = 1
    while True:
        yield delta ** k + (delta - 1) ** k
        delta += 1


def centered_polytope() -> Generator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 4 - 10 * delta ** 3 + 55 * delta ** 2 - 50 * delta + 24) // 24
        delta += 1


def k_dimensional_centered_hypertetrahedron(k: int) -> Generator[int]:
    delta = 1
    while True:
        yield acc_helper_centered_hypertetrahedron(k, delta)
        delta += 1


def centered_hyperoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 4 - 4 * delta ** 3 + 10 * delta ** 2 - 8 * delta + 3) // 3
        delta += 1


def orthoplex() -> Generator[int]:
    return centered_hyperoctahedral()


def nexus(k: int) -> Generator[int]:
    delta = 0
    while True:
        yield (delta + 1) ** (k + 1) - delta ** (k + 1)
        delta += 1


def k_dimensional_centered_hyperoctahedron(k: int) -> Generator[int]:
    delta = 1
    yield 1
    while True:
        yield helper_ext_int_double_sigma(k, delta)
        delta += 1


def generalized_pentatope(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta * (delta + 1) * (delta + 2) * (delta + 3) // 24
        delta += 1


def generalized_k_dimensional_hypertetrahedron(k: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield rising_factorial(delta, k) // factorial_iter(k)
        delta += 1


def generalized_biquadratic(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** 4
        delta += 1


def generalized_k_dimensional_hypercube(k: int = 5, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** k
        delta += 1


def generalized_hyperoctahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1


def generalized_k_dimensional_hyperoctahedron(k: int = 5, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        a = 0
        for i in range(0, (k - 1) + 1):
            a += (binomial_coefficient(k - 1, i) *
                  (rising_factorial(delta - i, k) // factorial_iter(k)))
        yield a
        delta += 1


def generalized_hyperdodecahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta * (261 * delta ** 3 - 504 * delta ** 2 + 283 * delta - 38)) // 2
        delta += 1


def generalized_hypericosahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta * (145 * delta ** 3 - 280 * delta ** 2 + 179 * delta - 38)) // 6
        delta += 1


def generalized_polyoctahedral(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** 2 * (3 * delta ** 2 - 4 * delta + 2)
        delta += 1


def generalized_k_dimensional_mgonal_pyramidal(k: int, m: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (pseudo_pochhammer_function(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def generalized_k_dimensional_centered_hypercube(k: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta ** k + (delta - 1) ** k
        delta += 1


def generalized_nexus(k: int, start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield (delta + 1) ** (k + 1) - delta ** (k + 1)
        delta += 1
