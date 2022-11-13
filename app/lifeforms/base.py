import abc
import numpy as np
from typing import Tuple


class Lifeform(abc.ABC):
    """Base class for all Lifeform implementation"""

    @abc.abstractproperty
    def layout(self) -> np.ndarray:
        pass

    @property
    def size(self) -> Tuple[int, int]:
        return self.layout.shape
