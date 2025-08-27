# python -m pytest tests/test_plane_figuratenum.py

from src.figuratenum.plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
pfgn = PlaneFigurateNum()


def test_polygonal():
    num_generator = pfgn.polygonal(6)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 15, 28, 45, 66, 91, 120, 153,  190,
                            231, 276, 325, 378, 435, 496, 561, 630, 703]


def test_triangular():
    result = nc.take_to_list(pfgn.triangular(), 20)
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55,
                66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
    assert result == expected


def test_square():
    result = nc.take_to_list(pfgn.square(), 20)
    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
                121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    assert result == expected


def test_pentagonal():
    result = nc.take_to_list(pfgn.pentagonal(), 20)
    expected = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145,
                176, 210, 247, 287, 330, 376, 425, 477, 532, 590]
    assert result == expected


def test_hexagonal():
    result = nc.take_to_list(pfgn.hexagonal(), 35)
    expected = [
        1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435, 496, 561, 630, 703, 780,
        861, 946, 1035, 1128, 1225, 1326, 1431, 1540, 1653, 1770, 1891, 2016, 2145, 2278, 2415
    ]
    assert result == expected


def test_heptagonal():
    result = nc.take_to_list(pfgn.heptagonal(), 35)
    expected = [
        1, 7, 18, 34, 55, 81, 112, 148, 189, 235, 286, 342, 403, 469, 540, 616, 697, 783, 874, 970,
        1071, 1177, 1288, 1404, 1525, 1651, 1782, 1918, 2059, 2205, 2356, 2512, 2673, 2839, 3010
    ]
    assert result == expected


def test_octagonal():
    result = nc.take_to_list(pfgn.octagonal(), 20)
    expected = [1, 8, 21, 40, 65, 96, 133, 176, 225, 280,
                341, 408, 481, 560, 645, 736, 833, 936, 1045, 1160]
    assert result == expected


def test_nonagonal():
    result = nc.take_to_list(pfgn.nonagonal(), 20)
    expected = [1, 9, 24, 46, 75, 111, 154, 204, 261, 325,
                396, 474, 559, 651, 750, 856, 969, 1089, 1216, 1350]
    assert result == expected


def test_decagonal():
    result = nc.take_to_list(pfgn.decagonal(), 45)
    expected = [
        1, 10, 27, 52, 85, 126, 175, 232, 297, 370, 451, 540, 637, 742, 855, 976, 1105, 1242, 1387, 1540,
        1701, 1870, 2047, 2232, 2425, 2626, 2835, 3052, 3277, 3510, 3751, 4000, 4257, 4522, 4795, 5076,
        5365, 5662, 5967, 6280, 6601, 6930, 7267, 7612, 7965
    ]
    assert result == expected


def test_hendecagonal():
    result = nc.take_to_list(pfgn.hendecagonal(), 20)
    expected = [1, 11, 30, 58, 95, 141, 196, 260, 333, 415,
                506, 606, 715, 833, 960, 1096, 1241, 1395, 1558, 1730]
    assert result == expected


def test_dodecagonal():
    result = nc.take_to_list(pfgn.dodecagonal(), 20)
    expected = [1, 12, 33, 64, 105, 156, 217, 288, 369, 460,
                561, 672, 793, 924, 1065, 1216, 1377, 1548, 1729, 1920]
    assert result == expected


def test_tridecagonal():
    result = nc.take_to_list(pfgn.tridecagonal(), 50)
    expected = [
        1, 13, 36, 70, 115, 171, 238, 316, 405, 505, 616, 738, 871, 1015, 1170, 1336, 1513, 1701, 1900, 2110,
        2331, 2563, 2806, 3060, 3325, 3601, 3888, 4186, 4495, 4815, 5146, 5488, 5841, 6205, 6580, 6966, 7363,
        7771, 8190, 8620, 9061, 9513, 9976, 10450, 10935, 11431, 11938, 12456, 12985, 13525
    ]
    assert result == expected


def test_tetradecagonal():
    result = nc.take_to_list(pfgn.tetradecagonal(), 20)
    expected = [1, 14, 39, 76, 125, 186, 259, 344, 441, 550,
                671, 804, 949, 1106, 1275, 1456, 1649, 1854, 2071, 2300]
    assert result == expected


