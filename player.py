from roles import *

"""
Class for player/user
"""

class Player:
    def __init__(self, user, roles):
        self.user = user
        self.roles = roles

        self.life = [True, True]

        self.is_assassin = False
        self._once_an_assassin()

    def life_check(self):
        for i in range(2):
            self.life[i] = self.roles[i].is_alive()

    def is_alive(self):
        return self.life[0] and self.life[1]

    def kill_card():
        cards_left = self.life.count(True)
        if cards_left == 2:
            # USER INPUT to decide
            index = input("which card do you want to kill (0 or 1)")
            self.roles[index].kill()
            self.life[index] = False
        else:
            index = self.roles.index(True)
            self.roles[index].kill()
            self.life[index] = False

    def is_assassin(self):
        return self.is_assassin

    def _once_an_assassin(self):
        """ Checks if player is an assassin """
        for role in self.roles:
            if str(role) == "Assassin":
                self.is_assassin = True

    def __getitem__(self, index):
        return self.roles[index]