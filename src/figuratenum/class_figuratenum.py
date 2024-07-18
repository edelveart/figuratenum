from typing import Iterator, List

from .class_plane_figuratenum import PlaneFigurateNum
from .class_space_figuratenum import SpaceFigurateNum
from .class_multidimensional_figuratenum import MultidimensionalFigurateNum


class FigurateNum(PlaneFigurateNum, SpaceFigurateNum, MultidimensionalFigurateNum):
    def __init__(self, generator: Iterator[int]):
        self.generator = generator

    def take(self, n: int) -> List[int]:
        result = []
        for _ in range(n):
            result.append(next(self.generator))
        return result
