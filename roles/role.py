"""
Interface class for roles
"""

class Role:
    def __init__(self, name):
        self.name = name
        self.is_used = False
        self.player = None
        self.night_teachered = False
        self.is_alive = True

    def night_role(self, game):
        pass

    def is_alive(self):
        return self.alive
    
    def is_usable(self):
        return self.is_alive and not self.is_used and not \
            self.night_teachered
    
    def set_player(self, player):
        self.player = player

    def on_death(self):
        pass

    def kill(self):
        self.on_death()
        self.is_alive = False
        self.is_used = False

    def __str__(self):
        return self.name