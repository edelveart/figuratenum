from typing import Literal
import numpy as np
import sympy as sp
from ..db_figuratenum.symbols_figuratenum import z
from ..db_figuratenum.SpaceSchema import SpaceTypes, x
from ..db_figuratenum.space_db import SPACE_DATABASE


class SpaceCViz:
    def __init__(self, m: int):
        self.m = m

    def evaluate_plot(self, name_seq: SpaceTypes, z_values: np.ndarray) -> np.ndarray:
        """Evaluate at numeric points (for plotting)."""
        schema = SPACE_DATABASE[name_seq]
        return schema.evaluate_numeric(z_values, self.m)

    def expand_series(self, name_seq: SpaceTypes, n_terms: int = 6,
                      coeffs: bool = False,
                      method: Literal["auto", "symbolic", "numeric"] = "auto"):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : SpaceTypes
            Sequence name
        n_terms : int, default=6
            Number of terms to compute
        coeffs : bool, default=False
            If True, return only coefficients as integers
        method : {'auto', 'symbolic', 'numeric'}
            - 'symbolic': Pure symbolic (exact, slower for large m)
            - 'numeric': Numeric substitution (fast, may need rounding)
            - 'auto': Choose based on m value (default)

        Returns
        -------
        list or sp.Series
            Integer coefficients if coeffs=True, else Series object
        """
        schema = SPACE_DATABASE[name_seq]

        if method == 'auto':
            method = 'numeric' if self.m > 10 else 'symbolic'

        if method == 'symbolic':
            expr = schema.substitute_symbolic(m=self.m)
            series_expansion = sp.series(expr, x, 0, n=n_terms)
            var_expand = x
        else:
            expr = schema.evaluate_numeric(z, m_sides=self.m)
            series_expansion = sp.series(expr, z, 0, n=n_terms)
            var_expand = z

        if coeffs:
            return [self._safe_int(series_expansion.coeff(var_expand, i))
                    for i in range(1, n_terms)]
        return series_expansion

    @staticmethod
    def _safe_int(coeff):
        """Convert coefficient to integer safely."""
        try:
            return int(coeff)
        except (TypeError, ValueError):
            return int(round(float(coeff)))
