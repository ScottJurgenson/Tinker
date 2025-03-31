from dataclasses import dataclass
from engine.player import Player
from engine.character_card import CharacterCard
from engine.card import Card
import random


@dataclass
class Game:
    player1: Player
    player2: Player
    active_player: Player
    inactive_player: Player
    turn_number: int = 1
    game_over: bool = False

    def start_game(self):
        print("===> Starting game...")
        self.player1.shuffle_deck()
        self.player2.shuffle_deck()
        self.player1.draw_card(7)
        self.player2.draw_card(7)
        self.active_player = self.player1
        self.inactive_player = self.player2

        while not self.game_over:
            self.run_turn()

    def run_turn(self):
        print(f"\n=== Turn {self.turn_number}: {self.active_player.name}'s turn ===")
        self.ready_phase()
        self.set_phase()
        self.draw_phase()
        self.main_phase()
        self.end_phase()
        self.check_win_condition()

        if not self.game_over:
            self.swap_players()
            self.turn_number += 1

    def ready_phase(self):
        for character in self.active_player.board:
            character.is_dry = True
            character.exerted = False
        print(f"{self.active_player.name} readies all characters.")

    def set_phase(self):
        # Placeholder for Set-phase triggers
        print(f"{self.active_player.name} enters Set phase.")

    def draw_phase(self):
        if not self.active_player.draw_card():
            print(f"💀 {self.active_player.name} loses the game by decking out!")
            self.game_over = True
        else:
            print(f"{self.active_player.name} draws a card.")


    def main_phase(self):
        print(f"{self.active_player.name} is in the Main phase.")
        self.turn_over = False

        while not self.turn_over and not self.game_over:
            actions = self.generate_legal_actions(self.active_player)
            action = self.get_player_action(actions)
            self.resolve_action(action)

        print(f"{self.active_player.name}'s board: {[char.name for char in self.active_player.board]}")
        print(f"Ink used: {self.active_player.used_ink} / {self.active_player.ink_pool}")
        print(f"Lore: {self.active_player.lore}")


    def end_phase(self):
        self.resolve_end_of_turn_banishments(self.active_player)
        self.active_player.reset_for_new_turn()
        print(f"{self.active_player.name}'s turn ends.")

    def check_win_condition(self):
        if self.active_player.lore >= 20:
            print(f"\n🏆 {self.active_player.name} wins with {self.active_player.lore} lore!")
            self.game_over = True

    def resolve_end_of_turn_banishments(self, player: Player):
        for char in player.board[:]:
            if isinstance(char, CharacterCard) and char.is_damage_banished():
                player.board.remove(char)
                player.discard.append(char)
                print(f"{char.name} is banished due to damage.")

    def swap_players(self):
        self.active_player, self.inactive_player = self.inactive_player, self.active_player

    def generate_legal_actions(self, player):
        actions = []

        # Inkable cards in hand
        if player.can_ink():
            for card in player.hand:
                if card.inkable:
                    actions.append({"type": "ink", "card": card})

        # Playable character cards
        available_ink = player.ink_pool - player.used_ink
        for card in player.hand:
            if isinstance(card, CharacterCard) and card.cost <= available_ink:
                actions.append({"type": "play", "card": card})

        # Questable characters
        for char in player.board:
            if isinstance(char, CharacterCard) and char.is_dry and not char.exerted:
                actions.append({"type": "quest", "card": char})

        # End turn is always allowed
        actions.append({"type": "end_turn"})

        return actions

    def get_player_action(self, actions):
        action = random.choice(actions)
        print(f"Randomly selected action: {action['type']} {action.get('card', {}).name if 'card' in action else ''}")
        return action

    def resolve_action(self, action):
        player = self.active_player

        if action["type"] == "ink":
            player.ink_card(action["card"])

        elif action["type"] == "play":
            player.play_card(action["card"])

        elif action["type"] == "quest":
            char = action["card"]
            char.exerted = True
            player.lore += char.lore or 0
            print(f"{player.name} quests with {char.name} for {char.lore} lore!")

        elif action["type"] == "end_turn":
            self.turn_over = True