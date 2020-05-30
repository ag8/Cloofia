async def assassin_turn(game, assassins):
        """
        input: assassins --> tuple with two assassins
        
        (1) assassins are the same player
        (2) only one assassin is alive
        (3) assassins are both alive, different players  """
        
        for assassin in assassins:
            if assassin.is_alive():
                await assassins[1].send_dm("")
        print("assassassin night")

        print(game.players_w_numbers())
        
        while True:
            msg = await game.client.wait_for("message")

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
            if not this_assassin.is_alive() and not this_assassin.get_player().get_name() == other_assassin.get_player().get_name():
                continue

            if msg.content.startswith("!choose"):
                target = msg.content.split(" ")[1]
                if msg.author.name == this_assassin.get_player().get_name() or msg.author.name == other_assassin.get_player().get_name():
                    if target.isdigit() and int(target) in range(len(game.get_usernames())):
                        game.cups[game.get_usernames()[int(target)]].append("A")
                        break
                    else:
                        print("invalid person")
                        continue
            else: # Relay message
                if this_assassin.get_player().get_name() == other_assassin.get_player().get_name():
                    continue
                await other_assassin.get_player().send_dm(f"[{this_assassin.get_player().get_name()}] {msg.content}")
        print("assassin night over")