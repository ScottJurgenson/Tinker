from dataclasses import dataclass, field
import os
import json
from typing import Optional, List
import uuid

@dataclass
class Card:
    # Core identity
    name: str
    cost: int
    inkable: bool
    type: str = "Character"

    # Stats (only relevant for characters)
    strength: Optional[int] = None
    willpower: Optional[int] = None
    lore: Optional[int] = None

    # Gameplay rules
    ability_text: Optional[str] = None
    classifications: List[str] = field(default_factory=list)
    color: List[str] = field(default_factory=list)

    # Metadata
    rarity: Optional[str] = None
    set_id: Optional[str] = None
    set_number: Optional[int] = None
    unique_id: Optional[str] = None
    image: Optional[str] = None

    # Instance tracking (unique per card copy)
    instance_id: str = field(default_factory=lambda: str(uuid.uuid4()), compare=False)

    def __str__(self):
        return f"{self.name}, (Cost: {self.cost}, {self.type})"
    
def load_cards_from_json(path: str) -> List[Card]:
    full_path = os.path.join(os.path.dirname(__file__), "..", path)
    with open(full_path, "r") as f:
        card_data = json.load(f)
    return [Card(**card) for card in card_data]