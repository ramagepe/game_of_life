from typing import Tuple
import numpy as np
from lifeforms.base import Lifeform


class Board:
    def __init__(self, size=(100, 100)) -> None:
        self.size = size
        self.state = np.zeros(size, dtype=bool)

    def render(self):
        to_render = ''
        for row in self.state:
            for i, cell in enumerate(row):
                if cell:
                    to_render += 'O '
                else:
                    to_render += '- '
                if i == len(row) - 1:
                    to_render += '\n'

        print(to_render)

    def add(self, lifeform: Lifeform, loc: Tuple[int, int]):
        """Add a lifeform to the board"""
        try:
            row, col = loc
            height, width = lifeform.size
            self.state[row: row + height, col: col + width] = lifeform.layout
        except ValueError:
            print("\nERROR: Lifeform out-of-bounds\n")
            raise
