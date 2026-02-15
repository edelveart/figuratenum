from .SpaceSchema import SpaceSchema, x, m

space_registers = [

    # Pyramidal
    SpaceSchema(
        "m_pyramidal",
        generating_function=x * (1 + (m - 3)*x) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "tetrahedral",
        generating_function=x / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "cubic",
        generating_function=x * (1 + 4*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "octahedral",
        generating_function=x * (x + 1)**2 / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "hauy_octahedral",
        generating_function=x * (1 + x)**3 / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "icosahedral",
        generating_function=x * (1 + 8*x + 6*x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "dodecahedral",
        generating_function=x * (1 + 16*x + 10*x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Archimedean
    SpaceSchema(
        "truncated_tetrahedral",
        generating_function=x * (1 + 12*x + 10*x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "truncated_cubic",
        generating_function=x * (1 + 52*x + 93*x**2 + 8*x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "truncated_octahedral",
        generating_function=x * (1 + 34*x + 55*x**2 + 6*x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Star
    SpaceSchema(
        "stella_octangula",
        generating_function=x * (1 + 10*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Centered
    SpaceSchema(
        "centered_cube",
        generating_function=x * (1 + 5*x + 5*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "rhombic_dodecahedral",
        generating_function=x * (1 + 11*x + 11*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "hauy_rhombic_dodecahedral",
        generating_function=x * (1 + 29*x + 59*x**2 + 7*x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Centered Pyramids
    SpaceSchema(
        "centered_tetrahedron",
        generating_function=x * (1 + x + x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_square_pyramid",
        generating_function=x * (1 + 2*x + 2*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_pentagonal_pyramid",
        generating_function=x * (1 + 3*x + 3*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_hexagonal_pyramid",
        generating_function=x * (1 + 4*x + 4*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_mgonal_pyramid",
        generating_function=x *
        (1 + (m - 2)*x + (m - 2)*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Centered
    SpaceSchema(
        "centered_octahedron",
        generating_function=x * (1 + 3*x + 3*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_icosahedron",
        generating_function=x * (1 + 9*x + 9*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_dodecahedron",
        generating_function=x * (1 + 17*x + 17*x**2 + x**3) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),

    # Centered Truncated
    SpaceSchema(
        "centered_truncated_tetrahedron",
        generating_function=x * (1 + x) * (1 + 12*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_truncated_cube",
        generating_function=x * (1 + x) * (1 + 44*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "centered_truncated_octahedron",
        generating_function=x * (1 + x) * (1 + 28*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),


    # Centered Pyramidal
    SpaceSchema(
        "centered_mgonal_pyramidal",
        generating_function=x * (1 + (m - 2)*x + x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
    # Prism
    SpaceSchema(
        "mgonal_prism",
        generating_function=x * (1 + (2*m - 2)*x + (m + 1)*x**2) / (1 - x)**4,
        galois_group="",
        galois_description=""
    ),
]


generalized_space_registers = [

    SpaceSchema(
        "generalized_mgonal_pyramidal",
        generating_function=x**2 *
        (1 + (m - 3)*x**2 - (m - 3)*x**3 - x**5) / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "generalized_cubic",
        generating_function=x**2 *
        (1 - x) * (1 + 4*x**2 + x**4) / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "generalized_octahedral",
        generating_function=x**2 * (1 - x) * (1 + x**2)**2 / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "generalized_icosahedral",
        generating_function=x**2 *
        (1 - 6*x + 8*x**2 - 8*x**3 + 6*x**4 - x**5) / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),
    SpaceSchema(
        "generalized_dodecahedral",
        generating_function=x**2 *
        (1 - 10*x + 16*x**2 - 16*x**3 + 10*x**4 - x**5) / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),


    # Generalized Centered
    SpaceSchema(
        "generalized_centered_cube",
        generating_function=x**2 *
        (1 - 9*x + 5*x**2 + x**3 + 5*x**4 - 5*x**5 + x**6 + x**7) / (1 - x**2)**4,
        galois_group="",
        galois_description=""
    ),

]

space_figuratenum_registers = space_registers + generalized_space_registers

SPACE_DATABASE = {seq.name: seq for seq in space_figuratenum_registers}
