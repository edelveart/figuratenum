from .GaussianPlots import GaussianPlots

from ..plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from ..space_figurate_numbers.SpaceFigurateNum import SpaceFigurateNum
from ..multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum


class DiscreteViz:
    """
    Visualizes figurate numbers in a discrete, customizable 2D layout.

    Generates circular 2D plots of figurate number sequences, where each number
    is represented as a point arranged along a circle. These can be seen as
    geometric or visual “multiplication tables,” showing numeric patterns
    through spatial arrangements. Customization includes colors, background,
    text annotations, rotation, and more.

    Inspired by an expository article by J. Rogelio Pérez Buendía.
    """

    def __init__(self, fig_sequence: list[int] | tuple[int, ...] = [], figsize: tuple[float, float] = (6, 6)):
        self.fig_sequence = fig_sequence
        self.figsize = figsize

    def _generate_sequence_from_class(self, seq_type: str,  figure_name: str, *args,  n_terms: int):
        if seq_type == "Plane":
            seq_loop = PlaneFigurateNum()
        elif seq_type == "Space":
            seq_loop = SpaceFigurateNum()
        elif seq_type == "MultiDim":
            seq_loop = MultidimensionalFigurateNum()
        else:
            raise ValueError(f"Unknown sequence type: {seq_type}")

        # Validate
        if not hasattr(seq_loop, figure_name):
            raise ValueError(
                f"'{figure_name}' method not found in {seq_type} class")

        # Call to method passing *args (future maybe only **kwargs)
        method = getattr(seq_loop, figure_name)
        gen = method(*args)

        return [next(gen) for _ in range(n_terms)]

    def _get_valid_figuratenum_methods(
        self, figurate_name,
            figClass: PlaneFigurateNum | SpaceFigurateNum | MultidimensionalFigurateNum
    ):
        valid_methods = [
            func for func in dir(figClass)
            if callable(getattr(figClass, func))
            and not func.startswith("__")
        ]

        if figurate_name not in valid_methods:
            raise ValueError(
                f"'{figurate_name}' is not a valid method. "
                f"Available methods: {valid_methods}"
            )

    def visualize_plane(self, figurate_name: str, *args, n_terms: int, show=True, **kwargs):
        self._get_valid_figuratenum_methods(figurate_name, PlaneFigurateNum())

        plane_seq = self._generate_sequence_from_class(
            "Plane", figurate_name, *args,  n_terms=n_terms)

        return GaussianPlots(plane_seq, self.figsize, **kwargs).draw(show=show)

    def visualize_space(self, figurate_name, *args, n_terms: int, show=True, **kwargs):
        self._get_valid_figuratenum_methods(figurate_name, SpaceFigurateNum())

        space = self._generate_sequence_from_class(
            "Space", figurate_name, *args, n_terms=n_terms)

        return GaussianPlots(space, self.figsize, **kwargs).draw(show=show)

    def visualize_multidim(self, figurate_name, *args,  n_terms: int, show=True, **kwargs):
        self._get_valid_figuratenum_methods(
            figurate_name, MultidimensionalFigurateNum())

        multidim = self._generate_sequence_from_class(
            "MultiDim",  figurate_name, *args,  n_terms=n_terms)

        return GaussianPlots(multidim, self.figsize, **kwargs).draw(show=show)

    def gaussian_plot(self, circ_color="g", bg_color: str = "k",
                      num_text: bool = False, num_color: str = "g",
                      rotate: int = 0, ext_circle: bool = False,
                      h_modulo: int | None = None) -> GaussianPlots:

        return GaussianPlots(self.fig_sequence, self.figsize, circ_color, bg_color, num_text,
                             num_color, rotate, ext_circle, h_modulo)

    def export_plot(self, filepath: str = "output.svg",
                    circ_color: str = "g",
                    bg_color: str = "k",
                    num_text: bool = False,
                    num_color: str = "g",
                    rotate: int = 0,
                    ext_circle: bool = False,
                    h_modulo: int | None = None,
                    **save_kwargs):
        plot = self.gaussian_plot(
            circ_color=circ_color,
            bg_color=bg_color,
            num_text=num_text,
            num_color=num_color,
            rotate=rotate,
            ext_circle=ext_circle,
            h_modulo=h_modulo
        )
        plot.draw(show=False)
        plot.save(filename=filepath, **save_kwargs)
