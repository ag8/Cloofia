from .role import Role

class Prostitute(Role):
    def __init__(self):
        super().__init__("Prostitute")

    async def night_role(self, game):
        await self.send_dm(f"Lmao you freak choose someone to sleep with ^_^\n{game.players_w_numbers()}")

        target = game.players[int(await game.hear_player_digit(self.get_player()))].get_name()

        game.cups[target].append("P")

        await self.send_dm(f"{target}'s cup: {game.cups[target]}")
