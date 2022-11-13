import numpy as np
from board import Board
from typing import Tuple

ALIVE = 1
DEAD = 0


def next_grid_state(init_state: Board) -> np.ndarray:
    """Determines the next state of the grid based on Conway's 4 rules of life

    Args:
        init_state (Board): initial state of the board

    Returns:
        ndarray: array with the new state of the board
    """
    size = init_state.size
    height, width = size
    new_grid = np.zeros(size, dtype=int)

    for x in range(height):
        for y in range(width):
            new_grid[x][y] = next_cell_state([x, y], init_state)

    return new_grid


def next_cell_state(cell_coords: Tuple[int, int], board: Board) -> int:
    """Determines the next state of a given cell

    Args:
        cell_coords (Tuple[int, int]): coordinates of the cell
        board (Board): the actual board where the cell resides

    Returns:
        _type_: _description_
    """

    height, width = board.size
    x = cell_coords[0]
    y = cell_coords[1]
    n_neighbours = 0

    for x_n in range((x-1), (x+1)+1):
        if x_n < 0 or x_n >= height:
            continue
        for y_n in range(y-1, (y+1)+1):
            if y_n < 0 or y_n >= width:
                continue
            if x_n == x and y_n == y:
                continue
            if board.state[x_n][y_n] == ALIVE:
                n_neighbours += 1

    cell_state = board.state[x][y]

    if cell_state == ALIVE:
        if n_neighbours <= 1:
            return DEAD
        if n_neighbours <= 3:
            return ALIVE
        if n_neighbours >= 3:
            return DEAD
    if cell_state == DEAD:
        if n_neighbours == 3:
            return ALIVE
        else:
            return DEAD
