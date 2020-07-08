from .role import Role

class Ghost(Role):
    def __init__(self):
        super().__init__("Ghost")

    def __str__(self):
        return("Ghost")
