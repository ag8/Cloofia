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

        # checks if message sent by right player
        # checks that selection is valid
        def _check(message):
            if message.author.name == self.player.get_name():
                if message.content.isdigit() and int(message.content) in range(len(game.get_usernames())):
                    return True
                else:
                    print("not valid person")
            else:
                pass
        print("\n---------------- \nNurse's Turn:")
        print(game.players_w_numbers())

        for _ in range(2):
            message = await game.client.wait_for("message", check=_check)
            saved = int(message.content)
            player_saved = game.get_usernames()[saved]
            game.cups[player_saved].append("N")
            print(f"{player_saved}'s cup: {game.cups[player_saved]}")


    
        