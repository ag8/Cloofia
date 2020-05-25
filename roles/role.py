"""
Interface class for roles
"""

class Role:
    def __init__(self):
        self.is_used = False
        self.player = None
        self.night_teachered = False

    def night_role(self):
        pass

    def is_alive(self):
        pass
    
    def is_usable(self):
        return self.night_teachered
    
    def set_player(self, player):
        self.player = player
        pass

    def on_death(self):
        pass

    def __str__(self):
        pass
