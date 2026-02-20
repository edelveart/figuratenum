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
matplotlib.use("Agg")


# -------------
# Manual Tests
# -------------
res = 20


def test_plane_centered_mgonal():
    viz = ComplexViz(figsize=(2, 2), resolution=res*20, brightness=0.4)
    fig = viz.visualize_plane(
        "centered_mgonal", m=5, plot_type="modulus_contours", show=False, show_axes=False, num_lines=5)
    assert isinstance(fig, Figure)


def test_space_centered_mgonal_pyramid():
    viz = ComplexViz(figsize=(1, 3), resolution=res*6)
    fig = viz.visualize_space(
        "centered_mgonal_pyramid", m=19, plot_type="phase_contours", cmap_color="cividis", show=False, poincare_disk=True)
    assert isinstance(fig, Figure)


def test_multidim_k_hypercube():
    viz = ComplexViz(figsize=(2, 1), resolution=res*5, cmap_color="plasma")
    fig = viz.visualize_multidim(
        "k_dim_hypercube", k=34, plot_type="pure_phase_portrait", show=False, brightness=0.2)
    assert isinstance(fig, Figure)


def test_multidim_k_dim_mgonal_pyramidal():
    viz = ComplexViz(figsize=(3, 4), resolution=res*2, num_lines=2)
    fig = viz.visualize_multidim(
        "k_dim_mgonal_pyramidal", m=6, k=10, plot_type="pure_phase_portrait", show=False)
    assert isinstance(fig, Figure)


# --------------
# pytest-fixture
# --------------
@pytest.fixture
def portrait():
    """Create a ComplexViz instance with standard test parameters."""
    return ComplexViz(figsize=(3, 3), resolution=100, plot_type="enhanced_phase_portrait")


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

# List of sequences that require parameters m and/or k
sequences_requiring_params = {
    "polygonal": ["m"],  # Example: polygonal sequence needs m
    "m_pyramidal": ["m"],
    "four_dim_mgonal_pyramidal": ["m"],
    "k_dim_mgonal_pyramidal": ["m", "k"],
}


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
        # Check if the sequence requires parameters like m or k
        if seq_name in sequences_requiring_params:
            params = sequences_requiring_params[seq_name]
            kwargs = {}
            for param in params:
                if param == "m":
                    kwargs["m"] = 5
                elif param == "k":
                    kwargs["k"] = 4

            fig = method(seq_name, show=False, **kwargs)
        else:
            fig = method(seq_name, show=False)
        assert isinstance(fig, Figure)


# # -------------
# # Invalid input
# # -------------
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


def test_invalid_m_or_k(portrait):
    with pytest.raises(ValueError):
        portrait.visualize_plane("polygonal", m=-5)
    with pytest.raises(ValueError):
        portrait.visualize_multidim("k_dim_mgonal_pyramidal", k=0)
