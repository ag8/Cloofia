from roles import *

"""
Class for player/user
"""

class Player:
    def __init__(self, user, roles):
        self.user = user
        self.roles = roles

        self.life = [True, True]

        self.is_assassin = False
        self._once_an_assassin()

        # assign player to each Role"

        for role in self.roles:
            role.set_player(player=self)

    def get_user(self):
        return self.user
    
    def get_name(self):
        return self.user.name
    
    def get_life(self):
        return self.life
    """
    def life_check(self):
        for i in range(2):
            self.life[i] = self.roles[i].is_alive()
    """

    def is_alive(self):
        return self.life[0] or self.life[1]

    # only run when one or two cards alive
    async def kill_card(self, game):
        cards_left = self.life.count(True)
        if cards_left == 2:
            await self.send_dm("Which card do you want to kill? (0 or 1)")
            index = int(await self.hear_dm(game))
            self.roles[index].kill(game)
            self.life[index] = False
        elif cards_left == 1:
            index = self.life.index(True)
            self.roles[index].kill(game)
            self.life[index] = False

    def get_is_assassin(self):
        return self.is_assassin

    def _once_an_assassin(self):
        """ Checks if player is an assassin """
        for role in self.roles:
            if str(role) == "Assassin":
                self.is_assassin = True
    
    async def send_dm(self, msg):
        if self.user.dm_channel is None:
            await self.user.create_dm()
        
        await self.user.dm_channel.send(msg)
    
    async def hear_dm(self, game, check=None):
        if self.user.dm_channel is None:
            await self.user.create_dm()
        
        def _check(msg):
            if msg.author.name == self.get_name():
                if msg.content.isdigit() and int(msg.content) in (0, 1):
                    
                    return True
            return False


        return (await game.client.wait_for("message", check=_check)).content

    def __getitem__(self, index):
        return self.roles[index]