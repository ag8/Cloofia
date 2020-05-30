from .role import Role

class Prostitute(Role):
    def __init__(self):
        super().__init__("Prostitute")
    
    def night_play(self):
        print("Prostitute Start")

    def __str__(self):
        return("Prostitute")