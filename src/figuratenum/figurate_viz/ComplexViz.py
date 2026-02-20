from typing import Callable, TypeAlias
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import warnings

from ..db_figuratenum.validation_helper import Validator
from ..db_figuratenum.PlaneSchema import PlaneTypes, PlaneSchema
from ..db_figuratenum.SpaceSchema import SpaceTypes, SpaceSchema
from ..db_figuratenum.MultiDimSchema import MultiDimTypes, MultiDimSchema
from ..db_figuratenum.plane_db import PLANE_DATABASE
from ..db_figuratenum.space_db import SPACE_DATABASE
from ..db_figuratenum.multidim_db import MULTIDIM_DATABASE
from .ComplexFzPlots import ComplexPhasePortrait, PlotType


SequenceType: TypeAlias = PlaneTypes | SpaceTypes | MultiDimTypes


class ComplexViz:
    """
    Unified interface for evaluating and visualizing generating functions
    of plane, space, and multidimensional figurate numbers, inspired by the style of Elias Wegert (2012).
    """

    def __init__(
        self,
        resolution: int = 800,
        figsize: tuple[float, float] = (6, 6),
        plot_type: PlotType = "enhanced_phase_portrait",
        cmap_color: str = "hsv",
        brightness: float = 0.7,
        num_lines: int = 3,
        poincare_disk: bool = False,
        show_axes: bool = True,
    ):
        """
        Constructs a ComplexViz instance.

        Parameters
        ----------
        resolution : int, default=800
            Default resolution of the evaluation grid.
        figsize : tuple[float,float], default=(8,8)
            Default figure size in inches.
        plot_type : PlotType, default='enhanced_phase_portrait'
            Default plot type.
        cmap_color : str, default='hsv'
            Default colormap for phase coloring.
        brightness : float, default=0.7
            Base brightness for contours (0-1).
        num_lines : int, default=3
            Default number of contour lines for phase and modulus.
        poincare_disk : bool, default=False
            Apply Poincaré disk mask if True.
        show_axes : bool, default=True
            Display axes by default.
        """
        self.resolution = resolution
        self.figsize = figsize
        self.plot_type = plot_type
        self.cmap_color = cmap_color
        self.brightness = brightness
        self.num_lines = num_lines
        self.poincare_disk = poincare_disk
        self.show_axes = show_axes

    def _get_evaluator_fz(self, name_seq: SequenceType, m: int | None = None, k: int | None = None) -> Callable[[np.ndarray], np.ndarray]:
        """
        Devuelve la función evaluadora f(z) para la secuencia dada.
         """
        schema = None

        def create_evaluator_parametrized(schema: PlaneSchema | SpaceSchema | MultiDimSchema, m=None, k=None):
            """
            Creates and returns an evaluator for the given sequence, verifies, checks, and orders the parameters.
            """
            if isinstance(schema, MultiDimSchema):
                needs_m = schema.requires_m()
                needs_k = schema.requires_k()

                Validator.validate_m_and_k(
                    m=m, k=k, name_seq=name_seq, needs_m=needs_m, needs_k=needs_k)

                kwargs = {}
                if needs_m:
                    kwargs['m_sides'] = m
                if needs_k:
                    kwargs['k_dimension'] = k

                return lambda z: schema.evaluate_numeric(z, **kwargs)

            else:  # PlaneSchema or SpaceSchema
                needs_m = schema.requires_m()
                needs_k = False

                Validator.validate_m_and_k(
                    m=m, k=k, name_seq=name_seq, needs_m=needs_m, needs_k=False)

                kwargs = {}
                if needs_m:
                    kwargs['m_sides'] = m

                return lambda z: schema.evaluate_numeric(z, **kwargs)

        if name_seq in PLANE_DATABASE:
            schema = PLANE_DATABASE[name_seq]
            return create_evaluator_parametrized(schema, m=m, k=k)

        elif name_seq in SPACE_DATABASE:
            schema = SPACE_DATABASE[name_seq]
            return create_evaluator_parametrized(schema, m=m, k=k)

        elif name_seq in MULTIDIM_DATABASE:
            schema = MULTIDIM_DATABASE[name_seq]
            return create_evaluator_parametrized(schema, m=m, k=k)

        else:
            raise ValueError(
                f"Unknown sequence '{name_seq}' in figuratenum complexviz database")

    def _render_phase_portrait(
        self,
        name_seq: SequenceType,
        plot_type: PlotType,
        m: int | None = None,
        k: int | None = None,
        radius: float = 2,
        xlim: tuple[float, float] | None = None,
        ylim: tuple[float, float] | None = None,
        resolution: int | None = None,
        figsize: tuple[float, float] = (6, 6),
        show: bool = True,
        **kwargs
    ) -> Figure:
        """
        Render a phase portrait with optional overrides.
        """
        resolution = resolution or self.resolution
        plot_type = plot_type or self.plot_type

        figsize = figsize or self.figsize
        if xlim is None:
            xlim = (-radius, radius)
        if ylim is None:
            ylim = (-radius, radius)

        func_fz = self._get_evaluator_fz(name_seq, m=m, k=k)

        portrait = ComplexPhasePortrait(
            func_fz, xlim=xlim, ylim=ylim, resolution=resolution
        )

        fig = portrait.plot_enhanced(
            plot_type=plot_type,
            figsize=figsize,
            cmap_color=kwargs.pop("cmap_color", self.cmap_color),
            brightness=kwargs.pop("brightness", self.brightness),
            num_lines=kwargs.pop("num_lines", self.num_lines),
            poincare_disk=kwargs.pop("poincare_disk", self.poincare_disk),
            show_axes=kwargs.pop("show_axes", self.show_axes),
            **kwargs
        )

        if show:
            plt.show()
        return fig

    def visualize_plane(
        self,
        name_seq: PlaneTypes,
        *, m: int | None = None,
        plot_type: PlotType = "enhanced_phase_portrait",
        **kwargs
    ) -> Figure:
        """
        Evaluates the generating function for the given plane figurate number
        and produces a visual representation in the complex plane inspired by
        the work of Elias Wegert (2012).

        Parameters
        ----------
        name_seq : PlaneTypes
            Plane figurate number sequence defining its generating function f(z).
        plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours', 'enhanced_phase_portrait'}, default='enhanced_phase_portrait'
            Type of plot to generate:
            - 'pure_phase_portrait': phase coloring only
            - 'phase_contours': phase coloring with contour lines
            - 'modulus_contours': phase coloring with modulus contours
            - 'enhanced_phase_portrait': combines phase and modulus contours
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Optional arguments passed to `ComplexPhasePortrait.plot_enhanced`:
            - figsize : tuple[float, float], default=(8, 8)
                Figure size in inches (width, height)
            - cmap_color : str, default='hsv'
                Colormap used for phase coloring
            - brightness : float, default=0.7
                Base brightness for contours (0-1)
            - num_lines : int, default=3
                Number of contour lines for phase and modulus
            - poincare_disk : bool, default=False
                Apply a Poincaré disk mask if True
            - show_axes : bool, default=True
                Display axes on the plot

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure object. The figure is displayed automatically.
        """
        return self._render_phase_portrait(name_seq, m=m, plot_type=plot_type, **kwargs)

    def visualize_space(
        self,
        name_seq: SpaceTypes,
        *, m: int | None = None,
        plot_type: PlotType = "enhanced_phase_portrait",
        **kwargs
    ) -> Figure:
        """
        Evaluates the generating function for the given space figurate number
        and produces a visual representation in the complex plane inspired by
        the work of Elias Wegert (2012).

        Parameters
        ----------
        name_seq : SpaceTypes
            Space figurate number sequence defining its generating function f(z).
        plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours', 'enhanced_phase_portrait'}, default='enhanced_phase_portrait'
            Type of plot to generate:
            - 'pure_phase_portrait': phase coloring only
            - 'phase_contours': phase coloring with contour lines
            - 'modulus_contours': phase coloring with modulus contours
            - 'enhanced_phase_portrait': combines phase and modulus contours
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Optional arguments passed to `ComplexPhasePortrait.plot_enhanced`:
            - figsize : tuple[float, float], default=(8, 8)
                Figure size in inches (width, height)
            - cmap_color : str, default='hsv'
                Colormap used for phase coloring
            - brightness : float, default=0.7
                Base brightness for contours (0-1)
            - num_lines : int, default=3
                Number of contour lines for phase and modulus
            - poincare_disk : bool, default=False
                Apply a Poincaré disk mask if True
            - show_axes : bool, default=True
                Display axes on the plot

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure object. The figure is displayed automatically.
        """
        return self._render_phase_portrait(name_seq, m=m, plot_type=plot_type,  **kwargs)

    def visualize_multidim(
        self,
        name_seq: MultiDimTypes,
        *, m: int | None = None, k: int | None = None,
        plot_type: PlotType = "enhanced_phase_portrait",
        **kwargs
    ) -> Figure:
        """
        Evaluates the generating function for the given multidimensional figurate number
        and produces a visual representation in the complex plane inspired by
        the work of Elias Wegert (2012).

        Parameters
        ----------
        name_seq : MultiDimTypes
            Multidimensional figurate number sequence defining its generating function f(z)..
        plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours', 'enhanced_phase_portrait'}, default='enhanced_phase_portrait'
            Type of plot to generate:
            - 'pure_phase_portrait': phase coloring only
            - 'phase_contours': phase coloring with contour lines
            - 'modulus_contours': phase coloring with modulus contours
            - 'enhanced_phase_portrait': combines phase and modulus contours
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Optional arguments passed to `ComplexPhasePortrait.plot_enhanced`:
            - figsize : tuple[float, float], default=(8, 8)
                Figure size in inches (width, height)
            - cmap_color : str, default='hsv'
                Colormap used for phase coloring
            - brightness : float, default=0.7
                Base brightness for contours (0-1)
            - num_lines : int, default=3
                Number of contour lines for phase and modulus
            - poincare_disk : bool, default=False
                Apply a Poincaré disk mask if True
            - show_axes : bool, default=True
                Display axes on the plot

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure object. The figure is displayed automatically.
        """
        return self._render_phase_portrait(name_seq, m=m, k=k, plot_type=plot_type, **kwargs)
