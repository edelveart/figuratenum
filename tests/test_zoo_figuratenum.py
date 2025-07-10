# python -m pytest tests/test_multidimensional_figuratenum.py

from src.figuratenum.zoo_figurate_numbers.ZooFigurateNum import ZooFigurateNum
zfgn = ZooFigurateNum()


def test_cuban_prime():
    num_generator = zfgn.cuban_prime()
    infinite_seq = []
    for _ in range(1, 51):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [7, 19, 37, 61, 91, 127, 169, 217, 271, 331,
                            397, 469, 547, 631, 721, 817, 919, 1027, 1141, 1261, 1387, 1519, 1657, 1801, 1951,
                            2107, 2269, 2437, 2611, 2791, 2977, 3169, 3367, 3571, 3781, 3997, 4219, 4447, 4681, 4921, 5167, 5419, 5677, 5941, 6211, 6487, 6769, 7057, 7351, 7651]


def test_pell():
    num_generator = zfgn.pell()
    infinite_seq = []
    for _ in range(1, 36):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741,
                            13_860, 33_461, 80_782, 195_025, 470_832, 1_136_689,
                            2_744_210, 6_625_109, 15_994_428, 38_613_965, 93_222_358,
                            225_058_681, 543_339_720, 1_311_738_121, 3_166_815_962,
                            7_645_370_045, 18_457_556_052, 44_560_482_149, 107_578_520_350,
                            259_717_522_849, 627_013_566_048, 1_513_744_654_945, 3_654_502_875_938]
