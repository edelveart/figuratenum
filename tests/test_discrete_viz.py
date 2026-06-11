import pytest

from figuratenum import FigurateNum
from figuratenum.figurate_viz import FigurateViz, DiscreteViz
from matplotlib.figure import Figure
import matplotlib
# Use a non-interactive backend for testing.
matplotlib.use("Agg")

fgn = FigurateNum()


def test_figurate_viz_init():
    num_generator = fgn.hexagonal()
    fig_sequence = [next(num_generator) for _ in range(700)]
    fig_viz = FigurateViz(fig_sequence, figsize=(6, 6))

    assert fig_viz.fig_sequence == fig_sequence
    assert fig_viz.figsize == (6, 6)

# --------
# New API
# --------


def test_plane_discreteviz_triangular():
    viz = DiscreteViz()
    fig = viz.visualize_plane(
        "triangular", n_terms=100, show=False, circ_color='r')
    assert isinstance(fig, Figure)


def test_plane_discreteviz_centered_mgonal():
    viz = DiscreteViz()
    fig = viz.visualize_plane("centered_mgonal", m=5, n_terms=100, show=False)
    assert isinstance(fig, Figure)


def test_space_discreteviz_octahedral():
    viz = DiscreteViz()
    fig = viz.visualize_space("octahedral", n_terms=704, show=False)
    assert isinstance(fig, Figure)


def test_multidim_discreteviz_k_hypercube():
    viz = DiscreteViz()
    fig = viz.visualize_multidim(
        "k_dimensional_hypercube",
        k=9,  n_terms=704, show=False)
    assert isinstance(fig, Figure)


def test_multidim_discreteviz_k_dimensional_mgonal_pyramidal():
    viz = DiscreteViz()
    fig = viz.visualize_multidim(
        "k_dimensional_mgonal_pyramidal",
        k=9, m=126, n_terms=704, show=False)
    assert isinstance(fig, Figure)


def test_invalid_m_or_k():
    viz = DiscreteViz()
    with pytest.raises(ValueError):
        viz.visualize_plane("polygonal", m=1,  n_terms=16)
    with pytest.raises(ValueError):
        viz.visualize_multidim("k_dimensional_hypercube", k=-2, n_terms=16)
