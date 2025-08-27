# python -m pytest tests/test_multidimensional_figuratenum.py

from src.figuratenum.multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum
from src.figuratenum.NumCollector import NumCollector as nc
mfgn = MultidimensionalFigurateNum()


def test_pentatope():
    num_generator = mfgn.pentatope()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 5, 15, 35, 70, 126, 210, 330, 495,
                            715, 1001, 1365, 1820, 2380, 3060, 3876, 4845, 5985, 7315]


def test_k_dimensional_hypertetrahedron():
    num_generator = mfgn.k_dimensional_hypertetrahedron(21)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 22, 253, 2024, 12650, 65780, 296010, 1184040, 4292145, 14307150, 44352165,
                            129024480, 354817320, 927983760, 2319959400, 5567902560, 12875774670, 28781143380, 62359143990]


def test_five_dimensional_hypertetrahedron():
    gen = mfgn.five_dimensional_hypertetrahedron()
    result = [next(gen) for _ in range(20)]
    expected = [1, 6, 21, 56, 126, 252, 462, 792, 1287, 2002, 3003,
                4368, 6188, 8568, 11628, 15504, 20349, 26334, 33649, 42504]
    assert result == expected


def test_six_dimensional_hypertetrahedron():
    gen = mfgn.six_dimensional_hypertetrahedron()
    result = [next(gen) for _ in range(20)]
    expected = [1, 7, 28, 84, 210, 462, 924, 1716, 3003, 5005, 8008,
                12376, 18564, 27132, 38760, 54264, 74613, 100947, 134596, 177100]
    assert result == expected


def test_biquadratic():
    num_generator = mfgn.biquadratic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 16, 81, 256, 625, 1296, 2401, 4096, 6561,
                            10000, 14641, 20736, 28561, 38416, 50625, 65536, 83521, 104976, 130321]


def test_k_dimensional_hypercube():
    num_generator = mfgn.k_dimensional_hypercube(16)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 65536, 43046721, 4294967296, 152587890625,
                            2821109907456, 33232930569601, 281474976710656, 1853020188851841, 10000000000000000, 45949729863572161, 184884258895036416, 665416609183179841, 2177953337809371136, 6568408355712890625, 18446744073709551616, 48661191875666868481, 121439531096594251776, 288441413567621167681]


def test_five_dimensional_hypercube():
    gen = mfgn.five_dimensional_hypercube()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049, 100000,
        161051, 248832, 371293, 537824, 759375, 1048576, 1419857,
        1889568, 2476099, 3200000, 4084101, 5153632, 6436343, 7962624, 9765625
    ]
    assert result == expected


def test_six_dimensional_hypercube():
    gen = mfgn.six_dimensional_hypercube()
    result = [next(gen) for _ in range(25)]
    expected = [
        1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441, 1000000,
        1771561, 2985984, 4826809, 7529536, 11390625, 16777216, 24137569,
        34012224, 47045881, 64000000, 85766121, 113379904, 148035889, 191102976, 244140625
    ]
    assert result == expected


def test_hyperoctahedral():
    num_generator = mfgn.hyperoctahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 8, 33, 96, 225, 456, 833, 1408, 2241,
                            3400, 4961, 7008, 9633, 12936, 17025, 22016, 28033, 35208, 43681]


def test_hypericosahedral():
    num_generator = mfgn.hypericosahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 120, 947, 3652, 9985, 22276, 43435, 76952, 126897, 197920,
                            295251, 424700, 592657, 806092, 1072555, 1400176, 1797665, 2274312, 2839987]


def test_hyperdodecahedral():
    num_generator = mfgn.hyperdodecahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 600, 4983, 19468, 53505, 119676, 233695, 414408, 683793, 1066960,
                            1592151, 2290740, 3197233, 4349268, 5787615, 7556176, 9701985, 12275208, 15329143]


def test_polyoctahedral():
    num_generator = mfgn.polyoctahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 24, 153, 544, 1425, 3096, 5929, 10368, 16929,
                            26200, 38841, 55584, 77233, 104664, 138825, 180736, 231489, 292248, 364249]


def test_four_dimensional_hyperoctahedron():
    gen = mfgn.four_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(50)]
    expected = [
        1, 8, 33, 96, 225, 456, 833, 1408, 2241, 3400, 4961, 7008, 9633, 12936, 17025,
        22016, 28033, 35208, 43681, 53600, 65121, 78408, 93633, 110976, 130625, 152776,
        177633, 205408, 236321, 270600, 308481, 350208, 396033, 446216, 501025, 560736,
        625633, 696008, 772161, 854400, 943041, 1038408, 1140833, 1250656, 1368225,
        1493896, 1628033, 1771008, 1923201, 2085000
    ]
    assert result == expected