def test_pentadecagonal():
    result = nc.take_to_list(pfgn.pentadecagonal(), 20)
    expected = [1, 15, 42, 82, 135, 201, 280, 372, 477, 595,
                726, 870, 1027, 1197, 1380, 1576, 1785, 2007, 2242, 2490]
    assert result == expected


def test_hexadecagonal():
    result = nc.take_to_list(pfgn.hexadecagonal(), 20)
    expected = [1, 16, 45, 88, 145, 216, 301, 400, 513, 640,
                781, 936, 1105, 1288, 1485, 1696, 1921, 2160, 2413, 2680]
    assert result == expected


def test_heptadecagonal():
    result = nc.take_to_list(pfgn.heptadecagonal(), 20)
    expected = [1, 17, 48, 94, 155, 231, 322, 428, 549, 685, 836,
                1002, 1183, 1379, 1590, 1816, 2057, 2313, 2584, 2870]
    assert result == expected


def test_octadecagonal():
    result = nc.take_to_list(pfgn.octadecagonal(), 20)
    expected = [1, 18, 51, 100, 165, 246, 343, 456, 585, 730,
                891, 1068, 1261, 1470, 1695, 1936, 2193, 2466, 2755, 3060]
    assert result == expected


def test_nonadecagonal():
    result = nc.take_to_list(pfgn.nonadecagonal(), 20)
    expected = [1, 19, 54, 106, 175, 261, 364, 484, 621, 775,
                946, 1134, 1339, 1561, 1800, 2056, 2329, 2619, 2926, 3250]
    assert result == expected


def test_icosagonal():
    result = nc.take_to_list(pfgn.icosagonal(), 20)
    expected = [1, 20, 57, 112, 185, 276, 385, 512, 657, 820,
                1001, 1200, 1417, 1652, 1905, 2176, 2465, 2772, 3097, 3440]
    assert result == expected


def test_icosihenagonal():
    result = nc.take_to_list(pfgn.icosihenagonal(), 20)
    expected = [1, 21, 60, 118, 195, 291, 406, 540, 693, 865,
                1056, 1266, 1495, 1743, 2010, 2296, 2601, 2925, 3268, 3630]
    assert result == expected


def test_icosidigonal():
    result = nc.take_to_list(pfgn.icosidigonal(), 20)
    expected = [1, 22, 63, 124, 205, 306, 427, 568, 729, 910,
                1111, 1332, 1573, 1834, 2115, 2416, 2737, 3078, 3439, 3820]
    assert result == expected


def test_icositrigonal():
    result = nc.take_to_list(pfgn.icositrigonal(), 20)
    expected = [1, 23, 66, 130, 215, 321, 448, 596, 765, 955,
                1166, 1398, 1651, 1925, 2220, 2536, 2873, 3231, 3610, 4010]
    assert result == expected


def test_icositetragonal():
    result = nc.take_to_list(pfgn.icositetragonal(), 20)
    expected = [1, 24, 69, 136, 225, 336, 469, 624, 801, 1000,
                1221, 1464, 1729, 2016, 2325, 2656, 3009, 3384, 3781, 4200]
    assert result == expected


def test_icosipentagonal():
    result = nc.take_to_list(pfgn.icosipentagonal(), 40)
    expected = [1, 25, 72, 142, 235, 351, 490, 652, 837, 1045,
                1276, 1530, 1807, 2107, 2430, 2776, 3145, 3537, 3952, 4390,
                4851, 5335, 5842, 6372, 6925, 7501, 8100, 8722, 9367, 10035,
                10726, 11440, 12177, 12937, 13720, 14526, 15355, 16207, 17082, 17980]
    assert result == expected


def test_icosihexagonal():
    result = nc.take_to_list(pfgn.icosihexagonal(), 25)
    expected = [1, 26, 75, 148, 245, 366, 511, 680, 873, 1090,
                1331, 1596, 1885, 2198, 2535, 2896, 3281, 3690, 4123, 4580,
                5061, 5566, 6095, 6648, 7225]
    assert result == expected


def test_icosiheptagonal():
    result = nc.take_to_list(pfgn.icosiheptagonal(), 25)
    expected = [1, 27, 78, 154, 255, 381, 532, 708, 909, 1135,
                1386, 1662, 1963, 2289, 2640, 3016, 3417, 3843, 4294, 4770,
                5271, 5797, 6348, 6924, 7525]
    assert result == expected


def test_icosioctagonal():
    result = nc.take_to_list(pfgn.icosioctagonal(), 25)
    expected = [1, 28, 81, 160, 265, 396, 553, 736, 945, 1180,
                1441, 1728, 2041, 2380, 2745, 3136, 3553, 3996, 4465, 4960,
                5481, 6028, 6601, 7200, 7825]
    assert result == expected


def test_icosinonagonal():
    result = nc.take_to_list(pfgn.icosinonagonal(), 20)
    expected = [1, 29, 84, 166, 275, 411, 574, 764, 981, 1225,
                1496, 1794, 2119, 2471, 2850, 3256, 3689, 4149, 4636, 5150]
    assert result == expected


def test_triacontagonal():
    result = nc.take_to_list(pfgn.triacontagonal(), 35)
    expected = [1, 30, 87, 172, 285, 426, 595, 792, 1017, 1270,
                1551, 1860, 2197, 2562, 2955, 3376, 3825, 4302, 4807, 5340,
                5901, 6490, 7107, 7752, 8425, 9126, 9855, 10612, 11397, 12210,
                13051, 13920, 14817, 15742, 16695]
    assert result == expected


def test_centered_triangular():
    gen = pfgn.centered_triangular()
    result = [next(gen) for _ in range(20)]
    expected = [1, 4, 10, 19, 31, 46, 64, 85, 109, 136,
                166, 199, 235, 274, 316, 361, 409, 460, 514, 571]
    assert result == expected


def test_centered_square():
    num_generator = pfgn.centered_square()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 13, 25, 41, 61, 85, 113,
                            145, 181, 221, 265, 313, 365,
                            421, 481, 545, 613, 685]


def test_centered_pentagonal():
    gen = pfgn.centered_pentagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 6, 16, 31, 51, 76, 106, 141, 181, 226,
                276, 331, 391, 456, 526, 601, 681, 766, 856, 951]
    assert result == expected


def test_centered_hexagonal():
    gen = pfgn.centered_hexagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 7, 19, 37, 61, 91, 127, 169, 217, 271,
                331, 397, 469, 547, 631, 721, 817, 919, 1027, 1141]
    assert result == expected


def test_centered_heptagonal():
    gen = pfgn.centered_heptagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 8, 22, 43, 71, 106, 148, 197, 253, 316,
                386, 463, 547, 638, 736, 841, 953, 1072, 1198, 1331]
    assert result == expected


def test_centered_octagonal():
    gen = pfgn.centered_octagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361,
                441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521]
    assert result == expected


def test_centered_nonagonal():
    gen = pfgn.centered_nonagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 10, 28, 55, 91, 136, 190, 253, 325, 406,
                496, 595, 703, 820, 946, 1081, 1225, 1378, 1540, 1711]
    assert result == expected


def test_centered_decagonal():
    gen = pfgn.centered_decagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 11, 31, 61, 101, 151, 211, 281, 361, 451,
                551, 661, 781, 911, 1051, 1201, 1361, 1531, 1711, 1901]
    assert result == expected


def test_centered_hendecagonal():
    gen = pfgn.centered_hendecagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 12, 34, 67, 111, 166, 232, 309, 397, 496,
                606, 727, 859, 1002, 1156, 1321, 1497, 1684, 1882, 2091]
    assert result == expected


def test_centered_dodecagonal():
    num_generator = pfgn.centered_dodecagonal()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 37, 73, 121, 181, 253, 337,  433, 541, 661,
                            793, 937, 1093, 1261, 1441, 1633, 1837, 2053]


def test_centered_tridecagonal():
    gen = pfgn.centered_tridecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 14, 40, 79, 131, 196, 274, 365, 469, 586, 716, 859, 1015, 1184, 1366, 1561, 1769, 1990, 2224, 2471, 2731, 3004,
                3290, 3589, 3901]
    assert result == expected


def test_centered_tetradecagonal():
    gen = pfgn.centered_tetradecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 15, 43, 85, 141, 211, 295, 393, 505, 631, 771, 925, 1093, 1275, 1471, 1681, 1905, 2143, 2395, 2661, 2941, 3235,
                3543, 3865, 4201]
    assert result == expected


def test_centered_pentadecagonal():
    gen = pfgn.centered_pentadecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 16, 46, 91, 151, 226, 316, 421, 541, 676, 826, 991, 1171, 1366, 1576, 1801, 2041, 2296, 2566, 2851, 3151, 3466,
                3796, 4141, 4501]
    assert result == expected


def test_centered_hexadecagonal():
    gen = pfgn.centered_hexadecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 17, 49, 97, 161, 241, 337, 449, 577, 721, 881, 1057, 1249, 1457, 1681, 1921, 2177, 2449, 2737, 3041, 3361, 3697,
                4049, 4417, 4801]
    assert result == expected


def test_centered_heptadecagonal():
    gen = pfgn.centered_heptadecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 18, 52, 103, 171, 256, 358, 477, 613, 766, 936, 1123, 1327, 1548, 1786, 2041, 2313, 2602, 2908, 3231, 3571, 3928,
                4302, 4693, 5101]
    assert result == expected


def test_centered_octadecagonal():
    gen = pfgn.centered_octadecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 19, 55, 109, 181, 271, 379, 505, 649, 811, 991, 1189, 1405, 1639, 1891, 2161, 2449,
                2755, 3079, 3421, 3781, 4159, 4555, 4969, 5401]
    assert result == expected


def test_centered_nonadecagonal():
    gen = pfgn.centered_nonadecagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 20, 58, 115, 191, 286, 400, 533, 685, 856, 1046, 1255, 1483, 1730,
                1996, 2281, 2585, 2908, 3250, 3611, 3991, 4390, 4808, 5245, 5701]
    assert result == expected


def test_centered_icosagonal():
    gen = pfgn.centered_icosagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 21, 61, 121, 201, 301, 421, 561, 721, 901, 1101, 1321, 1561, 1821,
                2101, 2401, 2721, 3061, 3421, 3801, 4201, 4621, 5061, 5521, 6001]
    assert result == expected


def test_centered_icosihenagonal():
    gen = pfgn.centered_icosihenagonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 22, 64, 127, 211, 316, 442, 589, 757, 946, 1156, 1387, 1639, 1912, 2206, 2521, 2857, 3214, 3592, 3991, 4411, 4852, 5314, 5797,
                6301]
    assert result == expected


def test_centered_icosidigonal():
    gen = pfgn.centered_icosidigonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 23, 67, 133, 221, 331, 463, 617, 793, 991, 1211, 1453, 1717, 2003, 2311, 2641, 2993, 3367, 3763, 4181, 4621, 5083, 5567, 6073,
                6601]
    assert result == expected


def test_centered_icositrigonal():
    gen = pfgn.centered_icositrigonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 24, 70, 139, 231, 346, 484, 645, 829, 1036, 1266, 1519, 1795, 2094, 2416, 2761, 3129, 3520, 3934, 4371, 4831, 5314,
                5820, 6349, 6901]
    assert result == expected


def test_centered_icositetragonal():
    gen = pfgn.centered_icositetragonal()
    result = [next(gen) for _ in range(25)]
    expected = [1, 25, 73, 145, 241, 361, 505, 673, 865, 1081, 1321, 1585, 1873, 2185, 2521, 2881, 3265, 3673, 4105, 4561, 5041, 5545,
                6073, 6625, 7201]
    assert result == expected


def test_centered_icosipentagonal():
    gen = pfgn.centered_icosipentagonal()
    result = [next(gen) for _ in range(30)]
    expected = [1, 26, 76, 151, 251, 376, 526, 701, 901, 1126, 1376, 1651, 1951, 2276, 2626, 3001, 3401, 3826, 4276, 4751, 5251, 5776,
                6326, 6901, 7501, 8126, 8776, 9451, 10151, 10876]
    assert result == expected


