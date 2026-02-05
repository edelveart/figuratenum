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
def centered_tetrahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + z + z**2 + z**3) / (1 - z)**4


def centered_square_pyramid(z: np.ndarray) -> np.ndarray:
    return z * (1 + 2*z + 2*z**2 + z**3) / (1 - z)**4


def centered_pentagonal_pyramid(z: np.ndarray) -> np.ndarray:
    return z * (1 + 3*z + 3*z**2 + z**3) / (1 - z)**4


def centered_hexagonal_pyramid(z: np.ndarray) -> np.ndarray:
    return z * (1 + 4*z + 4*z**2 + z**3) / (1 - z)**4


def centered__mgonal_pyramid(z: np.ndarray, m: int) -> np.ndarray:
    return z * (1 + (m - 2)*z + (m - 2)*z**2 + z**3) / (1 - z)**4


# Centered
def centered_octahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + 3*z + 3*z**2 + z**3) / (1 - z)**4


def centered_icosahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + 9*z + 9*z**2 + z**3) / (1 - z)**4


def centered_dodecahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + 17*z + 17*z**2 + z**3) / (1 - z)**4


# Centered Truncated
def centered_truncated_tetrahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + z) * (1 + 12*z + z**2) / (1 - z)**4


def centered_truncated_cube(z: np.ndarray) -> np.ndarray:
    return z * (1 + z) * (1 + 44*z + z**2) / (1 - z)**4


def centered_truncated_octahedron(z: np.ndarray) -> np.ndarray:
    return z * (1 + z) * (1 + 28*z + z**2) / (1 - z)**4


# Centered Pyramidal
def centered_mgonal_pyramidal(z: np.ndarray, m: int) -> np.ndarray:
    return z * (1 + (m - 2)*z + z**2) / (1 - z)**4


def m_prism(z: np.ndarray, m: int) -> np.ndarray:
    return z * (1 + (2*m - 2)*z + (m + 1)*z**2) / (1 - z)**4
