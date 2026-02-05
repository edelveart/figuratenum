import numpy as np
from .plane_ogf_z import (
    aztec_diamond, cross, diamond, generalized_centered_m_gonal, generalized_m_gonal, generalized_pronic, polygram, square_triangular, triangular, square, pentagonal, hexagonal,
    m_gonal, pronic, gnomonic, truncated_centered_hexagonal, truncated_centered_pentagonal, truncated_centered_square, truncated_centered_triangular,  truncated_triangular, truncated_square, truncated_pronic, centered_m_gonal, truncated_centered_m_gonal)


class PlaneGFuncsZ:
    def __init__(self, m: int):
        self.m = m

    def polygonal(self, z: np.ndarray) -> np.ndarray:
        return m_gonal(z, self.m)

    def triangular(self, z: np.ndarray) -> np.ndarray:
        return triangular(z)

    def square(self, z: np.ndarray) -> np.ndarray:
        return square(z)

    def pentagonal(self, z: np.ndarray) -> np.ndarray:
        return pentagonal(z)

    def hexagonal(self, z: np.ndarray) -> np.ndarray:
        return hexagonal(z)

    def centered_m_gonal(self, z: np.ndarray) -> np.ndarray:
        return centered_m_gonal(z, self.m)

    def pronic(self, z: np.ndarray) -> np.ndarray:
        return pronic(z)

    def gnomonic(self, z: np.ndarray) -> np.ndarray:
        return gnomonic(z)

    def truncated_triangular(self, z: np.ndarray) -> np.ndarray:
        return truncated_triangular(z)

    def truncated_square(self, z: np.ndarray) -> np.ndarray:
        return truncated_square(z)

    def truncated_pronic(self, z: np.ndarray) -> np.ndarray:
        return truncated_pronic(z)

    def truncated_centered_m_gonal(self, z: np.ndarray) -> np.ndarray:
        return truncated_centered_m_gonal(z, self.m)

    def truncated_centered_triangular(self, z: np.ndarray) -> np.ndarray:
        return truncated_centered_triangular(z)

    def truncated_centered_square(self, z: np.ndarray) -> np.ndarray:
        return truncated_centered_square(z)

    def truncated_centered_pentagonal(self, z: np.ndarray) -> np.ndarray:
        return truncated_centered_pentagonal(z)

    def truncated_centered_hexagonal(self, z: np.ndarray) -> np.ndarray:
        return truncated_centered_hexagonal(z)

    def polygram(self, z: np.ndarray) -> np.ndarray:
        return polygram(z, self.m)

    def aztec_diamond(self, z: np.ndarray) -> np.ndarray:
        return aztec_diamond(z)

    def cross(self, z: np.ndarray) -> np.ndarray:
        return cross(z)

    def diamond(self, z: np.ndarray) -> np.ndarray:
        return diamond(z)

    def square_triangular(self, z: np.ndarray) -> np.ndarray:
        return square_triangular(z)

    # Generalized Plane FigurateNum, n = 0, +/-1, +/-2, ...

    def generalized_m_gonal(self, z: np.ndarray) -> np.ndarray:
        return generalized_m_gonal(z, self.m)

    def generalized_centered_m_gonal(self, z: np.ndarray) -> np.ndarray:
        return generalized_centered_m_gonal(z, self.m)

    def generalized_pronic(self, z: np.ndarray) -> np.ndarray:
        return generalized_pronic(z)
