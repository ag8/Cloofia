from .role import Role

class Cook(Role):
    def __init__(self):
        super().__init__("Cook")
        self.uses = 2

    async def night_role(self, game):
        print("cook night")

        await self.get_player().send_dm(f"You have {self.uses} uses left.\nChoose a player or type 'none' to skip your turn")

        def _check(msg):
            return game.is_valid_player_digit(self.get_player(), msg) or msg.content == "none"

        player = await game.client.wait_for("message", check=_check)

        if player.content == "none":
            return
        else:
            self.uses -= 1

            await self.get_player().send_dm("Choose a card to check")
            card = await game.hear_card(self.get_player())

            await self.send_dm(str(game.players[int(player.content)].roles[card]))

            if self.uses == 1:
                await self.night_role(game)

    def is_usable(self):
        return super().is_usable() and self.uses > 0

    def replenish(self):
        self.uses = 2