def test_centered_icosihexagonal():
    gen = pfgn.centered_icosihexagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 27, 79, 157, 261, 391, 547, 729, 937, 1171, 1431, 1717, 2029, 2367, 2731, 3121, 3537, 3979, 4447,
                4941]
    assert result == expected


def test_centered_icosiheptagonal():
    gen = pfgn.centered_icosiheptagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 28, 82, 163, 271, 406, 568, 757, 973, 1216, 1486, 1783, 2107, 2458, 2836, 3241, 3673, 4132, 4618,
                5131]
    assert result == expected


def test_centered_icosioctagonal():
    gen = pfgn.centered_icosioctagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 29, 85, 169, 281, 421, 589, 785, 1009, 1261, 1541, 1849, 2185, 2549, 2941, 3361, 3809, 4285, 4789,
                5321]
    assert result == expected


def test_centered_icosinonagonal():
    gen = pfgn.centered_icosinonagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 30, 88, 175, 291, 436, 610, 813, 1045, 1306, 1596, 1915, 2263, 2640, 3046, 3481, 3945, 4438, 4960,
                5511]
    assert result == expected


def test_centered_triacontagonal():
    gen = pfgn.centered_triacontagonal()
    result = [next(gen) for _ in range(20)]
    expected = [1, 31, 91, 181, 301, 451, 631, 841, 1081, 1351, 1651, 1981, 2341, 2731, 3151, 3601, 4081, 4591, 5131,
                5701]
    assert result == expected


def test_centered_mgonal():
    num_generator = pfgn.centered_mgonal(19)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 20, 58, 115, 191, 286, 400, 533, 685, 856, 1046,
                            1255, 1483, 1730, 1996, 2281, 2585, 2908, 3250]


def test_pronic():
    num_generator = pfgn.pronic()
    infinite_seq = []
    for _ in range(1, 81):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380,
                            420, 462, 506, 552, 600, 650, 702, 756, 812, 870, 930, 992,
                            1056, 1122, 1190, 1260, 1332, 1406, 1482, 1560, 1640, 1722, 1806,
                            1892, 1980, 2070, 2162, 2256, 2352, 2450, 2550, 2652, 2756, 2862, 2970,
                            3080, 3192, 3306, 3422, 3540, 3660, 3782, 3906, 4032, 4160, 4290, 4422,
                            4556, 4692, 4830, 4970, 5112, 5256, 5402, 5550, 5700, 5852, 6006, 6162, 6320, 6480]


def test_polite():
    num_generator = pfgn.polite()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 3, 5, 6, 7, 9, 10, 11,
                            12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]


def test_impolite():
    num_generator = pfgn.impolite()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                            2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]


def test_cross():
    num_generator = pfgn.cross()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 9, 13, 17, 21, 25,
                            29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73]


def test_aztec_diamond():
    num_generator = pfgn.aztec_diamond()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [4, 12, 24, 40, 60, 84, 112, 144,
                            180, 220, 264, 312, 364, 420, 480, 544, 612, 684, 760]


def test_polygram():
    num_generator = pfgn.polygram(31)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 63, 187, 373, 621, 931, 1303, 1737,
                            2233, 2791, 3411, 4093, 4837, 5643, 6511, 7441, 8433, 9487, 10603]


def test_pentagram():
    num_generator = pfgn.pentagram()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 11, 31, 61, 101, 151, 211, 281,
                            361, 451, 551, 661, 781, 911, 1051, 1201, 1361, 1531, 1711]


def test_gnomic():
    num_generator = pfgn.gnomic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 3, 5, 7, 9, 11, 13, 15,
                            17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]


def test_truncated_triangular():
    num_generator = pfgn.truncated_triangular()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 7, 19, 37, 61, 91, 127, 169,
                            217, 271, 331, 397, 469, 547, 631, 721, 817, 919, 1027]


def test_truncated_square():
    num_generator = pfgn.truncated_square()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 12, 37, 76, 129, 196, 277, 372,
                            481, 604, 741, 892, 1057, 1236, 1429, 1636, 1857, 2092, 2341]


def test_truncated_pronic():
    num_generator = pfgn.truncated_pronic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 16, 44, 86, 142, 212, 296, 394,
                            506, 632, 772, 926, 1094, 1276, 1472, 1682, 1906, 2144, 2396]


