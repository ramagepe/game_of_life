"""
Oscillators are lifeforms that returns to its initial configuration
after some time
"""

from .base import Lifeform
import numpy as np


class Toad(Lifeform):
    def __init__(self) -> None:
        super(Toad, self).__init__()

    @property
    def layout(self) -> np.ndarray:
        return np.array([
            [0, 1, 1, 1],
            [1, 1, 1, 0]
        ])


class Beacon(Lifeform):
    def __init__(self) -> None:
        super(Beacon, self).__init__()

    @property
    def layout(self) -> np.ndarray:
        return np.array([
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 1]
        ])


class Blinker(Lifeform):
    def __init__(self) -> None:
        super(Blinker, self).__init__()

    @property
    def layout(self) -> np.ndarray:
        return np.array([
            [1, 1, 1],
        ])


class Pulsar(Lifeform):
    def __init__(self) -> None:
        super(Pulsar, self).__init__()

    @property
    def layout(self) -> np.ndarray:
        return np.array([
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        ])
