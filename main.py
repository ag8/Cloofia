# documentation: https://discordpy.readthedocs.io/en/latest/

import discord
from player import Player
from roles import *
from game import Game
from discord.ext import commands

client = discord.Client()#commands.Bot(command_prefix = "!")
game = None

@client.event
async def on_ready():
    print("Bot logged in successfully as {0.user}".format(client))

    game = Game(client)


@client.event
async def on_message(message):
    if not game.is_assassin_turn():
        return
    
    is_assassin = False
    for i in game.players:
        if message.author == game.players[i].user:
            if game.players[i].roles[0].
    

        
"""

@client.listen('test')
async def waiting_fun(val):
    print('one')

def t():
    client.load_extension("cogs.basic")
    client.run(input("Enter token:"))"""

if __name__ == "__main__":
    #client.run(input("Enter token:"))
    #game = Game()
    #t()

    client.run("NzE0NDgzNDM2NzE4NTIyNTA4.XsvU6A.SyWBtGsAjlYoDJwNCJabp-D_wNI")
    #loop.run_until_complete(client.login(input("Enter token")))



    """
    loop.run_until_complete(client.start(input("Enter token")))
    print("test2")

    task = loop.create_task(client.wait_for("message"))
    msg = loop.run_until_complete(task)

    print("got " + msg)
    """