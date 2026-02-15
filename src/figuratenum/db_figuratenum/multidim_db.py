from .MultiDimSchema import MultiDimSchema, x, k, m

from .multidim_special_seqs import k_dim_hypercube_x, k_dim_nexus_x, k_dim_centered_hypercube_x, generalized_k_dim_hypercube_x


multidim_figuratenum_registers = [

    # 4D
    MultiDimSchema(
        "hypertetrahedral",
        generating_function=x / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "hypercube",
        generating_function=x * (1 + 11*x + 11*x**2 + x**3) / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "hyperoctahedral",
        generating_function=x * (1 + x)**3 / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "hypericosahedral",
        generating_function=x * (1 + 115*x + 357*x**2 + 107*x**3) / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "hyperdodecahedral",
        generating_function=x * (1 + 595*x + 1993*x **
                                 2 + 543*x**3) / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "polyoctahedral",
        generating_function=x * (1 + 19*x + 43*x**2 + 9*x**3) / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),

    # K-Dimensional
    MultiDimSchema(
        "k_dim_hypertetrahedron",
        generating_function=x / (1 - x)**(k + 1),
        galois_group="",
        galois_description=""
    ),

    MultiDimSchema(
        "k_dim_hypercube",
        generating_function=k_dim_hypercube_x,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "k_dim_hyperoctahedron",
        generating_function=x * (1 + x)**(k - 1) / (1 - x)**(k + 1),
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "k_dim_nexus",
        generating_function=k_dim_nexus_x,
        galois_group="",
        galois_description=""
    ),

    # 4D Pyramidal
    MultiDimSchema(
        "four_dim_mgonal_pyramidal",
        generating_function=x * (1 + (m - 3)*x) / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),

    # K-Dimensional Pyramidal
    MultiDimSchema(
        "k_dim_mgonal_pyramidal",
        generating_function=x * (1 + (m - 3)*x) / (1 - x)**(k + 1),
        galois_group="",
        galois_description=""
    ),

    # 4D Centered
    MultiDimSchema(
        "centered_biquadratic",
        generating_function=x * (x**2 + 10*x + 1) * (x + 1)**2 / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "centered_hypertetrahedron",
        generating_function=x * (1 - x**5) / (1 - x)**6,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "centered_hyperoctahedron",
        generating_function=x * (1 + x)**4 / (1 - x)**5,
        galois_group="",
        galois_description=""
    ),

    # K-Dimensional Centered
    MultiDimSchema(
        "k_dim_centered_hypercube",
        generating_function=k_dim_centered_hypercube_x,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "k_dim_centered_hypertetrahedron",
        generating_function=x * (1 - x**(k + 1)) / (1 - x)**(k + 2),
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "k_dim_centered_hyperoctahedron",
        generating_function=x * (1 + x)**k / (1 - x)**(k + 1),
        galois_group="",
        galois_description=""
    ),

    # Generalized
    MultiDimSchema(
        "generalized_pentatope",
        generating_function=x**2 * (1 + x**5) / (1 - x**2)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "generalized_k_dim_hypertetrahedron",
        generating_function=x**2 *
        (1 + (-1)**k * x**(2*k - 3)) / (1 - x**2)**(k + 1),
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "generalized_biquadratic",
        generating_function=x**2 *
        (1 + x) * (1 + 11*x**2 + 11*x**4 + x**6) / (1 - x**2)**5,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "generalized_k_dim_hypercube",
        generating_function=generalized_k_dim_hypercube_x,
        galois_group="",
        galois_description=""
    ),
    MultiDimSchema(
        "generalized_k_dim_hyperoctahedron",
        generating_function=x**2 *
        (1 + x**2)**(k - 1) * (1 + (-1)**k * x) / (1 - x**2)**(k + 1),
        galois_group="",
        galois_description=""
    ),
]

MULTIDIM_DATABASE = {seq.name: seq for seq in multidim_figuratenum_registers}
