import pygame
from player import Player

# create a second class that will represent the game.
class Game:

    def __init__(self):
        # generate the player
        self.player = Player()
        self.pressed = {}