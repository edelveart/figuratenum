import numpy as np


def hypertetrahedral(z: np.ndarray) -> np.ndarray:
    return z / (1 - z)**5


def hypercube(z: np.ndarray) -> np.ndarray:
    return z * (1 + 11*z + 11*z**2 + z**3) / (1 - z)**5


def hyperoctahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + z)**3 / (1 - z)**5


def hypericosahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 115*z + 357*z**2 + 107*z**3) / (1 - z)**5
