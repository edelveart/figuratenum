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
def k_dim_hypertetrahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z / (1 - z)**(k + 1)


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


def k_dim_hypercube(z: np.ndarray, k: int) -> np.ndarray:
    k_coeffs = helper_coeffs(k)
    return z * sum(f_n * z**n for n, f_n in enumerate(k_coeffs)) / (1 - z)**(k + 1)


def k_dim_hyperoctahedron(z: np.ndarray, k: int) -> np.ndarray:
    return z * (1 + z)**(k - 1) / (1 - z)**(k + 1)
