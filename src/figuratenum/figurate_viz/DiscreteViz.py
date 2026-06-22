import inspect

from ..db_figuratenum.validator_helper import Validator
from .ModularPlots import ModularPlots
from ..plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from ..space_figurate_numbers.SpaceFigurateNum import SpaceFigurateNum
from ..multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum


class DiscreteViz:
    """
    Visualizes figurate number sequences as modular orbits in discrete circular space.

    Each term of a sequence is reduced modulo n and mapped to one of n positions
    on a circle. Consecutive terms are connected by edges, tracing an orbit in
    Z/nZ. The resulting pattern exhibits arithmetic periodicity that is not directly evident from the sequence values.

    Inspired by an expository article by J. Rogelio Pérez Buendía (2025).
    """

    def __init__(self, fig_sequence: list[int] | tuple[int, ...] = [], figsize: tuple[float, float] = (6, 6)):
        """
        Initialize a DiscreteViz instance.

        Default configuration for discrete geometric visualizations
        of figurate number sequences.

        Parameters
        ----------
        fig_sequence : list[int] | tuple[int, ...] | None, default=None
            Sequence of integers to visualize. If None, an empty sequence is used.
        figsize : tuple[float, float], default=(6, 6)
            Figure size in inches (width, height).
        """
        self.fig_sequence = fig_sequence
        self.figsize = figsize

    def _generate_sequence_from_class(self, seq_type: str,  name_seq: str, *, m: int | None = None, k: int | None = None,  n_terms: int):
        if seq_type == "Plane":
            seq_loop = PlaneFigurateNum()
        elif seq_type == "Space":
            seq_loop = SpaceFigurateNum()
        elif seq_type == "MultiDim":
            seq_loop = MultidimensionalFigurateNum()
        else:
            raise ValueError(f"Unknown sequence type: {seq_type}")

        # Validate
        if not hasattr(seq_loop, name_seq):
            raise ValueError(
                f"'{name_seq}' method not found in {seq_type} class")

        method = getattr(seq_loop, name_seq)
        sig = inspect.signature(method)

        needs_m = 'm' in sig.parameters
        needs_k = 'k' in sig.parameters

        Validator.validate_m_and_k(
            m=m, k=k, name_seq=name_seq, needs_m=needs_m, needs_k=needs_k)

        call_kwargs = {}
        if needs_m:
            call_kwargs['m'] = m
        if needs_k:
            call_kwargs['k'] = k

        gen = method(**call_kwargs)

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

    def visualize_plane(self, figuratenum_name: str, *, m: int | None = None, n_terms: int, show=True, **kwargs):
        """
        Visualize a plane figurate number sequence in a discrete modular geometry representation.

        This method generates a figurate number sequence and visualizes it using a modular
        polar transformation, producing a geometric pattern based on cyclic connections
        between sequence indices.

        Parameters
        ----------
        figuratenum_name : string
            Name of the plane figurate number sequence.
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        n_terms : int
            Number of terms to generate from the sequence for visualization.
        show : bool, default=True
            Whether to display the plot immediately. If False, the figure is created but not shown.
        **kwargs : dict
            - circ_color : str, default="g"
                Color of the connecting edges in the polar plot.
            - bg_color : str, default="k"
                Background color of the figure.
            - num_text : bool, default=False
                Whether to display numeric labels on the nodes.
            - num_color : str, default="g"
                Color of the numeric labels.
            - rotate : int, default=0
                Rotation offset applied to the sequence mapping.
            - ext_circle : bool, default=False
                Whether to display the outer polar boundary circle.
            - h_modulo : int | None, default=len(sequence)
                Modulo used for circular mapping of the sequence.

        Returns
        -------
        matplotlib.figure.Figure
            The generated modular visualization figure.
            Returned even if `show=True`.
        """
        self._get_valid_figuratenum_methods(
            figuratenum_name, PlaneFigurateNum())

        plane_seq = self._generate_sequence_from_class(
            "Plane", figuratenum_name, m=m, n_terms=n_terms)

        return ModularPlots(plane_seq, self.figsize, **kwargs).draw(show=show)

    def visualize_space(self, figuratenum_name, *, m: int | None = None, n_terms: int, show=True, **kwargs):
        """
        Visualize a space figurate number sequence in a discrete modular geometry representation.

        This method generates a figurate number sequence and visualizes it using a modular
        polar transformation, producing a geometric pattern based on cyclic connections
        between sequence indices.

        Parameters
        ----------
        figuratenum_name : string
            Name of the space figurate number sequence.
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        n_terms : int
            Number of terms to generate from the sequence for visualization.
        show : bool, default=True
            Whether to display the plot immediately. If False, the figure is created but not shown.
        **kwargs : dict
            - circ_color : str, default="g"
                Color of the connecting edges in the polar plot.
            - bg_color : str, default="k"
                Background color of the figure.
            - num_text : bool, default=False
                Whether to display numeric labels on the nodes.
            - num_color : str, default="g"
                Color of the numeric labels.
            - rotate : int, default=0
                Rotation offset applied to the sequence mapping.
            - ext_circle : bool, default=False
                Whether to display the outer polar boundary circle.
            - h_modulo : int | None, default=len(sequence)
                Modulo used for circular mapping of the sequence.

        Returns
        -------
        matplotlib.figure.Figure
            The generated modular visualization figure.
            Returned even if `show=True`.
        """
        self._get_valid_figuratenum_methods(
            figuratenum_name, SpaceFigurateNum())

        space = self._generate_sequence_from_class(
            "Space", figuratenum_name, m=m, n_terms=n_terms)

        return ModularPlots(space, self.figsize, **kwargs).draw(show=show)

    def visualize_multidim(self, figuratenum_name, *, m: int | None = None, k: int | None = None,  n_terms: int, show=True, **kwargs):
        """
        Visualize a multidimensional figurate number sequence in a discrete modular geometry representation.

        This method generates a figurate number sequence and visualizes it using a modular
        polar transformation, producing a geometric pattern based on cyclic connections
        between sequence indices.

        Parameters
        ----------
        figuratenum_name : string
            Name of the multidimensional figurate number sequence.
        m : int | None
            Parameter defining the m-gonal structure (if applicable).
        k : int | None
            Parameter defining the k-dimensional structure (if applicable).
        n_terms : int
            Number of terms to generate from the sequence for visualization.
        show : bool, default=True
            Whether to display the plot immediately. If False, the figure is created but not shown.
        **kwargs : dict
            - circ_color : str, default="g"
                Color of the connecting edges in the polar plot.
            - bg_color : str, default="k"
                Background color of the figure.
            - num_text : bool, default=False
                Whether to display numeric labels on the nodes.
            - num_color : str, default="g"
                Color of the numeric labels.
            - rotate : int, default=0
                Rotation offset applied to the sequence mapping.
            - ext_circle : bool, default=False
                Whether to display the outer polar boundary circle.
            - h_modulo : int | None, default=len(sequence)
                Modulo used for circular mapping of the sequence.

        Returns
        -------
        matplotlib.figure.Figure
            The generated modular visualization figure.
            Returned even if `show=True`.
        """
        self._get_valid_figuratenum_methods(
            figuratenum_name, MultidimensionalFigurateNum())

        multidim = self._generate_sequence_from_class(
            "MultiDim",  figuratenum_name, m=m, k=k,  n_terms=n_terms)

        return ModularPlots(multidim, self.figsize, **kwargs).draw(show=show)
