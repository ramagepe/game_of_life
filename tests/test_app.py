"""
TODO: do a test for every lifeform and its subsequent form
"""

from app.rules import next_grid_state


def test_all_dead_cells():
    """
    TEST 1: dead cells with no live neighbors
    should stay dead.
    """
    init_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_next_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state = next_grid_state(init_state)

    assert expected_next_state == actual_next_state


def test_dead_cells_with_neighbours():
    """
    TEST 2: dead cells with exactly 3 neighbors
    should come alive.
    """
    init_state = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    actual_next_state = next_grid_state(init_state)

    assert expected_next_state == actual_next_state
