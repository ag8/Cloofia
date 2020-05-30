from .role import Role

class Villager(Role):
    def __init__(self):
        super().__init__("Villager")
    
    async def night_role(self, game):
        print("Villager night")