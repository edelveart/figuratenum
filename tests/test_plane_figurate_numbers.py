from figurate_numbers.plane_figurate_numbers import polygonal_numbers


def test_polygonal_numbers():
    num_generator = polygonal_numbers(6)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 15, 28, 45, 66, 91, 120, 153,
                            190, 231, 276, 325, 378, 435, 496, 561, 630, 703]
