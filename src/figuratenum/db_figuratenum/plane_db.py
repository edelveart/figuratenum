from .PlaneSchema import PlaneSchema, x, m

plane_figuratenum_registers = [

    PlaneSchema(
        "polygonal",
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
        'centered_mgonal',
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
        'truncated_centered_mgonal',
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
        'generalized_mgonal',
        generating_function=x**2 *
        (1 + x) * (1 + (m - 4)*x + x**2) / (1 - x**2)**3,
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'generalized_centered_mgonal',
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

plane_highly_polygonal = [

    PlaneSchema(
        'square_triangular',
        generating_function=x * (1 + x) / ((1 - x)*(1 - 34*x + x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'pentagonal_triangular',
        # A014979 (Modified x**2 -> x)
        generating_function=x * (1 + 15*x) / ((1 - x) * (1 - 194*x + x**2)),
        galois_group='',
        galois_description=""
    ),

    PlaneSchema(
        'pentagonal_square',
        # A036353
        generating_function=x*(1+198*x+x**2)/((1-x)*(1-9602*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'hexagonal_square',
        # A046176
        generating_function=x*(1 + 70*x + x**2)/((1 - x)*(1 - 1154*x + x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'hexagonal_pentagonal',
        # A046180
        generating_function=x*(1+3120*x+15*x**2)/((1-x)*(1-37634*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'heptagonal_triangular',
        # A046194
        generating_function=x*(1+54*x+18034*x**2+54*x**3+x**4) /
        ((1-x)*(1-322*x+x**2)*(1+322*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'heptagonal_square',
        # A036354
        generating_function=-x*(1 + 80*x + 5848*x**2 + 222070*x**3 +
                                5848*x**4 + 80*x**5 + x**6) / ((x-1)*(x**6 - 2079362*x**3 + 1)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'heptagonal_pentagonal',
        # a048900
        generating_function=x*(1+504*x+7*x**2)/((1-x)*(1-3842*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'heptagonal_hexagonal',
        # A048903
        generating_function=x*(1+18088*x+55*x**2)/((1-x)*(1-103682*x+x**2)),
        galois_group='',
        galois_description=""
    ),

    PlaneSchema(
        'octagonal_triangular',
        # A046183
        generating_function=-x*(x**4+20*x**3+2158*x**2+20*x+1) /
        ((x-1)*(x**2-98*x+1)*(x**2+98*x+1)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'octagonal_square',
        # A036428
        generating_function=x*(x**2+30*x+1)/((1-x)*(1-194*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'octagonal_pentagonal',
        # A046189
        generating_function=x*(1+175*x+243535*x**2+5945*x **
                               3+40*x**4)/((1-x)*(1-1154*x+x**2)*(1+1154*x+x**2)),
        galois_group='',
        galois_description=""
    ),
    PlaneSchema(
        'octagonal_hexagonal',
        # A046192
        generating_function=x*(1 + 2178*x + 21*x**2) /
        ((1-x)*(1 - 9602*x + x**2)),
        galois_group='',
        galois_description=""
    ),
]


extended_plane_figuratenum_registers = plane_figuratenum_registers + \
    plane_highly_polygonal
PLANE_DATABASE = {
    seq.name: seq for seq in extended_plane_figuratenum_registers}
