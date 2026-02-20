from typing import Literal, TypeAlias
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m


PlaneTypes: TypeAlias = Literal[
    "polygonal",
    "triangular",
    "square",
    "pentagonal",
    "hexagonal",
    "centered_mgonal",
    "pronic",
    "gnomonic",
    "truncated_triangular",
    "truncated_square",
    "truncated_pronic",
    "truncated_centered_mgonal",
    "truncated_centered_triangular",
    "truncated_centered_square",
    "truncated_centered_pentagonal",
    "truncated_centered_hexagonal",
    "polygram",
    "aztec_diamond",
    "cross",
    "diamond",
    "square_triangular",
    "generalized_mgonal",
    "generalized_centered_mgonal",
    "generalized_pronic"
]


class PlaneSchema:
    def __init__(
        self,
        name: PlaneTypes,
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
