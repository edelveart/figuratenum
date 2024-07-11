from figurate_numbers.plane_figurate_numbers import polygonal_numbers, centered_square_numbers, centered_dodecagonal_numbers


def test_polygonal_numbers():
    num_generator = polygonal_numbers(6)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 15, 28, 45, 66, 91, 120, 153,
                            190, 231, 276, 325, 378, 435, 496, 561, 630, 703]


def test_centered_square_numbers():
    num_generator = centered_square_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 13, 25, 41, 61, 85, 113,
                            145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685]


def test_centered_dodecagonal_numbers():
    num_generator = centered_dodecagonal_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 37, 73, 121, 181, 253, 337,
                            433, 541, 661, 793, 937, 1093, 1261, 1441, 1633, 1837, 2053]
