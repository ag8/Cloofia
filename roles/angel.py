from .role import Role

class Angel(Role):
    def __init__(self):
        super().__init__()
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Nurse")