from .role import Role

class Gambler(Role):
    def __init__(self):
        super().__init__("Gambler")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Nurse")