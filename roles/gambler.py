from .role import Role

class Gambler(Role):
    def __init__(self):
        super().__init__("Gambler")
        self.uses = 1

    async def night_role(self, game):
        self.uses -= 1

        await self.send_dm("Choose a player")
        src_player = game.players[game.hear_player_digit(self.get_player())]

        await self.send_dm("Choose one of their cards")
        src_card = game.hear_card(self.get_player())

        await self.send_dm("Choose another player")
        tgt_player = game.players[game.hear_player_digit(self.get_player())]

        await self.send_dm("Choose one of their cards")
        src_card = game.hear_card(self.get_player())

        swap_temp = src_player.roles[src_card]
        src_player.roles[src_card] = tgt_player.roles[tgt_card]
        tgt_player.roles[tgt_card] = swap_temp

        src_player.roles[src_card].replenish()
        tgt_player.roles[tgt_card].replenish()

    def is_usable(self):
        return super().is_usable() and self.uses > 0

    def replenish(self):
        self.uses = 1
