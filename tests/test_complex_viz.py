# Run with:
# python -m pytest tests/test_complex_viz.py

from figuratenum.figurate_viz import ComplexViz
from figuratenum.db_figuratenum.PlaneSchema import PlaneTypes
from figuratenum.db_figuratenum.SpaceSchema import SpaceTypes
from figuratenum.db_figuratenum.MultiDimSchema import MultiDimTypes
from matplotlib.figure import Figure
import pytest
import numpy as np


import matplotlib
# Use a non-interactive backend for testing.
# Phase portraits of figurate number generating functions f(z) are rendered
# in the complex plane, but automated tests should not open GUI windows.
matplotlib.use("Agg")


@pytest.fixture
def portrait():
    """Create a ComplexViz instance with standard test parameters."""
    return ComplexViz(m=4, k=5, figsize=(8, 8), resolution=800)


# --------------------
# Visualization tests
# --------------------
plane_seqs_list: list[PlaneTypes] = [
    "cross", "triangular", "diamond", "polygonal"
]
space_seqs_list: list[SpaceTypes] = [
    "centered_icosahedron", "dodecahedral", "m_pyramidal"
]
multidim_seqs_list: list[MultiDimTypes] = [
    "hypertetrahedral", "four_dim_mgonal_pyramidal", "k_dim_mgonal_pyramidal"
]


METHOD_NAME_SEQ_LIST = "method_name, seq_list"


@pytest.mark.parametrize(
    METHOD_NAME_SEQ_LIST,
    [
        ("visualize_plane", plane_seqs_list),
        ("visualize_space", space_seqs_list),
        ("visualize_multidim", multidim_seqs_list),
    ],
)
def test_visualizations(portrait, method_name, seq_list):
    """
    Test that phase portraits are generated correctly for all figurate number sequences.

    All visualization tests use `show=False` to prevent opening interactive windows.
    We only verify that a valid matplotlib Figure is returned for each
    figurate number generating function f(z) in the complex plane.

    Parameters
    ----------
    portrait : ComplexViz
        Instance of the ComplexViz class.
    method_name : str
        Name of the visualization method ('visualize_plane', 'visualize_space', or 'visualize_multidim').
    seq_list : list[str]
        List of sequence names corresponding to the method being tested.
    """
    method = getattr(portrait, method_name)

    for seq_name in seq_list:
        fig = method(seq_name, show=False)
        assert isinstance(fig, Figure)


# -------------
# Invalid input
# -------------
def test_invalid_radius(portrait):
    with pytest.raises(ValueError):
        portrait.visualize_plane("aztec_diamond", radius=-3)


def test_invalid_limits(portrait):
    with pytest.raises(ValueError):
        portrait.visualize_space("cubic", xlim=(5, -5))


def test_get_evaluator_fz(portrait):
    evaluator = portrait._get_evaluator_fz("triangular")
    z = np.array([0.5, 1.0, 1.5, 2, 2.5, 3])  # 1.0 may cause division by zero
    """
    Many generating functions f(z) of figurate numbers have poles at z=1.
    Division by zero is mathematically expected behavior,
    so we suppress NumPy warnings only for testing purposes.
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        result = evaluator(z)
        result = np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)

    assert isinstance(result, np.ndarray)
    assert result.shape == (6,)
    assert not np.any(np.isnan(result))
    assert not np.any(np.isinf(result))


@pytest.mark.parametrize("invalid_seq", ["rectangle", "quadratic_field", ""])
def test_invalid_plane_sequence(portrait, invalid_seq):
    """
    Verify that passing an invalid PlaneTypes sequence raises a ValueError.
    """
    with pytest.raises(ValueError):
        portrait.visualize_plane(invalid_seq, show=False)


@pytest.mark.parametrize("invalid_seq", ["3489", "sphere", "_"])
def test_invalid_space_sequence(portrait, invalid_seq):
    """
    Verify that passing an invalid SpaceTypes sequence raises a ValueError.
    """
    with pytest.raises(ValueError):
        portrait.visualize_space(invalid_seq, show=False)


@pytest.mark.parametrize("invalid_seq", ["98 -.", "@", "trochoid"])
def test_invalid_multidim_sequence(portrait, invalid_seq):
    """
    Verify that passing an invalid MultiDimTypes sequence raises a ValueError.
    """
    with pytest.raises(ValueError):
        portrait.visualize_multidim(invalid_seq, show=False)
