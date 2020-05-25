from .role import Role

class Assassin(Role):
    def __init__(self):
        super().__init__()
    
    def night_play(self):
        print("assassin night")

    def __str__(self):
        return("Assassin")