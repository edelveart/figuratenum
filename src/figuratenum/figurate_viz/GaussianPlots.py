from types import ModuleType


class GaussianPlots:
    """
    Class to create geometric visualizations of sequences in polar coordinates
    with modular arithmetic. Allows customization of colors, sizes, and settings
    for the visualization.

    Parameters:
        sequence (list[int], tuple[int, ...]): Sequence of numbers to visualize.
        np (module): Numpy module for mathematical operations.
        plt (module): Matplotlib module for visualization.
        figsize (tuple[float, float]): Size of the figure (width, height).
        circ_color (str, optional): Color of the circle lines (default is "m").
        bg_color (str, optional): Background color of the figure (default is "w").
        num_text (bool, optional): Whether to display numbers in the visualization (default is False).
        num_color (str, optional): Color of the numbers (default is "k").
        rotate (int, optional): Rotate the starting point of the sequence in the circular graph (default is 0).
        ext_circle (bool, optional): Whether to show the outer circle (default is True).
        h_modulo (int | None, optional): Modulo of the sequence for visualization (default is len(sequence)).

    Methods:
        draw: Draws the visualization based on the provided parameters.
    """

    def __init__(self, sequence: list[int] | tuple[int, ...],
                 np: ModuleType, plt: ModuleType, figsize: tuple[float, float],
                 circ_color: str = "g", bg_color: str = "k", num_text: bool = False,
                 num_color: str = "g", rotate: int = 0, ext_circle: bool = False,
                 h_modulo: int | None = None):
        self.sequence = sequence
        self.np = np
        self.plt = plt
        self.figsize = figsize
        self.circ_color = circ_color
        self.bg_color = bg_color
        self.num_text = num_text
        self.num_color = num_color
        self.rotate = rotate
        self.ext_circle = ext_circle
        self.h_modulo = h_modulo or len(sequence)

        if self.h_modulo > len(self.sequence):
            raise ValueError(
                "h_modulo cannot be greater than the length of the sequence.")

    def draw(self):
        polar_indices = range(self.h_modulo)
        angles = self.np.linspace(
            0, 2 * self.np.pi, self.h_modulo, endpoint=False)

        self.plt.figure(figsize=self.figsize, facecolor=self.bg_color)
        ax = self.plt.subplot(111, projection='polar')
        ax.set_facecolor(self.bg_color)

        for i in polar_indices:
            result = (self.sequence[i] + self.rotate) % self.h_modulo
            angle1 = angles[i]
            angle2 = angles[result]
            ax.plot([angle1, angle2], [1.1, 1.1],
                    color=self.circ_color, linewidth=0.5)

        if self.num_text:
            for i in polar_indices:
                ax.text(angles[i], 1.105, str(polar_indices[i]),
                        ha='center', va='center', fontsize=8,
                        fontweight='normal', color=self.num_color)

        ax.set_theta_offset(self.np.pi / 2)
        ax.set_theta_direction(-1)

        ax.set_rticks([])
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.spines['polar'].set_visible(self.ext_circle)
        ax.spines['polar'].set_color(self.circ_color)
        ax.set_rmax(1.1)

        self.plt.grid(False)
        self.plt.show()
