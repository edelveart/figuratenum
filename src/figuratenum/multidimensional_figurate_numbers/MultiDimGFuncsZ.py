import numpy as np
from .multidim_ogf_z import (
    centered_biquadratic, centered_hyperoctahedron,    centered_hypertetrahedron,
    four_dim_mgonal_pyramidal,    generalized_biquadratic,
    generalized_k_dim_hypercube,    generalized_k_dim_hyperoctahedron,     generalized_k_dim_hypertetrahedron,
    generalized_pentatope,     hypercube,    hyperdodecahedral,    hypericosahedral,
    hyperoctahedral,    hypertetrahedral,    k_dim_centered_hypercube,    k_dim_centered_hyperoctahedron,
    k_dim_centered_hypertetrahedron,    k_dim_hypercube,    k_dim_hyperoctahedron,    k_dim_hypertetrahedron,
    k_dim_mgonal_pyramidal,    k_dim_nexus,    polyoctahedral
)


class MultiDimGFuncsZ:
    def __init__(self, k: int,  m: int):
        self.k = k
        self.m = m

    def hypertetrahedral(self, z: np.ndarray) -> np.ndarray:
        return hypertetrahedral(z)

    def hypercube(self, z: np.ndarray) -> np.ndarray:
        return hypercube(z)

    def hyperoctahedral(self, z: np.ndarray) -> np.ndarray:
        return hyperoctahedral(z)

    def hypericosahedral(self, z: np.ndarray) -> np.ndarray:
        return hypericosahedral(z)

    def hyperdodecahedral(self, z: np.ndarray) -> np.ndarray:
        return hyperdodecahedral(z)

    def polyoctahedral(self, z: np.ndarray) -> np.ndarray:
        return polyoctahedral(z)

    # K-Dimensional

    def k_dim_hypertetrahedron(self, z: np.ndarray) -> np.ndarray:
        return k_dim_hypertetrahedron(z, self.k)

    def k_dim_hypercube(self, z: np.ndarray) -> np.ndarray:
        return k_dim_hypercube(z, self.k)

    def k_dim_hyperoctahedron(self, z: np.ndarray) -> np.ndarray:
        return k_dim_hyperoctahedron(z, self.k)

    def k_dim_nexus(self, z: np.ndarray) -> np.ndarray:
        return k_dim_nexus(z, self.k)

    # 4D - Pyramidal

    def four_dim_mgonal_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return four_dim_mgonal_pyramidal(z, self.m)

    # K-Dimensional Pyramidal

    def k_dim_mgonal_pyramidal(self, z: np.ndarray) -> np.ndarray:
        return k_dim_mgonal_pyramidal(z, self.k, self.m)

    # 4D Centered

    def centered_biquadratic(self, z: np.ndarray) -> np.ndarray:
        return centered_biquadratic(z)

    def centered_hypertetrahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_hypertetrahedron(z)

    def centered_hyperoctahedron(self, z: np.ndarray) -> np.ndarray:
        return centered_hyperoctahedron(z)

    # K-Dimensional Centered

    def k_dim_centered_hypercube(self, z: np.ndarray) -> np.ndarray:
        return k_dim_centered_hypercube(z, self.k)

    def k_dim_centered_hypertetrahedron(self, z: np.ndarray) -> np.ndarray:
        return k_dim_centered_hypertetrahedron(z, self.k)

    def k_dim_centered_hyperoctahedron(self, z: np.ndarray) -> np.ndarray:
        return k_dim_centered_hyperoctahedron(z, self.k)

    # Generalized MultiDimensional FigurateNum, n = 0, +/-1, +/-2, ...

    def generalized_pentatope(self, z: np.ndarray) -> np.ndarray:
        return generalized_pentatope(z)

    def generalized_k_dim_hypertetrahedron(self, z: np.ndarray) -> np.ndarray:
        return generalized_k_dim_hypertetrahedron(z, self.k)

    def generalized_biquadratic(self, z: np.ndarray) -> np.ndarray:
        return generalized_biquadratic(z)

    def generalized_k_dim_hypercube(self, z: np.ndarray) -> np.ndarray:
        return generalized_k_dim_hypercube(z, self.k)

    def generalized_k_dim_hyperoctahedron(self, z: np.ndarray) -> np.ndarray:
        return generalized_k_dim_hyperoctahedron(z, self.k)
