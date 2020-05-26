from .role import Role

class Nurse(Role):
    def __init__(self):
        super().__init__("Nurse")

    def night_role(self, game):
        print("nurse night")