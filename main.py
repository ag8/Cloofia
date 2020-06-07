# documentation: https://discordpy.readthedocs.io/en/latest/

import discord
from player import Player
from roles import *
from game import Game
from discord.ext import commands

client = discord.Client()#commands.Bot(command_prefix = "!")
global game
game = None

@client.event
async def on_ready():
    print("Bot logged in successfully as {0.user}".format(client))

    game = Game(client)
    await game.game_loop()


"""

@client.listen('test')
async def waiting_fun(val):
    print('one')

def t():
    client.load_extension("cogs.basic")
    client.run(input("Enter token:"))"""

if __name__ == "__main__":
    client.run("NzE0NDgzNDM2NzE4NTIyNTA4.Xtf7Nw.aQUNXWABf48JFAobRKe1yJ-gnKk")
