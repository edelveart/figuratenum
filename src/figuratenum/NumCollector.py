from typing import List, Tuple
from array import array
from itertools import islice


class NumCollector():
    @staticmethod
    def take(generator, n: int) -> List[int]:
        """
        Takes the first n generated figurate numbers from the sequence and returns them as a list.

        Parameters
        ----------
        generator : iterator
            The figurate number generator.
        n : int
            Number of elements to take.

        Returns
        -------
        list
            List of the first n generated figurate numbers.
        """
        return [next(generator) for _ in range(n)]

    @staticmethod
    def take_to_list(generator, stop: int, start: int = 0, step: int = 1) -> List[int]:
        """
        Takes n generated figurate numbers from the sequence and returns them as a list.

        Parameters
        ----------
        generator : iterator
            The figurate number generator.
        stop : int
            Ending position.
        start : int
            Start position.
        step : int
            Interval between elements.

        Returns
        -------
        list
            List of the first n generated figurate numbers.
        """
        return list(islice(generator, start, stop, step))

    @staticmethod
    def take_to_array(generator, stop: int, start: int = 0, step: int = 1) -> array:
        """
        Takes n generated figurate numbers from the sequence and returns them as an array.

        Parameters
        ----------
        generator : iterator
            The figurate number generator.
        stop : int
            Number of elements to take.
        start : int
            Number of elements to take.
        step : int
            Interval between elements.

        Returns
        -------
        array('d')
            Array of double float containing the first n generated figurate numbers.
        """
        return array('d', islice(generator, start, stop, step))

    @staticmethod
    def take_to_tuple(generator, stop: int, start: int = 0, step: int = 1) -> Tuple[int, ...]:
        """
        Takes n generated figurate numbers from the sequence and returns them as a tuple.

        Parameters
        ----------
        generator : iterator
            The figurate number generator.
        stop : int
            Ending position.
        start : int
            Start position.
        step : int
            Interval between elements.

        Returns
        -------
        tuple
            Tuple of the first n generated figurate numbers.
        """
        return tuple(islice(generator, start, stop, step))

    @staticmethod
    def pick(generator, n: int) -> int:
        """
        Pick one figurate number at index n.

        Parameters
        ----------
        generator : iterator
            The figurate number generator.
        n : int
            Index in the generated sequence, starting from 0.

        Returns
        -------
        int
            Number selected by index in the generated sequence.
        """
        return next(islice(generator, n, None))
