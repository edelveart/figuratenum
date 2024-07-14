from typing import Iterator
from multidimensional_figuratenum import (
    rising_factorial,
    factorial_iter
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
