# FigurateNum — DiscreteViz API Reference

> Discrete geometric visualization of figurate number sequences

---

## Overview

```text
Visualizes figurate numbers in a discrete, customizable 2D layout.

Generates circular 2D plots of figurate number sequences, where each number
is represented as a point arranged along a circle. These can be seen as
geometric or visual “multiplication tables,” showing numeric patterns
through spatial arrangements. Customization includes colors, background,
text annotations, rotation, and more.

Inspired by an expository article by J. Rogelio Pérez Buendía.
```

---

## Constructor

```python
DiscreteViz(
    fig_sequence : list[int] | tuple[int, ...] = [],
    figsize : tuple[float, float] = (6, 6),
)
```

```text
Initialize a DiscreteViz instance.

Default configuration for discrete geometric visualizations
of figurate number sequences.

Parameters
----------
fig_sequence : list[int] | tuple[int, ...] | None, default=None
    Sequence of integers to visualize. If None, an empty sequence is used.
figsize : tuple[float, float], default=(6, 6)
    Figure size in inches (width, height).
```

---

## Visualization Methods

### `visualize_plane`

```python
visualize_plane(
    figuratenum_name : str,
    *,
    m : int | None = None,
    n_terms : int,
    show = True,
    **kwargs,
)
```

```text
Visualize a plane figurate number sequence in a discrete modular geometry representation.

This method generates a figurate number sequence and visualizes it using a modular
polar transformation, producing a geometric pattern based on cyclic connections
between sequence indices.

Parameters
----------
figuratenum_name : string
    Name of the plane figurate number sequence.
m : int | None
    Parameter defining the m-gonal structure (if applicable).
n_terms : int
    Number of terms to generate from the sequence for visualization.
show : bool, default=True
    Whether to display the plot immediately. If False, the figure is created but not shown.
**kwargs : dict
    - circ_color : str, default="g"
        Color of the connecting edges in the polar plot.
    - bg_color : str, default="k"
        Background color of the figure.
    - num_text : bool, default=False
        Whether to display numeric labels on the nodes.
    - num_color : str, default="g"
        Color of the numeric labels.
    - rotate : int, default=0
        Rotation offset applied to the sequence mapping.
    - ext_circle : bool, default=False
        Whether to display the outer polar boundary circle.
    - h_modulo : int | None, default=len(sequence)
        Modulo used for circular mapping of the sequence.

Returns
-------
matplotlib.figure.Figure
    The generated modular visualization figure.
    Returned even if `show=True`.
```

---

### `visualize_space`

```python
visualize_space(
    figuratenum_name,
    *,
    m : int | None = None,
    n_terms : int,
    show = True,
    **kwargs,
)
```

```text
Visualize a space figurate number sequence in a discrete modular geometry representation.

This method generates a figurate number sequence and visualizes it using a modular
polar transformation, producing a geometric pattern based on cyclic connections
between sequence indices.

Parameters
----------
figuratenum_name : string
    Name of the space figurate number sequence.
m : int | None
    Parameter defining the m-gonal structure (if applicable).
n_terms : int
    Number of terms to generate from the sequence for visualization.
show : bool, default=True
    Whether to display the plot immediately. If False, the figure is created but not shown.
**kwargs : dict
    - circ_color : str, default="g"
        Color of the connecting edges in the polar plot.
    - bg_color : str, default="k"
        Background color of the figure.
    - num_text : bool, default=False
        Whether to display numeric labels on the nodes.
    - num_color : str, default="g"
        Color of the numeric labels.
    - rotate : int, default=0
        Rotation offset applied to the sequence mapping.
    - ext_circle : bool, default=False
        Whether to display the outer polar boundary circle.
    - h_modulo : int | None, default=len(sequence)
        Modulo used for circular mapping of the sequence.

Returns
-------
matplotlib.figure.Figure
    The generated modular visualization figure.
    Returned even if `show=True`.
```

---

### `visualize_multidim`

```python
visualize_multidim(
    figuratenum_name,
    *,
    m : int | None = None,
    k : int | None = None,
    n_terms : int,
    show = True,
    **kwargs,
)
```

```text
Visualize a multidimensional figurate number sequence in a discrete modular geometry representation.

This method generates a figurate number sequence and visualizes it using a modular
polar transformation, producing a geometric pattern based on cyclic connections
between sequence indices.

Parameters
----------
figuratenum_name : string
    Name of the multidimensional figurate number sequence.
m : int | None
    Parameter defining the m-gonal structure (if applicable).
k : int | None
    Parameter defining the k-dimensional structure (if applicable).
n_terms : int
    Number of terms to generate from the sequence for visualization.
show : bool, default=True
    Whether to display the plot immediately. If False, the figure is created but not shown.
**kwargs : dict
    - circ_color : str, default="g"
        Color of the connecting edges in the polar plot.
    - bg_color : str, default="k"
        Background color of the figure.
    - num_text : bool, default=False
        Whether to display numeric labels on the nodes.
    - num_color : str, default="g"
        Color of the numeric labels.
    - rotate : int, default=0
        Rotation offset applied to the sequence mapping.
    - ext_circle : bool, default=False
        Whether to display the outer polar boundary circle.
    - h_modulo : int | None, default=len(sequence)
        Modulo used for circular mapping of the sequence.

Returns
-------
matplotlib.figure.Figure
    The generated modular visualization figure.
    Returned even if `show=True`.
```

---
