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


def test_triangular_pyramidal():
    gen = sfgn.triangular_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 4, 10, 20, 35, 56, 84, 120, 165, 220,
                286, 364, 455, 560, 680, 816, 969, 1140, 1330, 1540]
    assert result == expected


def test_square_pyramidal():
    gen = sfgn.square_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 506,
                650, 819, 1015, 1240, 1496, 1785, 2109, 2470, 2870]
    assert result == expected


def test_pentagonal_pyramidal():
    gen = sfgn.pentagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 6, 18, 40, 75, 126, 196, 288, 405, 550, 726,
                936, 1183, 1470, 1800, 2176, 2601, 3078, 3610, 4200]
    assert result == expected


def test_hexagonal_pyramidal():
    gen = sfgn.hexagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 7, 22, 50, 95, 161, 252, 372, 525, 715, 946,
                1222, 1547, 1925, 2360, 2856, 3417, 4047, 4750, 5530]
    assert result == expected


def test_heptagonal_pyramidal():
    gen = sfgn.heptagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 8, 26, 60, 115, 196, 308, 456, 645, 880, 1166,
                1508, 1911, 2380, 2920, 3536, 4233, 5016, 5890, 6860]
    assert result == expected


def test_octagonal_pyramidal():
    gen = sfgn.octagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 9, 30, 70, 135, 231, 364, 540, 765, 1045, 1386,
                1794, 2275, 2835, 3480, 4216, 5049, 5985, 7030, 8190]
    assert result == expected


def test_nonagonal_pyramidal():
    gen = sfgn.nonagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 10, 34, 80, 155, 266, 420, 624, 885, 1210,
                1606, 2080, 2639, 3290, 4040, 4896, 5865, 6954, 8170, 9520]
    assert result == expected


def test_decagonal_pyramidal():
    gen = sfgn.decagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 11, 38, 90, 175, 301, 476, 708, 1005, 1375,
                1826, 2366, 3003, 3745, 4600, 5576, 6681, 7923, 9310, 10850]
    assert result == expected


def test_hendecagonal_pyramidal():
    gen = sfgn.hendecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 12, 42, 100, 195, 336, 532, 792, 1125, 1540,
        2046, 2652, 3367, 4200, 5160, 6256, 7497, 8892,
        10450, 12180
    ]
    assert result == expected


def test_dodecagonal_pyramidal():
    gen = sfgn.dodecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 13, 46, 110, 215, 371, 588, 876, 1245, 1705,
        2266, 2938, 3731, 4655, 5720, 6936, 8313, 9861,
        11590, 13510
    ]
    assert result == expected


def test_tridecagonal_pyramidal():
    gen = sfgn.tridecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 14, 50, 120, 235, 406, 644, 960, 1365, 1870,
        2486, 3224, 4095, 5110, 6280, 7616, 9129, 10830,
        12730, 14840
    ]
    assert result == expected


def test_tetradecagonal_pyramidal():
    gen = sfgn.tetradecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 15, 54, 130, 255, 441, 700, 1044, 1485, 2035,
        2706, 3510, 4459, 5565, 6840, 8296, 9945, 11799,
        13870, 16170
    ]
    assert result == expected


def test_pentadecagonal_pyramidal():
    gen = sfgn.pentadecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 16, 58, 140, 275, 476, 756, 1128, 1605, 2200,
        2926, 3796, 4823, 6020, 7400, 8976, 10761, 12768,
        15010, 17500
    ]
    assert result == expected


def test_hexadecagonal_pyramidal():
    gen = sfgn.hexadecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 17, 62, 150, 295, 511, 812, 1212, 1725, 2365,
        3146, 4082, 5187, 6475, 7960, 9656, 11577, 13737,
        16150, 18830
    ]
    assert result == expected


def test_heptadecagonal_pyramidal():
    gen = sfgn.heptadecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 18, 66, 160, 315, 546, 868, 1296, 1845, 2530,
        3366, 4368, 5551, 6930, 8520, 10336, 12393, 14706,
        17290, 20160
    ]
    assert result == expected


def test_octadecagonal_pyramidal():
    gen = sfgn.octadecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 19, 70, 170, 335, 581, 924, 1380, 1965, 2695,
        3586, 4654, 5915, 7385, 9080, 11016, 13209, 15675,
        18430, 21490
    ]
    assert result == expected


