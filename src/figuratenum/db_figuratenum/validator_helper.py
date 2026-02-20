import warnings


class Validator:

    @staticmethod
    def validate_m_and_k(
            m: int | None,
            k: int | None,
            name_seq: str,
            needs_m: bool,
            needs_k: bool,
            MIN_VALUE: int = 3
    ):
        """
        Helper function to validate 'm' and 'k' parameters.

        Parameters
        ----------
        m : int | None
            The value of the parameter 'm' to validate.
        k : int | None
            The value of the parameter 'k' to validate.
        name_seq : str
            The name of the sequence being processed (for error messages).
        needs_m : bool
            Whether the sequence requires the parameter 'm'.
        needs_k : bool
            Whether the sequence requires the parameter 'k'.
        MIN_VALUE : int, default=3
            The minimum allowed value for 'm' and 'k'.
        """
        if m is not None and m < MIN_VALUE:
            raise ValueError(
                f"Parameter 'm' should be greater than or equal to {MIN_VALUE} for sequence '{name_seq}'.")

        if k is not None and k < MIN_VALUE:
            raise ValueError(
                f"Parameter 'k' should be greater than or equal to {MIN_VALUE} for sequence '{name_seq}'.")

        if needs_m and m is None:
            raise ValueError(f"Sequence '{name_seq}' requires parameter 'm'.")

        if needs_k and k is None:
            raise ValueError(f"Sequence '{name_seq}' requires parameter 'k'.")

        # Optional warning if parameter is provided but not needed
        if m is not None and not needs_m:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'm'; ignoring it.", stacklevel=2)

        if k is not None and not needs_k:
            warnings.warn(
                f"Sequence '{name_seq}' does not use parameter 'k'; ignoring it.", stacklevel=2)
