import numpy as np


def m_gonal(z: np.ndarray, m: int = 3) -> np.ndarray:
    return z * ((m - 3)*z + 1) / (1 - z)**3


def centered_m_gonal(z: np.ndarray, m: int = 3) -> np.ndarray:
    return z * ((1 + (m - 2)*z + z**2)) / (1 - z)**3


def pronic(z: np.ndarray) -> np.ndarray:
    return 2 * z / (1 - z)**3


def gnomonic(z: np.ndarray) -> np.ndarray:
    return z * (1 + z) / (1 - z)**2


def truncated_triangular(z: np.ndarray) -> np.ndarray:
    return z * (1 + z**2 + 4*z) / (1 - z)**3


def truncated_square(z: np.ndarray) -> np.ndarray:
    return z * (1 + 9*z + 4*z**2) / (1 - z)**3


def truncated_pronic(z: np.ndarray) -> np.ndarray:
    return z * (2 + 10*z + 2*z**2) / (1 - z)**3


def truncated_centered_m_gonal(z: np.ndarray, m: int = 5) -> np.ndarray:
    return z * (1 + (5*m - 2)*z + (1 + 2*m)*z**2) / (1 - z)**3


def truncated_centered_triangular(z: np.ndarray) -> np.ndarray:
    return z * (1 + 13*z + 7*z**2) / (1 - z)**3


def truncated_centered_square(z: np.ndarray) -> np.ndarray:
    return z * (1 + 18*z + 9*z**2) / (1 - z)**3


def truncated_centered_pentagonal(z: np.ndarray) -> np.ndarray:
    return z * (1 + 23*z + 11*z**2) / (1 - z)**3


def polygram(z: np.ndarray, m: int = 5) -> np.ndarray:
    return z * (1 + (2*m - 2)*z + z**2) / (1 - z)**3


def aztec_diamond(z: np.ndarray) -> np.ndarray:
    return 4 * z / (1 - z)**3


def cross(z: np.ndarray,) -> np.ndarray:
    return z * (1 + 3*z) / (1 - z)**2


def diamond(z: np.ndarray) -> np.ndarray:
    return z * (1 + 2*z + z**2) / (1 - z)**3


def square_triangular(z: np.ndarray) -> np.ndarray:
    return z * (1 + z) / ((1 - z)*(1 - 34*z + z**2))
