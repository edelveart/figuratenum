from typing import Iterator

from .PlaneFigurateNum import PlaneFigurateNum
from .SpaceFigurateNum import SpaceFigurateNum
from .MultidimensionalFigurateNum import MultidimensionalFigurateNum


class FigurateNum(PlaneFigurateNum, SpaceFigurateNum, MultidimensionalFigurateNum):
    """
    Generates plane, space and multidimensional figurate numbers.

    Methods
    -------
    take(n: int) -> List[int]
        Returns the first n figurate numbers as a list.

    take_to_array(n: int) -> array
        Returns the first n figurate numbers as an array.

    Examples
    --------
    >>> from figuratenum import FigurateNum as fgn
    >>> print(fgn.generalized_dodecahedral_numbers(-3).take(8))
    [-165, -56, -10, 0, 1, 20, 84, 220]
    >>> print(fgn.octadecagonal_pyramidal_numbers().take_to_array(5))
    array('i', [1, 19, 70, 170, 335])
    """

    def __init__(self, generator: Iterator[int]):
        self.generator = generator
