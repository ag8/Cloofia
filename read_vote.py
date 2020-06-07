def is_dead_ghost(player):
    return (player.roles[0].name == "ghost" and player.roles[0].is_dead()) or \
    (player.roles[1].name == "ghost" and player.roles[1].is_dead())

async def read_vote(game):
    votes = dict()
    votes_tally = dict()
    for player_id in range(len(game.players)):
        votes[game.players[player_id].get_name()] = None
        votes_tally[player_id] = 0

    def _check(msg):
        if msg.channel.id == game.CHANNEL_ID:
            if msg.content.startswith("!vote"):
                if msg.content.split(" ")[1].isdigit():
                    if int(msg.content.split(" ")[1]) in range(len(game.players)):
                        return True
            elif msg.content == "!tie":
                    return True
        return False

    voting_complete = False
    while not voting_complete:
        msg = await game.client.wait_for("message", check=_check)

        if msg.content == "!tie":
            game.tie_count[game.players.index(game.player_from_name(msg.author.name))] = True

        else:
            votes[msg.author.name] = msg.content.split(" ")[1]

            print(votes)

            all_votes_tallied = True
            for player,vote in votes.items():
                all_votes_tallied = all_votes_tallied and vote is not None

            voting_complete = all_votes_tallied

    for player,vote in votes.items():
        votes_tally[int(vote)] += 2 if is_dead_ghost(game.player_from_name(player)) else 1

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
        print(f"player killed is {game.players[killed[0]]}")
        await game.players[killed[0]].kill_card(game)
