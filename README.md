<h1 align="center"> FigurateNum </h1>

**FigurateNum** is a collection of **235 figurate number generators** based on the book [Figurate Numbers](https://books.google.com.pe/books/about/Figurate.html?id=cDxYdstLPz4C&redir_esc=y) by Michel Deza and Elena Deza, published in 2012.

<p align="center">
  <img src="https://img.shields.io/pypi/v/figuratenum" alt="PyPI - Version">
  <img src="https://img.shields.io/pypi/wheel/figuratenum" alt="PyPI - Wheel">
  <img alt="Pepy Total Downloads" src="https://img.shields.io/pepy/dt/figuratenum">
  <img src="https://img.shields.io/pypi/status/figuratenum" alt="PyPI - Status">
  <img src="https://img.shields.io/github/license/edelveart/figuratenum" alt="GitHub License">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/figuratenum.png" width="400">
</p>

## What is the purpose of FigurateNum?

**FigurateNum** helps discover patterns in figurate number sequences and supports numerical computation in mathematics-related projects. It integrates with other tools for visualizing geometric structures and serves as a companion to the book.

## How to install?

```bash
pip install figuratenum
```

### Optional: Graphical Visualization (v2.1.0)

Enable the `FigurateViz` class (requires `numpy` and `matplotlib`) by installing the optional dependencies:

```bash
pip install figuratenum[figurate-viz]
```

<p align="center">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/example_fgn_1.svg" width="300" alt="Example of Gaussian Graph Visualization">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/example_fgn_2.svg" width="300" alt="Example of Gaussian Graph Visualization">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/example_fgn_3.svg" width="300" alt="Example of Gaussian Graph Visualization">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/example_fgn_4.svg" width="300" alt="Example of Gaussian Graph Visualization">
</p>

## Features

The main class, `FigurateNum`, provides access to all figurate number sequences across different **dimensions**, while dedicated classes let you work with each dimension separately:

- 79 Plane figurate numbers → `PlaneFigurateNum` class — [Explore on GitHub](https://github.com/edelveart/figuratenum#plane-figurate-numbers)
- 86 Space figurate numbers → `SpaceFigurateNum` class — [Explore on GitHub](https://github.com/edelveart/figuratenum#space-figurate-numbers)
- 68 Multidimensional figurate numbers → `MultidimensionalFigurateNum` class — [Explore on GitHub](https://github.com/edelveart/figuratenum#multidimensional-figurate-numbers)
- 2 Zoo figurate numbers → `ZooFigurateNum` class — [Explore on GitHub](https://github.com/edelveart/figuratenum#zoo-figurate-numbers)

### FigurateViz Visualization

- Gaussian plots (2D) in polar coordinates with customizable colors, visibility options, and export capabilities.
- Seamless integration with any figurate number sequence (`list[int]` or `tuple[int, ...]`).

---

## How to use?

### 1. Import and generate sequences with `FigurateNum` and related classes

```python
from figuratenum import FigurateNum, MultidimensionalFigurateNum

# 1. General use: generate any figurate sequence via FigurateNum
seq = FigurateNum()
hyperdodecahedral_gen = seq.hyperdodecahedral()
print([next(hyperdodecahedral_gen) for _ in range(4)])
# Output: [1, 600, 4983, 19468]

# 2. Specialized classes: PlaneFigurateNum, SpaceFigurateNum,
#    MultidimensionalFigurateNum, ZooFigurateNum
multi = MultidimensionalFigurateNum()
hypertetrahedron_gen = multi.k_dimensional_centered_hypertetrahedron(21)
print([next(hypertetrahedron_gen) for _ in range(12)])
# Output: [1, 23, 276, 2300, 14950, 80730, 376740,
#          1560780, 5852925, 20160075, 64512240, 193536720]
```

### 2. Using `FigurateViz` to visualize and export

```python
from figuratenum import FigurateNum as fgn
from figuratenum.figurate_viz.FigurateViz import FigurateViz

# Generate figurate numbers
seq_loop = fgn()
gen = seq_loop.five_dimensional_hyperoctahedron()
figuratenum_seq = [next(gen) for _ in range(704)]

# Create and draw the Gaussian plot
viz = FigurateViz(figuratenum_seq, figsize=(6, 6))
viz.gaussian_plot(
    circ_color="m", bg_color="k", num_text=False,
    num_color="g", ext_circle=True, rotate=-1
).draw()

# Export plots as .svg, .pdf, .png (matplotlib compatible),
# with options e.g., dpi, transparent, bbox_inches, pad_inches, etc.
viz.export_plot(
    "figure1.svg", circ_color="cyan",
    transparent=True
)
```

### 3. Get sequence values easily with `NumCollector`

```python
from figuratenum import NumCollector as nc, FigurateNum

gen = FigurateNum().pentatope()
print(nc.take_to_tuple(gen, 10))  # first 10 values as tuple
# Output: (1, 5, 15, 35, 70, 126, 210, 330, 495, 715)

# Available methods:
# - take(n)               : first n values as iterator
# - take_to_list(stop, start=0, step=1)
# - take_to_tuple(stop, start=0, step=1)
# - take_to_array(stop, start=0, step=1)
# - pick(n)               : nth value
```

### Version History
> 🚨 Version **2.0.0** includes **renamed methods and changes in class usage**. These changes are **incompatible with previous versions**. Please review the updated usage instructions below to adapt your code to the new structure.

### Additional Resources

- [PDF Cheatsheet with LaTeX commands and examples](https://edelveart.github.io/resources-files/cheatsheet/figuratenum/figuratenum-python-cheatsheet.pdf).
- [Errata *Figurate Numbers (2012)*](https://github.com/edelveart/figuratenum#errata-for-figurate-numbers-2012).

---

## List of Figurate Numbers

### Plane Figurate Numbers

<details>
<summary>Show 79 sequences of the <code>PlaneFigurateNum</code> class</summary>

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
31. `centered_square` = `diamond`
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
</details>

### Space Figurate Numbers

<details>
<summary>Show 86 sequences of the <code>SpaceFigurateNum</code> class</summary>

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
</details>

### Multidimensional Figurate Numbers

<details>
<summary>Show 68 sequences of the <code>MultidimensionalFigurateNum</code> class</summary>

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
68. `generalized_nexus(k, start_num = 0)`
</details>

### Zoo Figurate Numbers

<details>
<summary>Show 2 sequences of the <code>ZooFigurateNum</code> class</summary>

1. `cuban_prime`
2. `pell`
</details>

---

## Errata for *Figurate Numbers (2012)*

<details>
<summary>Show errata and corrections</summary>

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

    | Name                 | Formula            |                       |
    | -------------------- | ------------------ | --------------------- |
    | Cent. icosihexagonal | `1/3n^2 - 13n + 1` | `546, 728, 936, 1170` |

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
  > `S_4^3(n) = ((2n - 1)(n^2 - n + 2)^2) / 3`

  Formula must write:

  > `S_4^3(n) = ((2n - 1)(n^2 - n + 2)) / 2`

- Chapter 3, page 188 (hyperoctahedral numbers) says:
  > `hexadecahoron numbers`

  It should read:

  > `hexadecachoron numbers`

- Chapter 3, page 190 (hypericosahedral numbers) says:
  > `hexacisihoron numbers`

  It should read:

  > `hexacosichoron numbers`

</details>

---

## Contributing

FigurateNum is currently under development, and we warmly invite your contributions. Just **fork** the project and then submit a **pull request**:

- Sequences from Chapters 1, 2, and 3 of the book
- New sequences not included in the book: If you have new sequences, please provide the source.
- Tests, documentation and errata in the book

When making commits, please use the following conventional prefixes to indicate the nature of the changes: `feat`, `refactor`, `fix`, `docs`, and `test`.
