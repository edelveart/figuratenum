
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from matplotlib.figure import Figure
from matplotlib import cm


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
        self.xlim = xlim
        self.ylim = ylim
        self.resolution = resolution

        self._create_mesh()
        self._evaluate_function()

    def _create_mesh(self):
        x = np.linspace(self.xlim[0], self.xlim[1], self.resolution)
        y = np.linspace(self.ylim[0], self.ylim[1], self.resolution)
        X, Y = np.meshgrid(x, y)
        self.Z = X + 1j*Y
        self.X = X
        self.Y = Y

    def _evaluate_function(self):
        try:
            self.F = self.func(self.Z)
        except Exception as e:
            print(f"Error when function fz executes: {e}")
            self.F = np.full_like(self.Z, np.nan, dtype=complex)

    def _compute_phase(self, normalized: bool = False):
        # if normalized, returns phase in [0,1] by converting [-\pi,\pi] → [0,2\pi)
        phase_f = np.angle(self.F)
        if normalized:
            phase_f = np.mod(phase_f, 2*np.pi)
            return phase_f / (2 * np.pi)  # normalize=[0, 1]
        return phase_f

    def _compute_modulus(self, logarithmic: bool = False):
        abs_f = np.abs(self.F)
        if logarithmic:
            return np.log(abs_f + 1e-12)  # avoid log(0)
        else:
            return abs_f

    def _create_phase_colormap(self, cmap_color: str):
        """Creates the basic phase portrait with different cmap colors"""
        phase_normalized = self._compute_phase(normalized=True)
        return cm.get_cmap(cmap_color)(phase_normalized)[..., :3]

    def _compute_modulus_contours(self, min_brightness=0.7,  frequency=3):
        """Brightness for modulus |f(z)| contour lines (via sawtooth g)"""
        log_mod = self._compute_modulus(logarithmic=True)
        scaled = frequency * log_mod
        g = np.ceil(scaled) - scaled
        return min_brightness + (1 - min_brightness) * (1 - g)

    def _compute_phase_contours(self,  min_brightness=0.7, frequency=3):
        """Brightness for phase arg(f(z)) contour lines (via sawtooth g)"""
        # Rotate phase by 180° ($ \arg(f(z)) + \pi$), following Wegert Book
        phase_normalized = self._compute_phase(normalized=False) + np.pi
        scaled = frequency * phase_normalized
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
        type_plot: str = "all",
        brightness=0.7,
        num_lines=3,
        poincare_disk: bool = False,
        cmap_color="hsv"
    ) -> Figure:
        """
        Creates an enhanced phase portrait (style of Elias Wegert), combining phase coloring,
        modulus contours, and optional shading.

        Args:
            figsize (tuple): Size of the figure (width, height). Default is (8, 8).
            type_plot (str): Type of plot to generate ('all', 'phase', 'modulus', 'contours').
            brightness (float): Base brightness for contours (0-1). Default is 0.7.
            num_lines (int): Number of contour lines for phase and modulus. Default is 3.
            poincare_disk (bool): If True, applies a Poincaré disk mask. Default is False.
            cmap_color (str): Colormap for phase coloring. Default is 'hsv'.

        Returns:
            A Matplotlib figure with the enhanced phase portrait.
        """
        fig, ax = plt.subplots(figsize=figsize)

        rgb_land = self._create_phase_colormap(cmap_color)

        b_mod = self._compute_modulus_contours(brightness, num_lines)
        b_phase = self._compute_phase_contours(brightness, num_lines)

        # Plot combinations
        # RGB * B_mod * B_phase
        if type_plot == "all":
            rgb_land = rgb_land * (b_mod * b_phase)[..., None]
        elif type_plot == "modulus":
            rgb_land = rgb_land * b_mod[..., None]
        elif type_plot == "phase":
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
            interpolation='bicubic'
        )
        plt.tight_layout()
        return fig
