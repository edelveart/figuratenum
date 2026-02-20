import pytest
from figuratenum import MultidimensionalFigurateNum
from figuratenum import NumCollector as nc
from figuratenum.figurate_viz import PowerSeriesExpansion


pfgn = MultidimensionalFigurateNum()
multidim = PowerSeriesExpansion()

n_terms = 20


# 4D
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypertetrahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hypertetrahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'hypertetrahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypercube_series(dual_method):
    expected = nc.take_to_list(pfgn.hypercube(), n_terms)
    result = multidim.expand_multidim_series(
        'hypercube', n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hyperoctahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hyperoctahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'hyperoctahedral', n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hypericosahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hypericosahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'hypericosahedral', n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hyperdodecahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hyperdodecahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'hyperdodecahedral', n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polyoctahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.polyoctahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'polyoctahedral', n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


# K-Dimensional
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_hypertetrahedron(24), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_hypertetrahedron', k=24,  n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hypercube_series(dual_method):
    expected = nc.take_to_list(pfgn.k_dimensional_hypercube(6), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_hypercube', k=6, n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.k_dimensional_hyperoctahedron(27), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_hyperoctahedron', k=27, n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_nexus_series(dual_method):
    expected = nc.take_to_list(pfgn.nexus(4), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_nexus', k=4,  n_terms=n_terms+1, coeffs=True, method=dual_method
    )
    assert result == expected


# 4D Pyramidal
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_four_dimensional_mgonal_pyramidal_series(dual_method):
    expected = nc.take_to_list(
        pfgn.four_dimensional_mgonal_pyramidal(m=93), n_terms)
    result = multidim.expand_multidim_series(
        'four_dim_mgonal_pyramidal', m=93,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


# K-Dimensional Pyramidal
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dimensional_mgonal_pyramidal_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_mgonal_pyramidal(k=17, m=9), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_mgonal_pyramidal', k=17, m=9,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


# 4D Centered
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_biquadratic_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_biquadratic(), n_terms)
    result = multidim.expand_multidim_series(
        'centered_biquadratic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_polytope(), n_terms)
    result = multidim.expand_multidim_series(
        'centered_hypertetrahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.centered_hyperoctahedral(), n_terms)
    result = multidim.expand_multidim_series(
        'centered_hyperoctahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


# K-Dimensional Centered
@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hypercube_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hypercube(5), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_centered_hypercube', k=5, n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hypertetrahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hypertetrahedron(42), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_centered_hypertetrahedron', k=42, n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_k_dim_centered_hyperoctahedron_series(dual_method):
    expected = nc.take_to_list(
        pfgn.k_dimensional_centered_hyperoctahedron(51), n_terms)
    result = multidim.expand_multidim_series(
        'k_dim_centered_hyperoctahedron', k=51,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected
