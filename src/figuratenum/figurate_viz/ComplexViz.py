from typing import Callable, TypeAlias
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

from ..db_figuratenum.validator_helper import Validator
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

    References
    ----------
    [1] Wegert, E. (2012). Visual Complex Functions: An Introduction
        with Phase Portraits. Birkhäuser Basel.
        https://doi.org/10.1007/978-3-0348-0180-5
    """

    def __init__(
        self,
        resolution: int = 800,
        figsize: tuple[float, float] = (6, 6),
        plot_type: PlotType = "enhanced_phase_portrait",
        cmap_color: str = "hsv",
        brightness: float = 0.7,
        num_lines: int = 20,
        domain_grid_radius: float = 2.0,
        disk_radius:  float | None = None,
        show_axes: bool = False,
    ):
        """
        Initialize a ComplexViz instance.

        Default configuration for phase portrait visualization of
        complex-valued generating functions of figurate numbers.

        Defaults are used unless overridden per method call.

        Parameters
        ----------
        resolution : int, default=800
            Default resolution of the evaluation grid.
        figsize : tuple[float, float], default=(6, 6)
            Figure size in inches (width, height)
        plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours', 'enhanced_phase_portrait'}, default='enhanced_phase_portrait'
            Type of plot to generate:
            - 'pure_phase_portrait': phase coloring only
            - 'phase_contours': phase coloring with contour lines
            - 'modulus_contours': phase coloring with modulus contours
            - 'enhanced_phase_portrait': combines phase and modulus contours
        cmap_color : str, default='hsv'
            Default colormap for phase coloring.
        brightness : float, default=0.7
            Base brightness for contours (0-1).
        num_lines : int, default=20
            Default number of contour lines for phase and modulus.
        disk_radius : float | None, default=None
            Radius of the circular masking region centered at (0, 0).
            Values outside this radius are excluded (set to transparent).
            Must be strictly positive if provided.
        domain_grid_radius : float, default=2.0
            Half-width of the square evaluation domain centered at the origin.
        show_axes : bool, default=False
            If True, displays the real (Re) and imaginary (Im) axes.
        """
        self.resolution = resolution
        self.figsize = figsize
        self.plot_type: PlotType = plot_type
        self.cmap_color = cmap_color
        self.brightness = brightness
        self.num_lines = num_lines
        self.disk_radius = disk_radius
        self.domain_grid_radius = domain_grid_radius
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
        elif name_seq in SPACE_DATABASE:
            schema = SPACE_DATABASE[name_seq]
        elif name_seq in MULTIDIM_DATABASE:
            schema = MULTIDIM_DATABASE[name_seq]
        else:
            raise ValueError(
                f"Unknown sequence '{name_seq}' in figuratenum complexviz database")

        return create_evaluator_parametrized(schema, m=m, k=k)

    def _render_phase_portrait(
        self,
        name_seq: SequenceType,
        plot_type: PlotType | None = None,
        m: int | None = None,
        k: int | None = None,
        xlim: tuple[float, float] | None = None,
        ylim: tuple[float, float] | None = None,
        resolution: int | None = None,
        figsize: tuple[float, float] | None = None,
        show: bool = True,
        **kwargs
    ) -> Figure:
        """
        Render a phase portrait with optional overrides.
        """
        if resolution is None:
            resolution = self.resolution
        if plot_type is None:
            plot_type = self.plot_type
        if figsize is None:
            figsize = self.figsize

        if xlim is None:
            xlim = (-self.domain_grid_radius, self.domain_grid_radius)
        if ylim is None:
            ylim = (-self.domain_grid_radius, self.domain_grid_radius)

        func_fz = self._get_evaluator_fz(name_seq, m=m, k=k)

        portrait = ComplexPhasePortrait(
            func_fz, xlim=xlim, ylim=ylim, resolution=resolution
        )

        fig = portrait.plot_enhanced(
            plot_type=plot_type,
            figsize=figsize,
            disk_radius=kwargs.pop("disk_radius", self.disk_radius),
            cmap_color=kwargs.pop("cmap_color", self.cmap_color),
            brightness=kwargs.pop("brightness", self.brightness),
            num_lines=kwargs.pop("num_lines", self.num_lines),
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
        plot_type: PlotType | None = None,
        show: bool = True,
        **kwargs
    ) -> Figure:
        """
        Visualize the generating function of a plane figurate number in the complex plane (phase portrait).

        Parameters
        ----------
        name_seq : PlaneTypes
            Plane figurate number sequence defining its generating function f(z).
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        plot_type : PlotType, optional
            Overrides the default plot type of the instance.
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Per-call plot options. Can override instance defaults:
            - xlim : tuple[float, float], optional
                Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
            - ylim : tuple[float, float], optional
                Vertical limits of the complex plane. Overrides `domain_grid_radius`.
            - show_axes : bool, optional
                Whether to display the real (Re) and imaginary (Im) axes.
            - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure. Automatically displayed if `show=True`.
        """
        return self._render_phase_portrait(name_seq, m=m, plot_type=plot_type, show=show, **kwargs)

    def visualize_space(
        self,
        name_seq: SpaceTypes,
        *, m: int | None = None,
        plot_type: PlotType | None = None,
        show: bool = True,
        **kwargs
    ) -> Figure:
        """
        Visualize the generating function of a space figurate number in the complex plane (phase portrait).

        Parameters
        ----------
        name_seq : SpaceTypes
            Space figurate number sequence defining its generating function f(z).
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        plot_type : PlotType, optional
            Overrides the default plot type of the instance.
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Per-call plot options. Can override instance defaults:
            - xlim : tuple[float, float], optional
                Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
            - ylim : tuple[float, float], optional
                Vertical limits of the complex plane. Overrides `domain_grid_radius`.
            - show_axes : bool, optional
                Whether to display the real (Re) and imaginary (Im) axes.
            - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure. Automatically displayed if `show=True`.
        """
        return self._render_phase_portrait(name_seq, m=m, plot_type=plot_type, show=show, **kwargs)

    def visualize_multidim(
        self,
        name_seq: MultiDimTypes,
        *, m: int | None = None, k: int | None = None,
        plot_type: PlotType | None = None,
        show: bool = True,
        **kwargs
    ) -> Figure:
        """
        Visualize the generating function of a multidimensional figurate number in the complex plane (phase portrait).

        Parameters
        ----------
        name_seq : MultiDimTypes
            Multidimensional figurate number sequence defining its generating function f(z).
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        k : int | None
            Parameter defining the k-dimensional structure (if applicable).
        plot_type : PlotType, optional
            Overrides the default plot type of the instance.
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Per-call plot options. Can override instance defaults:
            - xlim : tuple[float, float], optional
                Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
            - ylim : tuple[float, float], optional
                Vertical limits of the complex plane. Overrides `domain_grid_radius`.
            - show_axes : bool, optional
                Whether to display the real (Re) and imaginary (Im) axes.
            - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure. Automatically displayed if `show=True`.
        """
        return self._render_phase_portrait(name_seq, m=m, k=k, plot_type=plot_type, show=show, **kwargs)
