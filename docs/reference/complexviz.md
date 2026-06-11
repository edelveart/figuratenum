# FigurateNum — ComplexViz API Reference

> Phase portrait visualization of complex-valued generating functions
> of figurate numbers, based on **Elias Wegert (2012)**.

---

## Overview

```text
Unified interface for evaluating and visualizing generating functions
of plane, space, and multidimensional figurate numbers, inspired by the style of Elias Wegert (2012).

References
----------
[1] Wegert, E. (2012). Visual Complex Functions: An Introduction
    with Phase Portraits. Birkhäuser Basel.
    https://doi.org/10.1007/978-3-0348-0180-5
```

---

## Constructor

```python
ComplexViz(
    resolution : int = 800,
    figsize : tuple[float, float] = (6, 6),
    plot_type : PlotType = 'enhanced_phase_portrait',
    cmap_color : str = 'hsv',
    brightness : float = 0.7,
    num_lines : int = 20,
    domain_grid_radius : float = 2.0,
    disk_radius : float | None = None,
    show_axes : bool = False,
)
```

```text
Initialize a ComplexViz instance.

Default configuration for phase portrait visualization of
complex-valued generating functions of figurate numbers.

Defaults are used unless overridden per method call.

Parameters
----------
resolution : int, default=800
    Default resolution of the evaluation grid.
figsize : tuple[float, float], default=(6, 6)
    Figure size in inches (width, height)
plot_type : {'pure_phase_portrait', 'phase_contours', 'modulus_contours', 'enhanced_phase_portrait'}, default='enhanced_phase_portrait'
    Type of plot to generate:
    - 'pure_phase_portrait': phase coloring only
    - 'phase_contours': phase coloring with contour lines
    - 'modulus_contours': phase coloring with modulus contours
    - 'enhanced_phase_portrait': combines phase and modulus contours
cmap_color : str, default='hsv'
    Default colormap for phase coloring.
brightness : float, default=0.7
    Base brightness for contours (0-1).
num_lines : int, default=20
    Default number of contour lines for phase and modulus.
disk_radius : float | None, default=None
    Radius of the circular masking region centered at (0, 0).
    Values outside this radius are excluded (set to transparent).
    Must be strictly positive if provided.
domain_grid_radius : float, default=2.0
    Half-width of the square evaluation domain centered at the origin.
show_axes : bool, default=False
    If True, displays the real (Re) and imaginary (Im) axes.
```

---

## Visualization Methods

### `visualize_plane`

```python
visualize_plane(
    name_seq : PlaneTypes,
    *,
    m : int | None = None,
    plot_type : PlotType | None = None,
    show : bool = True,
    **kwargs,
)
```

```text
Visualize the generating function of a plane figurate number in the complex plane (phase portrait).

Parameters
----------
name_seq : PlaneTypes
    Plane figurate number sequence defining its generating function f(z).
m : int | None
    Parameter controlling the evaluation of the sequence.
plot_type : PlotType, optional
    Overrides the default plot type of the instance.
show : bool, default=True
    Whether to display the plot immediately. If False, the plot is generated but not shown.
**kwargs : dict
    Per-call plot options. Can override instance defaults:
    - xlim : tuple[float, float], optional
        Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
    - ylim : tuple[float, float], optional
        Vertical limits of the complex plane. Overrides `domain_grid_radius`.
    - show_axes : bool, optional
        Whether to display the real (Re) and imaginary (Im) axes.
    - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

Returns
-------
matplotlib.figure.Figure
    The generated figure. Automatically displayed if `show=True`.
```


#### Sequence Reference — PlaneTypes

The `name_seq` parameter accepts values from the table below. Each name identifies a figurate number sequence.

Pass to `visualize_plane(name_seq=...)`.

| name_seq                        | name_seq                    | name_seq                        |
| ------------------------------- | --------------------------- | ------------------------------- |
| `polygonal`                     | `triangular`                | `square`                        |
| `pentagonal`                    | `hexagonal`                 | `centered_mgonal`               |
| `pronic`                        | `gnomonic`                  | `truncated_triangular`          |
| `truncated_square`              | `truncated_pronic`          | `truncated_centered_mgonal`     |
| `truncated_centered_triangular` | `truncated_centered_square` | `truncated_centered_pentagonal` |
| `truncated_centered_hexagonal`  | `polygram`                  | `aztec_diamond`                 |
| `cross`                         | `diamond`                   | `generalized_mgonal`            |
| `generalized_centered_mgonal`   | `generalized_pronic`        | `square_triangular`             |
| `pentagonal_triangular`         | `pentagonal_square`         | `hexagonal_square`              |
| `hexagonal_pentagonal`          | `heptagonal_triangular`     | `heptagonal_square`             |
| `heptagonal_pentagonal`         | `heptagonal_hexagonal`      | `octagonal_triangular`          |
| `octagonal_square`              | `octagonal_pentagonal`      | `octagonal_hexagonal`           |
| `octagonal_heptagonal`          | `nonagonal_triangular`      | `nonagonal_square`              |
| `nonagonal_pentagonal`          | `nonagonal_hexagonal`       | `nonagonal_heptagonal`          |
| `nonagonal_octagonal`           |                             |                                 |

---

### `visualize_space`

