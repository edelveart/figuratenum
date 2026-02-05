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


# Archimedean Solids
def truncated_tetrahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 12*z + 10*z**2) / (1 - z)**4


def truncated_cubic(z: np.ndarray) -> np.ndarray:
    return z * (1 + 52*z + 93*z**2 + 8*z**3) / (1 - z)**4


def truncated_octahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 34*z + 55*z**2 + 6*z**3) / (1 - z)**4


# Star Polyhedral
def stella_octangula(z: np.ndarray) -> np.ndarray:
    return z * (1 + 10*z + z**2) / (1 - z)**4


# Centered
def centered_cube(z: np.ndarray) -> np.ndarray:
    return z * (1 + 5*z + 5*z**2 + z**3) / (1 - z)**4


def rhombic_dodecahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 11*z + 11*z**2 + z**3) / (1 - z)**4


def hauy_rhombic_dodecahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + 29*z + 59*z**2 + 7*z**3) / (1 - z)**4

# Centered pyramid


def centered_tetrahedral(z: np.ndarray) -> np.ndarray:
    return z * (1 + z + z**2 + z**3) / (1 - z)**4
