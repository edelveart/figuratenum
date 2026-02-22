
from matplotlib.colors import hsv_to_rgb
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Literal, TypeAlias
from matplotlib.figure import Figure

PlotType: TypeAlias = Literal[
    'pure_phase_portrait',
    'phase_contours',
    'modulus_contours',
    'enhanced_phase_portrait'
]


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

    def _compute_modulus_contours(self, min_brightness=0.7,  num_lines=3):
        """
        Brightness for modulus |f(z)| contour lines (via sawtooth g_floor)

        Period = 2π / num_lines
        """
        period = 2 * np.pi / num_lines
        return self._sawtooth_wegert(self._log_modulus,
                                     period,
                                     min_brightness, 1)

    def _compute_phase_contours(self,  min_brightness=0.7, num_lines=3):
        """Brightness for phase arg(f(z)) contour lines (via sawtooth g_floor)
        Period = 2π / num_lines
        """
        # Rotate phase by 180° ($ \arg(f(z)) + \pi$), i.e., an offset
        period = 2 * np.pi / num_lines
        return self._sawtooth_wegert(self._phase_raw,
                                     period,
                                     min_brightness, 1)

    @staticmethod
    def _sawtooth_wegert(x: np.ndarray, period: float,
                         min_brightness: float, max_brightness: float = 1) -> np.ndarray:
        """
        Sawtooth brightness (Wegert 2012, p.33):
        g = ⌈x/T⌉ - x/T  gives  descending -> sawtooth
        Used for:
        - Modulus contours: x = log|f|, contour lines at |f| = eⁿ
        - Phase contours:   x = arg(f), isochromatic lines per cycle
        Note: using np.floor gives ascending -> sawtooth (empet convention),
        which is visually equivalent but with inverted shading direction.
        """
        scaled = x / period
        frac_part = np.ceil(scaled) - scaled   # Wegert
        # frac_part = scaled - np.floor(scaled) # empet / ascending
        return min_brightness + (max_brightness - min_brightness) * frac_part

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
        plot_type: PlotType = "pure_phase_portrait",
        cmap_color: str = "hsv",
        brightness: float = 0.7,
        num_lines: int = 3,
        poincare_disk: bool = False,
        show_axes: bool = True
    ) -> Figure:
        """
        Creates an enhanced phase portrait (style of Elias Wegert).

        The portrait combines:
        - Phase portraits coloring (from Matplotlib colormaps)
        - Modulus and phase contours, number of contour lines
        - Optional shading (controlled by brightness)
        - Optional Poincaré disk masking

        Parameters
        ----------
        figsize : tuple[float, float], default=(8, 8)
            Size of the figure (width, height in inches).
        plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours',            'enhanced_phase_portrait'},  default='pure_phase_portrait'
            Type of plot to generate.
        cmap_color : str, default='hsv'
            Colormap used for phase coloring.
        brightness : float, default=0.7
            Base brightness for contour shading (range 0-1).
        num_lines : int, default=3
            Number of contour lines for phase and modulus.
        poincare_disk : bool, default=False
            If True, applies a Poincaré disk mask to the plot.
        show_axes : bool, default=True
            If True, displays axes on the plot.

        Returns
        -------
        matplotlib.figure.Figure
            Matplotlib figure object containing the enhanced phase portrait.
        """
        fig, ax = plt.subplots(figsize=figsize)

        rgb_land = self._build_rgb_wegert(
            plot_type=plot_type, cmap_color=cmap_color, num_lines=num_lines, brightness=brightness)

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

    def _build_rgb_wegert(
        self,
        plot_type: PlotType,
        cmap_color: str = "hsv",
        brightness: float = 0.7,
        num_lines: int = 3,
    ) -> np.ndarray:
        """
        Build the RGB image of the phase portrait.
        Adapted from empet's domain coloring implementation [1],
        extended to support arbitrary Matplotlib colormaps beyond HSV.

        - If cmap_color == 'hsv': uses the HSV color space (Wegert),
        modulating the V channel for contours. More precise.
        - Any other colormap: applies the Matplotlib colormap
        to the normalized phase, then multiplies the contours
        over the resulting RGB.
        References
        ----------
        [1] empet, "Domain Coloring", nbviewer.org/github/empet/Math/
            blob/master/DomainColoring.ipynb
        """
        if cmap_color == "hsv":
            H = self._phase_normalized
            S = 0.9 * np.ones_like(H)
            V_mod = self._compute_modulus_contours(brightness, num_lines)
            V_phase = self._compute_phase_contours(brightness, num_lines)

            V = {
                "pure_phase_portrait":    np.ones_like(H),
                "modulus_contours":       V_mod,
                "phase_contours":         V_phase,
                "enhanced_phase_portrait": V_mod * V_phase,
            }.get(plot_type)

            if V is None:
                raise ValueError(f"plot_type inválido: '{plot_type}'")

            return hsv_to_rgb(np.dstack([H, S, V]))

        else:
           # Arbitrary colormap: twilight, viridis, plasma, cividis, etc.
            rgb = plt.colormaps[cmap_color](self._phase_normalized)[..., :3]

            # Contours applied as multiplicative modulation over RGB
            V_mod = self._compute_modulus_contours(brightness, num_lines)
            V_phase = self._compute_phase_contours(brightness, num_lines)

            factor = {
                "pure_phase_portrait":     np.ones(self._phase_normalized.shape),
                "modulus_contours":        V_mod,
                "phase_contours":          V_phase,
                "enhanced_phase_portrait": V_mod * V_phase,
            }.get(plot_type)

            if factor is None:
                raise ValueError(f"plot_type inválido: '{plot_type}'")
            # Plot combinations
            # RGB * B_mod * B_phase | RGB * B_mod | RGB * B_phase | RGB
            return np.clip(rgb * factor[..., None], 0, 1)
