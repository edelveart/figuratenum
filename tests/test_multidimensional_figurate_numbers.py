from figurate_numbers.multidimensional_figurate_numbers import (
    pentatope_numbers, k_dimensional_hypertetrahedron_numbers, biquadratic_numbers,
    k_dimensional_hypercube_numbers, hyperoctahedral_numbers
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
