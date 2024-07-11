from figurate_numbers.plane_figurate_numbers import polygonal_numbers, centered_square_numbers, centered_dodecagonal_numbers, centered_mgonal_numbers, pronic_numbers, polite_numbers


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
