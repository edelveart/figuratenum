import warnings
from typing import Literal, TypeAlias
import sympy as sp

from ..db_figuratenum.symbols_figuratenum import x, z
from ..db_figuratenum.PlaneSchema import PlaneTypes
from ..db_figuratenum.plane_db import PLANE_DATABASE
from ..db_figuratenum.SpaceSchema import SpaceTypes
from ..db_figuratenum.space_db import SPACE_DATABASE
from ..db_figuratenum.MultiDimSchema import MultiDimTypes
from ..db_figuratenum.multidim_db import MULTIDIM_DATABASE


DualMethodType: TypeAlias = Literal["numeric", "symbolic"]


class PowerSeriesExpansion:
    _SEQ_TO_DOIT: set[MultiDimTypes] = {
        "k_dim_hypercube",
        "k_dim_nexus",
        "k_dim_centered_hypercube",
        "generalized_k_dim_hypercube"
    }

    def expand_plane_series(
        self,
        name_seq: PlaneTypes,
        *, m: int | None = None,
        n_terms: int = 6,
        coeffs: bool = False,
        method: DualMethodType = "numeric"
    ):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : PlaneTypes
            Sequence name
        m : int | None, default=None
            Number of sides of the figurate number.
        n_terms : int, default=6
            Number of terms to compute
        coeffs : bool, default=False
            If True, return only coefficients as integers
        method : {'symbolic', 'numeric'}, default='numeric'
            - 'symbolic': Pure symbolic (exact, slower)
            - 'numeric': Numeric substitution (fast, may need rounding)

        Returns
        -------
        list or sp.Series
            Integer coefficients if coeffs=True, else Series object
        """
        schema = PLANE_DATABASE[name_seq]

        needs_m = schema.requires_m()

        if m is not None and not needs_m:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'm'; ignoring it.",
                stacklevel=2
            )

        if needs_m and m is None:
            raise ValueError(
                f"Sequence '{name_seq}' requires parameter 'm'.")

        if method == "symbolic":
            subs_kwargs = {}
            if needs_m:
                subs_kwargs['m'] = m
            expr = schema.substitute_symbolic(**subs_kwargs)
            series_expansion = sp.series(expr, x, 0, n=n_terms)
            var_expand = x
        else:
            series_expansion = schema.evaluate_numeric(z, m_sides=m)
            series_expansion = sp.series(series_expansion, z, 0, n=n_terms)
            var_expand = z

        if coeffs:
            return [self._safe_int(series_expansion.coeff(var_expand, i))
                    for i in range(1, n_terms)]
        return series_expansion

    def expand_space_series(
        self,
        name_seq: SpaceTypes,
        *, m: int | None = None,
        n_terms: int = 6,
        coeffs: bool = False,
        method: DualMethodType = "numeric"
    ):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : SpaceTypes
            Sequence name
        m : int | None, default=None
            Number of sides of the figurate number
        n_terms : int, default=6
            Number of terms to compute

        coeffs : bool, default=False
            If True, return only coefficients as integers
        method : {'symbolic', 'numeric'}, default='numeric'
            - 'symbolic': Pure symbolic (exact, slower)
            - 'numeric': Numeric substitution (fast, may need rounding)

        Returns
        -------
        list or sp.Series
            Integer coefficients if coeffs=True, else Series object
        """
        schema = SPACE_DATABASE[name_seq]

        needs_m = schema.requires_m()

        if m is not None and not needs_m:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'm'; ignoring it.",
                stacklevel=2
            )

        if needs_m and m is None:
            raise ValueError(
                f"Sequence '{name_seq}' requires parameter 'm'.")

        if method == "symbolic":
            subs_kwargs = {}
            if needs_m:
                subs_kwargs['m'] = m
            expr = schema.substitute_symbolic(**subs_kwargs)
            series_expansion = sp.series(expr, x, 0, n=n_terms)
            var_expand = x
        else:
            series_expansion = schema.evaluate_numeric(z, m_sides=m)
            series_expansion = sp.series(series_expansion, z, 0, n=n_terms)
            var_expand = z

        if coeffs:
            return [self._safe_int(series_expansion.coeff(var_expand, i))
                    for i in range(1, n_terms)]
        return series_expansion

    def expand_multidim_series(
        self,
        name_seq: MultiDimTypes,
        *, k: int | None = None, m: int | None = None,
        n_terms: int = 6,
        coeffs: bool = False,
        method: DualMethodType = "numeric"
    ):
        """
        Expand generating function as Taylor series.

        Parameters
        ----------
        name_seq : MultiDimTypes
            Sequence name
        m : int | None, default=None
            Number of sides of the figurate number
        k: int | None, default=None
            Dimension k of the figurate number
        n_terms : int, default=6
            Number of terms to compute
        coeffs : bool, default=False
            If True, return only coefficients as integers
        method : {'symbolic', 'numeric'}, default='numeric'
            - 'symbolic': Pure symbolic (exact, slower for large k)
            - 'numeric': Numeric substitution (fast, may need rounding)

        Returns
        -------
        list or sp.Series
            Integer coefficients if coeffs=True, else Series object
        """
        schema = MULTIDIM_DATABASE[name_seq]

        needs_m = schema.requires_m()
        needs_k = schema.requires_k()

        if m is not None and not needs_m:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'm'; ignoring it.",
                stacklevel=2
            )

        if k is not None and not needs_k:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'k'; ignoring it.",
                stacklevel=2
            )

        if needs_m and m is None:
            raise ValueError(
                f"Sequence '{name_seq}' requires parameter 'm'.")
        if needs_k and k is None:
            raise ValueError(
                f"Sequence '{name_seq}' requires parameter 'k'.")

        if method == "symbolic":
            subs_kwargs = {}
            if needs_m:
                subs_kwargs['m'] = m
            if needs_k:
                subs_kwargs['k'] = k
            expr = schema.substitute_symbolic(**subs_kwargs)
            if name_seq in self._SEQ_TO_DOIT:
                expr = expr.doit()
            series_expansion = sp.series(expr, x, 0, n=n_terms)
            var_expand = x
        else:
            series_expansion = schema.evaluate_numeric(
                z,
                k_dimension=k,
                m_sides=m
            )
            series_expansion = sp.series(series_expansion, z, 0, n=n_terms)
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
