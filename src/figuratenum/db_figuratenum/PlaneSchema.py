from typing import Literal
import sympy as sp
import numpy as np
from .symbols_figuratenum import x, m


PlaneTypes = Literal["m_gonal",
                     "triangular",
                     "square",
                     "pentagonal",
                     "hexagonal",
                     "centered_m_gonal",
                     "pronic",
                     "gnomonic",
                     "truncated_triangular",
                     "truncated_square",
                     "truncated_pronic",
                     "truncated_centered_m_gonal",
                     "truncated_centered_triangular",
                     "truncated_centered_square",
                     "truncated_centered_pentagonal",
                     "truncated_centered_hexagonal",
                     "polygram",
                     "aztec_diamond",
                     "cross",
                     "diamond",
                     "square_triangular",
                     "generalized_m_gonal",
                     "generalized_centered_m_gonal",
                     "generalized_pronic"]


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
        self._lambdified = None

    def lambdify(self):
        """Generates (once) the numerical version"""
        if self._lambdified is None:
            self._lambdified = sp.lambdify((x, m), self.expression, "numpy")
        return self._lambdified

    def evaluate(self, z: np.ndarray, m_sides: int):
        """Evaluates the generating function f(z)"""
        return self.lambdify()(x=z, m=m_sides)

    def analytic_algebraic_properties(self):
        """Returns summarized metadata."""
        return {
            "name": self.name,
            "generating_function": self.expression,
            "galois_group": self.galois_group,
            "group_description": self.galois_description,
        }