def test_five_dimensional_hyperoctahedron():
    gen = mfgn.five_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(50)]
    expected = [
        1, 10, 51, 180, 501, 1182, 2471, 4712, 8361, 14002, 22363, 34332, 50973, 73542,
        103503, 142544, 192593, 255834, 334723, 432004, 550725, 694254, 866295, 1070904,
        1312505, 1595906, 1926315, 2309356, 2751085, 3258006, 3837087, 4495776, 5242017,
        6084266, 7031507, 8093268, 9279637, 10601278, 12069447, 13696008, 15493449,
        17474898, 19654139, 22045628, 24664509, 27526630, 30648559, 34047600, 37741809,
        41750010
    ]
    assert result == expected


def test_six_dimensional_hyperoctahedron():
    gen = mfgn.six_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(50)]
    expected = [
        1, 12, 73, 304, 985, 2668, 6321, 13504, 26577, 48940, 85305, 142000, 227305, 351820,
        528865, 774912, 1110049, 1558476, 2149033, 2915760, 3898489, 5143468, 6704017,
        8641216, 11024625, 13933036, 17455257, 21690928, 26751369, 32760460, 39855553,
        48188416, 57926209, 69252492, 82368265, 97493040, 114865945, 134746860, 157417585,
        183183040, 212372497, 245340844, 282469881, 324169648, 370879785, 423070924,
        481246113, 545942272, 617731681, 697223500
    ]
    assert result == expected


def test_seven_dimensional_hyperoctahedron():
    gen = mfgn.seven_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(10)]
    expected = [1, 14, 99, 476, 1765, 5418, 14407, 34232, 74313, 149830]
    assert result == expected


def test_eight_dimensional_hyperoctahedron():
    gen = mfgn.eight_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(10)]
    expected = [1, 16, 129, 704, 2945, 10128, 29953, 78592, 187137, 411280]
    assert result == expected


def test_nine_dimensional_hyperoctahedron():
    gen = mfgn.nine_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(10)]
    expected = [1, 18, 163, 996, 4645, 17718, 57799, 166344, 432073, 1030490]
    assert result == expected


def test_ten_dimensional_hyperoctahedron():
    gen = mfgn.ten_dimensional_hyperoctahedron()
    result = [next(gen) for _ in range(10)]
    expected = [1, 20, 201, 1360, 7001, 29364, 104881, 329024, 927441, 2390004]
    assert result == expected


def test_k_dimensional_hyperoctahedron():
    num_generator = mfgn.k_dimensional_hyperoctahedron(27)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 54, 1459, 26316, 356725, 3878946, 35267239, 275940504,
                            1897865641, 11663134350, 64878791131, 330159018084,
                            1550594372509, 6771089488506, 27667653828175, 106374643269936,
                            386682074864209, 1334658881073894, 4390658718085891]


def test_four_dimensional_mgonal_pyramidal():
    num_generator = mfgn.four_dimensional_mgonal_pyramidal(11)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 13, 55, 155, 350, 686, 1218, 2010, 3135,
                            4675, 6721, 9373, 12740, 16940, 22100,
                            28356, 35853, 44745, 55195]


def test_four_dimensional_square_pyramidal():
    gen = mfgn.four_dimensional_square_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 6, 20, 50, 105, 196, 336, 540, 825, 1210]
    assert result == expected


def test_four_dimensional_pentagonal_pyramidal():
    gen = mfgn.four_dimensional_pentagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 7, 25, 65, 140, 266, 462, 750, 1155, 1705]
    assert result == expected


def test_four_dimensional_hexagonal_pyramidal():
    gen = mfgn.four_dimensional_hexagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 8, 30, 80, 175, 336, 588, 960, 1485, 2200]
    assert result == expected


def test_four_dimensional_heptagonal_pyramidal():
    gen = mfgn.four_dimensional_heptagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 9, 35, 95, 210, 406, 714, 1170, 1815, 2695]
    assert result == expected


def test_four_dimensional_octagonal_pyramidal():
    gen = mfgn.four_dimensional_octagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 10, 40, 110, 245, 476, 840, 1380, 2145, 3190]
    assert result == expected


