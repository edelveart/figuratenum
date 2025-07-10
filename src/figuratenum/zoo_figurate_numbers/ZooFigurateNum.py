from typing import Iterator

from .zoo_figuratenum import (
    cuban_prime,
    pell
)


class ZooFigurateNum:
    def cuban_prime(self) -> Iterator[int]:
        return cuban_prime()

    def pell(self) -> Iterator[int]:
        return pell()
