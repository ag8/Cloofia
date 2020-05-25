from player import Player
from roles import *
import random

"""
Game class
"""

class Game:
    def __init__(self):
        self.cups = dict()
        roles = [Cupid(), Assassin(), Assassin(), Nurse(),
            Prostitute(), Scientist(), Cook(), Teacher(), Angel(), Gambler(), Ghost(), Hunter()]
        random.shuffle(roles)
        
        players = list()
        for i in range(0,12,2):
            players.append(Player((roles[i], roles[i+1])))