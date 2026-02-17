from typing import Literal
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from ..db_figuratenum.symbols_figuratenum import z
from ..db_figuratenum.MultiDimSchema import MultiDimTypes, x
from ..db_figuratenum.multidim_db import MULTIDIM_DATABASE
from .ComplexFzPlots import ComplexPhasePortrait


class MultiDimCViz:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k

    _SEQ_TO_DOIT: set[MultiDimTypes] = {
        "k_dim_hypercube",
        "k_dim_nexus",
        "k_dim_centered_hypercube",
        "generalized_k_dim_hypercube"
    }

    def _evaluate_fz_to_plot(self, name_seq: MultiDimTypes, z_values: np.ndarray) -> np.ndarray:
        """Evaluate at numeric points (for plotting)."""
        schema = MULTIDIM_DATABASE[name_seq]
        return schema.evaluate_numeric(z_values, m_sides=self.m, k_dimension=self.k)

    def visualize(
        self,
        name_seq: MultiDimTypes,
        radius: float = 2,
        xlim: tuple[float, float] | None = None,
        ylim: tuple[float, float] | None = None,
        plot_type="all",
        resolution: int = 800,
        show: bool = True,
        save_path: str | None = None,
        **kwargs,
    ):
        """
        Visualize a Multidimensional Figurate Number generating function as an enhanced phase portrait
        in the complex plane, following the style of Elias Wegert (2012).

        This method prepares the complex sequence numerically and generates a Matplotlib figure,
        optionally displaying it or saving it to a file.

        Parameters
        ----------
        name_seq : MultiDimTypes
            Type of multidimensional figurate number generating function to visualize.
        radius : float, default=2
            Half-width of the square viewing window.
            Creates the window [-radius, radius] x [-radius, radius].
            Ignored if `xlim` or `ylim` are provided.
        xlim : tuple[float, float] | None, optional
            Custom x-axis limits (xmin, xmax). Overrides `radius` for the x-axis.
        ylim : tuple[float, float] | None, optional
            Custom y-axis limits (ymin, ymax). Overrides `radius` for the y-axis.
        plot_type : {'all', 'phase', 'modulus', 'simple'}, default='all'
            Type of plot to generate.
        resolution : int, default=800
            Grid resolution (points per dimension) for evaluating the function.
        figsize : tuple[float, float], optional
            Size of the figure (width, height in inches).
        show : bool, default=True
            If True, display the figure.
        save_path : str | None, optional
            Path to save the figure if provided.
        **kwargs : dict
            Additional arguments to pass to the underlying `plot_enhanced` method.

        Returns
        -------
        matplotlib.figure.Figure
            The generated Matplotlib figure object (not displayed if `show=False`).
        """

        if radius <= 0:
            raise ValueError(f"radius must be positive, got {radius}")
        if xlim is None:
            xlim = (-radius, radius)
        if ylim is None:
            ylim = (-radius, radius)

        def func(z): return self._evaluate_fz_to_plot(name_seq, z)

        PORTRAIT = ComplexPhasePortrait(
            func, xlim=xlim, ylim=ylim, resolution=resolution)

        fig = PORTRAIT.plot_enhanced(
            plot_type=plot_type, **kwargs)

        if save_path:
            fig.savefig(save_path, dpi=300, bbox_inches='tight')
        if show:
            plt.show()
        return fig

    def expand_series(self, name_seq: MultiDimTypes, n_terms: int = 6,
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
