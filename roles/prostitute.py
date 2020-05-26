from .role import Role

class Prostitute(Role):
    def __init__(self):
        super().__init__("Prostitute")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Nurse")