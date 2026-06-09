from typing import Literal
import inspect

# =========================
# CONFIG
# =========================

OUTPUT_DIR = "docs"


# =========================
# METHODS + ALIASES
# =========================

def get_methods_with_aliases(cls, order_by: str):
    """
    Groups methods by actual function identity.
    Automatically detects real Python aliases.

    Parameters
    ----------
    order_by : str
        - "code": preserves class definition order
        - "alpha": sorts alphabetically by canonical name
    """

    groups = {}

    # order of definition in class
    original_order = [
        name
        for name in cls.__dict__.keys()
        if callable(getattr(cls, name)) and not name.startswith("_")
    ]

    # group by actual function identity
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
        raise ValueError(
            "order_by must be 'code' or 'alpha'"
        )

    return result


# =========================
# SEQUENCES GENERATOR
# =========================

def generate_sequences(order_by: Literal["code", "alpha"]):
    """
    Generates a markdown catalog of all sequence-generating methods.

    Output format:

    ## ClassName

    | # | Canonical | Aliases |
    |---|-----------|----------|
    | 1 | method() | alias1(), alias2() |

    Total per class and total global are included.
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

    total_sequences = 0

    with open(
        f"{OUTPUT_DIR}/sequences_api.md",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("# Complete Sequence Catalog\n\n")

        f.write("> Note: Some sequences have multiple names depending on geometric, combinatorial, or historical definitions in the literature. While they may generate identical outputs, their conceptual interpretations may differ.\n\n")

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

                canonical = (
                    f"`{names[0]}({param_str})`"
                )

                aliases = [
                    f"`{name}({param_str})`"
                    for name in names[1:]
                ]

                alias_str = (
                    ", ".join(aliases)
                    if aliases
                    else "—"
                )

                f.write(
                    f"| {i} | {canonical} | {alias_str} |\n"
                )

            f.write("\n")
            f.write(
                f"**Sequences in {cls.__name__}: "
                f"{class_total}**\n\n"
            )

        f.write("---\n\n")
        f.write("## Summary\n\n")
        f.write(
            f"**Total unique sequences: "
            f"{total_sequences}**\n"
        )


# =========================
# MAIN
# =========================

def main():
    generate_sequences(order_by="code")
    print("Sequences list generated successfully. ✔")


if __name__ == "__main__":
    main()
