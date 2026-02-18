
from typing import Literal
import sympy as sp

from ..db_figuratenum.symbols_figuratenum import x, z
from ..db_figuratenum.PlaneSchema import PlaneTypes
from ..db_figuratenum.plane_db import PLANE_DATABASE
from ..db_figuratenum.SpaceSchema import SpaceTypes
from ..db_figuratenum.space_db import SPACE_DATABASE
from ..db_figuratenum.MultiDimSchema import MultiDimTypes
from ..db_figuratenum.multidim_db import MULTIDIM_DATABASE


class PowerSeriesExpansion:
    def __init__(self, m: int, k: int | None = None):
        self.m = m
        self.k = k

    _SEQ_TO_DOIT: set[MultiDimTypes] = {
        "k_dim_hypercube",
        "k_dim_nexus",
        "k_dim_centered_hypercube",
        "generalized_k_dim_hypercube"
    }

    def expand_plane_series(self, name_seq: PlaneTypes, n_terms: int = 6,
                            coeffs: bool = False,
                            method: Literal["auto", "symbolic", "numeric"] = "auto"):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : PlaneTypes
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
        schema = PLANE_DATABASE[name_seq]

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

    def expand_space_series(self, name_seq: SpaceTypes, n_terms: int = 6,
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

    def expand_multidim_series(self, name_seq: MultiDimTypes, n_terms: int = 6,
                               coeffs: bool = False,
                               method: Literal["auto", "symbolic", "numeric"] = "auto"):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : MultiDimTypes
            Sequence name
        n_terms : int, default=6
            Number of terms to compute
        coeffs : bool, default=False
            If True, return only coefficients as integers
        method : {'auto', 'symbolic', 'numeric'}
            - 'symbolic': Pure symbolic (exact, slower for large k)
            - 'numeric': Numeric substitution (fast, may need rounding)
            - 'auto': Choose based on m value (default)

        Returns
        -------
        list or sp.Series
            Integer coefficients if coeffs=True, else Series object
        """
        schema = MULTIDIM_DATABASE[name_seq]

        if self.k:
            if method == 'auto':
                if name_seq in self._SEQ_TO_DOIT:
                    method = 'numeric' if self.k >= 6 else 'symbolic'
                else:
                    method = 'numeric' if self.k >= 24 else 'symbolic'

            if method == 'symbolic':
                expr = schema.substitute_symbolic(m=self.m, k=self.k)

                if name_seq in self._SEQ_TO_DOIT:
                    expr = expr.doit()

                series_expansion = sp.series(expr, x, 0, n=n_terms)
                var_expand = x
            else:

                expr = schema.evaluate_numeric(
                    z, m_sides=self.m, k_dimension=self.k)
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