def test_four_dimensional_nonagonal_pyramidal():
    gen = mfgn.four_dimensional_nonagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 11, 45, 125, 280, 546, 966, 1590, 2475, 3685]
    assert result == expected


def test_four_dimensional_decagonal_pyramidal():
    gen = mfgn.four_dimensional_decagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 12, 50, 140, 315, 616, 1092, 1800, 2805, 4180]
    assert result == expected


def test_four_dimensional_hendecagonal_pyramidal():
    gen = mfgn.four_dimensional_hendecagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 13, 55, 155, 350, 686, 1218, 2010, 3135, 4675]
    assert result == expected


def test_four_dimensional_dodecagonal_pyramidal():
    gen = mfgn.four_dimensional_dodecagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 14, 60, 170, 385, 756, 1344, 2220, 3465, 5170]
    assert result == expected


def test_k_dimensional_mgonal_pyramidal():
    num_generator = mfgn.k_dimensional_mgonal_pyramidal(9, 14)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 165, 825, 3135, 9867, 27027, 66495,
                            150150, 316030, 627198, 1184118, 2141490,
                            3730650, 6288810, 10296594, 16425519, 25597275, 39056875]


def test_five_dimensional_square_pyramidal():
    gen = mfgn.five_dimensional_square_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 7, 27, 77, 182, 378, 714, 1254, 2079, 3289]
    assert result == expected


def test_five_dimensional_pentagonal_pyramidal():
    gen = mfgn.five_dimensional_pentagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 8, 33, 98, 238, 504, 966, 1716, 2871, 4576]
    assert result == expected


def test_five_dimensional_hexagonal_pyramidal():
    gen = mfgn.five_dimensional_hexagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 9, 39, 119, 294, 630, 1218, 2178, 3663, 5863]
    assert result == expected


def test_five_dimensional_heptagonal_pyramidal():
    gen = mfgn.five_dimensional_heptagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 10, 45, 140, 350, 756, 1470, 2640, 4455, 7150]
    assert result == expected


def test_five_dimensional_octagonal_pyramidal():
    gen = mfgn.five_dimensional_octagonal_pyramidal()
    result = [next(gen) for _ in range(10)]
    expected = [1, 11, 51, 161, 406, 882, 1722, 3102, 5247, 8437]
    assert result == expected


def test_six_dimensional_square_pyramidal():
    gen = mfgn.six_dimensional_square_pyramidal()
    result = [next(gen) for _ in range(15)]
    expected = [1, 8, 35, 112, 294, 672, 1386, 2640, 4719, 8008,
                13013, 20384, 30940, 45696, 65892]
    assert result == expected


def test_six_dimensional_pentagonal_pyramidal():
    gen = mfgn.six_dimensional_pentagonal_pyramidal()
    result = [next(gen) for _ in range(15)]
    expected = [1, 9, 42, 140, 378, 882, 1848, 3564, 6435, 11011,
                18018, 28392, 43316, 64260, 93024]
    assert result == expected


def test_six_dimensional_hexagonal_pyramidal():
    gen = mfgn.six_dimensional_hexagonal_pyramidal()
    result = [next(gen) for _ in range(15)]
    expected = [1, 10, 49, 168, 462, 1092, 2310, 4488, 8151, 14014,
                23023, 36400, 55692, 82824, 120156]
    assert result == expected


def test_six_dimensional_heptagonal_pyramidal():
    gen = mfgn.six_dimensional_heptagonal_pyramidal()
    result = [next(gen) for _ in range(15)]
    expected = [1, 11, 56, 196, 546, 1302, 2772, 5412, 9867, 17017,
                28028, 44408, 68068, 101388, 147288]
    assert result == expected


def test_six_dimensional_octagonal_pyramidal():
    gen = mfgn.six_dimensional_octagonal_pyramidal()
    result = [next(gen) for _ in range(15)]
    expected = [1, 12, 63, 224, 630, 1512, 3234, 6336, 11583, 20020,
                33033, 52416, 80444, 119952, 174420]
    assert result == expected


def test_six_dimensional_mgonal_pyramidal():
    gen = mfgn.six_dimensional_mgonal_pyramidal(16)
    result = [next(gen) for _ in range(45)]
    expected = [1, 20, 119, 448, 1302, 3192, 6930, 13728, 25311, 44044,
                73073, 116480, 179452, 268464, 391476, 558144, 780045,
                1070916, 1446907, 1926848, 2532530, 3289000, 4224870,
                5372640, 6769035, 8455356, 10477845, 12888064, 15743288,
                19106912, 23048872, 27646080, 32982873, 39151476, 46252479,
                54395328, 63698830, 74291672, 86312954, 99912736, 115252599,
                132506220, 151859961, 173513472, 197680308]
    assert result == expected