```python
visualize_space(
    name_seq : SpaceTypes,
    *,
    m : int | None = None,
    plot_type : PlotType | None = None,
    show : bool = True,
    **kwargs,
)
```

```text
Visualize the generating function of a space figurate number in the complex plane (phase portrait).

Parameters
----------
name_seq : SpaceTypes
    Space figurate number sequence defining its generating function f(z).
m : int | None
    Parameter controlling the evaluation of the sequence.
plot_type : PlotType, optional
    Overrides the default plot type of the instance.
show : bool, default=True
    Whether to display the plot immediately. If False, the plot is generated but not shown.
**kwargs : dict
    Per-call plot options. Can override instance defaults:
    - xlim : tuple[float, float], optional
        Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
    - ylim : tuple[float, float], optional
        Vertical limits of the complex plane. Overrides `domain_grid_radius`.
    - show_axes : bool, optional
        Whether to display the real (Re) and imaginary (Im) axes.
    - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

Returns
-------
matplotlib.figure.Figure
    The generated figure. Automatically displayed if `show=True`.
```


#### Sequence Reference — SpaceTypes

The `name_seq` parameter accepts values from the table below. Each name identifies a figurate number sequence.

Pass to `visualize_space(name_seq=...)`.

| name_seq                                | name_seq                              | name_seq                           |
| --------------------------------------- | ------------------------------------- | ---------------------------------- |
| `m_pyramidal`                           | `tetrahedral`                         | `cubic`                            |
| `octahedral`                            | `hauy_octahedral`                     | `icosahedral`                      |
| `dodecahedral`                          | `truncated_tetrahedral`               | `truncated_cubic`                  |
| `truncated_octahedral`                  | `stella_octangula`                    | `centered_cube`                    |
| `rhombic_dodecahedral`                  | `hauy_rhombic_dodecahedral`           | `centered_tetrahedron`             |
| `centered_square_pyramid`               | `centered_pentagonal_pyramid`         | `centered_hexagonal_pyramid`       |
| `centered_mgonal_pyramid`               | `centered_octahedron`                 | `centered_icosahedron`             |
| `centered_dodecahedron`                 | `centered_truncated_tetrahedron`      | `centered_truncated_cube`          |
| `centered_truncated_octahedron`         | `centered_mgonal_pyramidal`           | `mgonal_prism`                     |
| `generalized_mgonal_pyramidal`          | `generalized_cubic`                   | `generalized_octahedral`           |
| `generalized_icosahedral`               | `generalized_dodecahedral`            | `generalized_centered_cube`        |
| `generalized_centered_tetrahedron`      | `generalized_centered_square_pyramid` | `generalized_rhombic_dodecahedral` |
| `generalized_centered_mgonal_pyramidal` | `generalized_hexagonal_prism`         |                                    |

---

### `visualize_multidim`

```python
visualize_multidim(
    name_seq : MultiDimTypes,
    *,
    m : int | None = None,
    k : int | None = None,
    plot_type : PlotType | None = None,
    show : bool = True,
    **kwargs,
)
```

```text
Visualize the generating function of a multidimensional figurate number in the complex plane (phase portrait).

Parameters
----------
name_seq : MultiDimTypes
    Multidimensional figurate number sequence defining its generating function f(z).
m, k : int | None
    Parameters controlling the evaluation of the sequence.
plot_type : PlotType, optional
    Overrides the default plot type of the instance.
show : bool, default=True
    Whether to display the plot immediately. If False, the plot is generated but not shown.
**kwargs : dict
    Per-call plot options. Can override instance defaults:
    - xlim : tuple[float, float], optional
        Horizontal limits of the complex plane. Overrides `domain_grid_radius`.
    - ylim : tuple[float, float], optional
        Vertical limits of the complex plane. Overrides `domain_grid_radius`.
    - show_axes : bool, optional
        Whether to display the real (Re) and imaginary (Im) axes.
    - Instance defaults applied if not provided: figsize, cmap_color, brightness, num_lines, disk_radius.

Returns
-------
matplotlib.figure.Figure
    The generated figure. Automatically displayed if `show=True`.
```


#### Sequence Reference — MultiDimTypes

The `name_seq` parameter accepts values from the table below. Each name identifies a figurate number sequence.

Pass to `visualize_multidim(name_seq=...)`.

| name_seq                      | name_seq                             | name_seq                         |
| ----------------------------- | ------------------------------------ | -------------------------------- |
| `hypertetrahedral`            | `hypercube`                          | `hyperoctahedral`                |
| `hypericosahedral`            | `hyperdodecahedral`                  | `polyoctahedral`                 |
| `k_dim_hypertetrahedron`      | `k_dim_hypercube`                    | `k_dim_hyperoctahedron`          |
| `k_dim_nexus`                 | `four_dim_mgonal_pyramidal`          | `k_dim_mgonal_pyramidal`         |
| `centered_biquadratic`        | `centered_hypertetrahedron`          | `centered_hyperoctahedron`       |
| `k_dim_centered_hypercube`    | `k_dim_centered_hypertetrahedron`    | `k_dim_centered_hyperoctahedron` |
| `generalized_pentatope`       | `generalized_k_dim_hypertetrahedron` | `generalized_biquadratic`        |
| `generalized_k_dim_hypercube` | `generalized_k_dim_hyperoctahedron`  |                                  |

