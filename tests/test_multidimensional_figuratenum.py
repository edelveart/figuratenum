# python -m pytest tests/test_multidimensional_figuratenum.py

from src.figuratenum.multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum

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


def test_k_dimensional_mgonal_pyramidal():
    num_generator = mfgn.k_dimensional_mgonal_pyramidal(9, 14)
    infinite_seq = []
    for _ in range(1, 20):
        next_number = next(num_generator)
        infinite_seq.append(next_number)
    assert infinite_seq == [1, 21, 165, 825, 3135, 9867, 27027, 66495,
                            150150, 316030, 627198, 1184118, 2141490,
                            3730650, 6288810, 10296594, 16425519, 25597275, 39056875]


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
