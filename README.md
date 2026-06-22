<h1 align="center">FigurateNum</h1>

<p align="center">
    <em>FigurateNum generates and visualizes 235+ plane, space, and multidimensional figurate number sequences and families</em>
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

<p align="center">
  <a href="https://edelveart.github.io/figuratenum/">Documentation</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/edelveart/figuratenum/tree/main/docs/reference">API Reference</a>
</p>

From polygonal numbers to Platonic solids and higher-dimensional analogues, **FigurateNum** unifies **235+** sequences and families of figurate numbers, following [Deza & Deza (2012)](https://doi.org/10.1142/8188).

## Gallery

<p align="center">
  <img src="https://raw.githubusercontent.com/edelveart/figuratenum/main/docs/images/figuratenum-gallery.webp" width="500" alt="Phase portraits and modular patterns generated with FigurateNum">
</p>

<p align="center">
  <em>Phase portraits in ℂ and modular patterns in ℤₙ, generated with the code below.</em>
</p>

## Quickstart

> Core sequence generators are stable. Visualization modules remain experimental.

```bash
# Stable release (sequence generators only)
pip install figuratenum

# Experimental visualization (ComplexViz and DiscreteViz)
# Requires: numpy, sympy, matplotlib
pip install figuratenum[figurate-viz]
```

### Sequence generators

```python
from figuratenum import FigurateNum

seq1 = FigurateNum().k_dim_centered_hypertetrahedron(4)
print([next(seq1) for _ in range(7)])
# [1, 7, 28, 210, 462, 923, 1709]

seq2 = FigurateNum().k_dim_hyperoctahedron(5)
print([next(seq2) for _ in range(7)])
# [1, 10, 51, 180, 501, 1182, 2471]
```

### Visualization

- **Phase portraits** of generating functions f(z): ℂ → ℂ in the complex plane, based on [Elias Wegert (2012)](https://doi.org/10.1007/978-3-0348-0180-5).
- **Modular patterns** in ℤₙ, inspired by [Rogelio Pérez Buendía (2025)](https://yoyontzin.substack.com/p/espirografos-orbitas-y-relojes), generalized here for this family.

```python
from figuratenum.figurate_viz import ComplexViz, DiscreteViz

# Phase portrait of the generating function f(z) in ℂ
c = ComplexViz()
c.visualize_multidim(
    "k_dim_centered_hypertetrahedron", k=4,
    cmap_color="cividis", disk_radius=2.0
)

# Modular pattern in ℤₙ
d = DiscreteViz()
d.visualize_multidim(
    "k_dim_hyperoctahedron", k=5, n_terms=704,
    circ_color="m", bg_color="k", num_text=False,
    num_color="g", ext_circle=True, rotate=-1
)
```

## Mathematical background

Sequences are organized by dimension:

- **Plane figurate numbers** (2D): polygonal, centered polygonal, pronic, and related forms, including their generalized variants.
- **Space figurate numbers** (3D): pyramidal, polyhedral (tetrahedral, cubic, octahedral, dodecahedral, icosahedral), and centered space forms, including their generalized variants.
- **Multidimensional figurate numbers** (4D and beyond): hypertetrahedra, hypercubes, hyperoctahedra, and their centered variants for arbitrary dimension `k`, including generalized forms.

## Documentation

| Resource                           | Link                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| Sequence Generators — Full Catalog | [sequences.md](https://github.com/edelveart/figuratenum/blob/main/docs/reference/sequences.md)     |
| ComplexViz API Reference           | [complexviz.md](https://github.com/edelveart/figuratenum/blob/main/docs/reference/complexviz.md)   |
| DiscreteViz API Reference          | [discreteviz.md](https://github.com/edelveart/figuratenum/blob/main/docs/reference/discreteviz.md) |


### Implementation Notes

> FigurateNum uses optimized implementations of figurate number formulas for performance, while preserving mathematically equivalent results. Original expressions from Deza & Deza (2012) are available via `*_from_book()` methods for reference and validation.

## Tests

Core sequence generators are validated against known closed-form values and classical results from number theory and OEIS.

## Contributing

FigurateNum is under active development. Contributions are welcome: fork the project and submit a pull request.

- New sequences, with a mathematical reference (OEIS, book, or paper).
- Tests for existing sequences.
- Documentation improvements.
- Errata corrections at [`docs/errata/errata-figuratenum.tex`](https://github.com/edelveart/figuratenum/blob/main/docs/errata/errata-figuratenum.tex).

When making commits, use conventional prefixes: `feat`, `refactor`, `fix`, `docs`, `test`.

## Citation

If you use FigurateNum in your research, thesis, or project, please cite it:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18250313.svg)](https://doi.org/10.5281/zenodo.18250313)

