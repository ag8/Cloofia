from .role import Role

class Cook(Role):
    def __init__(self):
        super().__init__("Cook")
    
    def night_play(self):
        print("nurse night")