def test_centered_biquadratic():
    num_generator = mfgn.centered_biquadratic()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 17, 97, 337, 881, 1921, 3697,
                            6497, 10657, 16561, 24641, 35377, 49297,
                            66977, 89041, 116161, 149057, 188497, 235297]


def test_k_dimensional_centered_hypercube():
    num_generator = mfgn.k_dimensional_centered_hypercube(31)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 2147483649, 617675543767595, 4612303691823671851,
                            4661224559095819966029, 1331100131197477539976781,
                            159101825553170206762441399, 10061295696317888005808036535, 391423944791228873827842892601, 10381520424476945831628649898809, 201943424957750480504146841291811, 3040459190554988156451550338468899, 36908459133046522160894572124006725, 372879996344233620392121690040396101, 3215085941470045635934544974294425839, 24143913821051915266488283417366372591, 160556565271409668427878930453953233649, 958597790281111140865704883498649895665, 5198174612988969212268967734721914749851]


def test_five_dimensional_centered_hypercube():
    gen = mfgn.five_dimensional_centered_hypercube()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 33, 275, 1267, 4149, 10_901, 24_583, 49_575, 91_817, 159_049,
        261_051, 409_883, 620_125, 909_117, 1_297_199, 1_807_951,
        2_468_433, 3_309_425, 4_365_667, 5_676_099
    ]
    assert result == expected


def test_six_dimensional_centered_hypercube():
    gen = mfgn.six_dimensional_centered_hypercube()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 65, 793, 4825, 19_721, 62_281, 164_305, 379_793, 793_585,
        1_531_441, 2_771_561, 4_757_545, 7_812_793, 12_356_345, 18_920_161,
        28_167_841, 40_914_785, 58_149_793, 81_058_105, 111_045_881
    ]
    assert result == expected


def test_centered_polytope():
    num_generator = mfgn.centered_polytope()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 6, 21, 56, 126, 251, 456, 771,
                            1231, 1876, 2751, 3906, 5396, 7281,
                            9626, 12501, 15981, 20146, 25081]


def test_k_dimensional_centered_hypertetrahedron():
    num_generator = mfgn.k_dimensional_centered_hypertetrahedron(9)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 11, 66, 286, 1001, 3003, 8008,
                            19448, 43758, 92378, 184755, 352705,
                            646580, 1143780, 1960255, 3265757,
                            5303727, 8416837, 13079352]


def test_five_dimensional_centered_hypertetrahedron():
    gen = mfgn.five_dimensional_centered_hypertetrahedron()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 7, 28, 84, 210, 462, 923, 1709, 2975, 4921,
        7798, 11_914, 17_640, 25_416, 35_757, 49_259,
        66_605, 88_571, 116_032, 149_968
    ]
    assert result == expected


def test_six_dimensional_centered_hypertetrahedron():
    gen = mfgn.six_dimensional_centered_hypertetrahedron()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 8, 36, 120, 330, 792, 1716, 3431, 6427, 11_404,
        19_328, 31_494, 49_596, 75_804, 112_848, 164_109,
        233_717, 326_656, 448_876, 607_412
    ]
    assert result == expected


def test_centered_hyperoctahedral():
    num_generator = mfgn.centered_hyperoctahedral()
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 9, 41, 129, 321, 681, 1289, 2241, 3649,
                            5641, 8361, 11969, 16641, 22569, 29961,
                            39041, 50049, 63241, 78889]


def test_nexus():
    num_generator = mfgn.nexus(7)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 255, 6305, 58975, 325089, 1288991, 4085185,
                            11012415, 26269505, 56953279, 114358881, 215622815,
                            385749025, 660058335, 1087101569, 1732076671,
                            2680790145, 4044203135, 5963602465]


def test_k_dimensional_centered_hyperoctahedron():
    num_generator = mfgn.k_dimensional_centered_hyperoctahedron(43)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 87, 3785, 109823, 2391489, 41699767, 606639529,
                            7575405375, 82913343041, 808229343063, 7106217293385,
                            56938472541375, 419317958443905, 2858763388855095,
                            18154539163583145, 107964506311713663, 604076883535802241,
                            3193065939329541975, 16003669096765488329]


