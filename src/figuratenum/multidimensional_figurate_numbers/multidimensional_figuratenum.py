from collections.abc import Generator

from ..utils import (
    factorial, binomial_coefficient,
    helper_centered_hypertetrahedron, pseudo_rising_factorial,
    pseudo_pochhammer_function, rising_factorial,
    helper_ext_int_double_sigma
)


def _quartic_generator(a: int, b: int, c: int, d: int, e: int) -> Generator[int]:
    while True:
        yield a
        a += b
        b += c
        c += d
        d += e


def pentatope() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * (delta + 3)) // 24
        delta += 1


def k_dimensional_hypertetrahedron_from_book(k: int) -> Generator[int]:
    """Book definition. For reference only."""
    delta = 1
    while True:
        yield rising_factorial(delta, k) // factorial(k)
        delta += 1


def k_dimensional_hypertetrahedron_from_book_2(k: int) -> Generator[int]:
    """Book definition alternative. For reference only"""
    delta = 1
    while True:
        yield binomial_coefficient(delta + k - 1, k)
        delta += 1


def k_dimensional_hypertetrahedron(k: int) -> Generator[int]:
    """Optimized version using iterative binomial coefficient update for better performance."""
    delta = 1
    bin_coeff = 1
    while True:
        yield bin_coeff
        bin_coeff = bin_coeff * (delta + k) // delta
        delta += 1


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


def hyperoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta ** 2 * (delta ** 2 + 2)) // 3
        delta += 1


def hypericosahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (145 * delta ** 3 - 280 * delta ** 2 + 179 * delta - 38)) // 6
        delta += 1


def hyperdodecahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (261 * delta ** 3 - 504 * delta ** 2 + 283 * delta - 38)) // 2
        delta += 1


def polyoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield delta ** 2 * (3 * delta ** 2 - 4 * delta + 2)
        delta += 1


def k_dimensional_hyperoctahedron_from_book(k: int) -> Generator[int]:
    """Book definition. For reference only."""
    delta = 1
    while True:
        a = 0
        for i in range(0, (k - 1) + 1):
            a += (binomial_coefficient(k - 1, i) *
                  (rising_factorial(delta - i, k) // factorial(k)))
        yield a
        delta += 1


def k_dimensional_hyperoctahedron_from_book_2(k: int) -> Generator[int]:
    """Optimized version from Book with precomputed coefficients."""
    bin_coeffs = [binomial_coefficient(k - 1, i) for i in range(k)]
    delta = 1
    while True:
        a = 0
        for i in range(k):
            a += bin_coeffs[i] * binomial_coefficient(delta - i + k - 1, k)
        yield a
        delta += 1


def k_dimensional_hyperoctahedron(k: int) -> Generator[int]:
    """
    Wrapper over the generalized hyperoctahedron
    version with fixed start_num = 1.
    """
    return generalized_k_dimensional_hyperoctahedron(k, 1)


def four_dimensional_mgonal_pyramidal(m: int) -> Generator[int]:
    delta = 1
    while True:
        yield (delta * (delta + 1) * (delta + 2) * ((m - 2) * delta - m + 6)) // 24
        delta += 1


def k_dimensional_mgonal_pyramidal_from_book(k: int, m: int) -> Generator[int]:
    """Book definition. For reference only."""
    delta = 1
    while True:
        yield (pseudo_rising_factorial(delta, k) * ((m - 2) * delta - m + k + 2)) // factorial(k)
        delta += 1


def k_dimensional_mgonal_pyramidal(k: int, m: int):
    """Optimized version using iterative binomial coefficient update for better performance."""
    delta = 1
    bin_coeff = 1
    while True:
        yield (bin_coeff * ((m - 2) * delta - m + k + 2)) // k
        bin_coeff = bin_coeff * (delta + k - 1) // delta
        delta += 1


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
    bin_coeffs_k = [binomial_coefficient(k + 1, k - i) for i in range(k)]
    a = 0
    delta = 1
    while True:
        a += helper_centered_hypertetrahedron(k, delta, bin_coeffs_k)
        yield a
        delta += 1


def centered_hyperoctahedral() -> Generator[int]:
    delta = 1
    while True:
        yield (2 * delta ** 4 - 4 * delta ** 3 + 10 * delta ** 2 - 8 * delta + 3) // 3
        delta += 1


def nexus(k: int) -> Generator[int]:
    delta = 0
    while True:
        yield (delta + 1) ** (k + 1) - delta ** (k + 1)
        delta += 1


def k_dimensional_centered_hyperoctahedron(k: int) -> Generator[int]:
    bin_coeffs_k = [binomial_coefficient(k, 1 + i) for i in range(k)]
    powers_of_2 = [2 ** (1 + i) for i in range(k)]
    delta = 1
    yield 1
    while True:
        yield helper_ext_int_double_sigma(k, delta, bin_coeffs_k, powers_of_2)
        delta += 1


def generalized_pentatope(start_num: int = 0) -> Generator[int]:
    delta = start_num
    while True:
        yield delta * (delta + 1) * (delta + 2) * (delta + 3) // 24
        delta += 1


def generalized_k_dimensional_hypertetrahedron_from_book(k: int, start_num: int = 0) -> Generator[int]:
    """Book alternative definition. For reference only"""
    den = factorial(k)
    delta = start_num
    while True:
        yield rising_factorial(delta, k) // den
        delta += 1


def generalized_k_dimensional_hypertetrahedron(k: int, start_num: int = 0) -> Generator[int]:
    """
    Incrementally optimized version using rising factorial for better performance.
    """
    den = factorial(k)
    delta = start_num
    rfact = rising_factorial(delta, k)
    while True:
        yield rfact // den
        delta += 1
        if delta - 1 != 0:
            rfact = rfact * (delta + k - 1) // (delta - 1)
        else:
            rfact = rising_factorial(delta, k)


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
    """Incrementally optimized generalized hyperoctahedron generator."""
    den = factorial(k)
    bin_coeffs = [binomial_coefficient(k - 1, i) for i in range(k)]
    delta = start_num
    risings = [rising_factorial(delta - i, k) for i in range(k)]
    while True:
        yield sum(bin_coeffs[i] * risings[i] // den for i in range(k))
        delta += 1
        for i in range(k):
            d_m_i_m_1 = delta - i - 1
            if d_m_i_m_1 != 0:
                risings[i] = risings[i] * (d_m_i_m_1 + k) // d_m_i_m_1
            else:
                risings[i] = rising_factorial(delta - i, k)


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
    den = factorial(k)
    delta = start_num
    while True:
        yield (pseudo_pochhammer_function(delta, k) * ((m - 2) * delta - m + k + 2)) // den
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
