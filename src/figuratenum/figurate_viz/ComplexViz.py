from typing import Callable, TypeVar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from .ComplexFzPlots import ComplexPhasePortrait, PlotType
import numpy as np

from .PlaneCViz import PlaneCViz
from .SpaceCViz import SpaceCViz
from .MultiDimCViz import MultiDimCViz
from ..db_figuratenum.PlaneSchema import PlaneTypes
from ..db_figuratenum.SpaceSchema import SpaceTypes
from ..db_figuratenum.MultiDimSchema import MultiDimTypes


T = TypeVar('T', PlaneTypes, SpaceTypes, MultiDimTypes)


class ComplexViz:
    """
    Creates enhanced phase portraits of generating functions f(z) of plane, space, and multidimensional
    figurate numbers in the complex plane, based on the style of Elias Wegert (2012).

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

        self.plane_viz = PlaneCViz(m=self.m)
        self.space_viz = SpaceCViz(m=self.m)
        self.multi_dim_viz = MultiDimCViz(m=self.m, k=self.k)

    def _render_phase_portrait(
        self,
        evaluator: Callable[[T, np.ndarray], np.ndarray],
        name_seq: T,
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
        Common function to visualize a figurate number generating function in the complex plane.
        It requires an evaluator function (`evaluator`) and the sequence (`name_seq`).
        """

        resolution = resolution or self.resolution
        figsize = figsize or self.figsize

        if radius <= 0:
            raise ValueError(f"radius must be positive, got {radius}")
        if xlim is None:
            xlim = (-radius, radius)
        if ylim is None:
            ylim = (-radius, radius)

        def func(z): return evaluator(name_seq, z)

        PORTRAIT = ComplexPhasePortrait(
            func, xlim=xlim, ylim=ylim, resolution=resolution)
        fig = PORTRAIT.plot_enhanced(plot_type=plot_type, **kwargs)

        if show:
            plt.show()
        return fig

    def visualize_plane(self, name_seq: PlaneTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs):
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
        return self._render_phase_portrait(
            self.plane_viz._evaluate_fz_to_plot,
            name_seq,
            plot_type=plot_type,
            **kwargs
        )

    def visualize_space(self, name_seq: SpaceTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs):
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
        return self._render_phase_portrait(
            self.space_viz._evaluate_fz_to_plot,
            name_seq,
            plot_type=plot_type,
            **kwargs
        )

    def visualize_multidim(self, name_seq: MultiDimTypes, plot_type: PlotType = "enhanced_phase_portrait", **kwargs):
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
        return self._render_phase_portrait(
            self.multi_dim_viz._evaluate_fz_to_plot,
            name_seq,
            plot_type=plot_type,
            **kwargs
        )
