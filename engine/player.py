from dataclasses import dataclass, field
from typing import List
from engine.card import Card
from engine.character_card import CharacterCard
import random


@dataclass
class Player:
    name: str
    deck: List[Card]
    hand: List[Card] = field(default_factory=list)
    discard: List[Card] = field(default_factory=list)
    board: List[CharacterCard] = field(default_factory=list)
    lore: int = 0
    ink_well: List[Card] = field(default_factory=list)
    ink_pool: int = 0
    used_ink: int = 0
    inked_this_turn: int = 0
    ink_limit: int = 1

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self, count: int = 1) -> bool:
        for _ in range(count):
            if self.deck:
                self.hand.append(self.deck.pop(0))
            else:
                print(f"{self.name} has no cards left to draw!")
                return False  # draw failed = game over condition
        return True

    def can_ink(self) -> bool:
        return self.inked_this_turn < self.ink_limit

    def ink_card(self, card: Card) -> bool:
        if not self.can_ink():
            print(f"{self.name} cannot ink more cards this turn.")
            return False
        if not card.inkable:
            print(f"{card.name} is not inkable.")
            return False
        if card not in self.hand:
            print(f"{card.name} is not in hand.")
            return False

        self.hand.remove(card)
        self.ink_pool += 1
        self.inked_this_turn += 1
        self.ink_well.append(card)
        print(f"{self.name} inks {card.name}. Total ink: {self.ink_pool}")
        return True

    def play_card(self, card: Card) -> bool:
        if card.cost > (self.ink_pool - self.used_ink):
            print(f"{self.name} cannot afford to play {card.name}.")
            return False
        if card not in self.hand:
            print(f"{card.name} is not in hand.")
            return False

        self.hand.remove(card)
        self.used_ink += card.cost

        if isinstance(card, CharacterCard):
            self.board.append(card)
            card.is_dry = False
            print(f"{self.name} plays {card.name} to the board.")
        else:
            self.discard.append(card)
            print(f"{self.name} plays {card.name} and it goes to the discard.")

        return True

    def reset_for_new_turn(self):
        self.used_ink = 0
        self.inked_this_turn = 0
