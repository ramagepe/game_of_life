"""
GAME OF LIFE

DONE: Implement NumPy for 2d arrays
DONE: OOP Refactor
TODO: Add more lifeforms and pre-made init states (GGG and others)
TODO: Better UI
TODO: Wiki parser (https://github.com/ljvmiranda921/seagull/blob/master/seagull/lifeforms/wiki.py)
"""


from board import Board
from lifeforms.gliders import Glider, MiddleweightSpaceship
from lifeforms.growers import Grower
from lifeforms.GGG import GGG, InvertedGGG
from lifeforms.oscillators import Toad, Beacon, Blinker, Pulsar
from rules import next_grid_state
from os import system
from time import sleep

# Initialize board
b = Board((40, 90))

# Drop some shapes
b.add(Glider(), (1, 6))
b.add(Glider(), (3, 12))
b.add(Grower(), (8, 12))
b.add(MiddleweightSpaceship(), (10, 10))
b.add(MiddleweightSpaceship(), (3, 1))
b.add(Glider(), (8, 2))
b.add(Glider(), (15, 15))
b.add(GGG(), (0, 0))
b.add(Pulsar(), (5, 5))

system('clear')
b.render()
input('Press ENTER to begin the simulation...')

while True:
    system('clear')
    b.render()
    sleep(0.1)
    b.state = next_grid_state(b)
