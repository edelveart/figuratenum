from typing import Iterator


def factorial_iter(num: int) -> int:
    t = 1
    for i in range(1, num):
        t *= i
    return t


def binomial_coefficient(n: int, k: int) -> int:
    return factorial_iter(n) // (factorial_iter(k) * factorial_iter(n - k))


def pentatope_numbers() -> Iterator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3)) // 24
        delta += 1


def hypertetrahedral_numbers() -> Iterator[int]:
    return pentatope_numbers()


def triangulotriangular_numbers() -> Iterator[int]:
    return pentatope_numbers()


def rising_factorial(n: int, k: int) -> int:
    t = 1
    for i in range(n, n + k - 1):
        t *= i
    return t


def k_dimensional_hypertetrahedron_numbers(k: int) -> Iterator[int]:
    delta = 1
    while True:
        yield rising_factorial(delta, k) // factorial_iter(k)
        delta += 1


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
