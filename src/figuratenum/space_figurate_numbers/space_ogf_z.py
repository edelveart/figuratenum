import numpy as np


def m_pyramidal(z: np.ndarray, m: int) -> np.ndarray:
    return z * (1 + (m - 3)*z) / (1 - z)**4


def tetrahedral(z: np.ndarray) -> np.ndarray:
    return z / (1 - z)**4


def cubic(z: np.ndarray) -> np.ndarray:
    return z * (1 + 4*z + z**2) / (1 - z)**4


def octahedral(z: np.ndarray) -> np.ndarray:
    return z * (z + 1)**2 / (1 - z)**4


def hauy_octahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + z)**3 / (1 - z)**4


def icosahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 8*z + 6*z**2) / (1 - z)**4


def dodecahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 16*z + 10*z**2) / (1 - z)**4


# Archimedean
def truncated_tetrahedral(z:  np.ndarray) -> np.ndarray:
    return z * (1 + 12*z + 10*z**2) / (1 - z)**4


def truncated_cubic(z: np.ndarray) -> np.ndarray:
    return z * (1 + 52*z + 93*z**2 + 8*z**3) / (1 - z)**4


def truncated_octahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 34*z + 55*z**2 + 6*z**3) / (1 - z)**4
