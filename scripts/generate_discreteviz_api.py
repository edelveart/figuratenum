import inspect
import re
from pathlib import Path
from typing import Union, get_args, get_origin, Literal

from figuratenum.figurate_viz.DiscreteViz import DiscreteViz

# =========================
# CONFIG
# =========================

OUTPUT_FILE = "docs/reference/discreteviz.md"


# ─────────────────────────────────────────────────────────────
# Annotation formatter
# ─────────────────────────────────────────────────────────────
def fmt_ann(ann) -> str:
    if ann is inspect._empty:
        return ""

    origin = get_origin(ann)
    args = get_args(ann)

    if origin is Union and type(None) in args:
        inner = [a for a in args if a is not type(None)]
        if len(inner) == 1:
            return f"{fmt_ann(inner[0])} | None"

    if origin is not None:
        return str(ann).replace("typing.", "")

    s = str(ann)
    s = re.sub(r"<class '([^']+)'>", r"\1", s)
    s = re.sub(r"(?:[\w]+\.)+(\w+)", r"\1", s)
    return s


# ─────────────────────────────────────────────────────────────
# Signature renderer
# ─────────────────────────────────────────────────────────────
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
        ann_col = f" : {ann}" if ann else ""
        default_col = f" = {repr(p.default)}" if p.default is not inspect._empty else ""

        lines.append(f"{indent}{p.name}{ann_col}{default_col},")

    return f"{name}(\n" + "\n".join(lines) + "\n)"


# ─────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────
def public_methods(cls, order_by: Literal["code", "alpha"] = "alpha"):
    methods = [
        (n, o)
        for n, o in cls.__dict__.items()
        if callable(o) and not n.startswith("_")
    ]

    if order_by == "alpha":
        methods.sort(key=lambda x: x[0])

    elif order_by == "code":
        pass

    else:
        raise ValueError("order_by must be 'code' or 'alpha'")

    return methods


# ─────────────────────────────────────────────────────────────
# Build document
# ─────────────────────────────────────────────────────────────
def generate_discreteviz_api(order_by: Literal["code", "alpha"]):
    cls = DiscreteViz
    Path("docs/reference").mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        def w(s=""):
            f.write(s + "\n")

        # ─ Header
        w("# FigurateNum — DiscreteViz API Reference")
        w()
        w("> Discrete geometric visualization of figurate number sequences")
        w()
        w("---")
        w()

        # ─ Class doc
        class_doc = inspect.getdoc(cls)
        if class_doc:
            w("## Overview")
            w()
            w("```text")
            w(class_doc)
            w("```")
            w()
            w("---")
            w()

        # ─ Constructor
        w("## Constructor")
        w()
        w("```python")
        w(render_call("DiscreteViz", inspect.signature(cls.__init__)))
        w("```")
        w()

        init_doc = inspect.getdoc(cls.__init__)
        if init_doc:
            w("```text")
            w(init_doc)
            w("```")
            w()

        w("---")
        w()

        # ─ Methods
        methods = public_methods(cls, order_by=order_by)

        w("## Visualization Methods")
        w()

        for i, (name, method) in enumerate(methods):
            if i:
                w("---")
                w()

            sig = inspect.signature(method)

            w(f"### `{name}`")
            w()
            w("```python")
            w(render_call(f"{name}", sig))
            w("```")
            w()

            doc = inspect.getdoc(method)
            if doc:
                w("```text")
                w(doc)
                w("```")
                w()

        w("---")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    generate_discreteviz_api(order_by="code")
    print(f"Documentation file written to:\n  {OUTPUT_FILE}")
    print("DiscreteViz API generated successfully ✔")


if __name__ == "__main__":
    main()
