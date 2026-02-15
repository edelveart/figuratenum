from typing import Literal
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m


SpaceTypes = Literal[

    # Pyramidal
    "m_pyramidal",
    "tetrahedral",
    "cubic",
    "octahedral",
    "hauy_octahedral",
    "icosahedral",
    "dodecahedral",

    # Archimedean
    "truncated_tetrahedral",
    "truncated_cubic",
    "truncated_octahedral",

    # Star Polyhedral
    "stella_octangula",

    # Centered
    "centered_cube",
    "rhombic_dodecahedral",
    "hauy_rhombic_dodecahedral",
    "centered_tetrahedron",
    "centered_square_pyramid",
    "centered_pentagonal_pyramid",
    "centered_hexagonal_pyramid",
    "centered_mgonal_pyramid",
    "centered_octahedron",
    "centered_icosahedron",
    "centered_dodecahedron",

    # Centered Truncated
    "centered_truncated_tetrahedron",
    "centered_truncated_cube",
    "centered_truncated_octahedron",

    # Centered Pyramidal / Prism
    "centered_mgonal_pyramidal",
    "mgonal_prism",

    # Generalized
    "generalized_mgonal_pyramidal",
    "generalized_cubic",
    "generalized_octahedral",
    "generalized_icosahedral",
    "generalized_dodecahedral",
    "generalized_centered_cube",
    "generalized_centered_tetrahedron",
    "generalized_centered_square_pyramid",
    "generalized_rhombic_dodecahedral",
    "generalized_centered_mgonal_pyramidal",
    "generalized_hexagonal_prism",]


class SpaceSchema:
    def __init__(
        self,
        name: SpaceTypes,
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
            self._lambdified = sp.lambdify((x, m), self.expression, "numpy")
        return self._lambdified

    def evaluate_numeric(self, z: np.ndarray, m_sides: int):
        """Evaluates the generating function f(z) numerically"""
        return self.lambdify()(x=z, m=m_sides)

    def analytic_algebraic_properties(self):
        """Returns summarized metadata."""
        return {
            "name": self.name,
            "generating_function": self.expression,
            "galois_group": self.galois_group,
            "group_description": self.galois_description,
        }
