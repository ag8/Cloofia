from .role import Role

class Assassin(Role):
    def __init__(self):
        super().__init__("Assassin")
    
    def night_play(self):
        print("assassin night")