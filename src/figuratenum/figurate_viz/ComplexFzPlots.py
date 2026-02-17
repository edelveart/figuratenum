
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from matplotlib.figure import Figure


class ComplexPhasePortrait:
    """
    Create phase portraits of complex functions
    based on the style of Elias Wegert (2012).
    """

    def __init__(
        self,
        func: Callable[[np.ndarray], np.ndarray],
        xlim: tuple[float, float] = (-2, 2),
        ylim: tuple[float, float] = (-2, 2),
        resolution: int = 800
    ):
        """
        Initialize the phase portrait.

        Args:
            func: Complex function f: C → C
            xlim: Re(z) axis limits (min, max)
            ylim: Im(z) axis limits (min, max)
            resolution: Grid resolution (points per dimension)
        """
        self.func = func
        self.xlim = self._validate_limits(xlim, 'xlim')
        self.ylim = self._validate_limits(ylim, 'ylim')
        self.resolution = resolution
        self._create_mesh()
        self._evaluate_function()

        # Ingredients: Modulus and Phase (cached)
        self._log_modulus = np.log(np.abs(self.F) + 1e-12)
        self._phase_raw = np.angle(self.F)  # arctan2(Im(z), Re(z))
        # phase normalized in [0,1] by converting (-\pi,\pi] → [0,2\pi)
        self._phase_normalized = np.mod(
            self._phase_raw,
            2 * np.pi
        ) / (2 * np.pi)

    @staticmethod
    def _validate_limits(limits: tuple[float, float], name: str) -> tuple[float, float]:
        a, b = limits
        if a >= b:
            raise ValueError(f"{name}[0] must be < {name}[1], got {limits}")
        return (float(a), float(b))

    def _create_mesh(self):
        x = np.linspace(self.xlim[0], self.xlim[1], self.resolution)
        y = np.linspace(self.ylim[0], self.ylim[1], self.resolution)
        X, Y = np.meshgrid(x, y)
        self.Z = X + 1j*Y

    def _evaluate_function(self):
        try:
            self.F = self.func(self.Z)
        except Exception as e:
            print(f"Error when function f(z) executes: {e}")
            self.F = np.full_like(self.Z, np.nan, dtype=complex)

    def _create_phase_colormap(self, cmap_color: str):
        """Creates the basic phase portrait with different cmap colors"""
        return plt.colormaps[cmap_color](self._phase_normalized)[..., :3]

    def _compute_modulus_contours(self, min_brightness=0.7,  frequency=3):
        """Brightness for modulus |f(z)| contour lines (via sawtooth g)"""
        scaled = frequency * self._log_modulus
        g = np.ceil(scaled) - scaled
        return min_brightness + (1 - min_brightness) * (1 - g)

    def _compute_phase_contours(self,  min_brightness=0.7, frequency=3):
        """Brightness for phase arg(f(z)) contour lines (via sawtooth g)"""
        # Rotate phase by 180° ($ \arg(f(z)) + \pi$), following Wegert Book
        scaled = frequency * (self._phase_raw + np.pi)
        g = np.ceil(scaled) - scaled
        return min_brightness + (1 - min_brightness) * (1 - g)

    def _poincare_disk_mask(self, rgb):
        """
        Apply Poincaré Disk Mask to RGB image
        : ${x + iy : x^2 + y^2 < 1}
        """
        mask = np.abs(self.Z) < 1
        alpha = mask.astype(float)
        return np.dstack([rgb, alpha])  # RGBA

    def plot_enhanced(
        self,
        figsize: tuple[float, float] = (8, 8),
        plot_type: str = "simple",
        cmap_color: str = "hsv",
        brightness: float = 0.7,
        num_lines: int = 3,
        poincare_disk: bool = False,
        show_axes: bool = True
    ) -> Figure:
        """
        Creates an enhanced phase portrait (style of Elias Wegert), combining phase coloring,
        modulus contours, and optional shading.

        Args:
            figsize (tuple[float, float]): Size of the figure (width, height). Default is (8, 8).
            plot_type (str): Type of plot to generate ('all', 'phase', 'modulus', 'simple'). Default is 'simple'.
            cmap_color (str): Colormap for phase coloring. Default is 'hsv'.
            brightness (float): Base brightness for contours (0-1). Default is 0.7.
            num_lines (int): Number of contour lines for phase and modulus. Default is 3.
            poincare_disk (bool): If True, applies a Poincaré disk mask. Default is False.
            show_axes (bool): If True, displays axes on the plot. Default is True.
        Returns:
            A Matplotlib figure with the enhanced phase portrait (Not Displayed)
        """
        fig, ax = plt.subplots(figsize=figsize)

        rgb_land = self._create_phase_colormap(cmap_color)

        # Plot combinations
        # RGB * B_mod * B_phase | RGB * B_mod | RGB * B_phase | RGB
        if plot_type == "all":
            b_mod = self._compute_modulus_contours(brightness, num_lines)
            b_phase = self._compute_phase_contours(brightness, num_lines)
            rgb_land = rgb_land * (b_mod * b_phase)[..., None]
        elif plot_type == "modulus":
            b_mod = self._compute_modulus_contours(brightness, num_lines)
            rgb_land = rgb_land * b_mod[..., None]
        elif plot_type == "phase":
            b_phase = self._compute_phase_contours(brightness, num_lines)
            rgb_land = rgb_land * b_phase[..., None]

        if poincare_disk:
            rgb_land = self._poincare_disk_mask(rgb_land)

        extent_tuple: tuple[float, float, float, float] = (
            self.xlim[0], self.xlim[1],
            self.ylim[0], self.ylim[1]
        )
        ax.imshow(
            rgb_land,
            extent=extent_tuple,
            origin='lower',
            interpolation='bicubic',
            aspect='equal'
        )
        if show_axes:
            ax.set_xlabel('Re(z)')
            ax.set_ylabel('Im(z)')
        else:
            ax.axis('off')

        plt.tight_layout()
        return fig
