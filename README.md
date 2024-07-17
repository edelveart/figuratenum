# FigurateNum

![PyPI - Version](https://img.shields.io/pypi/v/figuratenum)
![GitHub License](https://img.shields.io/github/license/edelveart/figuratenum)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/figuratenum)
![PyPI - Status](https://img.shields.io/pypi/status/figuratenum)


FigurateNum is a set of **figurate number generators** based on the book [Figurate Numbers (2012)](https://books.google.com.pe/books/about/Figurate_Numbers.html?id=cDxYdstLPz4C&redir_esc=y) by Michel Deza and Elena Deza.

FigurateNum generates the following types of **infinite sequences**:

- [x] 74 sequences of plane figurate numbers
- [x] 83 sequences of space figurate numbers
- [x] 68 sequences of multidimensional figurate numbers

## What is the purpose of FigurateNum?

FigurateNum facilitates the discovery of new patterns among sequences and enables various numerical calculations in mathematical projects and related endeavors. It can be integrated with other software to visualize the geometric objects described. Moreover, it serves as a valuable companion to the book!

## How to install?

```py
pip install figuratenum
```
* It is advisable to use a virtual environment.

## How to import figuratenum?

```py
import figuratenum as fgn
```

## How to use?

```py
>>> seq = fgn.hyperdodecahedral_numbers()

>>> first = next(seq)
>>> second = next(seq)
>>> third = next(seq)
>>> fourth = next(seq)

>>> print(first, second, third, fourth)
1 600 4983 19468
```

You could get a list of numbers using a loop:

```py
>>> generator = fgn.k_dimensional_centered_hypertetrahedron_numbers(21)
>>> sequence = []
>>> for _ in range(1, 15):
>>>     next_num = next(generator)
>>>     sequence.append(next_num)

>>> print(sequence)
[1, 23, 276, 2300, 14950, 80730, 376740, 1560780, 5852925, 20160075, 64512240, 193536720, 548354040, 1476337800]
```

Equivalently, using the array module:

```py
import array as arr_num

>>> generator = fgn.aztec_diamond_numbers()
>>> sequence = arr_num.array('i')
>>> for _ in range(1, 15):
>>>     next_num = next(generator)
>>>     sequence.append(next_num)

>>> print(sequence)
array('i', [4, 12, 24, 40, 60, 84, 112, 144, 180, 220, 264, 312, 364, 420])
```

## Plane figurate numbers

1. `polygonal_numbers`
2. `triangular_numbers`
3. `square_numbers`
4. `pentagonal_numbers`
5. `hexagonal_numbers`
6. `heptagonal_numbers`
7. `octagonal_numbers`
8. `nonagonal_numbers`
9.  `decagonal_numbers`
10. `hendecagonal_numbers`
11. `dodecagonal_numbers`
12. `tridecagonal_numbers`
13. `tetradecagonal_numbers`
14. `pentadecagonal_numbers`
15. `hexadecagonal_numbers`
16. `heptadecagonal_numbers`
17. `octadecagonal_numbers`
18. `nonadecagonal_numbers`
19. `icosagonal_numbers`
20. `icosihenagonal_numbers`
21. `icosidigonal_numbers`
22. `icositrigonal_numbers`
23. `icositetragonal_numbers`
24. `icosipentagonal_numbers`
25. `icosihexagonal_numbers`
26. `icosiheptagonal_numbers`
27. `icosioctagonal_numbers`
28. `icosinonagonal_numbers`
29. `triacontagonal_numbers`
30. `centered_triangular_numbers`
31. `centered_square_numbers` = `diamond numbers`
32. `centered_pentagonal_numbers`
33. `centered_hexagonal_numbers`
34. `centered_heptagonal_numbers`
35. `centered_octagonal_numbers`
36. `centered_nonagonal_numbers`
37. `centered_decagonal_numbers`
38. `centered_hendecagonal_numbers`
39. `centered_dodecagonal_numbers` = `star_numbers`
40. `centered_tridecagonal_numbers`
41. `centered_tetradecagonal_numbers`
42. `centered_pentadecagonal_numbers`
43. `centered_hexadecagonal_numbers`
44. `centered_heptadecagonal_numbers`
45. `centered_octadecagonal_numbers`
46. `centered_nonadecagonal_numbers`
47. `centered_icosagonal_numbers`
48. `centered_icosihenagonal_numbers`
49. `centered_icosidigonal_numbers`
50. `centered_icositrigonal_numbers`
51. `centered_icositetragonal_numbers`
52. `centered_icosipentagonal_numbers`
53. `centered_icosihexagonal_numbers`
54. `centered_icosiheptagonal_numbers`
55. `centered_icosioctagonal_numbers`
56. `centered_icosinonagonal_numbers`
57. `centered_triacontagonal_numbers`
58. `centered_mgonal_numbers`
59. `pronic_numbers` = `heteromecic_numbers = oblong_numbers`
60. `polite_numbers`
61. `impolite_numbers`
62. `cross_numbers`
63. `aztec_diamond_numbers`
64. `polygram_numbers(m)` = `centered_star_polygonal_numbers(m)`
65. `pentagram_numbers`
66. `gnomic_numbers`
67. `truncated_triangular_numbers`
68. `truncated_square_numbers`
69. `truncated_pronic_numbers`
70. `truncated_centered_pol_numbers(m)` = `truncated_centered_mgonal_numbers(m)`
71. `truncated_centered_hexagonal_numbers` = `truncated_hex_numbers`
72. `generalized_mgonal_numbers(m, start_numb)`
73. `generalized_centered_pol_numbers(m, start_numb)`
74. `generalized_pronic_numbers(start_numb)`

## Space figurate numbers

1. `m_pyramidal_numbers(m)`
2. `triangular_pyramidal_numbers`
3. `square_pyramidal_numbers` = `pyramidal_numbers`
4. `pentagonal_pyramidal_numbers`
5. `hexagonal_pyramidal_numbers`
6. `heptagonal_pyramidal_numbers`
7. `octagonal_pyramidal_numbers`
8. `nonagonal_pyramidal_numbers`
9. `decagonal_pyramidal_numbers`
10. `hendecagonal_pyramidal_numbers`
11. `dodecagonal_pyramidal_numbers`
12. `tridecagonal_pyramidal_numbers`
13. `tetradecagonal_pyramidal_numbers`
14. `pentadecagonal_pyramidal_numbers`
15. `hexadecagonal_pyramidal_numbers`
16. `heptadecagonal_pyramidal_numbers`
17. `octadecagonal_pyramidal_numbers`
18. `nonadecagonal_pyramidal_numbers`
19. `icosagonal_pyramidal_numbers`
20. `icosihenagonal_pyramidal_numbers`
21. `icosidigonal_pyramidal_numbers`
22. `icositrigonal_pyramidal_numbers`
23. `icositetragonal_pyramidal_numbers`
24. `icosipentagonal_pyramidal_numbers`
25. `icosihexagonal_pyramidal_numbers`
26. `icosiheptagonal_pyramidal_numbers`
27. `icosioctagonal_pyramidal_numbers`
28. `icosinonagonal_pyramidal_numbers`
29. `triacontagonal_pyramidal_numbers`
30. `cubic_numbers`
31. `tetrahedral_numbers`
32. `octahedral_numbers`
33. `dodecahedral_numbers`
34. `icosahedral_numbers`
35. `truncated_tetrahedral_numbers`
36. `truncated_cubic_numbers`
37. `truncated_octahedral_numbers`
38. `stella_octangula_numbers`
39. `centered_cube_numbers`
40. `rhombic_dodecahedral_numbers`
41. `hauy_rhombic_dodecahedral_numbers`
42. `centered_tetrahedron_numbers` = `centered_tetrahedral_numbers`
43. `centered_square_pyramid_numbers` = `centered_pyramid_numbers`
44. `centered_mgonal_pyramid_numbers(m)`
45. `centered_pentagonal_pyramid_numbers`
46. `centered_hexagonal_pyramid_numbers`
47. `centered_heptagonal_pyramid_numbers`
48. `centered_octagonal_pyramid_numbers`
49. `centered_octahedron_numbers`
50. `centered_icosahedron_numbers` = `centered_cuboctahedron_numbers`
51. `centered_dodecahedron_numbers`
52. `centered_truncated_tetrahedron_numbers`
53. `centered_truncated_cube_numbers`
54. `centered_truncated_octahedron_numbers`
55. `centered_mgonal_pyramidal_numbers(m)`
56. `centered_triangular_pyramidal_numbers`
57. `centered_square_pyramidal_numbers`
58. `centered_pentagonal_pyramidal_numbers`
59. `centered_heptagonal_pyramidal_numbers`
60. `centered_octagonal_pyramidal_numbers`
61. `centered_nonagonal_pyramidal_numbers`
62. `centered_decagonal_pyramidal_numbers`
63. `centered_hendecagonal_pyramidal_numbers`
64. `centered_dodecagonal_pyramidal_numbers`
65. `centered_hexagonal_pyramidal_numbers` = `hex_pyramidal_numbers`
66. `hexagonal_prism_numbers`
67. `mgonal_prism_numbers(m)`
68. `generalized_mgonal_pyramidal_numbers(m, start_num)`
69. `generalized_cubic_numbers(start_num)`
70. `generalized_octahedral_numbers(start_num)`
71. `generalized_icosahedral_numbers(start_num)`
72. `generalized_dodecahedral_numbers(start_num)`
73. `generalized_centered_cube_numbers(start_num)`
74. `generalized_centered_tetrahedron_numbers(start_num)`
75. `generalized_centered_square_pyramid_numbers(start_num)`
76. `generalized_rhombic_dodecahedral_numbers(start_num)`
77. `generalized_centered_mgonal_pyramidal_numbers(m, start_num)`
78. `generalized_mgonal_prism_numbers(m, start_num)`
79. `generalized_hexagonal_prism_numbers(start_num)`

## Multidimensional figurate numbers

1. `pentatope_numbers` = `hypertetrahedral_numbers` = `triangulotriangular_numbers`
2. `k_dimensional_hypertetrahedron_numbers(k)` = `k_hypertetrahedron_numbers(k)` = `regular_k_polytopic_numbers(k)` = `figurate_numbers_of_order_k(k)`
3. `five_dimensional_hypertetrahedron_numbers`
4. `six_dimensional_hypertetrahedron_numbers`
5. `biquadratic_numbers`
6. `k_dimensional_hypercube_numbers(k)` = `k_hypercube_numbers(k)`
7. `five_dimensional_hypercube_numbers`
8. `six_dimensional_hypercube_numbers`
9. `hyperoctahedral_numbers` = `hexadecachoron_numbers` = `four_cross_polytope_numbers` = `four_orthoplex_numbers`
10. `hypericosahedral_numbers` = `tetraplex_numbers` = `polytetrahedron_numbers` = `hexacosichoron_numbers`
11. `hyperdodecahedral_numbers` = `hecatonicosachoron_numbers` = `dodecaplex_numbers` = `polydodecahedron_numbers`
12. `polyoctahedral_numbers` = `icositetrachoron_numbers` = `octaplex_numbers` = `hyperdiamond_numbers`
13. `four_dimensional_hyperoctahedron_numbers`
14. `five_dimensional_hyperoctahedron_numbers`
15. `six_dimensional_hyperoctahedron_numbers`
16. `seven_dimensional_hyperoctahedron_numbers`
17. `eight_dimensional_hyperoctahedron_numbers`
18. `nine_dimensional_hyperoctahedron_numbers`
19. `ten_dimensional_hyperoctahedron_numbers`
20. `k_dimensional_hyperoctahedron_numbers(k)` = `k_cross_polytope_numbers(k)`
21. `four_dimensional_mgonal_pyramidal_numbers(m)` = `mgonal_pyramidal_numbers_of_the_second_order`
22. `four_dimensional_square_pyramidal_numbers`
23. `four_dimensional_pentagonal_pyramidal_numbers`
24. `four_dimensional_hexagonal_pyramidal_numbers`
25. `four_dimensional_heptagonal_pyramidal_numbers`
26. `four_dimensional_octagonal_pyramidal_numbers`
27. `four_dimensional_nonagonal_pyramidal_numbers`
28. `four_dimensional_decagonal_pyramidal_numbers`
29. `four_dimensional_hendecagonal_pyramidal_numbers`
30. `four_dimensional_dodecagonal_pyramidal_numbers`
31. `k_dimensional_mgonal_pyramidal_numbers(k, m)` = `mgonal_pyramidal_numbers_of_the_k_2_th_order(k, m)`
32. `five_dimensional_mgonal_pyramidal_numbers(m)`
33. `five_dimensional_square_pyramidal_numbers`
34. `five_dimensional_pentagonal_pyramidal_numbers`
35. `five_dimensional_hexagonal_pyramidal_numbers`
36. `five_dimensional_heptagonal_pyramidal_numbers`
37. `five_dimensional_octagonal_pyramidal_numbers`
38. `six_dimensional_mgonal_pyramidal_numbers(m)`
39. `six_dimensional_square_pyramidal_numbers`
40. `six_dimensional_pentagonal_pyramidal_numbers`
41. `six_dimensional_hexagonal_pyramidal_numbers`
42. `six_dimensional_heptagonal_pyramidal_numbers`
43. `six_dimensional_octagonal_pyramidal_numbers`
44. `centered_biquadratic_numbers`
45. `k_dimensional_centered_hypercube_numbers(k)`
46. `five_dimensional_centered_hypercube_numbers`
47. `six_dimensional_centered_hypercube_numbers`
48. `centered_polytope_numbers`
49. `k_dimensional_centered_hypertetrahedron_numbers(k)`
50. `five_dimensional_centered_hypertetrahedron_numbers`
51. `six_dimensional_centered_hypertetrahedron_numbers`
52. `centered_hyperoctahedral_numbers` = `orthoplex_numbers`
53. `nexus_numbers`
54. `k_dimensional_centered_hyperoctahedron_numbers(k)`
55. `five_dimensional_centered_hyperoctahedron_numbers`
56. `six_dimensional_centered_hyperoctahedron_numbers`
57. `generalized_pentatope_numbers`
58. `generalized_k_dimensional_hypertetrahedron_numbers(k = 5, start_num = 0)`
59. `generalized_biquadratic_numbers(start_num = 0)`
60. `generalized_k_dimensional_hypercube_numbers(k = 5, start_num = 0)`
61. `generalized_hyperoctahedral_numbers(start_num = 0)`
62. `generalized_k_dimensional_hyperoctahedron_numbers(k = 5, start_num = 0)`
63. `generalized_hyperdodecahedral_numbers(start_num = 0)`
64. `generalized_hypericosahedral_numbers(start_num = 0)`
65. `generalized_polyoctahedral_numbers(start_num = 0)`
66. `generalized_k_dimensional_mgonal_pyramidal_numbers(k, m, start_num = 0)`
67. `generalized_k_dimensional_centered_hypercube_numbers(k, start_num = 0)`
68. `generalized_nexus_numbers(start_num = 0)`

## Contributing

FigurateNumber is currently under development, and we warmly invite your contributions. Just **fork** the project and then submit a **pull request**:

- Sequences from Chapters 1, 2, and 3 of the book
- New sequences not included in the book: If you have new sequences, please provide the source.
- Tests, documentation and errata in the book

When making commits, please use the following conventional prefixes to indicate the nature of the changes: `feat`, `refactor`, `fix`, `docs`, and `test`.
