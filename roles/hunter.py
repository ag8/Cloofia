from .role import Role

class Hunter(Role):
    def __init__(self):
        super().__init__("Hunter")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Nurse")