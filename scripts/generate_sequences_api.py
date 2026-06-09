from typing import Literal
import inspect
import os

# =========================
# CONFIG
# =========================

OUTPUT_FILE = "docs/reference/sequences.md"


# =========================
# METHODS + ALIASES
# =========================

def get_methods_with_aliases(cls, order_by: str):
    """
    Groups methods by actual function identity.
    Automatically detects real Python aliases.
    """

    groups = {}

    original_order = [
        name
        for name in cls.__dict__.keys()
        if callable(getattr(cls, name)) and not name.startswith("_")
    ]

    for name, obj in cls.__dict__.items():
        if callable(obj) and not name.startswith("_"):
            groups.setdefault(id(obj), []).append(name)

    result = []

    for names in groups.values():
        canonical_name = next(
            n for n in original_order if n in names
        )

        func = getattr(cls, canonical_name)
        result.append((func, names))

    if order_by == "code":
        result.sort(
            key=lambda x: original_order.index(x[0].__name__)
        )

    elif order_by == "alpha":
        result.sort(
            key=lambda x: x[0].__name__
        )

    else:
        raise ValueError("order_by must be 'code' or 'alpha'")

    return result


# =========================
# SEQUENCES GENERATOR
# =========================

def generate_sequences(order_by: Literal["code", "alpha"]):
    """
    Generates a markdown catalog of all sequence-generating methods.
    """

    from figuratenum import (
        PlaneFigurateNum,
        SpaceFigurateNum,
        MultidimensionalFigurateNum,
        ZooFigurateNum,
    )

    CLASSES = [
        PlaneFigurateNum,
        SpaceFigurateNum,
        MultidimensionalFigurateNum,
        ZooFigurateNum,
    ]

    # -> ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    total_sequences = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        f.write("# FigurateNum Sequence Generators Reference\n\n")

        f.write(
            "> Note: Some sequences share names across geometric, combinatorial, "
            "or historical contexts. While outputs may coincide, their interpretations differ.\n\n"
        )

        for cls in CLASSES:

            methods = get_methods_with_aliases(
                cls,
                order_by=order_by
            )

            class_total = len(methods)
            total_sequences += class_total

            f.write(f"## {cls.__name__}\n\n")

            f.write("| # | Canonical | Aliases |\n")
            f.write("|---|-----------|----------|\n")

            for i, (func, names) in enumerate(methods, start=1):

                sig = inspect.signature(func)

                params = [
                    str(p)
                    for p in sig.parameters.values()
                    if p.name != "self"
                ]

                param_str = ", ".join(params)

                canonical = f"`{names[0]}({param_str})`"

                aliases = [
                    f"`{name}({param_str})`"
                    for name in names[1:]
                ]

                alias_str = ", ".join(aliases) if aliases else "—"

                f.write(f"| {i} | {canonical} | {alias_str} |\n")

            f.write("\n")
            f.write(f"**Sequences in {cls.__name__}: {class_total}**\n\n")

        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(f"**Total unique sequences: {total_sequences}**\n")


# =========================
# MAIN
# =========================

def main():
    generate_sequences(order_by="code")
    print("Sequences list generated successfully. ✔")


if __name__ == "__main__":
    main()
