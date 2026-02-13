from .PlaneSchema import PlaneSchema, x, m

plane_figuratenum_registers = [

    PlaneSchema(
        "m_gonal",
        generating_function=x * ((m - 3)*x + 1) / (1 - x)**3,
        galois_group="",
        galois_description=""
    ),
    PlaneSchema(
        "triangular",
        generating_function=x / (1 - x)**3,
        galois_group="",
        galois_description=""
    ),
    PlaneSchema(
        "square",
        generating_function=x * (x + 1) / (1 - x)**3,
        galois_group="",
        galois_description=""
    ),
    PlaneSchema(
        'pentagonal',
        generating_function=x * (2*x + 1) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'hexagonal',
        generating_function=x * (3*x + 1) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'centered_m_gonal',
        generating_function=x * (1 + (m - 2)*x + x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'pronic',
        generating_function=2 * x / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'gnomonic',
        generating_function=x * (1 + x) / (1 - x)**2,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_triangular',
        generating_function=x * (1 + 4*x + x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_square',
        generating_function=x * (1 + 9*x + 4*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_pronic',
        generating_function=x * (2 + 10*x + 2*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_centered_m_gonal',
        generating_function=x *
        (1 + (5*m - 2)*x + (1 + 2*m)*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_centered_triangular',
        generating_function=x * (1 + 13*x + 7*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_centered_square',
        generating_function=x * (1 + 18*x + 9*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_centered_pentagonal',
        generating_function=x * (1 + 23*x + 11*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'truncated_centered_hexagonal',
        generating_function=x * (1 + 28*x + 13*x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'polygram',
        generating_function=x * (1 + (2*m - 2)*x + x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'aztec_diamond',
        generating_function=4 * x / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'cross',
        generating_function=x * (1 + 3*x) / (1 - x)**2,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'diamond',
        generating_function=x * (1 + 2*x + x**2) / (1 - x)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'square_triangular',
        generating_function=x * (1 + x) / ((1 - x)*(1 - 34*x + x**2)
                                           ),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'generalized_m_gonal',
        generating_function=x**2 *
        (1 + x) * (1 + (m - 4)*x + x**2) / (1 - x**2)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'generalized_centered_m_gonal',
        generating_function=x**2 *
        (1 + (m + 1)*x + (m - 2)*x**2 - 2 *
         x**3 + x**4 + x**5) / (1 - x**2)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'generalized_pronic',
        generating_function=x * (2 + 2*x**3) / (1 - x**2)**3,
        galois_group='',
        galois_description=""
    ),

]


PLANE_DATABASE = {seq.name: seq for seq in plane_figuratenum_registers}
