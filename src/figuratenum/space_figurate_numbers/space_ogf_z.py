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