def test_nonadecagonal_pyramidal():
    gen = sfgn.nonadecagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 20, 74, 180, 355, 616, 980, 1464, 2085, 2860,
        3806, 4940, 6279, 7840, 9640, 11696, 14025, 16644,
        19570, 22820
    ]
    assert result == expected


def test_icosagonal_pyramidal():
    gen = sfgn.icosagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 21, 78, 190, 375, 651, 1036, 1548, 2205, 3025,
        4026, 5226, 6643, 8295, 10200, 12376, 14841, 17613,
        20710, 24150
    ]
    assert result == expected


def test_icosihenagonal_pyramidal():
    gen = sfgn.icosihenagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 22, 82, 200, 395, 686, 1092, 1632, 2325, 3190,
        4246, 5512, 7007, 8750, 10760, 13056, 15657, 18582,
        21850, 25480
    ]
    assert result == expected


def test_icosidigonal_pyramidal():
    gen = sfgn.icosidigonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 23, 86, 210, 415, 721, 1148, 1716, 2445, 3355,
        4466, 5798, 7371, 9205, 11320, 13736, 16473, 19551,
        22990, 26810
    ]
    assert result == expected


def test_icositrigonal_pyramidal():
    gen = sfgn.icositrigonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 24, 90, 220, 435, 756, 1204, 1800, 2565, 3520,
        4686, 6084, 7735, 9660, 11880, 14416, 17289, 20520,
        24130, 28140
    ]
    assert result == expected


def test_icositetragonal_pyramidal():
    gen = sfgn.icositetragonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 25, 94, 230, 455, 791, 1260, 1884, 2685, 3685,
        4906, 6370, 8099, 10115, 12440, 15096, 18105, 21489,
        25270, 29470
    ]
    assert result == expected


def test_icosipentagonal_pyramidal():
    gen = sfgn.icosipentagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 26, 98, 240, 475, 826, 1316, 1968, 2805, 3850,
        5126, 6656, 8463, 10570, 13000, 15776, 18921, 22458,
        26410, 30800
    ]
    assert result == expected


def test_icosihexagonal_pyramidal():
    gen = sfgn.icosihexagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 27, 102, 250, 495, 861, 1372, 2052, 2925, 4015,
        5346, 6942, 8827, 11025, 13560, 16456, 19737, 23427,
        27550, 32130
    ]
    assert result == expected


def test_icosiheptagonal_pyramidal():
    gen = sfgn.icosiheptagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 28, 106, 260, 515, 896, 1428, 2136, 3045, 4180,
        5566, 7228, 9191, 11480, 14120, 17136, 20553, 24396,
        28690, 33460
    ]
    assert result == expected


def test_icosioctagonal_pyramidal():
    gen = sfgn.icosioctagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 29, 110, 270, 535, 931, 1484, 2220, 3165, 4345,
        5786, 7514, 9555, 11935, 14680, 17816, 21369, 25365,
        29830, 34790
    ]
    assert result == expected


def test_icosinonagonal_pyramidal():
    gen = sfgn.icosinonagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 30, 114, 280, 555, 966, 1540, 2304, 3285, 4510,
        6006, 7800, 9919, 12390, 15240, 18496, 22185, 26334,
        30970, 36120
    ]
    assert result == expected


def test_triacontagonal_pyramidal():
    gen = sfgn.triacontagonal_pyramidal()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 31, 118, 290, 575, 1001, 1596, 2388, 3405, 4675,
        6226, 8086, 10283, 12845, 15800, 19176, 23001, 27303,
        32110, 37450
    ]
    assert result == expected


def test_tetrahedral_square_pyramidal():
    gen = sfgn.tetrahedral_square_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1] * 10
    assert result == expected


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


def test_centered_pentagonal_pyramid():
    gen = sfgn.centered_pentagonal_pyramid()
    result = [next(gen) for _ in range(10)]
    expected = [1, 7, 25, 63, 129, 231, 377, 575, 833, 1159]
    assert result == expected


