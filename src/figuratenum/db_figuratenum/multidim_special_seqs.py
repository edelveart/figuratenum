from .symbols_figuratenum import sp, x, k
from sympy.abc import i, j

# K-Dimensional
a_i_k = sp.Sum((-1)**j * sp.binomial(k + 1, j) * (i + 1 - j)**k, (j, 0, i))

k_dim_hypercube_x = x * sp.Sum(a_i_k * x**i, (i, 0, k - 1)) / (1 - x)**(k + 1)


a_i_k_plus_1 = sp.Sum((-1)**j * sp.binomial(k + 2, j)
                      * (i + 1 - j)**(k + 1), (j, 0, i))

k_dim_nexus_x = x * sp.Sum(a_i_k_plus_1 * x**i, (i, 0, k)) / (1 - x)**(k + 1)


# K-Dimensional Centered
k_dim_centered_hypercube_x = (1 + x) * k_dim_hypercube_x
