from .role import Role

class Cupid(Role):
    def __init__(self):
        super().__init__("Cupid")
        self.first_turn = True
    
    def night_role(self, game, use = (True, True)):
        if self.first_turn:
            if use[0]:
                self._choose_lovers()
            
            if use[1]:
                self._choose_enemies()

            self.first_turn = False

    def _choose_lovers(self, game):
            self.send_dm(f"It is your turn as Cupid. Select the first lover by typing the number next to their name.\n{game.players_w_numbers()}")
            
            lover_one = int((await self.client.wait_for("message", check=game.is_valid_player_digit())).content)
            
            self.send_dm("Type 0 or 1 to select their card.")

            lover_one_card = await game.hear_card()

            def _check(msg):
                return game.is_valid_player_digit() and msg.content != lover_one

            self.send_dm("Select the second lover by typing the number next to their name.")

            lover_two = int((await self.client.wait_for("message", check=_check)).content)

            self.send_dm("Type 0 or 1 to select their card.")

            lover_two_card =  await game.hear_card()

            lovers = (self.players[int(lover_one)][lover_one_card], self.players[int(lover_two)][lover_two_card])

            game.set_lovers(lovers) 
    
            await lovers[0].send_dm(f"Your {lovers[0]} is lovers with card {lover_two_card} of {lovers[1].get_player()}")

            await lovers[1].send_dm(f"Your {lovers[1]} is lovers with card {lover_one_card} of {lovers[0].get_player()}")

    def _choose_enemies(self, game):
            self.send_dm(f"Now choose enemies – cannot choose same two players. Select the first lover by typing the number next to their name.\n{game.players_w_numbers()}")
            
            lover_one = int((await self.client.wait_for("message", check=game.is_valid_player_digit())).content)
            
            self.send_dm("Type 0 or 1 to select their card.")

            lover_one_card = await game.hear_card()

            def _check(msg):
                return game.is_valid_player_digit() and msg.content != lover_one

            self.send_dm("Select the second lover by typing the number next to their name.")

            lover_two = int((await self.client.wait_for("message", check=_check)).content)

            self.send_dm("Type 0 or 1 to select their card.")

            lover_two_card =  await game.hear_card()

            lovers = (self.players[int(lover_one)][lover_one_card], self.players[int(lover_two)][lover_two_card])
    
            await lovers[0].send_dm(f"Your {lovers[0]} is enemies with card {lover_two_card} of {lovers[1].get_player()}")

            await lovers[1].send_dm(f"Your {lovers[1]} is enemies with card {lover_one_card} of {lovers[0].get_player()}")

