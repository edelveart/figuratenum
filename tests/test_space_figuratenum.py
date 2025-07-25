# python -m pytest tests/test_space_figuratenum.py

from src.figuratenum.space_figurate_numbers.SpaceFigurateNum import SpaceFigurateNum

sfgn = SpaceFigurateNum()


def test_m_pyramidal():
    num_generator = sfgn.m_pyramidal(8)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 9, 30, 70, 135, 231, 364, 540, 765,
                            1045, 1386, 1794, 2275, 2835, 3480, 4216, 5049, 5985, 7030]


def test_cubic():
    num_generator = sfgn.cubic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 27, 64, 125, 216, 343, 512, 729,
                            1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]


def test_tetrahedral():
    num_generator = sfgn.tetrahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 4, 10, 20, 35, 56, 84, 120,
                            165, 220, 286, 364, 455, 560, 680, 816, 969, 1140, 1330]


def test_octahedral():
    num_generator = sfgn.octahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 19, 44, 85, 146, 231, 344, 489,
                            670, 891, 1156, 1469, 1834, 2255, 2736, 3281, 3894, 4579]


def test_dodecahedral():
    num_generator = sfgn.dodecahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 20, 84, 220, 455, 816, 1330, 2024, 2925,
                            4060, 5456, 7140, 9139, 11480, 14190, 17296, 20825, 24804, 29260]


def test_icosahedral():
    num_generator = sfgn.icosahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 12, 48, 124, 255, 456, 742, 1128, 1629,
                            2260, 3036, 3972, 5083, 6384, 7890, 9616, 11577, 13788, 16264]


def test_truncated_tetrahedral():
    num_generator = sfgn.truncated_tetrahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 68, 180, 375, 676, 1106, 1688, 2445,
                            3400, 4576, 5996, 7683, 9660, 11950, 14576, 17561, 20928, 24700]


def test_truncated_cubic():
    num_generator = sfgn.truncated_cubic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 56, 311, 920, 2037, 3816, 6411, 9976, 14665,
                            20632, 28031, 37016, 47741, 60360, 75027, 91896, 111121, 132856, 157255]


def test_truncated_octahedral():
    num_generator = sfgn.truncated_octahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 38, 201, 586, 1289, 2406, 4033, 6266, 9201,
                            12934, 17561, 23178, 29881, 37766, 46929, 57466, 69473, 83046, 98281]


def test_stella_octangula():
    num_generator = sfgn.stella_octangula()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 14, 51, 124, 245, 426, 679, 1016, 1449,
                            1990, 2651, 3444, 4381, 5474, 6735, 8176, 9809, 11646, 13699]


def test_centered_cube():
    num_generator = sfgn.centered_cube()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 9, 35, 91, 189, 341, 559, 855, 1241,
                            1729, 2331, 3059, 3925, 4941, 6119, 7471, 9009, 10745, 12691]


def test_rhombic_dodecahedral():
    num_generator = sfgn.rhombic_dodecahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 15, 65, 175, 369, 671, 1105, 1695, 2465,
                            3439, 4641, 6095, 7825, 9855, 12209, 14911, 17985, 21455, 25345]


def test_hauy_rhombic_dodecahedral():
    num_generator = sfgn.hauy_rhombic_dodecahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 33, 185, 553, 1233, 2321, 3913, 6105, 8993,
                            12673, 17241, 22793, 29425, 37233, 46313, 56761, 68673, 82145, 97273]


def test_centered_tetrahedron():
    num_generator = sfgn.centered_tetrahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 15, 35, 69, 121, 195, 295, 425,
                            589, 791, 1035, 1325, 1665, 2059, 2511, 3025, 3605, 4255]


def test_centered_square_pyramid():
    num_generator = sfgn.centered_square_pyramid()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 20, 49, 99, 176, 286, 435, 629,
                            874, 1176, 1541, 1975, 2484, 3074, 3751, 4521, 5390, 6364]


def test_centered_mgonal_pyramid():
    num_generator = sfgn.centered_mgonal_pyramid(14)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 70, 189, 399, 726, 1196, 1835, 2669,
                            3724, 5026, 6601, 8475, 10674, 13224, 16151, 19481, 23240, 27454]


def test_centered_octahedron():
    num_generator = sfgn.centered_octahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 7, 25, 63, 129, 231, 377, 575, 833,
                            1159, 1561, 2047, 2625, 3303, 4089, 4991, 6017, 7175, 8473]


def test_centered_icosahedron():
    num_generator = sfgn.centered_icosahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 55, 147, 309, 561, 923, 1415, 2057,
                            2869, 3871, 5083, 6525, 8217, 10179, 12431, 14993, 17885, 21127]


def test_centered_dodecahedron():
    num_generator = sfgn.centered_dodecahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 95, 259, 549, 1001, 1651, 2535, 3689,
                            5149, 6951, 9131, 11725, 14769, 18299, 22351, 26961, 32165, 37999]