def test_truncated_centered_pol():
    num_generator = pfgn.truncated_centered_pol(47)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 236, 800, 1693, 2915, 4466, 6346, 8555, 11093,
                            13960, 17156, 20681, 24535, 28718, 33230, 38071, 43241, 48740, 54568]


def test_truncated_centered_triangular():
    result = nc.take_to_list(pfgn.truncated_centered_triangular(), 20)
    expected = [1, 16, 52, 109, 187, 286, 406, 547, 709, 892,
                1096, 1321, 1567, 1834, 2122, 2431, 2761, 3112, 3484, 3877]
    assert result == expected


def test_truncated_centered_square():
    result = nc.take_to_list(pfgn.truncated_centered_square(), 20)
    expected = [1, 21, 69, 145, 249, 381, 541, 729, 945, 1189,
                1461, 1761, 2089, 2445, 2829, 3241, 3681, 4149, 4645, 5169]
    assert result == expected


def test_truncated_centered_pentagonal():
    result = nc.take_to_list(pfgn.truncated_centered_pentagonal(), 20)
    expected = [1, 26, 86, 181, 311, 476, 676, 911, 1181, 1486,
                1826, 2201, 2611, 3056, 3536, 4051, 4601, 5186, 5806, 6461]
    assert result == expected


def test_truncated_centered_hexagonal():
    num_generator = pfgn.truncated_centered_hexagonal()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 31, 103, 217, 373, 571, 811, 1093,
                            1417, 1783, 2191, 2641, 3133, 3667, 4243, 4861, 5521, 6223, 6967]


def test_generalized_mgonal():
    num_generator = pfgn.generalized_mgonal(53, -34)
    infinite_seq = []
    for _ in range(1, 60):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [30311, 28578, 26896, 25265, 23685, 22156, 20678, 19251,
                            17875, 16550, 15276, 14053,  12881, 11760, 10690, 9671,
                            8703,  7786, 6920, 6105, 5341, 4628, 3966, 3355, 2795,
                            2286, 1828, 1421, 1065, 760, 506, 303, 151, 50, 0, 1, 53,
                            156, 310, 515, 771, 1078, 1436, 1845, 2305, 2816, 3378,
                            3991, 4655, 5370, 6136, 6953, 7821, 8740, 9710, 10731, 11803, 12926, 14100]


def test_generalized_centered_pol():
    num_generator = pfgn.generalized_centered_pol(50, -40)
    infinite_seq = []
    for _ in range(1, 70):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [41001, 39001, 37051, 35151, 33301, 31501, 29751, 28051,
                            26401, 24801, 23251, 21751, 20301, 18901, 17551, 16251,
                            15001, 13801, 12651, 11551, 10501, 9501, 8551, 7651, 6801,
                            6001, 5251, 4551, 3901, 3301, 2751, 2251, 1801, 1401, 1051,
                            751, 501, 301, 151, 51, 1, 1, 51, 151, 301, 501, 751, 1051,
                            1401, 1801, 2251, 2751, 3301, 3901, 4551, 5251, 6001, 6801,
                            7651, 8551, 9501, 10501, 11551, 12651, 13801, 15001, 16251, 17551, 18901]


def test_generalized_pronic():
    num_generator = pfgn.generalized_pronic(-50)
    infinite_seq = []
    for _ in range(1, 100):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2450, 2352, 2256, 2162, 2070, 1980, 1892, 1806, 1722,
                            1640, 1560, 1482, 1406, 1332, 1260, 1190, 1122, 1056,
                            992, 930, 870, 812, 756, 702, 650, 600, 552, 506, 462,
                            420, 380, 342, 306, 272, 240, 210, 182, 156, 132, 110,
                            90, 72, 56, 42, 30, 20, 12, 6, 2, 0, 0, 2, 6, 12, 20,
                            30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272,
                            306, 342, 380, 420, 462, 506, 552, 600, 650, 702, 756,
                            812, 870, 930, 992, 1056, 1122, 1190, 1260, 1332, 1406,
                            1482, 1560, 1640, 1722, 1806, 1892, 1980, 2070, 2162, 2256, 2352]
