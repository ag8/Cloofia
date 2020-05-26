from player import Player
from roles import *
import random
import copy

"""
Game class
"""

class Game:
    def __init__(self, client):
        self.client = client
        self.cups = dict()
        roles = [Assassin(), Assassin(), Nurse()]

        self.order = copy.deepcopy(roles)

        roles += [Villager] * 3

        random.shuffle(roles)

        self.players = list()
        for i in range(0,len(client.users)):
            self.players.append(Player(client.users[i], (roles[2*i], roles[2*i+1])))
        
        self.is_assassin_turn = False

        self.game_loop()

    def is_assassin_turn(self):
        return self.is_assassin_turn


    def is_game_won(self):
        """ Run after day/night to determine if game is over and who is_game_won
        Returns:
            0 --> keep playing
            1 --> assassins won
            2 --> villagers won
            3 --> neither win
        """

        good_count = 0
        assassins_count = 0

        for player in self.players:
            if player.is_alive():
                if player.is_assassin():
                    assassins_count += 1
                else:
                    good_count += 1
        
        if good_count == 0 and assassins_count > 0:
            return 1
        if good_count == 0 and assassins_count == 0:
            return 4
        if good_count > 0 and assassins_count > 0:
            return 0
        if good_count > 0 and assassins_count == 0:
            return 2

    def game_loop(self):
        self.night()

    def assassin_turn(self, assassins):
        """
        input: assassins --> tuple with two assassins
        
        (1) assassins are the same player
        (2) only one assassin is alive
        (3) assassins are both alive, different players  """
        self.is_assassin_turn = True
        print("assassassin night")
        self.is_assassin_turn = False

    def night(self):
        for i in range(len(self.order)):
            this_role = self.order[i]
            if str(this_role) != "Assassin":
                if this_role.is_usable():
                    this_role.night_role(self)
                else:
                    pass # maybe stall for a few seconds if teachered

            elif str(this_role) == str(self.order[i+1]):
                self.assassin_turn( (this_role, self.order[i+1]) )
                    
    def day(self):
        pass

