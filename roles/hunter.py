from .role import Role

class Hunter(Role):
    def __init__(self):
        super().__init__("Hunter")
    
    def night_role(self):
        return

    def on_death(self, game):
        game.send_to_all("Hunter, choose a player to kill")

        target = await game.hear_player_digit(self.get_player())

        game.players[int(target)].kill_card()