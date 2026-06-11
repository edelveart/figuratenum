import ast
import importlib.util
import inspect
import re
from pathlib import Path
from typing import Literal, Union, get_args, get_origin, Callable

from figuratenum.figurate_viz.ComplexViz import ComplexViz

OUTPUT_FILE = "docs/reference/complexviz.md"
# AST extractor


def extract_literal(module_path: str, alias_name: str) -> list[str]:
    """
    Resolves *module_path* to its source file and extracts string values from:

        <alias_name>: TypeAlias = Literal["a", "b", ...]

    Pure AST — no import, no sympy, no side effects.
    """
    spec = importlib.util.find_spec(module_path)
    if spec is None or spec.origin is None:
        raise ModuleNotFoundError(f"Cannot locate module: {module_path!r}")

    source = Path(spec.origin).read_text(encoding="utf-8")
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if not isinstance(node, ast.AnnAssign):
            continue
        if not isinstance(node.target, ast.Name):
            continue
        if node.target.id != alias_name:
            continue
        val = node.value
        if not (isinstance(val, ast.Subscript)
                and isinstance(val.value, ast.Name)
                and val.value.id == "Literal"):
            continue
        slice_node = val.slice
        if isinstance(slice_node, ast.Tuple):
            return [
                elt.value for elt in slice_node.elts
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
            ]
        if isinstance(slice_node, ast.Constant):
            return [slice_node.value]  # type: ignore

    raise ValueError(f"Alias '{alias_name}' not found in {module_path!r}")


# Sequence catalogs (sourced from schema files)

PLANE_SEQS = extract_literal(
    "figuratenum.db_figuratenum.PlaneSchema",    "PlaneTypes")
SPACE_SEQS = extract_literal(
    "figuratenum.db_figuratenum.SpaceSchema",    "SpaceTypes")
MULTIDIM_SEQS = extract_literal(
    "figuratenum.db_figuratenum.MultiDimSchema", "MultiDimTypes")

# PlotType: extracted from ComplexViz.__init__ signature — no extra import needed.
_plot_ann = inspect.signature(
    ComplexViz.__init__).parameters["plot_type"].annotation
PLOT_TYPE_VALS = list(get_args(_plot_ann))

# Alias registry: frozenset(values) → display name
_ALIASES: dict[frozenset, str] = {
    frozenset(PLANE_SEQS):     "PlaneTypes",
    frozenset(SPACE_SEQS):     "SpaceTypes",
    frozenset(MULTIDIM_SEQS):  "MultiDimTypes",
    frozenset(PLOT_TYPE_VALS): "PlotType",
}


#  Annotation formatter

def fmt_ann(ann) -> str:
    if ann is inspect._empty:
        return ""
    origin = get_origin(ann)
    args = get_args(ann)

    if origin is Union and type(None) in args:
        inner = [a for a in args if a is not type(None)]
        if len(inner) == 1:
            return f"{fmt_ann(inner[0])} | None"

    if origin is Literal:
        key = frozenset(args)
        if key in _ALIASES:
            return _ALIASES[key]
        vals = list(dict.fromkeys(str(v) for v in args))
        return "{" + " | ".join(f"'{v}'" for v in vals) + "}"

    s = str(ann)
    s = re.sub(r"<class '([^']+)'>", r"\1", s)
    s = re.sub(r"(?:[\w]+\.)+(\w+)", r"\1", s)
    s = s.replace("typing.", "")
    return s

# =========================
# Signature renderer
# =========================


def render_call(name: str, sig: inspect.Signature, indent: str = "    ") -> str:
    lines = []
    kw_written = False

    for p in sig.parameters.values():
        if p.name == "self":
            continue
        if p.kind == p.VAR_KEYWORD:
            lines.append(f"{indent}**{p.name},")
            continue
        if p.kind == p.VAR_POSITIONAL:
            continue
        if p.kind == p.KEYWORD_ONLY and not kw_written:
            lines.append(f"{indent}*,")
            kw_written = True

        ann = fmt_ann(p.annotation)
        default = repr(p.default) if p.default is not inspect._empty else ""
        ann_col = f" : {ann}" if ann else ""
        default_col = f" = {default}" if default else ""
        lines.append(f"{indent}{p.name}{ann_col}{default_col},")

    return f"{name}(\n" + "\n".join(lines) + "\n)"


# =========================
# Helpers
# =========================


