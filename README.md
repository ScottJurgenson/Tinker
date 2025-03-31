# Tinker

**Tinker** is a text-based simulation engine for the Disney Lorcana Trading Card Game.  
Its goal is to simulate matches between two players (human or AI), execute core game mechanics, and provide a flexible, extensible foundation for exploring card interactions, rule enforcement, and gameplay testing — all without a graphical interface.

---

## ✨ Goals

- Create a fully playable, rule-abiding Lorcana match engine.
- Allow two players (or bots) to play games in a text-based environment.
- Support core gameplay mechanics including:
  - Deck building
  - Turn structure
  - Inking
  - Playing characters
  - Questing
  - Challenging
- Present readable game state and available actions each turn.
- Load card data from human-readable files (YAML or JSON).
- Make it easy to extend cards, rules, and abilities over time.
- Emphasize maintainability and modularity to support ongoing expansion.

---

## 🛠 Project Structure (Planned)
tinker/ ├── cards/ # Card definitions (YAML/JSON) ├── engine/ # Core game logic │ ├── card.py │ ├── character.py │ ├── player.py │ ├── game.py │ ├── actions.py │ └── rules.py ├── data/ # Match logs, results ├── main.py # CLI-based game runner └── README.md

---

## 🔍 What It’s Not

This project does **not** aim to:
- Provide a GUI or online multiplayer interface
- Include automated or advanced AI logic (yet)
- Implement machine learning or data-driven gameplay (yet)

---

## 📜 License

This project is licensed under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).  
Use, modify, and share freely — just not for commercial purposes.  
If you’d like to use this commercially, reach out and let’s chat!

---

## 📫 Contact

For feedback, contributions, or questions, feel free to open an issue or contact the maintainer.