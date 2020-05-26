from .role import Role

class Scientist(Role):
    def __init__(self):
        super().__init__("Scientist")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Scientist")