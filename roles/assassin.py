from .role import Role

class Assassin(Role):
    def __init__(self):
        super().__init__("Assassin")
""" 
    def night_play(self, game, other):
        if self.player.get_user().dm_channel is None:
            await self.player.get_user().create_dm()
        while True:
            msg = await game.client.wait_for("message")

            if not msg.content.startswith("!choose"):
                await other.get_user().dm_channel.send(msg)
"""