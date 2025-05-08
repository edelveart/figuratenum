<h1 align="center"> FigurateNum </h1>

**FigurateNum** is a collection of **233 figurate number generators** based on the book [Figurate Numbers](https://books.google.com.pe/books/about/Figurate.html?id=cDxYdstLPz4C&redir_esc=y) by Michel Deza and Elena Deza, published in 2012.

<p align="center">
  <img src="https://img.shields.io/pypi/v/figuratenum" alt="PyPI - Version">
  <img src="https://img.shields.io/pypi/wheel/figuratenum" alt="PyPI - Wheel">
  <img alt="Pepy Total Downloads" src="https://img.shields.io/pepy/dt/figuratenum">
  <img src="https://img.shields.io/pypi/status/figuratenum" alt="PyPI - Status">
  <img src="https://img.shields.io/github/license/edelveart/figuratenum" alt="GitHub License">
</p>

![figuratenumber-social-image](https://raw.githubusercontent.com/edelveart/figuratenum/main/figuratenum.png)

## What is the purpose of FigurateNum?

**FigurateNum** facilitates the discovery of new patterns among sequences and enables various numerical calculations in mathematical projects and related applications. It can be integrated with other software to visualize the geometric objects described. Moreover, it serves as a valuable companion to the book.

## How to install?

```py
pip install figuratenum
```

🚨 Version **2.0.0** includes **renamed methods and changes in class usage**. These changes are **incompatible with previous versions**. Please review the updated usage instructions below to adapt your code to the new structure.

## Features

FigurateNum generates the following categories of **infinite sequences**:

- [x] 79 sequences of plane figurate numbers  [Explore all sequences](#plane-figurate-numbers)
- [x] 86 sequences of space figurate numbers [Explore all sequences](#space-figurate-numbers)
- [x] 68 sequences of multidimensional figurate numbers [Explore all sequences](#multidimensional-figurate-numbers)

During the development of this package, errata were identified in *Figurate Numbers (2012)*. The corresponding corrections are available [here](#errata-for-figurate-numbers-2012).

## How to use?

### 1. Import all sequences via the `FigurateNum` class
```py
from figuratenum import FigurateNum as fgn
```

```py
>>> seq = fgn()
>>> hyperdodecahedral = seq.hyperdodecahedral()

>>> first = next(hyperdodecahedral)
>>> second = next(hyperdodecahedral)
>>> third = next(hyperdodecahedral)
>>> fourth = next(hyperdodecahedral)

>>> print(first, second, third, fourth)
1 600 4983 19468
```

### 2. Import sequences through specialized classes: Plane, Space, and Multidimensional

```py
# from figuratenum import PlaneFigurateNum as pfgn
# from figuratenum import SpacedimensionalFigurateNum as sfgn
from figuratenum import MultidimensionalFigurateNum as mfgn
```

```py
>>> seq_loop = mfgn()
>>> k_dimensional_centered_hypertetrahedron = seq_loop.k_dimensional_centered_hypertetrahedron(21)

>>> figuratenum_arr = []
>>> for _ in range(1, 15):
>>>     next_num = next(k_dimensional_centered_hypertetrahedron)
>>>     figuratenum_arr.append(next_num)

>>> print(figuratenum_arr)
[1, 23, 276, 2300, 14950, 80730, 376740, 1560780, 5852925, 20160075, 64512240, 193536720, 548354040, 1476337800]
```

### 3. Using the `NumCollector` class for sequence collection

```py
from figuratenum import NumCollector as nc
```

Importing the `NumCollector` class allows you to use practical methods to return lists, tuples or arrays with the requested number of elements:

- `take(n)`
- `take_to_list(stop, start, step)`
- `take_to_array(stop, start, step)`
- `take_to_tuple(stop, start, step)`
- `pick(n)`

```py
>>> seq = fgn()
>>> pentatope = seq.pentatope()

>>> print(nc.take_to_list(pentatope, 10))
[1, 5, 15, 35, 70, 126, 210, 330, 495, 715]
```

## Plane figurate numbers

1. `polygonal`
2. `triangular`
3. `square`
4. `pentagonal`
5. `hexagonal`
6. `heptagonal`
7. `octagonal`
8. `nonagonal`
9.  `decagonal`
10. `hendecagonal`
11. `dodecagonal`
12. `tridecagonal`
13. `tetradecagonal`
14. `pentadecagonal`
15. `hexadecagonal`
16. `heptadecagonal`
17. `octadecagonal`
18. `nonadecagonal`
19. `icosagonal`
20. `icosihenagonal`
21. `icosidigonal`
22. `icositrigonal`
23. `icositetragonal`
24. `icosipentagonal`
25. `icosihexagonal`
26. `icosiheptagonal`
27. `icosioctagonal`
28. `icosinonagonal`
29. `triacontagonal`
30. `centered_triangular`
31. `centered_square` = `diamond numbers`
32. `centered_pentagonal`
33. `centered_hexagonal`
34. `centered_heptagonal`
35. `centered_octagonal`
36. `centered_nonagonal`
37. `centered_decagonal`
38. `centered_hendecagonal`
39. `centered_dodecagonal` = `star`
40. `centered_tridecagonal`
41. `centered_tetradecagonal`
42. `centered_pentadecagonal`
43. `centered_hexadecagonal`
44. `centered_heptadecagonal`
45. `centered_octadecagonal`
46. `centered_nonadecagonal`
47. `centered_icosagonal`
48. `centered_icosihenagonal`
49. `centered_icosidigonal`
50. `centered_icositrigonal`
51. `centered_icositetragonal`
52. `centered_icosipentagonal`
53. `centered_icosihexagonal`
54. `centered_icosiheptagonal`
55. `centered_icosioctagonal`
56. `centered_icosinonagonal`
57. `centered_triacontagonal`
58. `centered_mgonal(m)`
59. `pronic` = `heteromecic = oblong`
60. `polite`
61. `impolite`
62. `cross`
63. `aztec_diamond`
64. `polygram(m)` = `centered_star_polygonal(m)`
65. `pentagram`
66. `gnomic`
67. `truncated_triangular`
68. `truncated_square`
69. `truncated_pronic`
70. `truncated_centered_pol(m)` = `truncated_centered_mgonal(m)`
71. `truncated_centered_triangular`
72. `truncated_centered_square`
73. `truncated_centered_pentagonal`
74. `truncated_centered_hexagonal` = `truncated_hex`
75. `generalized_mgonal(m, start_numb)`
76. `generalized_pentagonal(start_numb)`
77. `generalized_hexagonal(start_numb)`
78. `generalized_centered_pol(m, start_numb)`
79. `generalized_pronic(start_numb)`

## Space figurate numbers

1. `m_pyramidal(m)`
2. `triangular_pyramidal`
3. `square_pyramidal` = `pyramidal`
4. `pentagonal_pyramidal`
5. `hexagonal_pyramidal`
6. `heptagonal_pyramidal`
7. `octagonal_pyramidal`
8. `nonagonal_pyramidal`
9. `decagonal_pyramidal`
10. `hendecagonal_pyramidal`
11. `dodecagonal_pyramidal`
12. `tridecagonal_pyramidal`
13. `tetradecagonal_pyramidal`
14. `pentadecagonal_pyramidal`
15. `hexadecagonal_pyramidal`
16. `heptadecagonal_pyramidal`
17. `octadecagonal_pyramidal`
18. `nonadecagonal_pyramidal`
19. `icosagonal_pyramidal`
20. `icosihenagonal_pyramidal`
21. `icosidigonal_pyramidal`
22. `icositrigonal_pyramidal`
23. `icositetragonal_pyramidal`
24. `icosipentagonal_pyramidal`
25. `icosihexagonal_pyramidal`
26. `icosiheptagonal_pyramidal`
27. `icosioctagonal_pyramidal`
28. `icosinonagonal_pyramidal`
29. `triacontagonal_pyramidal`
30. `triangular_tetrahedral[finite]`
31. `triangular_square_pyramidal[finite]`
32. `square_tetrahedral[finite]`
33. `square_square_pyramidal[finite]`
34. `tetrahedral_square_pyramidal[finite]`
35. `cubic`
36. `tetrahedral`
37. `octahedral`
38. `dodecahedral`
39. `icosahedral`
40. `truncated_tetrahedral`
41. `truncated_cubic`
42. `truncated_octahedral`
43. `stella_octangula`
44. `centered_cube`
45. `rhombic_dodecahedral`
46. `hauy_rhombic_dodecahedral`
47. `centered_tetrahedron` = `centered_tetrahedral`
48. `centered_square_pyramid` = `centered_pyramid`
49. `centered_mgonal_pyramid(m)`
50. `centered_pentagonal_pyramid`
51. `centered_hexagonal_pyramid`
52. `centered_heptagonal_pyramid`
53. `centered_octagonal_pyramid`
54. `centered_octahedron`
55. `centered_icosahedron` = `centered_cuboctahedron`
56. `centered_dodecahedron`
57. `centered_truncated_tetrahedron`
58. `centered_truncated_cube`
59. `centered_truncated_octahedron`
60. `centered_mgonal_pyramidal(m)`
61. `centered_triangular_pyramidal`
62. `centered_square_pyramidal`
63. `centered_pentagonal_pyramidal`
64. `centered_heptagonal_pyramidal`
65. `centered_octagonal_pyramidal`
66. `centered_nonagonal_pyramidal`
67. `centered_decagonal_pyramidal`
68. `centered_hendecagonal_pyramidal`
69. `centered_dodecagonal_pyramidal`
70. `centered_hexagonal_pyramidal` = `hex_pyramidal`
71. `hexagonal_prism`
72. `mgonal_prism(m)`
73. `generalized_mgonal_pyramidal(m, start_num)`
74. `generalized_pentagonal_pyramidal(start_num)`
75. `generalized_hexagonal_pyramidal(start_num)`
76. `generalized_cubic(start_num)`
77. `generalized_octahedral(start_num)`
78. `generalized_icosahedral(start_num)`
79. `generalized_dodecahedral(start_num)`
80. `generalized_centered_cube(start_num)`
81. `generalized_centered_tetrahedron(start_num)`
82. `generalized_centered_square_pyramid(start_num)`
83. `generalized_rhombic_dodecahedral(start_num)`
84. `generalized_centered_mgonal_pyramidal(m, start_num)`
85. `generalized_mgonal_prism(m, start_num)`
86. `generalized_hexagonal_prism(start_num)`

## Multidimensional figurate numbers

1. `k_dimensional_hypertetrahedron(k)` = `k_hypertetrahedron(k)` = `regular_k_polytopic(k)` = `figurate_of_order_k(k)`
2. `five_dimensional_hypertetrahedron`
3. `six_dimensional_hypertetrahedron`
4. `k_dimensional_hypercube(k)` = `k_hypercube(k)`
5. `five_dimensional_hypercube`
6. `six_dimensional_hypercube`
7. `hypertetrahedral` = `pentachoron` = `pentatope` = `triangulotriangular` = `cell_5`
8. `hypercube` = `octachoron` = `tesseract` = `biquadratic` = `cell_8`
9. `hyperoctahedral` = `hexadecachoron` = `four_cross_polytope` = `four_orthoplex` = `cell_16`
10. `hypericosahedral` = `hexacosichoron` = `polytetrahedron` = `tetraplex` = `cell_600`
11. `hyperdodecahedral` = `hecatonicosachoron` = `dodecaplex` = `polydodecahedron` = `cell_120`
12. `polyoctahedral` = `icositetrachoron` = `octaplex` = `hyperdiamond` = `cell_24`
13. `four_dimensional_hyperoctahedron`
14. `five_dimensional_hyperoctahedron`
15. `six_dimensional_hyperoctahedron`
16. `seven_dimensional_hyperoctahedron`
17. `eight_dimensional_hyperoctahedron`
18. `nine_dimensional_hyperoctahedron`
19. `ten_dimensional_hyperoctahedron`
20. `k_dimensional_hyperoctahedron(k)` = `k_cross_polytope(k)`
21. `four_dimensional_mgonal_pyramidal(m)` = `mgonal_pyramidal_of_the_second_order(m)`
22. `four_dimensional_square_pyramidal`
23. `four_dimensional_pentagonal_pyramidal`
24. `four_dimensional_hexagonal_pyramidal`
25. `four_dimensional_heptagonal_pyramidal`
26. `four_dimensional_octagonal_pyramidal`
27. `four_dimensional_nonagonal_pyramidal`
28. `four_dimensional_decagonal_pyramidal`
29. `four_dimensional_hendecagonal_pyramidal`
30. `four_dimensional_dodecagonal_pyramidal`
31. `k_dimensional_mgonal_pyramidal(k, m)` = `mgonal_pyramidal_of_the_k_2_th_order(k, m)`
32. `five_dimensional_mgonal_pyramidal(m)`
33. `five_dimensional_square_pyramidal`
34. `five_dimensional_pentagonal_pyramidal`
35. `five_dimensional_hexagonal_pyramidal`
36. `five_dimensional_heptagonal_pyramidal`
37. `five_dimensional_octagonal_pyramidal`
38. `six_dimensional_mgonal_pyramidal(m)`
39. `six_dimensional_square_pyramidal`
40. `six_dimensional_pentagonal_pyramidal`
41. `six_dimensional_hexagonal_pyramidal`
42. `six_dimensional_heptagonal_pyramidal`
43. `six_dimensional_octagonal_pyramidal`
44. `centered_biquadratic`
45. `k_dimensional_centered_hypercube(k)`
46. `five_dimensional_centered_hypercube`
47. `six_dimensional_centered_hypercube`
48. `centered_polytope`
49. `k_dimensional_centered_hypertetrahedron(k)`
50. `five_dimensional_centered_hypertetrahedron`
51. `six_dimensional_centered_hypertetrahedron`
52. `centered_hyperoctahedral` = `orthoplex`
53. `nexus(k)`
54. `k_dimensional_centered_hyperoctahedron(k)`
55. `five_dimensional_centered_hyperoctahedron`
56. `six_dimensional_centered_hyperoctahedron`
57. `generalized_pentatope(start_num = 0)`
58. `generalized_k_dimensional_hypertetrahedron(k = 5, start_num = 0)`
59. `generalized_biquadratic(start_num = 0)`
60. `generalized_k_dimensional_hypercube(k = 5, start_num = 0)`
61. `generalized_hyperoctahedral(start_num = 0)`
62. `generalized_k_dimensional_hyperoctahedron(k = 5, start_num = 0)`
63. `generalized_hyperdodecahedral(start_num = 0)`
64. `generalized_hypericosahedral(start_num = 0)`
65. `generalized_polyoctahedral(start_num = 0)`
66. `generalized_k_dimensional_mgonal_pyramidal(k, m, start_num = 0)`
67. `generalized_k_dimensional_centered_hypercube(k, start_num = 0)`
68. `generalized_nexus(start_num = 0)`


## Errata for *Figurate Numbers (2012)*

This section lists the errata and corrections for the book *Figurate Numbers (2012)* by Michel Deza and Elena Deza. If you find any errors in the content, please feel free to contribute corrections.

- Chapter 1, formula in the table on page 6 says:

  | Name   | Formula             |     |
  | ------ | ------------------- | --- |
  | Square | `1/2 (n^2 - 0 * n)` |     |


  It should be:
  | Name   | Formula              |     |
  | ------ | -------------------- | --- |
  | Square | `1/2 (2n^2 - 0 * n)` |     |

- Chapter 1, formula in the table on page 51 says:

  | Name                 | Formula               |                       |
  | -------------------- | --------------------- | --------------------- |
  | Cent. icosihexagonal | `1/3n^2 - 13 * n + 1` | `546, 728, 936, 1170` |


  It should be:
  | Name                 | Formula           |                       |
  | -------------------- | ----------------- | --------------------- |
  | Cent. icosihexagonal | `13n^2 - 13n + 1` | `547, 729, 937, 1171` |

- Chapter 1, formula in the table on page 51 says:

  | Name                  | Formula |       |
  | --------------------- | ------- | ----- |
  | Cent. icosiheptagonal |         | `972` |


  It should be:
  | Name                  | Formula |       |
  | --------------------- | ------- | ----- |
  | Cent. icosiheptagonal |         | `973` |

- Chapter 1, formula in the table on page 51 says:

  | Name                 | Formula |      |
  | -------------------- | ------- | ---- |
  | Cent. icosioctagonal |         | `84` |


  It should be:
  | Name                 | Formula |      |
  | -------------------- | ------- | ---- |
  | Cent. icosioctagonal |         | `85` |

- Chapter 1, page 65 (polite numbers) says:
  > `inpolite numbers`

  It should read:

  > `impolite numbers`

- Chapter 1, formula (truncated centered pentagonal numbers) on  page 72 says:
  > `TCSS_5(n) = (35n^2 - 55n) / 2 + 3`

  It should be:
  > `TCSS_5(n) = (35n^2 - 55n) / 2 + 11`

- Chapter 2, formula of octagonal pyramidal number on  page 92 says:
  > `n(n+1)(6n-1) / 6`

  It should be:
  > `n(n+1)(6n-3) / 6`

- Chapter 2, page 140 says:
  > centered square pyramidal numbers are 1, 6, 19, 44, 85, 111, 146, 231, ...

  This sequence must exclude the number 111:

  > centered square pyramidal numbers are 1, 6, 19, 44, 85, ~~111~~, 146, 231, ...

- Chapter 2, page 155 (generalized centered tetrahedron numbers) says:
  > `S_3^3(n) = ((2n - 1)(n^2 + n + 3)) / 3`

  Formula must have a negative sign:

  > `S_3^3(n) = ((2n - 1)(n^2 - n + 3)) / 3`

- Chapter 2, page 156 (generalized centered square pyramid numbers) says:
  > `S_4^3(n) = ((2n - 1) * (n^2 - n + 2)^2) / 3`

  Formula must write:

  > `S_4^3(n) = ((2n - 1) * (n^2 - n + 2)) / 2`

- Chapter 3, page 188 (hyperoctahedral numbers) says:
  > `hexadecahoron numbers`

  It should read:

  > `hexadecachoron numbers`

- Chapter 3, page 190 (hypericosahedral numbers) says:
  > `hexacisihoron numbers`

  It should read:

  > `hexacosichoron numbers`


## Contributing

FigurateNumber is currently under development, and we warmly invite your contributions. Just **fork** the project and then submit a **pull request**:

- Sequences from Chapters 1, 2, and 3 of the book
- New sequences not included in the book: If you have new sequences, please provide the source.
- Tests, documentation and errata in the book

When making commits, please use the following conventional prefixes to indicate the nature of the changes: `feat`, `refactor`, `fix`, `docs`, and `test`.
