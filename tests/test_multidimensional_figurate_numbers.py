from figurate_numbers.multidimensional_figurate_numbers import (
    pentatope_numbers, k_dimensional_hypertetrahedron_numbers, biquadratic_numbers,
    k_dimensional_hypercube_numbers, hyperoctahedral_numbers, hypericosahedral_numbers,
    hyperdodecahedral_numbers, polyoctahedral_numbers, k_dimensional_hyperoctahedron_numbers,
    four_dimensional_mgonal_pyramidal_numbers, k_dimensional_mgonal_pyramidal_numbers
)


def test_pentatope_numbers():
    num_generator = pentatope_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 15, 35, 70, 126, 210, 330, 495,
                            715, 1001, 1365, 1820, 2380, 3060, 3876, 4845, 5985, 7315]


def test_k_dimensional_hypertetrahedron_numbers():
    num_generator = k_dimensional_hypertetrahedron_numbers(21)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 22, 253, 2024, 12650, 65780, 296010, 1184040, 4292145, 14307150, 44352165,
                            129024480, 354817320, 927983760, 2319959400, 5567902560, 12875774670, 28781143380, 62359143990]


def test_biquadratic_numbers():
    num_generator = biquadratic_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 81, 256, 625, 1296, 2401, 4096, 6561,
                            10000, 14641, 20736, 28561, 38416, 50625, 65536, 83521, 104976, 130321]


def test_k_dimensional_hypercube_numbers():
    num_generator = k_dimensional_hypercube_numbers(16)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 65536, 43046721, 4294967296, 152587890625,
                            2821109907456, 33232930569601, 281474976710656, 1853020188851841, 10000000000000000, 45949729863572161, 184884258895036416, 665416609183179841, 2177953337809371136, 6568408355712890625, 18446744073709551616, 48661191875666868481, 121439531096594251776, 288441413567621167681]


def test_hyperoctahedral_numbers():
    num_generator = hyperoctahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 33, 96, 225, 456, 833, 1408, 2241,
                            3400, 4961, 7008, 9633, 12936, 17025, 22016, 28033, 35208, 43681]


def test_hypericosahedral_numbers():
    num_generator = hypericosahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 120, 947, 3652, 9985, 22276, 43435, 76952, 126897, 197920,
                            295251, 424700, 592657, 806092, 1072555, 1400176, 1797665, 2274312, 2839987]


def test_hyperdodecahedral_numbers():
    num_generator = hyperdodecahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 600, 4983, 19468, 53505, 119676, 233695, 414408, 683793, 1066960,
                            1592151, 2290740, 3197233, 4349268, 5787615, 7556176, 9701985, 12275208, 15329143]


def test_polyoctahedral_numbers():
    num_generator = polyoctahedral_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 24, 153, 544, 1425, 3096, 5929, 10368, 16929,
                            26200, 38841, 55584, 77233, 104664, 138825, 180736, 231489, 292248, 364249]


def test_k_dimensional_hyperoctahedron_numbers():
    num_generator = k_dimensional_hyperoctahedron_numbers(27)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 54, 1459, 26316, 356725, 3878946, 35267239, 275940504,
                            1897865641, 11663134350, 64878791131, 330159018084,
                            1550594372509, 6771089488506, 27667653828175, 106374643269936,
                            386682074864209, 1334658881073894, 4390658718085891]


def test_four_dimensional_mgonal_pyramidal_numbers():
    num_generator = four_dimensional_mgonal_pyramidal_numbers(11)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 55, 155, 350, 686, 1218, 2010, 3135,
                            4675, 6721, 9373, 12740, 16940, 22100,
                            28356, 35853, 44745, 55195]


def test_k_dimensional_mgonal_pyramidal_numbers():
    num_generator = k_dimensional_mgonal_pyramidal_numbers(9, 14)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 165, 825, 3135, 9867, 27027, 66495,
                            150150, 316030, 627198, 1184118, 2141490,
                            3730650, 6288810, 10296594, 16425519, 25597275, 39056875]
