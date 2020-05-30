from .role import Role

class Nurse(Role):
    def __init__(self):
        super().__init__("Nurse")

    async def night_role(self, game):
        """
        if self.player.get_user().dm_channel is None:
            await self.player.get_user().create_dm()
        
        await self.player.get_user().dm_channel.send(game.get_usernames())
        await self.player.send_dm("Type the number next to the player you want to save.")
        """

        await self.send_dm("Nurses turn. Select the number next to the person you want to save.")
        await self.send_dm(game.players_w_numbers())

        for _ in range(2):
            saved = await game.hear_player_digit(self.get_player())
            player_saved = game.get_usernames()[saved]
            game.cups[player_saved].append("N")
            await self.send_dm(f"{player_saved}'s cup: {game.cups[player_saved]}")