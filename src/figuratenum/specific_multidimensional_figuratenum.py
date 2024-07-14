from typing import Iterator
from .multidimensional_figuratenum import (
    rising_factorial,
    factorial_iter,
    pseudo_rising_factorial,
    acc_helper_centered_hypertetrahedron,
    helper_ext_int_double_sigma
)

# specific cases of k_dimensional_hypertetrahedron_numbers(k)


def five_dimensional_hypertetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, 5) // factorial_iter(5)
        delta += 1


def six_dimensional_hypertetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, 6) // factorial_iter(6)
        delta += 1


# specific cases of k_dimensional_hypercube_numbers(k)


def five_dimensional_hypercube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 5
        delta += 1


def six_dimensional_hypercube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 6
        delta += 1


# specific cases of k_dimensional_hyperoctahedron_numbers(k) = k_cross_polytope_numbers(k)


def four_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (delta ** 2 + 2) // 3
        delta += 1


def five_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta * (2 * delta ** 4 + 10 * delta ** 2 + 3) // 15
        delta += 1


def six_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (2 * delta ** 4 + 20 * delta ** 2 + 23) // 45
        delta += 1


def seven_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (4 * delta ** 6 + 70 * delta ** 4 + 196 * delta ** 2 + 45) * delta // 315
        delta += 1


def eight_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta ** 6 + 28 * delta ** 4 + 154 * delta ** 2 + 132) * (delta ** 2) // 315
        delta += 1


def nine_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 8 + 84 * delta ** 6 + 798 * delta ** 4 + 1636 * delta ** 2 + 315) * delta // 2835
        delta += 1


def ten_dimensional_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 8 + 120 * delta ** 6 + 1806 * delta ** 4 + 7180 * delta ** 2 + 5067) * delta ** 2 // 14175
        delta += 1


# specific cases of four_dimensional_mgonal_pyramidal_numbers(m) = mgonal_pyramidal_numbers_of_the_second_order(m)


def four_dimensional_square_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((4 - 2) * delta - 4 + 6)) // 24
        delta += 1


def four_dimensional_pentagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((5 - 2) * delta - 5 + 6)) // 24
        delta += 1


def four_dimensional_hexagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((6 - 2) * delta - 6 + 6)) // 24
        delta += 1


def four_dimensional_heptagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((7 - 2) * delta - 7 + 6)) // 24
        delta += 1


def four_dimensional_octagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((8 - 2) * delta - 8 + 6)) // 24
        delta += 1


def four_dimensional_nonagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((9 - 2) * delta - 9 + 6)) // 24
        delta += 1


def four_dimensional_decagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((10 - 2) * delta - 10 + 6)) // 24
        delta += 1


def four_dimensional_hendecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((11 - 2) * delta - 11 + 6)) // 24
        delta += 1


def four_dimensional_dodecagonal_pyramidal_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((12 - 2) * delta - 12 + 6)) // 24
        delta += 1


# specific cases of k_dimensional_mgonal_pyramidal_numbers(k, m) = mgonal_pyramidal_numbers_of_the_k_2_th_order(k, m)


def five_dimensional_mgonal_pyramidal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3) * ((m - 2) * delta - m + 7)) // 120
        delta += 1


def five_dimensional_square_pyramidal_numbers() -> Iterator[int]:
    k = 5
    m = 4
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def five_dimensional_pentagonal_pyramidal_numbers() -> Iterator[int]:
    k = 5
    m = 5
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def five_dimensional_hexagonal_pyramidal_numbers() -> Iterator[int]:
    k = 5
    m = 6
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def five_dimensional_heptagonal_pyramidal_numbers() -> Iterator[int]:
    k = 5
    m = 7
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def five_dimensional_octagonal_pyramidal_numbers() -> Iterator[int]:
    k = 5
    m = 8
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def six_dimensional_mgonal_pyramidal_numbers(m: int) -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3) * (delta + 4) * ((m - 2) * delta - m + 8)) // 720
        delta += 1


def six_dimensional_square_pyramidal_numbers() -> Iterator[int]:
    k = 6
    m = 4
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def six_dimensional_pentagonal_pyramidal_numbers() -> Iterator[int]:
    k = 6
    m = 5
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def six_dimensional_hexagonal_pyramidal_numbers() -> Iterator[int]:
    k = 6
    m = 6
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def six_dimensional_heptagonal_pyramidal_numbers() -> Iterator[int]:
    k = 6
    m = 7
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


def six_dimensional_octagonal_pyramidal_numbers() -> Iterator[int]:
    k = 6
    m = 8
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial_iter(k)
        delta += 1


# specific cases of k_dimensional_centered_hypercube_numbers(k)


def five_dimensional_centered_hypercube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 5 + (delta - 1) ** 5
        delta += 1


def six_dimensional_centered_hypercube_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield delta ** 6 + (delta - 1) ** 6
        delta += 1


# specific cases of k_dimensional_centered_hypertetrahedron_numbers(k)

def five_dimensional_centered_hypertetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield acc_helper_centered_hypertetrahedron(5, delta)
        delta += 1


def six_dimensional_centered_hypertetrahedron_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield acc_helper_centered_hypertetrahedron(6, delta)
        delta += 1


# specific cases of k_dimensional_centered_hyperoctahedron_numbers(k)


def five_dimensional_centered_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    yield 1
    while True:
        yield helper_ext_int_double_sigma(5, delta)
        delta += 1


def six_dimensional_centered_hyperoctahedron_numbers() -> Iterator[int]:
    delta = 1
    yield 1
    while True:
        yield helper_ext_int_double_sigma(6, delta)
        delta += 1
