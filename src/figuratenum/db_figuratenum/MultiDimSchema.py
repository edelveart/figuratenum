from typing import Literal, TypeAlias
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m, k


MultiDimTypes: TypeAlias = Literal[
    # 4D
    "hypertetrahedral",
    "hypercube",
    "hyperoctahedral",
    "hypericosahedral",
    "hyperdodecahedral",
    "polyoctahedral",

    # K-Dimensional
    "k_dim_hypertetrahedron",
    "k_dim_hypercube",
    "k_dim_hyperoctahedron",
    "k_dim_nexus",

    # 4D Pyramidal
    "four_dim_mgonal_pyramidal",

    # K-Dimensional Pyramidal
    "k_dim_mgonal_pyramidal",

    # 4D Centered
    "centered_biquadratic",
    "centered_hypertetrahedron",
    "centered_hyperoctahedron",

    # K-Dimensional Centered
    "k_dim_centered_hypercube",
    "k_dim_centered_hypertetrahedron",
    "k_dim_centered_hyperoctahedron",

    # Generalized
    "generalized_pentatope",
    "generalized_k_dim_hypertetrahedron",
    "generalized_biquadratic",
    "generalized_k_dim_hypercube",
    "generalized_k_dim_hyperoctahedron",
]


class MultiDimSchema:
    def __init__(
        self,
        name: MultiDimTypes,
        generating_function: sp.Expr,
        galois_group: str | None = None,
        galois_description: str | None = None,
    ):
        self.name = name
        self.expression = generating_function
        self.galois_group = galois_group
        self.galois_description = galois_description
        self._lambdified_z = None
        self._lambdified_z_m = None
        self._lambdified_z_k = None
        self._lambdified_z_k_m = None

    def substitute_symbolic(self, **kwargs) -> sp.Expr | sp.Basic:
        """Substitute symbols in expression."""
        return self.expression.subs(kwargs)

    def lambdify_z(self):
        """Lambdify for expressions that only depend on z."""
        if self._lambdified_z is None:
            self._lambdified_z = sp.lambdify(x, self.expression, "numpy")
        return self._lambdified_z

    def lambdify_z_m(self):
        """Lambdify for expressions that depend on both z and m."""
        if self._lambdified_z_m is None:
            self._lambdified_z_m = sp.lambdify(
                (x, m), self.expression, "numpy")
        return self._lambdified_z_m

    def lambdify_z_k(self):
        """Lambdify for expressions that depend on z and k."""
        if self._lambdified_z_k is None:
            self._lambdified_z_k = sp.lambdify(
                (x, k), self.expression, "numpy")
        return self._lambdified_z_k

    def lambdify_z_k_m(self):
        """Lambdify for expressions that depend on z, m and k"""
        if self._lambdified_z_k_m is None:
            self._lambdified_z_k_m = sp.lambdify(
                (x, k, m), self.expression, "numpy")
        return self._lambdified_z_k_m

    def evaluate_numeric(self, z: np.ndarray, k_dimension: int | None = None, m_sides: int | None = None):
        """Evaluates the generating function f(z) numerically"""

        needs_m = self.requires_m()
        needs_k = self.requires_k()

        if needs_m and m_sides is None:
            raise ValueError(
                f"Sequence '{self.name}' requires parameter 'm_sides'")
        if needs_k and k_dimension is None:
            raise ValueError(
                f"Sequence '{self.name}' requires parameter 'k_dimension'")

        if needs_m and needs_k:
            return self.lambdify_z_k_m()(x=z, k=k_dimension, m=m_sides)
        elif needs_m:
            return self.lambdify_z_m()(x=z, m=m_sides)
        elif needs_k:
            return self.lambdify_z_k()(x=z, k=k_dimension)
        else:
            return self.lambdify_z()(x=z)

    def analytic_algebraic_properties(self):
        """Returns summarized metadata."""
        return {
            "name": self.name,
            "generating_function": self.expression,
            "galois_group": self.galois_group,
            "group_description": self.galois_description,
        }

    def requires_m(self) -> bool:
        """Returns True if the sequence requires m (i.e., if m is a free symbol in the generating function)."""
        return m in self.expression.free_symbols

    def requires_k(self) -> bool:
        """Returns True if the sequence requires k (i.e., if k is a free symbol in the generating function)."""
        return k in self.expression.free_symbols
