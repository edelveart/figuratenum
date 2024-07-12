from figurate_numbers.multidimensional_figurate_numbers import (
    pentatope_numbers, k_dimensional_hypertetrahedron_numbers
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
