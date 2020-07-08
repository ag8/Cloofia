from .role import Role

class Angel(Role):
    def __init__(self):
        super().__init__("Angel")

    async def night_play(self):
        print("Angel Night")

        await self.get_player().send_dm(f"Select the player your would like to save or \"none\" if you want to pass your turn.")

        def _check(msg):
            return game.is_valid_player_digit(self.get_player(), msg) or msg.content == "none"

        player = await game.client.wait_for("message", check=_check)

        if player.content == "none":
            return
        else:
            await self.get_player().send_dm("Choose a card to check")

            def _check_card_is_dead(msg):
                if msg.author.name == player.get_name():
                    if msg.content.isdigit() and int(msg.content) in range(2):
                        if not player[int(msg.content)].is_alive():
                            return True
                        else:
                            print("Card already alive")
                    else:
                        print("not valid card")
                else:
                    pass

            card = int(await self.client.wait_for("message", check=_check_card_is_dead).content)

            game.players[int(player.content)].roles[card].revive()

        print("Angel Night end")

    def replenish(self):
        self.is_used = False

    def __str__(self):
        return("Angel")
