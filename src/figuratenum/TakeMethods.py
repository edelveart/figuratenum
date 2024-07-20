from typing import List, Tuple
from array import array
from itertools import islice


class TakeMethods():
    def take(self, n: int) -> List[int]:
        """
        Takes the first n generated figurate numbers from the sequence and returns them as a list.

        Parameters
        ----------
        n : int
            Number of elements to take.

        Returns
        -------
        list
            List of the first n generated figurate numbers.
        """
        return [next(self.generator) for _ in range(n)]

    def take_to_list(self,  stop: int,  start: int = 0, step: int = 1) -> List[int]:
        """
        Takes n generated figurate numbers from the sequence and returns them as a list.

        Parameters
        ----------
        stop : int
            Ending position.
        start : int
            Start position.
        step : int
            Interval between elements

        Returns
        -------
        list
            List of the first n generated figurate numbers.
        """
        return list(islice(self.generator, start, stop, step))

    def take_to_array(self, stop: int,  start: int = 0, step: int = 1) -> array:
        """
        Takes n generated figurate numbers from the sequence and returns them as an array.

        Parameters
        ----------
        stop : int
            Number of elements to take.
        start : int
            Number of elements to take.
        step : int
            I between elements

        Returns
        -------
        array('i')
            Array of double float containing the first n generated figurate numbers.
        """
        return array('d', islice(self.generator, start, stop, step))

    def take_to_tuple(self, stop: int,  start: int = 0, step: int = 1) -> Tuple[int, ...]:
        """
        Takes n generated figurate numbers from the sequence and returns them as a tuple.

        Parameters
        ----------
        stop : int
            Ending position.
        start : int
            Start position.
        step : int
            I between elements

        Returns
        -------
        tuple
            Tuple of the first n generated figurate numbers.
        """
        return tuple(islice(self.generator, start, stop, step))

    def pick(self, n: int) -> int:
        """
        Pick one figurate number at index n.

        Parameters
        ----------
        n : int
            Index in the generated sequence, start at 0.

        Returns
        -------
        int
            Number selected by index in the generated sequence.
        """
        return next(islice(self.generator, n, None))
