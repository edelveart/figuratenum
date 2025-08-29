from types import ModuleType
from .GaussianPlots import GaussianPlots


class FigurateViz:
    """
    Class for visualizing figurate numbers.

    This class allows you to generate plots of a figurate number sequence using
    2D visualizations. It uses the optional libraries `numpy` and `matplotlib`
    to create the plots. If you want to use the visualization functionality,
    make sure you have these dependencies installed.

    Requires the following optional dependencies:
        - numpy >= 1.23
        - matplotlib >= 3.7

    If you don't need visualization, you can safely ignore this error and continue
    using the basic functionality of the library.
    """

    def __init__(self, fig_sequence: list[int] | tuple[int, ...], figsize: tuple[float, float] = (5, 5)):
        self.fig_sequence = fig_sequence
        self.figsize = figsize
        self._np, self._plt = self._load_viz_dependencies()

    def _load_viz_dependencies(self) -> tuple[ModuleType, ModuleType]:
        try:
            import numpy as np
            import matplotlib.pyplot as plt
            return np, plt
        except ImportError as e:
            raise ImportError(
                "To use FigurateViz, you need to install the optional dependencies. "
                "Please run the following command:\n"
                "pip install figuratenum[figurate-viz]\n"
                "Note: Make sure you have numpy >= 1.23 and matplotlib >= 3.7. "
                "If you don't need visualization, you can safely ignore this error."
            ) from e

    def gaussian_graph(self, circ_color="m", bg_color: str = "w",
                       num_text: bool = False, num_color: str = "k",
                       rotate: int = 0, ext_circle: bool = True,
                       h_modulo: int | None = None) -> GaussianPlots:

        return GaussianPlots(self.fig_sequence, self._np, self._plt,
                             self.figsize, circ_color, bg_color, num_text,
                             num_color, rotate, ext_circle, h_modulo)
