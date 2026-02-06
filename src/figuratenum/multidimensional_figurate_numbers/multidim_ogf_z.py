from math import comb
import math
import numpy as np

# 4D


def hypertetrahedral(z: np.ndarray) -> np.ndarray:
    return z / (1 - z)**5


def hypercube(z: np.ndarray) -> np.ndarray:
    return z * (1 + 11*z + 11*z**2 + z**3) / (1 - z)**5


def hyperoctahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + z)**3 / (1 - z)**5


def hypericosahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 115*z + 357*z**2 + 107*z**3) / (1 - z)**5


def hyperdodecahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 595*z + 1993*z**2 + 543*z**3) / (1 - z)**5


def polyoctahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 19*z + 43*z**2 + 9*z**3) / (1 - z)**5


# K-Dimensional

def helper_a_i_k(i, k):
    return sum(
        (-1)**j * comb(k + 1, j) * (i + 1 - j)**k
        for j in range(i + 1)
    )


def helper_coeffs(k):
    coeffs = [0] * k
    coeffs[0] = 1
    coeffs[k - 1] = 1

    p = math.floor((k - 1) / 2)
    for i in range(1, p + 1):
        a = helper_a_i_k(i, k)
        coeffs[i] = a
        coeffs[k - 1 - i] = a
    return coeffs


def k_dim_hypertetrahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z / (1 - z)**(k + 1)


def k_dim_hypercube(z: np.ndarray, k: int) -> np.ndarray:
    k_coeffs = helper_coeffs(k)
    return z * sum(f_n * z**n for n, f_n in enumerate(k_coeffs)) / (1 - z)**(k + 1)


def k_dim_hyperoctahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z * (1 + z)**(k - 1) / (1 - z)**(k + 1)


def k_dim_nexus(z: np.ndarray, k: int) -> np.ndarray:
    k_coeffs = helper_coeffs(k + 1)
    return z * sum(f_n * z**n for n, f_n in enumerate(k_coeffs)) / (1 - z)**(k + 1)


# 4D - Pyramidal
def four_dim_mgonal_pyramidal(z: np.ndarray, m: int) -> np.ndarray:
    return z * (1 + (m - 3)*z) / (1 - z)**5


# K-Dimensional Pyramidal
def k_dim_mgonal_pyramidal(z: np.ndarray, k: int, m: int) -> np.ndarray:
    return z * (1 + (m - 3)*z) / (1 - z)**(k + 1)


# 4D Centered
def centered_biquadratic(z: np.ndarray) -> np.ndarray:
    return (1 + z)**2 * (1 + 10*z + z**2) / (1 - z)**5


def centered_hypertetrahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 - z**5) / (1 - z)**6


def centered_hyperoctahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + z)**4 / (1 - z)**5


# K-Dimensional Centered
def k_dim_centered_hypercube(z: np.ndarray, k: int) -> np.ndarray:
    k_coeffs = helper_coeffs(k)
    return z * (1 + z) * sum(f_n * z**n for n, f_n in enumerate(k_coeffs)) / (1 - z)**(k + 1)


def k_dim_centered_hypertetrahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z * (1 - z**(k + 1)) / (1 - z)**(k + 2)


def k_dim_centered_hyperoctahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z * (1 + z)**k / (1 - z)**(k + 1)


# Generalized MultiDimensional FigurateNum, n = 0, +/-1, +/-2, ...
def generalized_pentatope(z: np.ndarray) -> np.ndarray:
    return z**2 * (1 + z**5) / (1 - z**2)**5


def generalized_k_dim_hypertetrahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z**2 * (1 + (-1)**k * z**(2*k - 3)) / (1 - z**2)**(k + 1)


def generalized_biquadratic(z: np.ndarray) -> np.ndarray:
    return z**2 * (1 + z) * (1 + 11*z**2 + 11*z**4 + z**6) / (1 - z**2)**5


def generalized_k_dim_hypercube(z: np.ndarray, k: int) -> np.ndarray:
    coeffs = helper_coeffs(k)
    k_dim = z**2 * (1 + (-1)**k * z)
    return k_dim * sum(f_n * (z**(n*2)) for n, f_n in enumerate(coeffs)) / (1-z**2)**(k+1)


def generalized_k_dim_hyperoctahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z**2 * (1 + z**2)**(k - 1) * (1 + (-1)**k * z) / (1 - z**2)**(k + 1)
