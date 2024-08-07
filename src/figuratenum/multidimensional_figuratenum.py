from typing import Iterator
from .utils import (
    factorial_iter, binomial_coefficient, pseudo_rising_factorial,
    pseudo_pochhammer_function, rising_factorial,
    acc_helper_centered_hypertetrahedron,
    helper_ext_int_double_sigma
)


def pentatope_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3)) // 24
        delta += 1


def hypertetrahedral_numbers() -> Iterator[int]:
    return pentatope_numbers()


def triangulotriangular_numbers() -> Iterator[int]:
    return pentatope_numbers()


def k_dimensional_hypertetrahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, k) // factorial_iter(k)
        delta += 1


def k_hypertetrahedron_numbers(k: int) -> Iterator[int]:
    return k_dimensional_hypertetrahedron_numbers(k)


def regular_k_polytopic_numbers(k: int) -> Iterator[int]:
    return k_dimensional_hypertetrahedron_numbers(k)


def figurate_numbers_of_order_k(k: int) -> Iterator[int]:
    return k_dimensional_hypertetrahedron_numbers(k)


def biquadratic_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 4
        delta += 1


def k_dimensional_hypercube_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** k
        delta += 1


def k_hypercube_numbers(k: int) -> Iterator[int]:
    return k_dimensional_hypercube_numbers(k)


def hyperoctahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1


def hexadecachoron_numbers() -> Iterator[int]:
    return hyperoctahedral_numbers()


def four_cross_polytope_numbers() -> Iterator[int]:
    return hyperoctahedral_numbers()


def four_orthoplex_numbers() -> Iterator[int]:
    return hyperoctahedral_numbers()


def hypericosahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (145 * delta ** 3 - 280 * delta ** 2 + 179 * delta - 38)) // 6
        delta += 1


def tetraplex_numbers() -> Iterator[int]:
    return hypericosahedral_numbers()


def polytetrahedron_numbers() -> Iterator[int]:
    return hypericosahedral_numbers()


def hexacosichoron_numbers() -> Iterator[int]:
    return hypericosahedral_numbers()


def hyperdodecahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (261 * delta ** 3 - 504 * delta ** 2 + 283 * delta - 38)) // 2
        delta += 1


def hecatonicosachoron_numbers() -> Iterator[int]:
    return hyperdodecahedral_numbers()


def dodecaplex_numbers() -> Iterator[int]:
    return hyperdodecahedral_numbers()


def polydodecahedron_numbers() -> Iterator[int]:
    return hyperdodecahedral_numbers()


def polyoctahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (3 * delta ** 2 - 4 * delta + 2)
        delta += 1


def icositetrachoron_numbers() -> Iterator[int]:
    return polyoctahedral_numbers()


def octaplex_numbers() -> Iterator[int]:
    return polyoctahedral_numbers()


def hyperdiamond_numbers() -> Iterator[int]:
    return polyoctahedral_numbers()


def k_dimensional_hyperoctahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        a = 0
        for i in range(0, (k - 1) + 1):
            a += (binomial_coefficient(k - 1, i) *
                  (rising_factorial(delta - i, k) // factorial_iter(k)))
        yield a
        delta += 1


def k_cross_polytope_numbers(k: int) -> Iterator[int]:
    return k_dimensional_hyperoctahedron_numbers(k)


def four_dimensional_mgonal_pyramidal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((m - 2) * delta - m + 6)) // 24
        delta += 1


def mgonal_pyramidal_numbers_of_the_second_order(m: int) -> Iterator[int]:
    return four_dimensional_mgonal_pyramidal_numbers(m)


def k_dimensional_mgonal_pyramidal_numbers(k: int, m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def mgonal_pyramidal_numbers_of_the_k_2_th_order(k: int, m: int) -> Iterator[int]:
    return k_dimensional_mgonal_pyramidal_numbers(k, m)


def centered_biquadratic_numbers() -> Iterator[int]:
    delta = 1
    a = 0
    while True:
        a += delta ** 4 - (delta - 2) ** 4
        yield a + 1
        delta += 1


def k_dimensional_centered_hypercube_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** k + (delta - 1) ** k
        delta += 1


def centered_polytope_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (5 * delta ** 4 - 10 * delta ** 3 + 55 * delta ** 2 - 50 * delta + 24) // 24
        delta += 1


def k_dimensional_centered_hypertetrahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield acc_helper_centered_hypertetrahedron(k, delta)
        delta += 1


def centered_hyperoctahedral_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 4 - 4 * delta ** 3 + 10 * delta ** 2 - 8 * delta + 3) // 3
        delta += 1


def orthoplex_numbers() -> Iterator[int]:
    return centered_hyperoctahedral_numbers()


def nexus_numbers(k: int) -> Iterator[int]:
    delta = 0
    while True:
        yield (delta + 1) ** (k + 1) - delta ** (k + 1)
        delta += 1


def k_dimensional_centered_hyperoctahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    yield 1
    while True:
        yield helper_ext_int_double_sigma(k, delta)
        delta += 1


def generalized_pentatope_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta * (delta + 1) * (delta + 2) * (delta + 3) // 24
        delta += 1


def generalized_k_dimensional_hypertetrahedron_numbers(k: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield rising_factorial(delta, k) / factorial_iter(k)
        delta += 1


def generalized_biquadratic_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** 4
        delta += 1


def generalized_k_dimensional_hypercube_numbers(k: int = 5, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** k
        delta += 1


def generalized_hyperoctahedral_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1


def generalized_k_dimensional_hyperoctahedron_numbers(k: int = 5, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        a = 0
        for i in range(0, (k - 1) + 1):
            a += (binomial_coefficient(k - 1, i) *
                  (rising_factorial(delta - i, k) // factorial_iter(k)))
        yield a
        delta += 1


def generalized_hyperdodecahedral_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta * (261 * delta ** 3 - 504 * delta ** 2 + 283 * delta - 38)) // 2
        delta += 1


def generalized_hypericosahedral_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta * (145 * delta ** 3 - 280 * delta ** 2 + 179 * delta - 38)) // 6
        delta += 1


def generalized_polyoctahedral_numbers(start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** 2 * (3 * delta ** 2 - 4 * delta + 2)
        delta += 1


def generalized_k_dimensional_mgonal_pyramidal_numbers(k: int, m: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (pseudo_pochhammer_function(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def generalized_k_dimensional_centered_hypercube_numbers(k: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield delta ** k + (delta - 1) ** k
        delta += 1


def generalized_nexus_numbers(k: int, start_num: int = 0) -> Iterator[int]:
    delta = start_num
    while True:
        yield (delta + 1) ** (k + 1) - delta ** (k + 1)
        delta += 1
