import pytest
from src.figuratenum.multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
from src.figuratenum.figurate_viz.MultiDimCViz import MultiDimCViz


pfgn = MultidimensionalFigurateNum()

n = 20


# 4D
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypertetrahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hypertetrahedral(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'hypertetrahedral', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypercube_series(dual_method):
    expected = nc.take_to_list(pfgn.hypercube(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'hypercube', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hyperoctahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hyperoctahedral(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'hyperoctahedral', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypericosahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hypericosahedral(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'hypericosahedral', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hyperdodecahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hyperdodecahedral(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'hyperdodecahedral', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polyoctahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.polyoctahedral(), n)
    multidim = MultiDimCViz(m=3, k=5)
    result = multidim.expand_series(
        'polyoctahedral', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


# K-Dimensional
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.k_dimensional_hypertetrahedron(24), n)
    multidim = MultiDimCViz(m=3, k=24)
    result = multidim.expand_series(
        'k_dim_hypertetrahedron', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hypercube_series(dual_method):
    expected = nc.take_to_list(pfgn.k_dimensional_hypercube(6), n)
    multidim = MultiDimCViz(m=3, k=6)
    result = multidim.expand_series(
        'k_dim_hypercube', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.k_dimensional_hyperoctahedron(27), n)
    multidim = MultiDimCViz(m=3, k=27)
    result = multidim.expand_series(
        'k_dim_hyperoctahedron', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_nexus_series(dual_method):
    expected = nc.take_to_list(pfgn.nexus(4), n)
    multidim = MultiDimCViz(m=3, k=4)
    result = multidim.expand_series(
        'k_dim_nexus', n_terms=n+1, coeffs=True, method=dual_method
    )
    assert result == expected


# 4D Pyramidal
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_four_dimensional_mgonal_pyramidal_series(dual_method):
    expected = nc.take_to_list(
        pfgn.four_dimensional_mgonal_pyramidal(m=93), n)
    multidim = MultiDimCViz(m=93, k=5)
    result = multidim.expand_series(
        'four_dim_mgonal_pyramidal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


# K-Dimensional Pyramidal
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dimensional_mgonal_pyramidal_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_mgonal_pyramidal(k=17, m=9), n)
    multidim = MultiDimCViz(m=9, k=17)
    result = multidim.expand_series(
        'k_dim_mgonal_pyramidal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


# 4D Centered
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_biquadratic_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_biquadratic(), n)
    multidim = MultiDimCViz(m=4, k=1)
    result = multidim.expand_series(
        'centered_biquadratic', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_polytope(), n)
    multidim = MultiDimCViz(m=4, k=1)
    result = multidim.expand_series(
        'centered_hypertetrahedron', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_hyperoctahedral(), n)
    multidim = MultiDimCViz(m=4, k=1)
    result = multidim.expand_series(
        'centered_hyperoctahedron', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


# K-Dimensional Centered
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hypercube_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hypercube(5), n)
    multidim = MultiDimCViz(m=4, k=5)
    result = multidim.expand_series(
        'k_dim_centered_hypercube', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hypertetrahedron(42), n)
    multidim = MultiDimCViz(m=4, k=42)
    result = multidim.expand_series(
        'k_dim_centered_hypertetrahedron', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hyperoctahedron(51), n)
    multidim = MultiDimCViz(m=4, k=51)
    result = multidim.expand_series(
        'k_dim_centered_hyperoctahedron', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected
