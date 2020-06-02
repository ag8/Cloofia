from player import Player
from roles import *
import random
import copy
import time

from assassin_turn import assassin_turn
from read_vote import read_vote

"""
Game class
"""

class Game:
    def __init__(self, client):
        self.client = client
        self.cups = dict()
        
        self.lovers = tuple()

        self.CHANNEL_ID = 714714388166082573

        a1, a2, n, c = [Assassin(), Assassin(), Nurse(), Cook()]

        roles = [a1, a2, n, c]
        #roles += [Villager()] * 1
        #random.shuffle(roles)

        self.order = [a1, a2, n, c]

        members = list()
        for user in client.users:
            #if not user.bot:
            if user.name == "MichaelG" or user.name == "Smitty Werbenjaegermanjensen":
                members.append(user)
                self.cups[user.name] = list()
            if len(members) == 2:
                break

        self.players = list()
        for i in range(0,len(members)):
            self.players.append(Player(members[i], (roles[2*i], roles[2*i+1])))
            print("player " + self.players[i].get_name() + " is " + self.players[i].roles[0].name + " and " + self.players[i].roles[1].name)
        
        self.is_assassin_turn = False

    def set_lovers(self, roles):
        self.lovers = roles

    def get_lives(self):
        output = ""
        for player in self.players:
            output += f"{player.get_name()}: {player.get_life()}\n"
        return output
    
    def is_valid_player_digit(self, player, msg):
        return msg.author.name == player.get_name() and msg.content.isdigit() and int(msg.content) in range(len(self.get_usernames())) and self.players[int(msg.content)].is_alive()
    
    async def hear_player_digit(self, player):
        def _check(msg):
            if msg.author.name == player.get_name():
                if msg.content.isdigit() and int(msg.content) in range(len(self.get_usernames())):
                    if self.players[int(msg.content)].is_alive():
                        return True
                    else:
                        print("Player is not alive")
                else:
                    print("not valid person")
            else:
                pass

        return int((await self.client.wait_for("message", check=_check)).content)

    async def hear_card(self, player):
        def _check(msg):
            if msg.author.name == player.get_name():
                if msg.content.isdigit() and int(msg.content) in range(2):
                    if player[int(msg.content)].is_alive():
                        return True
                    else:
                        print("Card is not alive")
                else:
                    print("not valid card")
            else:
                pass

        return int((await self.client.wait_for("message", check=_check)).content)

    def clear_cups(self):
        for member in self.cups:
            self.cups[member] = list() 

    def get_client(self):
        return self.client

    async def is_assassin_turn(self):
        return self.is_assassin_turn

    def players_w_numbers(self):
        players = self.get_usernames()
        output = str()
        for i in range(len(players)):
            if self.player_from_name(players[i]).is_alive():
                output += f"{players[i]} – {i}\n"

        return output

    def get_usernames(self):
        return list(player.get_name() for player in self.players)

    def is_game_won(self):
        
        return 0
        
        """ Run after day/night to determine if game is over and who is_game_won
        Returns:
            0 --> keep playing
            1 --> assassins won
            2 --> villagers won
            3 --> neither win
        """

        good_count = 0
        assassins_count = 0

        for player in self.players:
            if player.is_alive():
                if player.get_is_assassin():
                    assassins_count += 1
                else:
                    good_count += 1
        
        if good_count == 0 and assassins_count > 0:
            return 1
        if good_count == 0 and assassins_count == 0:
            return 3
        if good_count > 0 and assassins_count > 0:
            return 0
        if good_count > 0 and assassins_count == 0:
            return 2

    async def game_loop(self):
        while(self.is_game_won() == 0):
            await self.night()
            await self.end_night()
            if self.is_game_won() != 0:
                break
            await self.day()
        print(self.is_game_won())


    async def night(self):
        for i in range(len(self.order)):
            this_role = self.order[i]
            if str(this_role) != "Assassin":
                if this_role.is_usable():
                    await this_role.night_role(self)
                elif this_role.is_alive():
                    #time.sleep()
                    print("Wait a random number of seconds")
            elif str(this_role) == str(self.order[i+1]):
                await assassin_turn(self, (this_role, self.order[i+1]) )
                    
    def player_from_name(self, name):
        for player in self.players:
            if player.get_name() == name:
                return player
        else:
            return None
    
    async def send_to_all(self, msg):
        await self.client.get_channel(self.CHANNEL_ID).send(msg)

    async def end_night(self):
        print("starting end night")
        print(self.cups)
        for player, effects in self.cups.items():
            player = self.player_from_name(player)
            for effect in effects:
                if effect == 'A' and not 'N' in effects:
                    await player.kill_card(self)
        self.clear_cups()
        print(self.cups)
        print(self.get_lives())
        print("ending night end")

    async def day(self):
        await read_vote(self)