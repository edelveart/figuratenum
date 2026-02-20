import pytest
from figuratenum import SpaceFigurateNum
from figuratenum import NumCollector as nc
from figuratenum.figurate_viz import PowerSeriesExpansion


pfgn = SpaceFigurateNum()

n_terms = 35

space = PowerSeriesExpansion()


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_m_pyramidal_series(dual_method):
    expected = nc.take_to_list(pfgn.m_pyramidal(3), n_terms)
    result = space.expand_space_series(
        'm_pyramidal', m=3,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_tetrahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.tetrahedral(), n_terms)
    result = space.expand_space_series(
        'tetrahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_cubic_series(dual_method):
    expected = nc.take_to_list(pfgn.cubic(), n_terms)
    result = space.expand_space_series(
        'cubic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_octahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.octahedral(), n_terms)
    result = space.expand_space_series(
        'octahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hauy_octahedral_series(dual_method):
    pass


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_icosahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.icosahedral(), n_terms)
    result = space.expand_space_series(
        'icosahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_dodecahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.dodecahedral(), n_terms)
    result = space.expand_space_series(
        'dodecahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_tetrahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_tetrahedral(), n_terms)
    result = space.expand_space_series(
        'truncated_tetrahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_cubic_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_cubic(), n_terms)
    result = space.expand_space_series(
        'truncated_cubic', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_truncated_octahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.truncated_octahedral(), n_terms)
    result = space.expand_space_series(
        'truncated_octahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_stella_octangula_series(dual_method):
    expected = nc.take_to_list(pfgn.stella_octangula(), n_terms)
    result = space.expand_space_series(
        'stella_octangula', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_cube_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_cube(), n_terms)
    result = space.expand_space_series(
        'centered_cube', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_rhombic_dodecahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.rhombic_dodecahedral(), n_terms)
    result = space.expand_space_series(
        'rhombic_dodecahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_hauy_rhombic_dodecahedral_series(dual_method):
    expected = nc.take_to_list(pfgn.hauy_rhombic_dodecahedral(), n_terms)
    result = space.expand_space_series(
        'hauy_rhombic_dodecahedral', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_tetrahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_tetrahedron(), n_terms)
    result = space.expand_space_series(
        'centered_tetrahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_square_pyramid_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_square_pyramid(), n_terms)
    result = space.expand_space_series(
        'centered_square_pyramid', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_pentagonal_pyramid_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_pentagonal_pyramid(), n_terms)
    result = space.expand_space_series(
        'centered_pentagonal_pyramid', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_hexagonal_pyramid_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_hexagonal_pyramid(), n_terms)
    result = space.expand_space_series(
        'centered_hexagonal_pyramid', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_mgonal_pyramid_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_mgonal_pyramid(9), n_terms)
    result = space.expand_space_series(
        'centered_mgonal_pyramid', m=9,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_octahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_octahedron(), n_terms)
    result = space.expand_space_series(
        'centered_octahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_icosahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_icosahedron(), n_terms)
    result = space.expand_space_series(
        'centered_icosahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_dodecahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_dodecahedron(), n_terms)
    result = space.expand_space_series(
        'centered_dodecahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_truncated_tetrahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_truncated_tetrahedron(), n_terms)
    result = space.expand_space_series(
        'centered_truncated_tetrahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_truncated_cube_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_truncated_cube(), n_terms)
    result = space.expand_space_series(
        'centered_truncated_cube', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_truncated_octahedron_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_truncated_octahedron(), n_terms)
    result = space.expand_space_series(
        'centered_truncated_octahedron', n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_centered_mgonal_pyramidal_series(dual_method):
    expected = nc.take_to_list(pfgn.centered_mgonal_pyramidal(11), n_terms)
    result = space.expand_space_series(
        'centered_mgonal_pyramidal', m=11, n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected


@pytest.mark.parametrize("dual_method", ["symbolic", "numeric"])
def test_mgonal_prism_series(dual_method):
    expected = nc.take_to_list(pfgn.mgonal_prism(7), n_terms)
    result = space.expand_space_series(
        'mgonal_prism', m=7,  n_terms=n_terms+1, coeffs=True, method=dual_method)
    assert result == expected