def test_five_dimensional_centered_hyperoctahedron():
    gen = mfgn.five_dimensional_centered_hyperoctahedron()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 11, 61, 231, 681, 1683, 3653, 7183, 13_073, 22_363,
        36_365, 56_695, 85_305, 124_515, 177_045, 246_047,
        335_137, 448_427, 590_557, 766_727
    ]
    assert result == expected


def test_six_dimensional_centered_hyperoctahedron():
    gen = mfgn.six_dimensional_centered_hyperoctahedron()
    result = [next(gen) for _ in range(20)]
    expected = [
        1, 13, 85, 377, 1289, 3653, 8989, 19_825, 40_081, 75_517,
        134_245, 227_305, 369_305, 579_125, 880_685, 1_303_777,
        1_884_961, 2_668_525, 3_707_509, 5_064_793
    ]
    assert result == expected


def test_generalized_pentatope():
    result = nc.take_to_list(mfgn.generalized_pentatope(-18), 40)
    expected = [
        3060, 2380, 1820, 1365, 1001, 715, 495, 330, 210, 126, 70, 35, 15, 5, 1, 0, 0, 0, 0, 1, 5, 15, 35, 70, 126, 210,
        330, 495, 715, 1001, 1365, 1820, 2380, 3060, 3876, 4845, 5985, 7315, 8855, 10626
    ]
    assert result == expected


def test_generalized_k_dimensional_hypertetrahedron():
    result = nc.take_to_list(
        mfgn.generalized_k_dimensional_hypertetrahedron(17, -23), 45)
    expected = [
        -100947, -26334, -5985, -1140, -171, -18, -
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 18, 171, 1140,
        5985, 26334, 100947, 346104, 1081575, 3124550, 8436285, 21474180, 51895935, 119759850, 265182525, 565722720,
        1166803110, 2333606220, 4537567650, 8597496600, 15905368710
    ]
    assert result == expected


def test_generalized_biquadratic():
    result = nc.take_to_list(mfgn.generalized_biquadratic(), 20)
    expected = [
        0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 14641, 20736, 28561, 38416, 50625, 65536, 83521, 104976,
        130321
    ]
    assert result == expected


def test_generalized_k_dimensional_hypercube():
    result = nc.take_to_list(
        mfgn.generalized_k_dimensional_hypercube(19, -23), 45)
    expected = [
        -74_615_470_927_590_710_561_908_487, -32_064_977_213_018_365_645_815_808, -13_248_496_640_331_026_125_580_781, -5_242_880_000_000_000_000_000_000, -1_978_419_655_660_313_589_123_979, -708_235_345_355_337_676_357_632, -239_072_435_685_151_324_847_153, -75_557_863_725_914_323_419_136, -22_168_378_200_531_005_859_375, -5_976_303_958_948_914_397_184, -1_461_920_290_375_446_110_677, -319_479_999_370_622_926_848, -61_159_090_448_414_546_291, -10_000_000_000_000_000_000, -1_350_851_717_672_992_089, -144_115_188_075_855_872, -11_398_895_185_373_143, -609_359_740_010_496, -19_073_486_328_125, -
        274_877_906_944, -1_162_261_467, -524_288, -1, 0, 1, 524_288, 1_162_261_467, 274_877_906_944, 19_073_486_328_125, 609_359_740_010_496, 11_398_895_185_373_143, 144_115_188_075_855_872, 1_350_851_717_672_992_089, 10_000_000_000_000_000_000, 61_159_090_448_414_546_291, 319_479_999_370_622_926_848, 1_461_920_290_375_446_110_677, 5_976_303_958_948_914_397_184, 22_168_378_200_531_005_859_375, 75_557_863_725_914_323_419_136, 239_072_435_685_151_324_847_153, 708_235_345_355_337_676_357_632, 1_978_419_655_660_313_589_123_979, 5_242_880_000_000_000_000_000_000, 13_248_496_640_331_026_125_580_781
    ]
    assert result == expected


def test_generalized_hyperoctahedral():
    result = nc.take_to_list(mfgn.generalized_hyperoctahedral(), 20)
    expected = [
        0, 1, 8, 33, 96, 225, 456, 833, 1408, 2241,
        3400, 4961, 7008, 9633, 12936, 17025, 22016, 28033, 35208, 43681
    ]
    assert result == expected


