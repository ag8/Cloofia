"""
Interface class for roles
"""

class Role:
    def __init__(self, name):
        self.name = name
        self.is_used = False
        self.player = None
        self.night_teachered = False
        self.alive = True

    def night_role(self, game):
        pass


    def is_alive(self):
        return self.alive

    def is_dead(self):
        return not self.is_alive()

    def is_usable(self):
        return self.alive and not self.is_used and not \
            self.night_teachered

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def on_death(self, game):
        pass

    async def send_dm(self, msg):
        await self.player.send_dm(msg)

    async def kill(self, game):
        self.on_death(game)
        self.alive = False
        self.is_used = False

        # l1 - lover that died first
        async def kill_lover(lovers):
            l1, l2 = lovers
            await game.send_to_all(f"{l2.get_player()} was {l1.get_player()}'s lover, so their {str(l2)} dies.")
            l2.kill(game)

        # check if lover cards
        if self is game.lovers[0]:
            kill_lover(game.lovers)
        elif self is game.lovers[1]:
            kill_lover(game.lovers[::-1])

    def __str__(self):
        return self.name

    def revive(self):
        self.alive = True
        self.replenish()

    def replenish(self):
        self.is_used = False
