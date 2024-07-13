from src.figuratenum.plane_figuratenum import (
    polygonal_numbers, centered_square_numbers,
    centered_dodecagonal_numbers, centered_mgonal_numbers,
    pronic_numbers, polite_numbers, impolite_numbers,
    cross_numbers, aztec_diamond_numbers, polygram_numbers, pentagram_numbers,
    gnomic_numbers, truncated_triangular_numbers, truncated_square_numbers,
    truncated_pronic_numbers, truncated_centered_pol_numbers,
    truncated_centered_hexagonal_numbers, generalized_mgonal_numbers,
    generalized_centered_pol_numbers, generalized_pronic_numbers
)


def test_polygonal_numbers():
    num_generator = polygonal_numbers(6)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 15, 28, 45, 66, 91, 120, 153,  190,
                            231, 276, 325, 378, 435, 496, 561, 630, 703]


def test_centered_square_numbers():
    num_generator = centered_square_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 13, 25, 41, 61, 85, 113,
                            145, 181, 221, 265, 313, 365,
                            421, 481, 545, 613, 685]


def test_centered_dodecagonal_numbers():
    num_generator = centered_dodecagonal_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 37, 73, 121, 181, 253, 337,  433, 541, 661,
                            793, 937, 1093, 1261, 1441, 1633, 1837, 2053]


def test_centered_mgonal_numbers():
    num_generator = centered_mgonal_numbers(19)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 20, 58, 115, 191, 286, 400, 533, 685, 856, 1046,
                            1255, 1483, 1730, 1996, 2281, 2585, 2908, 3250]


def test_pronic_numbers():
    num_generator = pronic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 5, 10, 17, 26, 37, 50, 65,
                            82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362]


def test_polite_numbers():
    num_generator = polite_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 3, 5, 6, 7, 9, 10, 11,
                            12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]


def test_impolite_numbers():
    num_generator = impolite_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                            2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]


def test_cross_numbers():
    num_generator = cross_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 9, 13, 17, 21, 25,
                            29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73]


def test_aztec_diamond_numbers():
    num_generator = aztec_diamond_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [4, 12, 24, 40, 60, 84, 112, 144,
                            180, 220, 264, 312, 364, 420, 480, 544, 612, 684, 760]


def test_polygram_numbers():
    num_generator = polygram_numbers(31)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 63, 187, 373, 621, 931, 1303, 1737,
                            2233, 2791, 3411, 4093, 4837, 5643, 6511, 7441, 8433, 9487, 10603]


def test_pentagram_numbers():
    num_generator = pentagram_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 11, 31, 61, 101, 151, 211, 281,
                            361, 451, 551, 661, 781, 911, 1051, 1201, 1361, 1531, 1711]


def test_gnomic_numbers():
    num_generator = gnomic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 3, 5, 7, 9, 11, 13, 15,
                            17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]


def test_truncated_triangular_numbers():
    num_generator = truncated_triangular_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 7, 19, 37, 61, 91, 127, 169,
                            217, 271, 331, 397, 469, 547, 631, 721, 817, 919, 1027]


def test_truncated_square_numbers():
    num_generator = truncated_square_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 12, 37, 76, 129, 196, 277, 372,
                            481, 604, 741, 892, 1057, 1236, 1429, 1636, 1857, 2092, 2341]


def test_truncated_pronic_numbers():
    num_generator = truncated_pronic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [2, 16, 44, 86, 142, 212, 296, 394,
                            506, 632, 772, 926, 1094, 1276, 1472, 1682, 1906, 2144, 2396]


def test_truncated_centered_pol_numbers():
    num_generator = truncated_centered_pol_numbers(47)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 236, 800, 1693, 2915, 4466, 6346, 8555, 11093,
                            13960, 17156, 20681, 24535, 28718, 33230, 38071, 43241, 48740, 54568]


def test_truncated_centered_hexagonal_numbers():
    num_generator = truncated_centered_hexagonal_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 31, 103, 217, 373, 571, 811, 1093,
                            1417, 1783, 2191, 2641, 3133, 3667, 4243, 4861, 5521, 6223, 6967]


def test_generalized_mgonal_numbers():
    num_generator = generalized_mgonal_numbers(53, -34)
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


def test_generalized_centered_pol_numbers():
    num_generator = generalized_centered_pol_numbers(50, -40)
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


def test_generalized_pronic_numbers():
    num_generator = generalized_pronic_numbers(-50)
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
