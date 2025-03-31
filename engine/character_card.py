from dataclasses import dataclass, field
from typing import Optional
from engine.card import Card

@dataclass
class CharacterCard(Card):
    damage: int = 0
    exerted: bool = False
    is_dry: bool = False
    can_challenge_ready: bool = False

    def is_damage_banished(self) -> bool:
        return self.damage >= (self.willpower or 0)

    def __str__(self):
        return (
            f"{self.name} (Cost: {self.cost}) "
            f"[{self.strength}/{self.willpower} | Lore: {self.lore}] "
            f"{'(Exerted)' if self.exerted else '(Ready)'}"
        )