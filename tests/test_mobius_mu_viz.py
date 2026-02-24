from sympy import sieve
from figuratenum.figurate_viz import MobiusMuViz


n_terms = 8191
mu_viz = MobiusMuViz()


expect = [i for i in sieve.mobiusrange(1, n_terms)]


def test_mu_values():
    mu_values = []
    for i in range(1, n_terms):
        mu_values.append(mu_viz._mobius_single(i))
    assert mu_values == expect
