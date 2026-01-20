# Dino's Adventure (Python RPG)

A passion project to build a turn-based RPG in Python with Pygame. Fight enemies, rest at the campfire, visit the village shop, and progress through increasingly difficult days.

## Features

### Core Gameplay
- **Party-based combat:** Control 3 characters with unique stats, equipment, and progression
- **Turn-based battles:** Strategic combat with dodge chance, critical hits, and spell casting
- **Day progression system:** Each action advances the day; enemies scale in difficulty
- **Dynamic enemy spawning:** Tier-based monsters with boss encounters (chance increases over time)
- **Campfire rest:** Heal your party between battles

### Character Progression
- **Experience & Leveling:** Gain XP from battles; level up to increase stats
- **Stat points system:** Spend points to upgrade max HP, attack, defense, agility, or intelligence
- **Equipment & loot:** Buy gear from the village shop with weighted rarity scaling
- **Inventory & gold:** Track equipment, items, and wealth across your party

### Village Shop
- **Daily rotating inventory:** 3 random items each day with rarity-weighted selection
- **Progressive difficulty:** Higher rarity items appear as days increase
- **Stat bonuses:** Equipment permanently boosts attack, defense, and max HP

### Save System
- **JSON-based saves:** Store day number and full party state
- **Load existing games:** Resume progress from main menu

## Installation & Launch Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/TheDelta29/RPG-game.git
cd RPG-game
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Run the Game
```bash
python run.py
```

## How to Play

### Main menu
- **Start Game** - Begin a new game with 3 default characters
- **Load Game** - Resume from your last save (if savegame.json exists)
- **Options** - Audio/Video settings (placeholder)
- **Quit** - Exit the game

## Overworld (Day Menu)
### Each day you can choose one action: 
- **Battle** - Fight a randomly selected enemy; gain XP and gold on victory
- **Rest at a campfire** - Heal all living party members; advance to next day
- **Visit the village shop** - Shop for equipment to boost stats
- **Check Stats** - View character stats and spend stat points
- **Save & Quit** - Saves your game and quits
- **Quit without saving** - Exits without saving

## Combat
- **Attack** — Deal physical damage based on attack stat and opponent's defense

- **Cast Spell** — Use Fireball or Icequake (cost mana, have crit chance)

- **Use Item** — Drink a potion to heal (30 HP)

- **Run** — Attempt to escape the battle

## Combat Features:

- Dodge chance (scales with agility)

- Critical hits for attacks and spells

- Enemy turn-based responses

- Loot and XP rewards on victory

## Project Structure

```bash
RPG/
├── main.py                 # Core game logic (combat, progression, items)
├── run.py                  # Entry point; starts the Pygame loop
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── UI/                     # All UI states and rendering
│   ├── __init__.py
│   ├── button.py           # Button class for UI interaction
│   ├── mainmenu.py         # Main Pygame loop and state machine
│   ├── menustate.py        # Menu screen (Start/Load/Quit)
│   ├── overworldstate.py   # Overworld day menu
│   ├── battlestate.py      # Turn-based combat UI
│   └── (future: villagestate.py, statsstate.py, etc.)
│
└── data/                   # Game data files (JSON)
    ├── enemies.json        # Enemy definitions (tiered)
    ├── bosses.json         # Boss definitions
    ├── players.json        # Default party template
    ├── shop_items.json     # Equipment catalog with rarities
    ├── spells.json         # Spell definitions (mana cost, damage)
    ├── crits.json          # Critical hit multiplier text
    └── backgrounds/        # Background images for UI states
```

## Game Architecture
The game uses a **state machine pattern** with Pygame:

- Single main loop in ```mainmenu.py``` delegates to the current state

- States (Menu, Overworld, Battle) handle their own events, updates, and rendering

- Transitions between states return action tuples (e.g., ```("switch", "battle")```)

- Game logic in ```main.py``` is decoupled from UI rendering

This keeps code modular and makes adding new screens (Village, Stats, etc.) straightforward.

## Requirements

``` bash
pygame==2.5.2
colorama==0.4.6
```

## License
This is a personal learning project. Feel free to fork and modify!

## Contact
For questions or feedback, open an issue on GitHub.

Made with ❤️ while learning Python game development