import numpy as np


def hypertetrahedral(z: np.ndarray) -> np.ndarray:
    return z / (1 - z)**5
