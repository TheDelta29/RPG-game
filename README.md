# Text RPG (Python)
A simple text-based RPG written in Python where you manage a party, fight enemies, rest to recover, and visit a village shop to upgrade your characters.

## Features
- Party-based gameplay (multiple characters with their own gold and stats).
- Turn-based combat loop (battle / rest / village).
- Village shop with a rotating daily inventory.
- Weighted rarity system: the shop can roll any rarity at any time, but higher rarities become more likely as in-game days progress (using `random.choices` weights).

## Tech / Structure
- Pure Python (no external dependencies).
- Data-driven items: shop items are stored as a list of dictionaries (name, rarity, stats, price).
- Save system: game state can be stored and loaded (JSON-based).
  
## Notes
This project is a learning-focused RPG prototype. Balance values, items, and rarity weights are expected to change over time.
