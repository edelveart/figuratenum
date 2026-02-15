from src.figuratenum.space_figurate_numbers.SpaceFigurateNum import SpaceFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
from src.figuratenum.figurate_viz.SpaceCViz import SpaceCViz


pfgn = SpaceFigurateNum()

n = 20


def test_m_pyramidal_series():
    expected = nc.take_to_list(pfgn.m_pyramidal(3), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'm_pyramidal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_tetrahedral_series():
    expected = nc.take_to_list(pfgn.tetrahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'tetrahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_cubic_series():
    expected = nc.take_to_list(pfgn.cubic(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'cubic', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_octahedral_series():
    expected = nc.take_to_list(pfgn.octahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'octahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_hauy_octahedral_series():
    pass


def test_icosahedral_series():
    expected = nc.take_to_list(pfgn.icosahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'icosahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_dodecahedral_series():
    expected = nc.take_to_list(pfgn.dodecahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'dodecahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_tetrahedral_series():
    expected = nc.take_to_list(pfgn.truncated_tetrahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'truncated_tetrahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_cubic_series():
    expected = nc.take_to_list(pfgn.truncated_cubic(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'truncated_cubic', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_truncated_octahedral_series():
    expected = nc.take_to_list(pfgn.truncated_octahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'truncated_octahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_stella_octangula_series():
    expected = nc.take_to_list(pfgn.stella_octangula(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'stella_octangula', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_cube_series():
    expected = nc.take_to_list(pfgn.centered_cube(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_cube', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_rhombic_dodecahedral_series():
    expected = nc.take_to_list(pfgn.rhombic_dodecahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'rhombic_dodecahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_hauy_rhombic_dodecahedral_series():
    expected = nc.take_to_list(pfgn.hauy_rhombic_dodecahedral(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'hauy_rhombic_dodecahedral', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_tetrahedron_series():
    expected = nc.take_to_list(pfgn.centered_tetrahedron(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_tetrahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_square_pyramid_series():
    expected = nc.take_to_list(pfgn.centered_square_pyramid(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_square_pyramid', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_pentagonal_pyramid_series():
    expected = nc.take_to_list(pfgn.centered_pentagonal_pyramid(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_pentagonal_pyramid', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_hexagonal_pyramid_series():
    expected = nc.take_to_list(pfgn.centered_hexagonal_pyramid(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_hexagonal_pyramid', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_mgonal_pyramid_series():
    expected = nc.take_to_list(pfgn.centered_mgonal_pyramid(9), n)
    space = SpaceCViz(m=9)
    result = space.expand_series(
        'centered_mgonal_pyramid', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_octahedron_series():
    expected = nc.take_to_list(pfgn.centered_octahedron(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_octahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_icosahedron_series():
    expected = nc.take_to_list(pfgn.centered_icosahedron(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_icosahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_dodecahedron_series():
    expected = nc.take_to_list(pfgn.centered_dodecahedron(), n)
    space = SpaceCViz(m=3)
    result = space.expand_series(
        'centered_dodecahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_truncated_tetrahedron_series():
    expected = nc.take_to_list(pfgn.centered_truncated_tetrahedron(), n)
    plane = SpaceCViz(m=3)
    result = plane.expand_series(
        'centered_truncated_tetrahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_truncated_cube_series():
    expected = nc.take_to_list(pfgn.centered_truncated_cube(), n)
    plane = SpaceCViz(m=3)
    result = plane.expand_series(
        'centered_truncated_cube', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_truncated_octahedron_series():
    expected = nc.take_to_list(pfgn.centered_truncated_octahedron(), n)
    plane = SpaceCViz(m=3)
    result = plane.expand_series(
        'centered_truncated_octahedron', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_centered_mgonal_pyramidal_series():
    expected = nc.take_to_list(pfgn.centered_mgonal_pyramidal(11), n)
    plane = SpaceCViz(m=11)
    result = plane.expand_series(
        'centered_mgonal_pyramidal', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected


def test_mgonal_prism_series():
    expected = nc.take_to_list(pfgn.mgonal_prism(7), n)
    plane = SpaceCViz(m=7)
    result = plane.expand_series(
        'mgonal_prism', n_terms=n+1, coeffs=True, method='numeric')
    assert result == expected
