from figurate_numbers.multidimensional_figurate_numbers import (
    pentatope_numbers
)


def test_pentatope_numbers():
    num_generator = pentatope_numbers()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 15, 35, 70, 126, 210, 330, 495,
                            715, 1001, 1365, 1820, 2380, 3060, 3876, 4845, 5985, 7315]
