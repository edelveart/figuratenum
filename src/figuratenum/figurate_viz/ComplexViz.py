from typing import Callable, TypeAlias
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

from ..db_figuratenum.PlaneSchema import PlaneTypes
from ..db_figuratenum.SpaceSchema import SpaceTypes
from ..db_figuratenum.MultiDimSchema import MultiDimTypes
from ..db_figuratenum.plane_db import PLANE_DATABASE
from ..db_figuratenum.space_db import SPACE_DATABASE
from ..db_figuratenum.multidim_db import MULTIDIM_DATABASE
from .ComplexFzPlots import ComplexPhasePortrait, PlotType


SequenceType: TypeAlias = PlaneTypes | SpaceTypes | MultiDimTypes


class ComplexViz:
    """
    Unified interface for evaluating and visualizing generating functions
    of plane, space, and multidimensional figurate numbers, inspired on the style of Elias Wegert (2012).
    """

    def __init__(self, m: int, k: int, resolution: int = 800, figsize: tuple[float, float] = (8, 8)):
        """
        Constructs a ComplexViz instance for generating functionsf(z) of figurate numbers.

        Parameters
        ----------
        m : int
            Number of sides of the figurate number. This parameter defines the type of
            figurate number to create (e.g., 3 for triangular numbers, 4 for square numbers, etc.).
        k : int
            Dimension of the space. Typically used for values greater than 4 (such as 4D, 5D),
            representing multidimensional sequences.
            class ComplexViz:
        resolution : int, default=800
            Resolution of the evaluation grid used in the complex plane. Higher values
            generate finer plots but take more time and memory.
        figsize : tuple[float, float], default=(8, 8)
            Figure size (width, height in inches) for the generated plots.
        """
        self.m = m
        self.k = k
        self.resolution = resolution
        self.figsize = figsize

    def _get_evaluator(self, name_seq: SequenceType) -> Callable[[np.ndarray], np.ndarray]:
        """
        Get the appropriate numeric evaluator for a given sequence name.

        Parameters
        ----------
        name_seq : SequenceType
        The name of the sequence for which to obtain the evaluator function.
        This can correspond to a plane, space, or multidimensional sequence.

        Returns
        -------
        Callable[[np.ndarray], np.ndarray]
        A function that evaluates the generating function f(z) for the given
        sequence at any complex input `z` (or array of complex values).
        """
        # Determine which database based on type
        if name_seq in PLANE_DATABASE:
            schema = PLANE_DATABASE[name_seq]
            return lambda z: schema.evaluate_numeric(z, m_sides=self.m)

        elif name_seq in SPACE_DATABASE:
            schema = SPACE_DATABASE[name_seq]
            return lambda z: schema.evaluate_numeric(z, m_sides=self.m)

        elif name_seq in MULTIDIM_DATABASE:
            schema = MULTIDIM_DATABASE[name_seq]
            return lambda z: schema.evaluate_numeric(z, m_sides=self.m, k_dimension=self.k)

        else:
            raise ValueError(f"Unknown sequence: {name_seq}")

    def _render_phase_portrait(
        self,
        name_seq: SequenceType,
        radius: float = 2,
        plot_type: PlotType = "enhanced_phase_portrait",
        xlim: tuple[float, float] | None = None,
        ylim: tuple[float, float] | None = None,
        resolution: int | None = None,
        figsize: tuple[float, float] | None = None,
        show=True,
        **kwargs
    ) -> Figure:
        """
        Common method to visualize a figurate number generating function in the complex plane.
        It requires an evaluator function (`evaluator`) and the sequence (`name_seq`).

        Parameters
        ----------
        name_seq : SequenceType
            The figurate number sequence to visualize, which can be a plane, space, or multidimensional sequence.
        radius : float, default=2
            The radius of the complex plane region to display. The plot will focus on this circular region.
        plot_type : PlotType, default='enhanced_phase_portrait'
            Type of plot to generate. Options include:
            - 'pure_phase_portrait': phase coloring only
            - 'phase_contours': phase coloring with contour lines
            - 'modulus_contours': phase coloring with modulus contours
            - 'enhanced_phase_portrait': combines phase and modulus contours
        xlim : tuple[float, float] | None, optional
            The x-axis limits for the plot. If None, defaults to the range (-radius, radius).
        ylim : tuple[float, float] | None, optional
            The y-axis limits for the plot. If None, defaults to the range (-radius, radius).
        resolution : int | None, optional
            The resolution of the evaluation grid. Defaults to the resolution set in the instance (default is 800).
        figsize : tuple[float, float] | None, optional
            Size of the generated figure. If None, defaults to (8, 8).
        show : bool, default=True
            Whether to display the plot immediately. If False, the plot is generated but not shown.
        **kwargs : dict
            Additional keyword arguments passed to `ComplexPhasePortrait.plot_enhanced`.

        Returns
        -------
        matplotlib.figure.Figure
            The generated figure object. The figure is displayed automatically if `show=True`, otherwise
            it can be displayed later.
        """

        resolution = resolution or self.resolution
        figsize = figsize or self.figsize

        if radius <= 0:
            raise ValueError(f"radius must be positive, got {radius}")
        if xlim is None:
            xlim = (-radius, radius)
        if ylim is None:
            ylim = (-radius, radius)

        func_fz = self._get_evaluator(name_seq)

        PORTRAIT = ComplexPhasePortrait(
            func_fz, xlim=xlim, ylim=ylim, resolution=resolution)

        fig = PORTRAIT.plot_enhanced(
            figsize=figsize,
            plot_type=plot_type,
            **kwargs
        )

        if show:
            plt.show()
        return fig

    def visualize_plane(self, name_seq: PlaneTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs) -> Figure:
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
        return self._render_phase_portrait(name_seq, plot_type=plot_type, **kwargs)

    def visualize_space(self, name_seq: SpaceTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs) -> Figure:
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
        return self._render_phase_portrait(name_seq, plot_type=plot_type, **kwargs)

    def visualize_multidim(self, name_seq: MultiDimTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs) -> Figure:
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
        return self._render_phase_portrait(name_seq, plot_type=plot_type, **kwargs)