def visualize_methods(cls, order_by: Literal["code", "alpha"]) -> list[tuple[str, Callable]]:
    """
    Return all public visualize methods of a class.

    Parameters
    ----------
    cls : class
        The class containing visualization methods.
    order_by : str, default="alpha"
        "alpha"      : sort alphabetically by method name (default)
        "code"       : sort by definition order in the source code / class __dict__

    Returns
    -------
    list of (name, method) tuples
    """
    methods = [
        (name, getattr(cls, name))
        for name in cls.__dict__  # preserves definition order
        if name.startswith("visualize") and callable(getattr(cls, name))
    ]

    if order_by == "alpha":
        methods.sort(key=lambda x: x[0])
    elif order_by == "code":
        pass
    else:
        raise ValueError(f"Unknown order_by value: {order_by!r}")

    return methods


def name_table(names: list[str], cols: int = 3, order_by: Literal["alpha", "code"] = "code") -> str:
    """Return a markdown table of names, optionally sorted alphabetically."""
    if order_by == "alpha":
        names = sorted(names)
    padded = names + [""] * ((-len(names)) % cols)
    rows = [padded[i:i + cols] for i in range(0, len(padded), cols)]
    header = "| " + " | ".join(["name_seq"] * cols) + " |"
    sep = "| " + " | ".join(["---"] * cols) + " |"
    lines = [header, sep]
    for row in rows:
        lines.append(
            "| " + " | ".join(f"`{v}`" if v else "" for v in row) + " |")
    return "\n".join(lines)


def write_sequence_reference(
    w: Callable[[str], None],
    seq_name: str,
    seqs: list[str],
    viz_call: str,
    order_by: Literal["alpha", "code"] = "code"
):
    """Writes a table of sequences for a visualization method."""
    w("")
    w(f"#### Sequence Reference — {seq_name}")
    w("")
    w("The `name_seq` parameter accepts values from the table below. "
      "Each name identifies a figurate number sequence.")
    w("")
    w(f"Pass to `{viz_call}(name_seq=...)`.")
    w("")
    w(name_table(seqs, order_by=order_by))
    w("")


# =========================
# Build document
# =========================
def generate_complexviz_api(order_by: Literal["code", "alpha"]):
    Path("docs/reference").mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        def w(s=""):
            f.write(s + "\n")

        w("# FigurateNum — ComplexViz API Reference")
        w()
        w("> Phase portrait visualization of complex-valued generating functions")
        w("> of figurate numbers, based on **Elias Wegert (2012)**.")
        w()
        w("---")
        w()

        class_doc = inspect.getdoc(ComplexViz)
        if class_doc:
            w("## Overview")
            w()
            w("```text")
            w(class_doc)
            w("```")
            w()
            w("---")
            w()

        w("## Constructor")
        w()
        w("```python")
        w(render_call("ComplexViz", inspect.signature(ComplexViz.__init__)))
        w("```")
        w()
        init_doc = inspect.getdoc(ComplexViz.__init__)
        if init_doc:
            w("```text")
            w(init_doc)
            w("```")
        w()
        w("---")
        w()

        w("## Visualization Methods")
        w()

        METHOD_SEQ_MAP = {
            "visualize_plane": ("PlaneTypes", PLANE_SEQS),
            "visualize_space": ("SpaceTypes", SPACE_SEQS),
            "visualize_multidim": ("MultiDimTypes", MULTIDIM_SEQS),
        }

        for i, (name, method) in enumerate(visualize_methods(ComplexViz, order_by)):
            if i > 0:
                w("---")
                w()

            w(f"### `{name}`")
            w()
            w("```python")
            w(render_call(name, inspect.signature(method)))
            w("```")
            w()
            doc = inspect.getdoc(method)
            if doc:
                w("```text")
                w(doc)
                w("```")
                w()

            if name in METHOD_SEQ_MAP:
                seq_name, seqs = METHOD_SEQ_MAP[name]
                write_sequence_reference(
                    w, seq_name, seqs, name, order_by=order_by)


# =========================
# MAIN
# =========================

def main():
    generate_complexviz_api(order_by="code")

    # Summary
    total = len(PLANE_SEQS) + len(SPACE_SEQS) + len(MULTIDIM_SEQS)
    summary = (
        f"Sequences summary:\n"
        f"  • visualize_planePlaneTypes   : {len(PLANE_SEQS)}\n"
        f"  • SpaceTypes   : {len(SPACE_SEQS)}\n"
        f"  • MultiDimTypes: {len(MULTIDIM_SEQS)}\n"
        f"  ──────────────\n"
        f"  Total sequences: {total}\n"
        f"Documentation file written to:\n  {OUTPUT_FILE} \n"
        f"ComplexViz API generated successfully ✔"
    )
    print(summary)


if __name__ == "__main__":
    main()
