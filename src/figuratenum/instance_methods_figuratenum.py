from typing import List
from array import array


class InstanceMethodsFigurateNum():
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
        seq_num = []
        for _ in range(n):
            seq_num.append(next(self.generator))
        return seq_num

    def take_to_array(self, n: int) -> array:
        """
        Takes the first n generated figurate numbers from the sequence and returns them as an array.

        Parameters
        ----------
        n : int
            Number of elements to take.

        Returns
        -------
        array('i')
            Array of signed integers containing the first n generated figurate numbers.
        """
        seq_num = array("i", [])
        for _ in range(n):
            seq_num.append(next(self.generator))
        return seq_num
