from .role import Role

class Cupid(Role):
    def __init__(self):
        super().__init__("Cupid")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Nurse")