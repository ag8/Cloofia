from .role import Role

class Villager(Role):
    def __init__(self):
        super().__init__("Villager")
    
    def night_play(self):
        print("Villager night")