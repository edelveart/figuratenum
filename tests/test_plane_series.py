import pytest
from figuratenum import PlaneFigurateNum
from figuratenum import NumCollector as nc
from figuratenum.figurate_viz import PowerSeriesExpansion

pfgn = PlaneFigurateNum()

n_terms = 35

plane = PowerSeriesExpansion()


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_triangular_series(dual_method):
    expected = nc.take_to_list(pfgn.triangular(), n_terms)
    result = plane.expand_plane_series(
        'triangular', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_square_series(dual_method):
    expected = nc.take_to_list(pfgn.square(), n_terms)
    result = plane.expand_plane_series(
        'square', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_pentagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.pentagonal(), n_terms)
    result = plane.expand_plane_series(
        'pentagonal', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hexagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.hexagonal(), n_terms)
    result = plane.expand_plane_series(
        'hexagonal', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_mgonal_series(dual_method):
    m_sides = 9
    expected = nc.take_to_list(pfgn.centered_mgonal(m=m_sides), n_terms)
    result = plane.expand_plane_series(
        'centered_mgonal', m=m_sides, n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polygonal_series(dual_method):
    m_sides = 17
    expected = nc.take_to_list(pfgn.polygonal(m=m_sides), n_terms)
    result = plane.expand_plane_series(
        'polygonal', m=m_sides,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_pronic_series(dual_method):
    expected = nc.take_to_list(pfgn.pronic(), n_terms)
    result = plane.expand_plane_series(
        'pronic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_gnomonic_series(dual_method):
    expected = nc.take_to_list(pfgn.gnomonic(), n_terms)
    result = plane.expand_plane_series(
        'gnomonic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_triangular_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_triangular(), n_terms)

    result = plane.expand_plane_series(
        'truncated_triangular', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_square_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_square(), n_terms)
    result = plane.expand_plane_series(
        'truncated_square', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_pronic_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_pronic(), n_terms)
    result = plane.expand_plane_series(
        'truncated_pronic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_mgonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_mgonal(11), n_terms)
    result = plane.expand_plane_series(
        'truncated_centered_mgonal', m=11, n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_square_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_square(), n_terms)
    result = plane.expand_plane_series(
        'truncated_centered_square', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_pentagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_pentagonal(), n_terms)
    result = plane.expand_plane_series(
        'truncated_centered_pentagonal', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_hexagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_hexagonal(), n_terms)
    result = plane.expand_plane_series(
        'truncated_centered_hexagonal', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polygram_series(dual_method):
    m_sides = 12
    expected = nc.take_to_list(pfgn.polygram(m_sides), n_terms)
    result = plane.expand_plane_series(
        'polygram', m=m_sides,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_aztec_diamond_series(dual_method):
    expected = nc.take_to_list(pfgn.aztec_diamond(), n_terms)
    result = plane.expand_plane_series(
        'aztec_diamond', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_cross_series(dual_method):
    expected = nc.take_to_list(pfgn.cross(), n_terms)
    result = plane.expand_plane_series(
        'cross', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_diamond_series(dual_method):
    expected = nc.take_to_list(pfgn.diamond(), n_terms)
    result = plane.expand_plane_series(
        'diamond', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_square_triangular_series(dual_method):
    pass
