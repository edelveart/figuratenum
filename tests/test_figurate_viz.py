import pytest
from src.figuratenum.FigurateNum import FigurateNum
from src.figuratenum.figurate_viz.FigurateViz import FigurateViz
from src.figuratenum.figurate_viz.GaussianPlots import GaussianPlots
fgn = FigurateNum()


def test_figurate_viz_init():
    num_generator = fgn.hexagonal()
    fig_sequence = [next(num_generator) for _ in range(700)]
    fig_viz = FigurateViz(fig_sequence, figsize=(6, 6))

    assert fig_viz.fig_sequence == fig_sequence
    assert fig_viz.figsize == (6, 6)


def test_gaussian_graph_default_params():
    length = 500
    num_generator = fgn.cross()
    fig_sequence = [next(num_generator) for _ in range(length)]
    fig_viz = FigurateViz(fig_sequence, figsize=(6, 6))

    gaussian_plot = fig_viz.gaussian_plot()

    assert isinstance(gaussian_plot, GaussianPlots)
    assert gaussian_plot.circ_color == "g"
    assert gaussian_plot.bg_color == "k"
    assert gaussian_plot.num_text is False
    assert gaussian_plot.num_color == "g"
    assert gaussian_plot.rotate == 0
    assert gaussian_plot.ext_circle is False
    assert gaussian_plot.h_modulo == length


def test_gaussian_graph():
    rotate_start_value = -1
    num_generator = fgn.hexagonal()
    fig_sequence = [next(num_generator) for _ in range(20)]
    fig_viz = FigurateViz(fig_sequence, figsize=(8, 8))

    gaussian_plot = fig_viz.gaussian_plot(
        circ_color="m", bg_color="c", num_text=True, num_color="g",
        rotate=rotate_start_value, ext_circle=False)

    assert isinstance(gaussian_plot, GaussianPlots)
    assert gaussian_plot.circ_color == "m"
    assert gaussian_plot.bg_color == "c"
    assert gaussian_plot.num_text is True
    assert gaussian_plot.num_color == "g"
    assert gaussian_plot.rotate == rotate_start_value
    assert gaussian_plot.ext_circle is False


def test_gaussian_graph_h_modulo_error():
    num_generator = fgn.centered_icositetragonal()
    fig_sequence = [next(num_generator) for _ in range(100)]
    fig_viz = FigurateViz(fig_sequence, figsize=(7, 7))

    with pytest.raises(ValueError, match="h_modulo cannot be greater than the length of the sequence"):
        fig_viz.gaussian_plot(
            circ_color="y", bg_color="b", num_text=True, num_color="y",
            rotate=3, ext_circle=False, h_modulo=600)
