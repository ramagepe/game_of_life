"""Growers are lifeforms that exhibit asymptotically unbounded growth"""

from .base import Lifeform
import numpy as np


class Grower(Lifeform):
    def __init__(self) -> None:
        super(Grower, self).__init__()

    @property
    def layout(self) -> np.ndarray:
        return np.array([
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
        ])
