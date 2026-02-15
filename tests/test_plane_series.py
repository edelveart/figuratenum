from src.figuratenum.plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
from src.figuratenum.figurate_viz.PlaneCViz import PlaneCViz


pfgn = PlaneFigurateNum()

n = 20


def test_triangular_series():
    expected = nc.take_to_list(pfgn.triangular(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'triangular', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_square_series():
    expected = nc.take_to_list(pfgn.square(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'square', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_pentagonal_series():
    expected = nc.take_to_list(pfgn.pentagonal(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'pentagonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_hexagonal_series():
    expected = nc.take_to_list(pfgn.hexagonal(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'hexagonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_mgonal_series():
    expected = nc.take_to_list(pfgn.centered_mgonal(9), n)
    plane = PlaneCViz(m=9)
    result = plane.expand_series(
        'centered_mgonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_polygonal_series():
    expected = nc.take_to_list(pfgn.polygonal(17), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'polygonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_pronic_series():
    expected = nc.take_to_list(pfgn.pronic(), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'pronic', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_gnomonic_series():
    expected = nc.take_to_list(pfgn.gnomonic(), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'gnomonic', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_triangular_series():
    expected = nc.take_to_list(pfgn.truncated_triangular(), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'truncated_triangular', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_square_series():
    expected = nc.take_to_list(pfgn.truncated_square(), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'truncated_square', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_pronic_series():
    expected = nc.take_to_list(pfgn.truncated_pronic(), n)
    plane = PlaneCViz(m=17)
    result = plane.expand_series(
        'truncated_pronic', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_centered_mgonal_series():
    expected = nc.take_to_list(pfgn.truncated_centered_mgonal(11), n)
    plane = PlaneCViz(m=11)
    result = plane.expand_series(
        'truncated_centered_mgonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_centered_square_series():
    expected = nc.take_to_list(pfgn.truncated_centered_square(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'truncated_centered_square', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_centered_pentagonal_series():
    expected = nc.take_to_list(pfgn.truncated_centered_pentagonal(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'truncated_centered_pentagonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_centered_hexagonal_series():
    expected = nc.take_to_list(pfgn.truncated_centered_hexagonal(), n)
    plane = PlaneCViz(m=3)
    result = plane.expand_series(
        'truncated_centered_hexagonal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_polygram_series():
    expected = nc.take_to_list(pfgn.polygram(12), n)
    plane = PlaneCViz(m=12)
    result = plane.expand_series(
        'polygram', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_aztec_diamond_series():
    expected = nc.take_to_list(pfgn.aztec_diamond(), n)
    plane = PlaneCViz(m=12)
    result = plane.expand_series(
        'aztec_diamond', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_cross_series():
    expected = nc.take_to_list(pfgn.cross(), n)
    plane = PlaneCViz(m=12)
    result = plane.expand_series(
        'cross', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_diamond_series():
    expected = nc.take_to_list(pfgn.diamond(), n)
    plane = PlaneCViz(m=12)
    result = plane.expand_series(
        'diamond', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_square_triangular_series():
    pass
