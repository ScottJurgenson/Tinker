from engine.card import load_cards_from_json
from engine.character_card import CharacterCard
from engine.player import Player
from engine.game import Game
import random

# Load card templates from JSON
raw_cards = load_cards_from_json("cards/basic_cards.json")

# Convert cards to CharacterCard instances for gameplay (just a demo)
def build_deck_from_templates(card_templates, copies_per_card=3):
    deck = []
    for card in card_templates:
        for _ in range(copies_per_card):
            # In a real version you'd conditionally create different subclasses here
            deck.append(CharacterCard(**card.__dict__))
    random.shuffle(deck)
    return deck

# Create decks
deck1 = build_deck_from_templates(raw_cards, copies_per_card=20)
deck2 = build_deck_from_templates(raw_cards, copies_per_card=20)

# Create players
player1 = Player(name="Alice", deck=deck1)
player2 = Player(name="Bob", deck=deck2)

# Create and start the game
game = Game(player1=player1, player2=player2, active_player=player1, inactive_player=player2)
game.start_game()
print("Main file finished.")
