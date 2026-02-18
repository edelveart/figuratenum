import pytest
from src.figuratenum.plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
from src.figuratenum.figurate_viz.SeriesExpansion import PowerSeriesExpansion

pfgn = PlaneFigurateNum()

n = 20


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_triangular_series(dual_method):
    expected = nc.take_to_list(pfgn.triangular(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'triangular', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_square_series(dual_method):
    expected = nc.take_to_list(pfgn.square(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'square', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_pentagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.pentagonal(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'pentagonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hexagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.hexagonal(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'hexagonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_mgonal_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_mgonal(9), n)
    plane = PowerSeriesExpansion(m=9)
    result = plane.expand_plane_series(
        'centered_mgonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polygonal_series(dual_method):
    expected = nc.take_to_list(pfgn.polygonal(17), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'polygonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_pronic_series(dual_method):
    expected = nc.take_to_list(pfgn.pronic(), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'pronic', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_gnomonic_series(dual_method):
    expected = nc.take_to_list(pfgn.gnomonic(), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'gnomonic', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_triangular_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_triangular(), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'truncated_triangular', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_square_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_square(), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'truncated_square', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_pronic_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_pronic(), n)
    plane = PowerSeriesExpansion(m=17)
    result = plane.expand_plane_series(
        'truncated_pronic', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_mgonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_mgonal(11), n)
    plane = PowerSeriesExpansion(m=11)
    result = plane.expand_plane_series(
        'truncated_centered_mgonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_square_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_square(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'truncated_centered_square', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_pentagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_pentagonal(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'truncated_centered_pentagonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_centered_hexagonal_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_centered_hexagonal(), n)
    plane = PowerSeriesExpansion(m=3)
    result = plane.expand_plane_series(
        'truncated_centered_hexagonal', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_polygram_series(dual_method):
    expected = nc.take_to_list(pfgn.polygram(12), n)
    plane = PowerSeriesExpansion(m=12)
    result = plane.expand_plane_series(
        'polygram', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_aztec_diamond_series(dual_method):
    expected = nc.take_to_list(pfgn.aztec_diamond(), n)
    plane = PowerSeriesExpansion(m=12)
    result = plane.expand_plane_series(
        'aztec_diamond', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_cross_series(dual_method):
    expected = nc.take_to_list(pfgn.cross(), n)
    plane = PowerSeriesExpansion(m=12)
    result = plane.expand_plane_series(
        'cross', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_diamond_series(dual_method):
    expected = nc.take_to_list(pfgn.diamond(), n)
    plane = PowerSeriesExpansion(m=12)
    result = plane.expand_plane_series(
        'diamond', n_terms=n+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_square_triangular_series(dual_method):
    pass
