from .plane_figurate_numbers.PlaneFigurateNum import PlaneFigurateNum
from .space_figurate_numbers.SpaceFigurateNum import SpaceFigurateNum
from .multidimensional_figurate_numbers.MultidimensionalFigurateNum import MultidimensionalFigurateNum


class FigurateNum(PlaneFigurateNum, SpaceFigurateNum, MultidimensionalFigurateNum):
    pass
