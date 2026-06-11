<h1 align="center"> FigurateNum </h1>

<p align="center">
  <em>Python library for generating and visualizing 235+ plane, space, and multidimensional figurate number sequences</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/figuratenum.png" width="800" alt="FigurateNum HeroImage">
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/figuratenum" alt="PyPI - Version">
  <img alt="Pepy Total Downloads" src="https://img.shields.io/pepy/dt/figuratenum">
  <a href="https://doi.org/10.5281/zenodo.18250313"><img src="https://zenodo.org/badge/825541958.svg" alt="DOI"></a>
  <img src="https://img.shields.io/pypi/status/figuratenum" alt="PyPI - Status">
  <img src="https://img.shields.io/pypi/wheel/figuratenum" alt="PyPI - Wheel">
  <img src="https://img.shields.io/github/license/edelveart/figuratenum" alt="GitHub License">
  <img src="https://img.shields.io/github/actions/workflow/status/edelveart/figuratenum/tests.yml" alt="GitHub Actions Workflow Status" >
</p>

FigurateNum implements **classical polygonal numbers, Platonic solids, and higher-dimensional figurate numbers**, grounded in [Elena Deza & Michel Deza (2012)](https://doi.org/10.1142/8188).

It offers two complementary visualization perspectives:

- **Phase portraits** of generating functions f(z): ℂ → ℂ in the complex plane, based on [Elias Wegert (2012)](https://doi.org/10.1007/978-3-0348-0180-5).
- **Modular patterns** in ℤₙ, inspired by [Rogelio Pérez Buendía (2025)](https://yoyontzin.substack.com/p/espirografos-orbitas-y-relojes), further explored through [Plouffe’s site](https://www.plouffe.fr/simon/cercles/circles.html), and generalized here for this family.

 > Sequence generators are stable; visualization modules are experimental.

## Quickstart

```bash
# Stable version (only generators)
pip install figuratenum

# Experimental version (ComplexViz and DiscreteViz)
# requires numpy, sympy, matplotlib
pip install figuratenum[figurate-viz]
```

<p align="center">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/complex-viz-example.png" width="400" alt="Example of ComplexViz and DiscreteViz Sequences">
</p>
<p align="center">
  <em>Phase portrait of a 4D centered hypertetrahedron (left) and a modular pattern of a 5D hyperoctahedron (right)</em>
</p>

### Minimal code example

```python
# Stable sequence generators
from figuratenum import FigurateNum

seq1 = FigurateNum().k_dim_centered_hypertetrahedron(4)
print([next(seq1) for _ in range(7)])
# [1, 7, 28, 210, 462, 923, 1709]

seq2 = FigurateNum().k_dim_hyperoctahedron(5)
print([next(seq2) for _ in range(7)])
# [1, 10, 51, 180, 501, 1182, 2471]


# Experimental visualization (requires numpy, sympy, matplotlib)
from figuratenum.figurate_viz import ComplexViz, DiscreteViz

# Phase portrait (ComplexViz)
c = ComplexViz()
c.visualize_multidim(
    "k_dim_centered_hypertetrahedron", k=4,
    cmap_color="cividis", disk_radius=2.0
)

# Modular pattern (DiscreteViz)
d = DiscreteViz()
d.visualize_multidim(
    "k_dim_hyperoctahedron", k=5, n_terms=704,
    circ_color="m", bg_color="k", num_text=False,
    num_color="g", ext_circle=True, rotate=-1
)
```

## Documentation

Full references are available in `docs/reference/` in this repository:

- [**Sequence Generators API Reference — Full Catalog**](https://github.com/edelveart/figuratenum/blob/main/docs/reference/sequences.md)
- [**ComplexViz API Reference**](https://github.com/edelveart/figuratenum/blob/main/docs/reference/complexviz.md)
- [**DiscreteViz API Reference**](https://github.com/edelveart/figuratenum/blob/main/docs/reference/discreteviz.md)

External references and materials:

- [**Errata PDF: Figurate Numbers (2012)**](https://edelveart.github.io/resources-files/errata-figuratenum.pdf) — source `.tex` available in `docs/errata/errata-figuratenum.tex`
- [**PDF Cheatsheet**](https://edelveart.github.io/resources-files/cheatsheet/figuratenum/figuratenum-python-cheatsheet.pdf)

## Contributing

FigurateNum is under active development, and we warmly welcome your contributions.

## Citation

If you use FigurateNum in your research, thesis, or project, please cite it:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18250313.svg)](https://doi.org/10.5281/zenodo.18250313)