def test_centered_hexagonal_pyramid():
    gen = sfgn.centered_hexagonal_pyramid()
    result = [next(gen) for _ in range(75)]
    expected = [
        1, 8, 30, 77, 159, 286, 468, 715, 1037, 1444,
        1946, 2553, 3275, 4122, 5104, 6231, 7513, 8960,
        10582, 12389, 14391, 16598, 19020, 21667, 24549,
        27676, 31058, 34705, 38627, 42834, 47336, 52143,
        57265, 62712, 68494, 74621, 81103, 87950, 95172,
        102779, 110781, 119188, 128010, 137257, 146939,
        157066, 167648, 178695, 190217, 202224, 214726,
        227733, 241255, 255302, 269884, 285011, 300693,
        316940, 333762, 351169, 369171, 387778, 407000,
        426847, 447329, 468456, 490238, 512685, 535807,
        559614, 584116, 609323, 635245, 661892, 689274
    ]
    assert result == expected


def test_centered_heptagonal_pyramid():
    gen = sfgn.centered_heptagonal_pyramid()
    result = [next(gen) for _ in range(10)]
    expected = [1, 9, 35, 91, 189, 341, 559, 855, 1241, 1729]
    assert result == expected


def test_centered_octagonal_pyramid():
    gen = sfgn.centered_octagonal_pyramid()
    result = [next(gen) for _ in range(10)]
    expected = [1, 10, 40, 105, 219, 396, 650, 995, 1445, 2014]
    assert result == expected


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


def test_centered_triangular_pyramidal():
    gen = sfgn.centered_triangular_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 5, 15, 34, 65, 111, 175, 260, 369, 505,
        671, 870, 1105, 1379, 1695, 2056, 2465, 2925,
        3439, 4010, 4641, 5335, 6095, 6924, 7825
    ]
    assert result == expected


def test_centered_square_pyramidal():
    gen = sfgn.centered_square_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 6, 19, 44, 85, 146, 231, 344, 489, 670,
        891, 1156, 1469, 1834, 2255, 2736, 3281, 3894,
        4579, 5340, 6181, 7106, 8119, 9224, 10425
    ]
    assert result == expected


def test_centered_pentagonal_pyramidal():
    gen = sfgn.centered_pentagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 7, 23, 54, 105, 181, 287, 428, 609, 835,
        1111, 1442, 1833, 2289, 2815, 3416, 4097, 4863,
        5719, 6670, 7721, 8877, 10143, 11524, 13025
    ]
    assert result == expected


def test_centered_hexagonal_pyramidal():
    num_generator = sfgn.centered_hexagonal_pyramidal()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 27, 64, 125, 216, 343, 512, 729,
                            1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]


def test_centered_heptagonal_pyramidal():
    gen = sfgn.centered_heptagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 9, 31, 74, 145, 251, 399, 596, 849, 1165,
        1551, 2014, 2561, 3199, 3935, 4776, 5729, 6801,
        7999, 9330, 10801, 12419, 14191, 16124, 18225
    ]
    assert result == expected


def test_centered_octagonal_pyramidal():
    gen = sfgn.centered_octagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 10, 35, 84, 165, 286, 455, 680, 969, 1330,
        1771, 2300, 2925, 3654, 4495, 5456, 6545, 7770,
        9139, 10660, 12341, 14190, 16215, 18424, 20825
    ]
    assert result == expected


def test_centered_nonagonal_pyramidal():
    gen = sfgn.centered_nonagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 11, 39, 94, 185, 321, 511, 764, 1089, 1495,
        1991, 2586, 3289, 4109, 5055, 6136, 7361, 8739,
        10279, 11990, 13881, 15961, 18239, 20724, 23425
    ]
    assert result == expected


def test_centered_decagonal_pyramidal():
    gen = sfgn.centered_decagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 12, 43, 104, 205, 356, 567, 848, 1209, 1660,
        2211, 2872, 3653, 4564, 5615, 6816, 8177, 9708,
        11419, 13320, 15421, 17732, 20263, 23024, 26025
    ]
    assert result == expected


def test_centered_hendecagonal_pyramidal():
    gen = sfgn.centered_hendecagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 13, 47, 114, 225, 391, 623, 932, 1329, 1825,
        2431, 3158, 4017, 5019, 6175, 7496, 8993, 10677,
        12559, 14650, 16961, 19503, 22287, 25324, 28625
    ]
    assert result == expected


def test_centered_dodecagonal_pyramidal():
    gen = sfgn.centered_dodecagonal_pyramidal()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 14, 51, 124, 245, 426, 679, 1016, 1449, 1990,
        2651, 3444, 4381, 5474, 6735, 8176, 9809, 11646,
        13699, 15980, 18501, 21274, 24311, 27624, 31225
    ]
    assert result == expected


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
