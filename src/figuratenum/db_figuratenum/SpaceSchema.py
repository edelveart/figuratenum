from typing import Literal, TypeAlias
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m


SpaceTypes: TypeAlias = Literal[

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
    "generalized_hexagonal_prism",
]


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
        self._lambdified_z = None
        self._lambdified_z_m = None

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

    def evaluate_numeric(self, z: np.ndarray, m_sides: int | None = None):
        """
        Evaluates the generating function f(z) numerically.
        Chooses the correct lambdified function based on whether m is required.
        """
        if self.requires_m():
            if m_sides is None:
                raise ValueError(
                    f"Sequence '{self.name}' requires parameter 'm_sides'.")
            return self.lambdify_z_m()(x=z, m=m_sides)
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
