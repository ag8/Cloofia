from player import Player
from roles import *
import random
import copy

"""
Game class
"""

class Game:
    def __init__(self, client):
        self.client = client
        self.cups = dict()
        
        a1, a2, n = Assassin(), Assassin(), Nurse()
        roles = [a1, a2, n]
        roles += [Villager()] * 1
        #random.shuffle(roles)

        self.order = [a1, a2, n]

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

    def get_lives(self):
        output = ""
        for player in self.players:
            output += f"{player.get_name()}: {player.get_life()}\n"
        return output

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
            output += f"{players[i]} – {i}\n"

        return output

    def get_usernames(self):
        return list(player.get_name() for player in self.players)

    def is_game_won(self):
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
            return 4
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


    async def assassin_turn(self, assassins):
        """
        input: assassins --> tuple with two assassins
        
        (1) assassins are the same player
        (2) only one assassin is alive
        (3) assassins are both alive, different players  """
        print("assassassin night")

        print(self.players_w_numbers())
        
        while True:
            msg = await self.client.wait_for("message")

            this_assassin = None
            other_assassin = None

            if msg.author.name == assassins[0].get_player().get_name():
                this_assassin = assassins[0]
                other_assassin = assassins[1]
            elif msg.author.name == assassins[1].get_player().get_name():
                this_assassin = assassins[1]
                other_assassin = assassins[0]
            else:
                continue
            
            # todo: make sure the assassin is alive
            if not this_assassin.is_alive():
                continue

            if msg.content.startswith("!choose"):
                target = msg.content.split(" ")[1]
                if msg.author.name == this_assassin.get_player().get_name() or msg.author.name == other_assassin.get_player().get_name():
                    if target.isdigit() and int(target) in range(len(self.get_usernames())):
                        self.cups[self.get_usernames()[int(target)]].append("A")
                        break
                    else:
                        print("invalid person")
                        continue
            else: # Relay message
                if this_assassin.get_player().get_name() == other_assassin.get_player().get_name():
                    continue
                await other_assassin.get_player().send_dm(f"[{this_assassin.get_player().get_name()}] {msg.content}")
        print("assassin night over")
        

    async def night(self):
        for i in range(len(self.order)):
            this_role = self.order[i]
            if str(this_role) != "Assassin":
                if this_role.is_usable():
                    await this_role.night_role(self)
                else:
                    pass # maybe stall for a few seconds if teachered

            elif str(this_role) == str(self.order[i+1]):
                await self.assassin_turn( (this_role, self.order[i+1]) )
                    
    def player_from_name(self, name):
        for player in self.players:
            if player.get_name() == name:
                return player
        else:
            return None
    
    async def send_to_all(self, msg):
        for channel in self.client.get_all_channels():
            if channel.name == "general":
                gen_channel = channel
        await gen_channel.send(msg)

    async def read_vote(self):
        votes = dict()
        votes_tally = dict()
        for player_id in range(len(self.players)):
            votes[self.players[player_id].get_name()] = None
            votes_tally[player_id] = 0

        def _check(msg):
            if hasattr(msg.channel, "name") and msg.channel.name == "general":
                if msg.content.startswith("!vote"):
                    if msg.content.split(" ")[1].isdigit():
                        if int(msg.content.split(" ")[1]) in range(len(self.players)):
                            return True
            return False

        voting_complete = False
        while not voting_complete:
            msg = await self.client.wait_for("message", check=_check)
            votes[msg.author.name] = msg.content.split(" ")[1]

            print(votes)
    
            all_votes_tallied = True
            for player,vote in votes.items():
                all_votes_tallied = all_votes_tallied and vote is not None
            
            voting_complete = all_votes_tallied
        
        for player in votes:
            votes_tally[int(votes[player])] += 1

        killed = []
        killed_score = -1
        for player,tally in votes_tally.items():
            if tally > killed_score:
                killed = [player]
                killed_score = tally
            elif tally == killed_score:
                killed.append(player)
        
        if len(killed) >= 2:
            print("tie")
        else:
            print(f"player killed is {killed[0]}")
            await self.players[killed[0]].kill_card(self)

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
        await self.read_vote()