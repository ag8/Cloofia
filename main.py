# documentation: https://discordpy.readthedocs.io/en/latest/

import discord
from players import *

client = discord.Client()

@client.event
async def on_ready():
    print("Bot logged in successfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

if __name__ == "__main__":
    #client.run(input("Enter token:"))
    test()