def test_centered_truncated_tetrahedron():
    num_generator = sfgn.centered_truncated_tetrahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 17, 75, 203, 429, 781, 1287, 1975, 2873,
                            4009, 5411, 7107, 9125, 11493, 14239, 17391, 20977, 25025, 29563]


def test_centered_truncated_cube():
    num_generator = sfgn.centered_truncated_cube()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 49, 235, 651, 1389, 2541, 4199, 6455, 9401,
                            13129, 17731, 23299, 29925, 37701, 46719, 57071, 68849, 82145, 97051]


def test_centered_truncated_octahedron():
    num_generator = sfgn.centered_truncated_octahedron()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 33, 155, 427, 909, 1661, 2743, 4215, 6137,
                            8569, 11571, 15203, 19525, 24597, 30479, 37231, 44913, 53585, 63307]


def test_centered_mgonal_pyramidal():
    num_generator = sfgn.centered_mgonal_pyramidal(19)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 79, 194, 385, 671, 1071, 1604, 2289,
                            3145, 4191, 5446, 6929, 8659, 10655, 12936, 15521, 18429, 21679]


def test_centered_hexagonal_pyramidal():
    num_generator = sfgn.centered_hexagonal_pyramidal()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 27, 64, 125, 216, 343, 512, 729,
                            1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]


def test_hexagonal_prism():
    num_generator = sfgn.hexagonal_prism()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 14, 57, 148, 305, 546, 889, 1352, 1953,
                            2710, 3641, 4764, 6097, 7658, 9465, 11536, 13889, 16542, 19513]


def test_mgonal_prism():
    num_generator = sfgn.mgonal_prism(35)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 72, 318, 844, 1755, 3156, 5152, 7848, 11349,
                            15760, 21186, 27732, 35503, 44604, 55140, 67216, 80937, 96408, 113734]


def test_generalized_mgonal_pyramidal():
    num_generator = sfgn.generalized_mgonal_pyramidal(8, -10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-945, -684, -476, -315, -195, -110,
                            -54, -21, -5, 0, 0, 1, 9, 30, 70, 135, 231, 364, 540]


def test_generalized_cubic():
    num_generator = sfgn.generalized_cubic(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-1000, -729, -512, -343, -216, -125,
                            -64, -27, -8, -1, 0, 1, 8, 27, 64, 125, 216, 343, 512]


def test_generalized_octahedral():
    num_generator = sfgn.generalized_octahedral(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-670, -489, -344, -231, -146, -85,
                            -44, -19, -6, -1, 0, 1, 6, 19, 44, 85, 146, 231, 344]


def test_generalized_icosahedral():
    num_generator = sfgn.generalized_icosahedral(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-2760, -2034, -1448, -987, -636, -380,
                            -204, -93, -32, -6, 0, 1, 12, 48, 124, 255, 456, 742, 1128]


def test_generalized_dodecahedral():
    num_generator = sfgn.generalized_dodecahedral(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-4960, -3654, -2600, -1771, -1140, -680, -364,
                            -165, -56, -10, 0, 1, 20, 84, 220, 455, 816, 1330, 2024]


def test_generalized_centered_cube():
    num_generator = sfgn.generalized_centered_cube(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-2331, -1729, -1241, -855, -559, -341,
                            -189, -91, -35, -9, -1, 1, 9, 35, 91, 189, 341, 559, 855]


def test_generalized_centered_tetrahedron():
    num_generator = sfgn.generalized_centered_tetrahedron(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-791, -589, -425, -295, -195, -121,
                            -69, -35, -15, -5, -1, 1, 5, 15, 35, 69, 121, 195, 295]


def test_generalized_centered_square_pyramid():
    num_generator = sfgn.generalized_centered_square_pyramid(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-1176, -874, -629, -435, -286, -176,
                            -99, -49, -20, -6, -1, 1, 6, 20, 49, 99, 176, 286, 435]


def test_generalized_rhombic_dodecahedral():
    num_generator = sfgn.generalized_rhombic_dodecahedral(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-4641, -3439, -2465, -1695, -1105, -671, -
                            369, -175, -65, -15, -1, 1, 15, 65, 175, 369, 671, 1105, 1695]


def test_generalized_centered_mgonal_pyramidal():
    num_generator = sfgn.generalized_centered_mgonal_pyramidal(7, -10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-1165, -849, -596, -399, -251, -
                            145, -74, -31, -9, -1, 0, 1, 9, 31, 74, 145, 251, 399, 596]


def test_generalized_mgonal_prism():
    num_generator = sfgn.generalized_mgonal_prism(23, -10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-12660, -9324, -6632, -4515, -2904, -1730, -
                            924, -417, -140, -24, 0, 1, 48, 210, 556, 1155, 2076, 3388, 5160]


def test_generalized_hexagonal_prism():
    num_generator = sfgn.generalized_hexagonal_prism(-10)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [-3310, -2439, -1736, -1183, -762, -455,
                            -244, -111, -38, -7, 0, 1, 14, 57, 148, 305, 546, 889, 1352]
