from .role import Role

class Teacher(Role):
    def __init__(self):
        super().__init__("Teacher")
    
    def night_play(self):
        print("nurse night")

    def __str__(self):
        return("Teacher")