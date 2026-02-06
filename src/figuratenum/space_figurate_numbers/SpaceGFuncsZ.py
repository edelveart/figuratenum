import numpy as np
from .space_ogf_z import (
    centered__mgonal_pyramid, centered_cube, centered_dodecahedron, centered_hexagonal_pyramid, centered_icosahedron, centered_mgonal_pyramidal, centered_octahedron, centered_pentagonal_pyramid, centered_square_pyramid, centered_tetrahedron, centered_truncated_cube, centered_truncated_octahedron, centered_truncated_tetrahedron, dodecahedral, generalized_centered_cube, generalized_centered_mgonal_pyramidal, generalized_centered_square_pyramid, generalized_centered_tetrahedron, generalized_cubic, generalized_dodecahedral, generalized_hexagonal_prism, generalized_icosahedral, generalized_mgonal_pyramidal, generalized_octahedral, generalized_rhombic_dodecahedral, hauy_octahedral, hauy_rhombic_dodecahedral, icosahedral, m_prism, m_pyramidal, octahedral, rhombic_dodecahedral, stella_octangula, tetrahedral, cubic, truncated_cubic, truncated_octahedral, truncated_tetrahedral
)


class SpaceGFuncsZ:
    def __init__(self, m: int):
        self.m = m

    def m_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return m_pyramidal(z, self.m)

    def tetrahedral(self, z: np.ndarray) -> np.ndarray:
        return tetrahedral(z)

    def cubic(self, z: np.ndarray) -> np.ndarray:
        return cubic(z)

    def octahedral(self, z: np.ndarray) -> np.ndarray:
        return octahedral(z)

    def hauy_octahedral(self, z: np.ndarray) -> np.ndarray:
        return hauy_octahedral(z)

    def icosahedral(self, z: np.ndarray) -> np.ndarray:
        return icosahedral(z)

    def dodecahedral(self, z: np.ndarray) -> np.ndarray:
        return dodecahedral(z)

    # Archimedean Solids

    def truncated_tetrahedral(self, z: np.ndarray) -> np.ndarray:
        return truncated_tetrahedral(z)

    def truncated_cubic(self, z: np.ndarray) -> np.ndarray:
        return truncated_cubic(z)

    def truncated_octahedral(self, z: np.ndarray) -> np.ndarray:
        return truncated_octahedral(z)

    # Star Polyhedral

    def stella_octangula(self, z: np.ndarray) -> np.ndarray:
        return stella_octangula(z)

    # Centered

    def centered_cube(self, z: np.ndarray) -> np.ndarray:
        return centered_cube(z)

    def rhombic_dodecahedral(self, z: np.ndarray) -> np.ndarray:
        return rhombic_dodecahedral(z)

    def hauy_rhombic_dodecahedral(self, z: np.ndarray) -> np.ndarray:
        return hauy_rhombic_dodecahedral(z)

    # Centered pyramid

    def centered_tetrahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_tetrahedron(z)

    def centered_square_pyramid(self, z: np.ndarray) -> np.ndarray:
        return centered_square_pyramid(z)

    def centered_pentagonal_pyramid(self, z: np.ndarray) -> np.ndarray:
        return centered_pentagonal_pyramid(z)

    def centered_hexagonal_pyramid(self, z: np.ndarray) -> np.ndarray:
        return centered_hexagonal_pyramid(z)

    def centered__mgonal_pyramid(self, z: np.ndarray) -> np.ndarray:
        return centered__mgonal_pyramid(z, self.m)

    # Centered

    def centered_octahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_octahedron(z)

    def centered_icosahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_icosahedron(z)

    def centered_dodecahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_dodecahedron(z)

    # Centered Truncated

    def centered_truncated_tetrahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_truncated_tetrahedron(z)

    def centered_truncated_cube(self, z: np.ndarray) -> np.ndarray:
        return centered_truncated_cube(z)

    def centered_truncated_octahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_truncated_octahedron(z)

    # Centered Pyramidal

    def centered_mgonal_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return centered_mgonal_pyramidal(z, self.m)

    def m_prism(self, z: np.ndarray) -> np.ndarray:
        return m_prism(z, self.m)

    # Generalized Space FigurateNum, n = 0, +/-1, +/-2, ...

    def generalized_mgonal_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return generalized_mgonal_pyramidal(z, self.m)

    def generalized_cubic(self, z: np.ndarray) -> np.ndarray:
        return generalized_cubic(z)

    def generalized_octahedral(self, z: np.ndarray) -> np.ndarray:
        return generalized_octahedral(z)

    def generalized_icosahedral(self, z: np.ndarray) -> np.ndarray:
        return generalized_icosahedral(z)

    def generalized_dodecahedral(self, z:  np.ndarray) -> np.ndarray:
        return generalized_dodecahedral(z)

    # Generalized Centered

    def generalized_centered_cube(self, z: np.ndarray) -> np.ndarray:
        return generalized_centered_cube(z)

    def generalized_centered_tetrahedron(self, z: np.ndarray) -> np.ndarray:
        return generalized_centered_tetrahedron(z)

    def generalized_centered_square_pyramid(self, z: np.ndarray) -> np.ndarray:
        return generalized_centered_square_pyramid(z)

    def generalized_rhombic_dodecahedral(self, z: np.ndarray) -> np.ndarray:
        return generalized_rhombic_dodecahedral(z)

    def generalized_centered_mgonal_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return generalized_centered_mgonal_pyramidal(z, self.m)

    def generalized_hexagonal_prism(self, z: np.ndarray) -> np.ndarray:
        return generalized_hexagonal_prism(z)
