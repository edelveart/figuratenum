from typing import Literal
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m, k


MultiDimTypes = Literal[
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
        self._lambdified = None

    def substitute_symbolic(self, **kwargs) -> sp.Expr | sp.Basic:
        """Substitute symbols in expression."""
        return self.expression.subs(kwargs)

    def lambdify(self):
        """Generates (once) the numerical version"""
        if self._lambdified is None:
            self._lambdified = sp.lambdify((x, k, m), self.expression, "numpy")
        return self._lambdified

    def evaluate_numeric(self, z: np.ndarray, k_dimension: int, m_sides: int):
        """Evaluates the generating function f(z) numerically"""
        return self.lambdify()(x=z, k=k_dimension, m=m_sides)

    def analytic_algebraic_properties(self):
        """Returns summarized metadata."""
        return {
            "name": self.name,
            "generating_function": self.expression,
            "galois_group": self.galois_group,
            "group_description": self.galois_description,
        }
