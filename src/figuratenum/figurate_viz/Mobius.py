import inspect
import numpy as np
import matplotlib.pyplot as plt
from ..FigurateNum import FigurateNum
from ..db_figuratenum.validator_helper import Validator
from matplotlib.ticker import MaxNLocator


class MobiusViz:
    def __init__(self, figsize: tuple[float, float] = (8, 5)):
        self._PRIMES = self._small_primes()
        self.figsize = figsize

    def _small_primes(self, limit=10**6):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        primes = []
        for i in range(2, limit + 1):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        return primes

    def _mobius_single(self, n: int) -> int:
        """
        Compute the Möbius function μ(n) for a single integer efficiently,
        without generating large arrays.

        Parameters
        ----------
        n : int
            The integer for which to compute μ(n).

        Returns
        -------
        int
            μ(n), which is:
            - 0 if n is divisible by a square,
            - 1 if n is a product of an even number of distinct primes or n = 1,
            - -1 if n is a product of an odd number of distinct primes.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        x = n
        count = 0
        is_square_free = True

        for p in self._PRIMES:
            if p * p > x:
                break
            if x % p == 0:
                exp = 0
                while x % p == 0:
                    x //= p
                    exp += 1
                if exp > 1:
                    is_square_free = False
                    break
                count += 1
        # Last prime factor greater than the small primes limit
        if x > 1:
            count += 1

        if not is_square_free:
            return 0
        return -1 if count % 2 else 1

    def _get_valid_figuratenum_methods(self, figurate_name,
                                       figClass: FigurateNum):
        valid_methods = [
            func for func in dir(figClass)
            if callable(getattr(figClass, func))
            and not func.startswith("__")
        ]

        if figurate_name not in valid_methods:
            raise ValueError(
                f"'{figurate_name}' is not a valid method. "
                f"Available methods: {valid_methods}"
            )

    def _generate_sequence_from_class(self, seq_type: str,  name_seq: str, *, m: int | None = None, k: int | None = None):
        if seq_type == "FigurateNum":
            seq_loop = FigurateNum()
        else:
            raise ValueError(f"Unknown sequence type: {seq_type}")

        # Validate
        if not hasattr(seq_loop, name_seq):
            raise ValueError(
                f"'{name_seq}' method not found in {seq_type} class")

        method = getattr(seq_loop, name_seq)
        sig = inspect.signature(method)

        needs_m = 'm' in sig.parameters
        needs_k = 'k' in sig.parameters

        Validator.validate_m_and_k(
            m=m, k=k, name_seq=name_seq, needs_m=needs_m, needs_k=needs_k)

        call_kwargs = {}
        if needs_m:
            call_kwargs['m'] = m
        if needs_k:
            call_kwargs['k'] = k

        gen = method(**call_kwargs)

        return gen

    def _calculate_mu(self, gen_seq, n_terms: int):
        mu_values = np.empty(n_terms, dtype=np.int8)
        for i in range(n_terms):
            n = next(gen_seq)
            mu_values[i] = self._mobius_single(n)
        return mu_values

    def _cumulative_mu(self, gen_seq, n_terms: int):
        return np.cumsum(self._calculate_mu(gen_seq, n_terms))

    def __visualize_mobius(self, name_seq: str, *, m: int | None = None, k: int | None = None, n_terms: int, show: bool = True):
        self._get_valid_figuratenum_methods(name_seq, FigurateNum())

        gen = self._generate_sequence_from_class(
            "FigurateNum", name_seq, m=m, k=k)

        mu_values = self._calculate_mu(gen_seq=gen, n_terms=n_terms)

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.scatter(
            range(1, n_terms + 1),
            mu_values,
            s=3,
            color='blue',
            marker="s",
            zorder=100
        )

        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        step = max(1, n_terms // 10)

        ax.set_xlim(1, n_terms)
        ax.set_xticks(range(0, n_terms + 1, step))

        ax.set_ylim(-1.5, 1.5)
        ax.set_yticks([-1, 0, 1])

        ax.set_title(f"Möbius Function for {name_seq}")
        ax.set_xlabel("n")
        ax.set_ylabel("μ(n)")

        # Vertical Lines
        ax.grid(True, axis='x', color='black', linewidth=0.8)

        for line in ax.get_xgridlines():
            line.set_ydata([0.46, 0.54])
            line.set_linestyle('-')
            line.set_alpha(0.7)

        # Alone y=0 line
        ax.axhline(y=0, color='black', linewidth=0.8)

        fig.tight_layout()
        if show:
            plt.show()

        return fig

    def moebius(self, name_seq: str, *, m: int | None = None, k: int | None = None, n_terms: int):
        """
        Compute the Möbius function values μ(n) for a sequence of figurate numbers.

        Parameters
        ----------
        name_seq : str
            The name of the figurate number sequence (e.g., 'triangle', 'square').
        m : int, optional
            Optional parameter for the sequence (if applicable).
        k : int, optional
            Optional parameter for the sequence (if applicable).
        n_terms : int
            Number of terms in the sequence to compute.

        Returns
        -------
        list[int]
            A list of μ(n) values corresponding to the first `n_terms` of the sequence.
        """
        self._get_valid_figuratenum_methods(name_seq, FigurateNum())
        gen = self._generate_sequence_from_class(
            "FigurateNum", name_seq, m=m, k=k)

        return self._calculate_mu(gen_seq=gen, n_terms=n_terms)

    def mertens(self, name_seq: str, *, m: int | None = None, k: int | None = None, n_terms: int):
        """
        Compute the cumulative Mertens function M(n) for a sequence of figurate numbers.

        Parameters
        ----------
        name_seq : str
            The name of the figurate number sequence.
        m : int, optional
            Optional parameter for the sequence (if applicable).
        k : int, optional
            Optional parameter for the sequence (if applicable).
        n_terms : int
            Number of terms in the sequence to compute.

        Returns
        -------
        list[int]
            A list of cumulative M(n) values corresponding to the first `n_terms` of the sequence.
        """
        self._get_valid_figuratenum_methods(name_seq, FigurateNum())
        gen = self._generate_sequence_from_class(
            "FigurateNum", name_seq, m=m, k=k)

        return self._cumulative_mu(gen_seq=gen, n_terms=n_terms)

    def visualize_mertens(self, name_seq: str, *, m: int | None = None, k: int | None = None, n_terms: int, show: bool = True):
        """
        Plot the cumulative Mertens function M(n) for a sequence of figurate numbers.

        Parameters
        ----------
        name_seq : str
            The name of the figurate number sequence.
        m : int, optional
            Optional parameter for the sequence (if applicable).
        k : int, optional
            Optional parameter for the sequence (if applicable).
        n_terms : int
            Number of terms in the sequence to plot.
        show : bool, default=True
            Whether to display the figure immediately.

        Returns
        -------
        matplotlib.figure.Figure
            The figure object containing the Mertens function plot.
        """
        self._get_valid_figuratenum_methods(name_seq, FigurateNum())
        gen = self._generate_sequence_from_class(
            "FigurateNum", name_seq, m=m, k=k)

        cum_mu_values = self._cumulative_mu(gen_seq=gen, n_terms=n_terms)

        fig, ax = plt.subplots(figsize=self.figsize)

        ax.plot(
            range(1, n_terms + 1),
            cum_mu_values,
            marker=None,
            linestyle='-',
            color='red',
            markersize=None,
            linewidth=0.8,
        )

        step = max(1, n_terms // 10)
        ax.set_xticks(range(0, n_terms + 1, step))
        ax.set_xlim(1, n_terms)
        ax.margins(x=0)
        ax.set_title(f"Mertens function for {name_seq}")
        ax.set_xlabel("n")
        ax.set_ylabel("M(n)")
        ax.grid(False)

        fig.tight_layout()
        if show:
            plt.show()

        return fig
