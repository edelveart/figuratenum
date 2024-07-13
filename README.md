# FigurateNum

FigurateNum is a set of figurate number generators based on the book [Figurate Numbers (2012)](https://books.google.com.pe/books/about/Figurate_Numbers.html?id=cDxYdstLPz4C&redir_esc=y) by Michel Deza and Elena Deza.

It contains in total:
- [x] 20 plane figurate numbers
- [x] 38 space figurate numbers
- [x] 18 multidimensional figurate numbers

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

>>> generator = fgn.k_dimensional_centered_hypertetrahedron_numbers(21)
>>> sequence = arr_num.array('i')
>>> for _ in range(1, 15):
>>>     next_num = next(generator)
>>>     sequence.append(next_num)

>>> print(sequence)
array('i', [4, 12, 24, 40, 60, 84, 112, 144, 180, 220, 264, 312, 364, 420])
```


## Plane figurate numbers

1. `polygonal_numbers`
2. `centered_square_numbers` = `diamond numbers`
3. `centered_dodecagonal_numbers` = `star_numbers`
4. `centered_mgonal_numbers`
5. `pronic_numbers` = `heteromecic_numbers = oblong_numbers`
6. `polite_numbers`
7. `impolite_numbers`
8. `cross_numbers`
9.  `aztec_diamond_numbers`
10. `polygram_numbers(m)` = `centered_star_polygonal_numbers(m)`
11. `pentagram_numbers`
12. `gnomic_numbers`
13. `truncated_triangular_numbers`
14. `truncated_square_numbers`
15. `truncated_pronic_numbers`
16. `truncated_centered_pol_numbers(m)` = `truncated_centered_pol_numbers(m)`
17. `truncated_centered_hexagonal_numbers` = `truncated_hex_numbers`
18. `generalized_mgonal_numbers(m, start_numb)`
19. `generalized_centered_pol_numbers(m, start_numb)`
20. `generalized_pronic_numbers(start_numb)`

## Space figurate numbers

1. `m_pyramidal_numbers(m)`
2. `cubic_numbers`
3. `tetrahedral_numbers`
4. `octahedral_numbers`
5. `dodecahedral_numbers`
6. `icosahedral_numbers`
7. `truncated_tetrahedral_numbers`
8. `truncated_cubic_numbers`
9. `truncated_octahedral_numbers`
10. `stella_octangula_numbers`
11. `centered_cube_numbers`
12. `rhombic_dodecahedral_numbers`
13. `hauy_rhombic_dodecahedral_numbers`
14. `centered_tetrahedron_numbers` = `centered_tetrahedral_numbers`
15. `centered_square_pyramid_numbers` = `centered_pyramid_numbers`
16. `centered_mgonal_pyramid_numbers(m)`
17. `centered_octahedron_numbers`
18. `centered_icosahedron_numbers` = `centered_cuboctahedron_numbers`
19. `centered_dodecahedron_numbers`
20. `centered_truncated_tetrahedron_numbers`
21. `centered_truncated_cube_numbers`
22. `centered_truncated_octahedron_numbers`
23. `centered_mgonal_pyramidal_numbers(m)`
24. `centered_hexagonal_pyramidal_numbers` = `hex_pyramidal_numbers`
25. `hexagonal_prism_numbers`
26. `mgonal_prism_numbers(m)`
27. `generalized_mgonal_pyramidal_numbers(m, start_num)`
28. `generalized_cubic_numbers(start_num)`
29. `generalized_octahedral_numbers(start_num)`
30. `generalized_icosahedral_numbers(start_num)`
31. `generalized_dodecahedral_numbers(start_num)`
32. `generalized_centered_cube_numbers(start_num)`
33. `generalized_centered_tetrahedron_numbers(start_num)`
34. `generalized_centered_square_pyramid_numbers(start_num)`
35. `generalized_rhombic_dodecahedral_numbers(start_num)`
36. `generalized_centered_mgonal_pyramidal_numbers(m, start_num)`
37. `generalized_mgonal_prism_numbers(m, start_num)`
38. `generalized_hexagonal_prism_numbers(start_num)`

## Multidimensional figurate numbers

1. `pentatope_numbers` = `hypertetrahedral_numbers` = `triangulotriangular_numbers`
2. `k_dimensional_hypertetrahedron_numbers(k)` = `k_hypertetrahedron_numbers(k)` = `regular_k_polytopic_numbers(k)` = `figurate_numbers_of_order_k(k)`
3. `biquadratic_numbers`
4. `k_dimensional_hypercube_numbers(k)` = `k_hypercube_numbers(k)`
5. `hyperoctahedral_numbers` = `hexadecachoron_numbers` = `four_cross_polytope_numbers` = `four_orthoplex_numbers`
6. `hypericosahedral_numbers` = `tetraplex_numbers` = `polytetrahedron_numbers` = `hexacosichoron_numbers`
7. `hyperdodecahedral_numbers` = `hecatonicosachoron_numbers` = `dodecaplex_numbers` = `polydodecahedron_numbers`
8. `polyoctahedral_numbers` = `icositetrachoron_numbers` = `octaplex_numbers` = `hyperdiamond_numbers`
9. `k_dimensional_hyperoctahedron_numbers(k)` = `k_cross_polytope_numbers(k)`
10. `four_dimensional_mgonal_pyramidal_numbers(m)` = `mgonal_pyramidal_numbers_of_the_second_order`
11. `k_dimensional_mgonal_pyramidal_numbers(k, m)` = `mgonal_pyramidal_numbers_of_the_k_2_th_order(k, m)`
12. `centered_biquadratic_numbers`
13. `k_dimensional_centered_hypercube_numbers(k)`
14. `centered_polytope_numbers`
15. `k_dimensional_centered_hypertetrahedron_numbers(k)`
16. `centered_hyperoctahedral_numbers` = `orthoplex_numbers`
17. `nexus_numbers`
18. `k_dimensional_centered_hyperoctahedron_numbers(k)`

## License

[MIT](https://github.com/edelveart/figuratenum/blob/main/LICENSE)


