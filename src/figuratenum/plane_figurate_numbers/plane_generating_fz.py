import numpy as np


def m_gonal(z: np.ndarray, m: int = 3) -> np.ndarray:
    return z * ((m - 3)*z + 1) / (1 - z)**3


def centered_m_gonal(z: np.ndarray, m: int = 3) -> np.ndarray:
    return z * ((1 + (m - 2) * z + z**2)) / (1 - z)**3
