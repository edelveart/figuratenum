from figurate_numbers.space_figurate_numbers import (
    m_pyramidal_numbers, cubic_numbers, tetrahedral_numbers,
    octahedral_numbers, dodecahedral_numbers, icosahedral_numbers,
    truncated_tetrahedral_numbers, truncated_cubic_numbers, truncated_octahedral_numbers,
    stella_octangula_numbers, centered_cube_numbers, rhombic_dodecahedral_numbers,
    hauy_rhombic_dodecahedral_numbers, centered_tetrahedron_numbers,
    centered_square_pyramid_numbers, centered_mgonal_pyramid_numbers,
    centered_octahedron_numbers, centered_icosahedron_numbers, centered_dodecahedron_numbers,
    centered_truncated_tetrahedron_numbers, centered_truncated_cube_numbers, centered_truncated_octahedron_numbers, centered_mgonal_pyramidal_numbers, centered_hexagonal_pyramidal_numbers
)


def test_m_pyramidal_numbers():
    num_generator = m_pyramidal_numbers(8)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 9, 30, 70, 135, 231, 364, 540, 765,
                            1045, 1386, 1794, 2275, 2835, 3480, 4216, 5049, 5985, 7030]


def test_cubic_numbers():
    num_generator = cubic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 27, 64, 125, 216, 343, 512, 729,
                            1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]


def test_tetrahedral_numbers():
    num_generator = tetrahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 4, 10, 20, 35, 56, 84, 120,
                            165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330]


def test_octahedral_numbers():
    num_generator = octahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 19, 44, 85, 146, 231, 344, 489,
                            670, 891, 1156, 1469, 1834, 2255, 2736, 3281, 3894, 4579]


def test_dodecahedral_numbers():
    num_generator = dodecahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 20, 84, 220, 455, 816, 1330, 2024, 2925,
                            4060, 5456, 7140, 9139, 11480, 14190, 17296, 20825, 24804, 29260]


def test_icosahedral_numbers():
    num_generator = icosahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 12, 48, 124, 255, 456, 742, 1128, 1629,
                            2260, 3036, 3972, 5083, 6384, 7890, 9616, 11577, 13788, 16264]


def test_truncated_tetrahedral_numbers():
    num_generator = truncated_tetrahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 68, 180, 375, 676, 1106, 1688, 2445,
                            3400, 4576, 5996, 7683, 9660, 11950, 14576, 17561, 20928, 24700]


def test_truncated_cubic_numbers():
    num_generator = truncated_cubic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 56, 311, 920, 2037, 3816, 6411, 9976, 14665,
                            20632, 28031, 37016, 47741, 60360, 75027, 91896, 111121, 132856, 157255]


def test_truncated_octahedral_numbers():
    num_generator = truncated_octahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 38, 201, 586, 1289, 2406, 4033, 6266, 9201,
                            12934, 17561, 23178, 29881, 37766, 46929, 57466, 69473, 83046, 98281]


def test_stella_octangula_numbers():
    num_generator = stella_octangula_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 14, 51, 124, 245, 426, 679, 1016, 1449,
                            1990, 2651, 3444, 4381, 5474, 6735, 8176, 9809, 11646, 13699]


def test_centered_cube_numbers():
    num_generator = centered_cube_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 9, 35, 91, 189, 341, 559, 855, 1241,
                            1729, 2331, 3059, 3925, 4941, 6119, 7471, 9009, 10745, 12691]


def test_rhombic_dodecahedral_numbers():
    num_generator = rhombic_dodecahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 15, 65, 175, 369, 671, 1105, 1695, 2465,
                            3439, 4641, 6095, 7825, 9855, 12209, 14911, 17985, 21455, 25345]


def test_hauy_rhombic_dodecahedral_numbers():
    num_generator = hauy_rhombic_dodecahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 33, 185, 553, 1233, 2321, 3913, 6105, 8993,
                            12673, 17241, 22793, 29425, 37233, 46313, 56761, 68673, 82145, 97273]


def test_centered_tetrahedron_numbers():
    num_generator = centered_tetrahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 15, 35, 69, 121, 195, 295, 425,
                            589, 791, 1035, 1325, 1665, 2059, 2511, 3025, 3605, 4255]


def test_centered_square_pyramid_numbers():
    num_generator = centered_square_pyramid_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 20, 49, 99, 176, 286, 435, 629,
                            874, 1176, 1541, 1975, 2484, 3074, 3751, 4521, 5390, 6364]


def test_centered_mgonal_pyramid_numbers():
    num_generator = centered_mgonal_pyramid_numbers(14)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 70, 189, 399, 726, 1196, 1835, 2669,
                            3724, 5026, 6601, 8475, 10674, 13224, 16151, 19481, 23240, 27454]


def test_centered_octahedron_numbers():
    num_generator = centered_octahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 7, 25, 63, 129, 231, 377, 575, 833,
                            1159, 1561, 2047, 2625, 3303, 4089, 4991, 6017, 7175, 8473]


def test_centered_icosahedron_numbers():
    num_generator = centered_icosahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 55, 147, 309, 561, 923, 1415, 2057,
                            2869, 3871, 5083, 6525, 8217, 10179, 12431, 14993, 17885, 21127]


def test_centered_dodecahedron_numbers():
    num_generator = centered_dodecahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 95, 259, 549, 1001, 1651, 2535, 3689,
                            5149, 6951, 9131, 11725, 14769, 18299, 22351, 26961, 32165, 37999]


def test_centered_truncated_tetrahedron_numbers():
    num_generator = centered_truncated_tetrahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 17, 75, 203, 429, 781, 1287, 1975, 2873,
                            4009, 5411, 7107, 9125, 11493, 14239, 17391, 20977, 25025, 29563]


def test_centered_truncated_cube_numbers():
    num_generator = centered_truncated_cube_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 49, 235, 651, 1389, 2541, 4199, 6455, 9401,
                            13129, 17731, 23299, 29925, 37701, 46719, 57071, 68849, 82145, 97051]


def test_centered_truncated_octahedron_numbers():
    num_generator = centered_truncated_octahedron_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 33, 155, 427, 909, 1661, 2743, 4215, 6137,
                            8569, 11571, 15203, 19525, 24597, 30479, 37231, 44913, 53585, 63307]


def test_centered_mgonal_pyramidal_numbers():
    num_generator = centered_mgonal_pyramidal_numbers(19)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 79, 194, 385, 671, 1071, 1604, 2289,
                            3145, 4191, 5446, 6929, 8659, 10655, 12936, 15521, 18429, 21679]


def test_centered_hexagonal_pyramidal_numbers():
    num_generator = centered_hexagonal_pyramidal_numbers(19)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 27, 64, 125, 216, 343, 512, 729,
                            1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
