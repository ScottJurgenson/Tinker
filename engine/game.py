from dataclasses import dataclass
from engine.player import Player
from engine.character_card import CharacterCard
from engine.card import Card


@dataclass
class Game:
    player1: Player
    player2: Player
    active_player: Player
    inactive_player: Player
    turn_number: int = 1
    game_over: bool = False

    def start_game(self):
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
            character.exerted = False
        print(f"{self.active_player.name} readies all characters.")

    def set_phase(self):
        # Placeholder for Set-phase triggers
        print(f"{self.active_player.name} enters Set phase.")

    def draw_phase(self):
        self.active_player.draw_card()
        print(f"{self.active_player.name} draws a card.")

    def main_phase(self):
        # Stub: here you'd handle inking, playing cards, questing, etc.
        print(f"{self.active_player.name} is in the Main phase.")
        # This would eventually present choices or simulate them.

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
