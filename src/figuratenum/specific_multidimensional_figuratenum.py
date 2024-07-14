from typing import Iterator
from multidimensional_figuratenum import (
    rising_factorial,
    factorial_iter
)

# k_dimensional_hypertetrahedron_numbers(k)


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