def test_generalized_k_dimensional_hyperoctahedron():
    result = nc.take_to_list(
        mfgn.generalized_k_dimensional_hyperoctahedron(16, -23), 45)
    expected = [
        15671921130497, 8025697116448, 3998179870209, 1933232552320, 905007786497, 409008911904, 177880832001,
        74174404608, 29532022785, 11172756000, 3994294785, 1340645760, 419239425, 121040160, 31910913, 7579136,
        1594369, 290592, 44545, 5504, 513, 32, 1, 0, 1, 32, 513, 5504, 44545, 290592, 1594369, 7579136, 31910913,
        121040160, 419239425, 1340645760, 3994294785, 11172756000, 29532022785, 74174404608, 177880832001,
        409008911904, 905007786497, 1933232552320, 3998179870209
    ]
    assert result == expected


def test_generalized_hyperdodecahedral():
    result = nc.take_to_list(mfgn.generalized_hyperdodecahedral(-20), 40)
    expected = [
        22952980, 18786801, 15215220, 12178783, 9621168, 7489185, 5732776, 4305015, 3162108, 2263393, 1571340,
        1051551, 672760, 406833, 228768, 116695, 51876, 18705, 4708, 543, 0, 1, 600, 4983, 19468, 53505, 119676,
        233695, 414408, 683793, 1066960, 1592151, 2290740, 3197233, 4349268, 5787615, 7556176, 9701985, 12275208,
        15329143
    ]
    assert result == expected


def test_generalized_hypericosahedral():
    result = nc.take_to_list(mfgn.generalized_hypericosahedral(-20), 40)
    expected = [
        4252060, 3480401, 2818860, 2256427, 1782672, 1387745, 1062376, 797875, 586132, 419617,
        291380, 195051, 124840, 75537, 42512, 21715, 9676, 3505, 892, 107, 0, 1, 120, 947, 3652, 9985, 22276, 43435,
        76952, 126897, 197920, 295251, 424700, 592657, 806092, 1072555, 1400176, 1797665, 2274312, 2839987
    ]
    assert result == expected


def test_generalized_polyoctahedral():
    result = nc.take_to_list(mfgn.generalized_polyoctahedral(-20), 40)
    expected = [
        512800, 419121, 338904, 270793, 213504, 165825, 126616, 94809, 69408, 49489,
        34200, 22761, 14464, 8673, 4824, 2425, 1056, 369, 88, 9,
        0, 1, 24, 153, 544, 1425, 3096, 5929, 10368, 16929,
        26200, 38841, 55584, 77233, 104664, 138825, 180736, 231489, 292248, 364249
    ]
    assert result == expected


def test_generalized_k_dimensional_mgonal_pyramidal():
    result = nc.take_to_list(
        mfgn.generalized_k_dimensional_mgonal_pyramidal(7, 8, -10), 20)
    expected = [
        -1770, -636, -188, -41, -5, 0, 0, 0, 0, 0,
        0, 1, 13, 76, 300, 930, 2442, 5676, 12012, 23595
    ]
    assert result == expected


def test_generalized_k_dimensional_centered_hypercube():
    result = nc.take_to_list(
        mfgn.generalized_k_dimensional_centered_hypercube(7, -10), 20)
    expected = [
        -29487171, -14782969, -6880121, -2920695, -
        1103479, -358061, -94509, -18571, -2315, -129,
        -1, 1, 129, 2315, 18571, 94509, 358061, 1103479, 2920695, 6880121
    ]
    assert result == expected


def test_generalized_nexus():
    result = nc.take_to_list(mfgn.generalized_nexus(23, -17), 40)
    expected = [
        -260220508800347567049960166785, -
        62394050318236105019081059711, -13619912495610491637711803009,
        -2671398930043370423979492255, -
        463303923170979668638153825, -69647114527583233038729695,
        -8849732675807611094711841, -920233556923127490136639, -75044076594002864649665,
        -4530785251489078799295, -186842850042244797505, -4678776693546226271,
        -59323169798679969, -281192547174175, -282412759265, -
        16777215, -1, 1, 16777215, 282412759265,
        281192547174175, 59323169798679969, 4678776693546226271, 186842850042244797505,
        4530785251489078799295, 75044076594002864649665, 920233556923127490136639,
        8849732675807611094711841, 69647114527583233038729695, 463303923170979668638153825,
        2671398930043370423979492255, 13619912495610491637711803009, 62394050318236105019081059711,
        260220508800347567049960166785, 998810173737782797796233865855, 3560504085908452115276557294945,
        11878453069039153182283704722079, 37330982377272584130510593262881, 111142894267009681649466420951775,
        314999671352219711010188742728385
    ]
    assert result == expected
