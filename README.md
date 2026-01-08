# Dino's Adventure (Python Text RPG)

A simple text-based, party-based RPG in Python: fight enemies, rest at the campfire, and visit a village shop to buy equipment as the days get harder. 

## Features
- Party-based gameplay: 3 characters with their own stats, gold, mana, inventory, equipment, XP, and levels.
- Turn-based combat with:
  - Dodge chance (based on agility).
  - Critical hits for basic attacks and spells.
  - Spells with mana costs (Fireball, Icequake).
  - Items during combat (Potion healing).
- Day progression system:
  - Each main-menu action advances the day.
  - Enemies scale up slightly with day count (HP/attack/defense/rewards).
- Campfire rest: heals the party (if alive).
- Village shop:
  - Daily rotating selection (3 items).
  - Weighted rarity system that shifts toward higher rarities as days increase.
  - Buying items permanently increases stats (attack/defense/max HP) and records equipment owned.
- Progression:
  - Gold + XP rewards after battles.
  - Level ups grant max HP and stat points.
  - Spend stat points to upgrade max HP, attack, defense, agility, or intelligence.
- Save/Load system:
  - JSON save file (`savegame.json`) stores day + party data.

## Requirements
- Python 3.x
- `colorama` (used for colored combat output)

Install:
```bash
pip install colorama
