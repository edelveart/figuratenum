from figurate_numbers.space_figurate_numbers import (
    m_pyramidal_numbers, cubic_numbers, tetrahedral_numbers,
    octahedral_numbers, dodecahedral_numbers, icosahedral_numbers,
    truncated_tetrahedral_numbers, truncated_cubic_numbers, truncated_octahedral_numbers,
    stella_octangula_numbers, centered_cube_numbers, rhombic_dodecahedral_numbers,
    hauy_rhombic_dodecahedral_numbers
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
