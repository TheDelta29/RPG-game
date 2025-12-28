## ============================================================================
## PART 1: PLAYER DATA STRUCTURES
## ============================================================================

import random
import copy
import json

player1 = {
    "name": "Aria",
    "hp": 100,
    "max_hp": 100,
    "attack": 15,
    "defense": 5,
    "gold": 20,
    "inventory":
        {
            "potion" : 2,
            "elixir": 1
        },
    "equipment": {}
}

player2 = {
    "name": "Borin",
    "hp": 80,
    "max_hp": 80,
    "attack": 20,
    "defense": 2,
    "gold": 15,
    "inventory":
        {
            "potion" : 1,
            "bomb" : 1
         },
    "equipment": {}
}

player3 = {
    "name": "Cyra",
    "hp": 50,
    "max_hp": 60,
    "attack": 10,
    "defense": 8,
    "gold": 15,
    "inventory": {},
    "equipment": {}
}

party = [player1, player2, player3]

ironsword = [
    {
        "name": "Iron Sword",
        "attack": 5,
        "price": 50,
    }
]

leatherarmor = [
    {
        "name": "Leather Armor",
        "defense": 3,
        "price": 40,
    }
]

shop_items = [
    # ===== COMMON =====
    {"name": "Rusty Sword", "rarity": "common", "attack": 3, "defense": 0, "max_hp": 0, "price": 40},
    {"name": "Wooden Club", "rarity": "common", "attack": 2, "defense": 1, "max_hp": 0, "price": 35},
    {"name": "Training Dagger", "rarity": "common", "attack": 2, "defense": 0, "max_hp": 0, "price": 45},
    {"name": "Padded Vest", "rarity": "common", "attack": 0, "defense": 3, "max_hp": 0, "price": 40},
    {"name": "Worn Buckler", "rarity": "common", "attack": 0, "defense": 2, "max_hp": 0, "price": 50},
    {"name": "Traveler's Boots", "rarity": "common", "attack": 0, "defense": 2, "max_hp": 0, "price": 45},
    {"name": "Simple Amulet", "rarity": "common", "attack": 0, "defense": 0, "max_hp": 3, "price": 35},
    {"name": "Leather Gloves", "rarity": "common", "attack": 1, "defense": 1, "max_hp": 0, "price": 30},

    # ===== UNCOMMON =====
    {"name": "Steel Shortsword", "rarity": "uncommon", "attack": 6, "defense": 0, "max_hp": 0, "price": 80},
    {"name": "Balanced Spear", "rarity": "uncommon", "attack": 5, "defense": 2, "max_hp": 0, "price": 95},
    {"name": "Hunter's Bow", "rarity": "uncommon", "attack": 5, "defense": 0, "max_hp": 0, "price": 100},
    {"name": "Reinforced Leather Armor", "rarity": "uncommon", "attack": 0, "defense": 6, "max_hp": 0, "price": 90},
    {"name": "Guard's Shield", "rarity": "uncommon", "attack": 0, "defense": 4, "max_hp": 0, "price": 100},
    {"name": "Scout's Boots", "rarity": "uncommon", "attack": 0, "defense": 3, "max_hp": 0, "price": 95},
    {"name": "Sturdy Pendant", "rarity": "uncommon", "attack": 0, "defense": 0, "max_hp": 10, "price": 80},
    {"name": "Warrior's Gloves", "rarity": "uncommon", "attack": 3, "defense": 1, "max_hp": 0, "price": 90},

    # ===== RARE =====
    {"name": "Knight's Longsword", "rarity": "rare", "attack": 10, "defense": 0, "max_hp": 0, "price": 150},
    {"name": "Twinfang Daggers", "rarity": "rare", "attack": 8, "defense": 0, "max_hp": 0, "price": 170},
    {"name": "Warhammer of Bruising", "rarity": "rare", "attack": 11, "defense": 0, "max_hp": 0, "price": 160},
    {"name": "Scale Mail Armor", "rarity": "rare", "attack": 0, "defense": 10, "max_hp": 0, "price": 150},
    {"name": "Tower Shield", "rarity": "rare", "attack": 0, "defense": 8, "max_hp": 0, "price": 180},
    {"name": "Strider's Boots", "rarity": "rare", "attack": 0, "defense": 5, "max_hp": 0, "price": 170},
    {"name": "Heartstone Amulet", "rarity": "rare", "attack": 0, "defense": 0, "max_hp": 25, "price": 160},
    {"name": "Brawler's Wraps", "rarity": "rare", "attack": 7, "defense": 2, "max_hp": 0, "price": 170},

    # ===== EPIC =====
    {"name": "Dragonscale Saber", "rarity": "epic", "attack": 15, "defense": 0, "max_hp": 0, "price": 260},
    {"name": "Storm Pike", "rarity": "epic", "attack": 13, "defense": 4, "max_hp": 0, "price": 270},
    {"name": "Shadowstrike Blades", "rarity": "epic", "attack": 14, "defense": -5, "max_hp": 0, "price": 280},
    {"name": "Dragonscale Armor", "rarity": "epic", "attack": 0, "defense": 15, "max_hp": 0, "price": 260},
    {"name": "Bulwark of Dawn", "rarity": "epic", "attack": 0, "defense": 12, "max_hp": 0, "price": 280},
    {"name": "Windrunner Greaves", "rarity": "epic", "attack": 0, "defense": 8, "max_hp": 0, "price": 270},
    {"name": "Amulet of Vitality", "rarity": "epic", "attack": 0, "defense": 0, "max_hp": 50, "price": 260},
    {"name": "Gauntlets of Fury", "rarity": "epic", "attack": 12, "defense": 4, "max_hp": 0, "price": 280},

    # ===== LEGENDARY =====
    {"name": "Blade of the Fallen Star", "rarity": "legendary", "attack": 20, "defense": 0, "max_hp": 0, "price": 380},
    {"name": "Lance of the Eternal Guard", "rarity": "legendary", "attack": 18, "defense": 6, "max_hp": 0, "price": 390},
    {"name": "Nightveil Daggers", "rarity": "legendary", "attack": 17, "defense": -5, "max_hp": 0, "price": 400},
    {"name": "Aegis of Ages", "rarity": "legendary", "attack": 0, "defense": 20, "max_hp": 0, "price": 380},
    {"name": "Celestial Plate", "rarity": "legendary", "attack": 0, "defense": 18, "max_hp": 40, "price": 390},
    {"name": "Boots of the Horizon", "rarity": "legendary", "attack": 0, "defense": 10, "max_hp": 0, "price": 380},
    {"name": "Charm of the Titan Heart", "rarity": "legendary", "attack": 0, "defense": 5, "max_hp": 80, "price": 390},
    {"name": "Gauntlets of the Colossus", "rarity": "legendary", "attack": 18, "defense": 8, "max_hp": 0, "price": 400},

    # ===== MYTHIC =====
    {"name": "Worldbreaker Greatsword", "rarity": "mythic", "attack": 28, "defense": -5, "max_hp": 0, "price": 600},
    {"name": "Spear of Infinite Dawn", "rarity": "mythic", "attack": 24, "defense": 10, "max_hp": 0, "price": 620},
    {"name": "Phantom Edge", "rarity": "mythic", "attack": 26, "defense": -8, "max_hp": 0, "price": 620},
    {"name": "Mythic Dragonplate", "rarity": "mythic", "attack": 0, "defense": 26, "max_hp": 60, "price": 600},
    {"name": "Shield of Timeless Silence", "rarity": "mythic", "attack": 0, "defense": 24, "max_hp": 0, "price": 620},
    {"name": "Boots of the First Wind", "rarity": "mythic", "attack": 0, "defense": 14, "max_hp": 0, "price": 600},
    {"name": "Heart of the World Tree", "rarity": "mythic", "attack": 0, "defense": 8, "max_hp": 120, "price": 620},
    {"name": "Gauntlets of Primordial Rage", "rarity": "mythic", "attack": 24, "defense": 10, "max_hp": 0, "price": 620},

    # ===== EVIL =====
    {"name": "Blood-Drinker Blade", "rarity": "evil", "attack": 24, "defense": 0, "max_hp": -5, "price": 450},
    {"name": "Chains of Torment", "rarity": "evil", "attack": 0, "defense": 22, "max_hp": -10, "price": 430},
    {"name": "Cowl of Whispers", "rarity": "evil", "attack": 18, "defense": 0, "max_hp": -20, "price": 420},
    {"name": "Grasp of the Damned", "rarity": "evil", "attack": 20, "defense": 5, "max_hp": 0, "price": 440},
    {"name": "Boots of the Condemned", "rarity": "evil", "attack": 0, "defense": 10, "max_hp": 0, "price": 430},
    {"name": "Amulet of Withering", "rarity": "evil", "attack": 0, "defense": -4, "max_hp": 80, "price": 450},

    # ===== VOIDLESS =====
    {"name": "Voidless Edge", "rarity": "voidless", "attack": 40, "defense": -10, "max_hp": 0, "price": 9500},
    {"name": "Spear of Null Horizons", "rarity": "voidless", "attack": 35, "defense": 20, "max_hp": 0, "price": 9500},
    {"name": "Armor of the Empty King", "rarity": "voidless", "attack": 0, "defense": 35, "max_hp": 120, "price": 9500},
    {"name": "Shield of Unmade Light", "rarity": "voidless", "attack": 0, "defense": 32, "max_hp": 0, "price": 9500},
    {"name": "Boots of Silent Infinity", "rarity": "voidless", "attack": 0, "defense": 20, "max_hp": 0, "price": 9500},
    {"name": "Heart of the Voidless", "rarity": "voidless", "attack": 0, "defense": 12, "max_hp": 200, "price": 9500},
]

enemies = [
    {
        "name": "Slime",
        "hp": 30,
        "max_hp": 30,
        "attack": 8,
        "defense": 1,
        "inventory": [],
        "gold_reward": 10
    },
    {
        "name": "Big Slime",
        "hp": 50,
        "max_hp": 50,
        "attack": 13,
        "defense": 3,
        "inventory": [],
        "gold_reward": 30
    },
    {
        "name": "Goblin",
        "hp": 45,
        "max_hp": 45,
        "attack": 12,
        "defense": 3,
        "inventory": [],
        "gold_reward": 20
    },
    {
        "name": "Orc",
        "hp": 70,
        "max_hp": 70,
        "attack": 18,
        "defense": 5,
        "inventory": [],
        "gold_reward": 35
    },
]

## ============================================================================
## PART 2: CORE BATTLE FUNCTIONS
## ============================================================================

def calculate_damage(attacker, defender):
    base_damage = attacker["attack"] - defender["defense"]
    if base_damage <= 0:
        base_damage = 0
    return base_damage


def apply_damage(attacker, defender):
    damage = calculate_damage(attacker, defender)
    defender["hp"] = defender["hp"] - damage
    if defender["hp"] <= 0:
        defender["hp"] = 0
    return defender["hp"]


def is_alive(player):
    return player["hp"] > 0


def find_lowest_hp(party):
    if not party:
        return None

    lowest_hp=party[0]
    for player in party:
        if player["hp"] < lowest_hp["hp"]:
            lowest_hp=player
    return lowest_hp

def count_item(player, item_name):
    counter=0
    for item in player["inventory"]:
        if item == item_name:
            counter+=1
    return counter

def use_potion(player, heal_amount):
    if count_item(player, "potion") > 0:
        player["hp"] += heal_amount
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        player["inventory"].remove("potion")
        return True
    return False

def party_attack_power(party):
    total = 0
    if not party:
        return 0
    for player in party:
        if is_alive(player):
            total += player["attack"]
    return total

def party_take_damage(party, attacker):
    new_hp=[]
    for player in party:
        new_hp.append(apply_damage(attacker, player))
    return new_hp

def remove_dead(party):
    new_party=[]
    for player in party:
        if is_alive(player):
            new_party.append(player)
    return new_party

def party_is_alive(party):
    for player in party:
        if player["hp"] > 0:
            return True
    return False

def player_turn(attacker, defender):
    was_alive = is_alive(defender)
    dmg = calculate_damage(attacker, defender)
    if was_alive:
        apply_damage(attacker, defender)
        print("=" * 60)
        print(f"{attacker['name']} has dealt", dmg, f"damage to {defender['name']}")
        print(f"{defender['name']} : ", defender["hp"],'/',defender["max_hp"], "HP")
        print("=" * 60)
        if not is_alive(defender):
            print(f"{defender['name']} has fallen!")
    return defender["hp"]

def battle_round(party, enemy):
    for player in party:
        if is_alive(player):
            player_turn(player, enemy)
            pause()
        if not is_alive(enemy):
            return remove_dead(party), enemy
    if is_alive(enemy):
        enemy_turn(enemy, party)
        pause()

    return remove_dead(party), enemy

def battle(party, enemy):
    round_number = 1
    while party_is_alive(party) and is_alive(enemy):
        print("=" * 60)
        print("ROUND NUMBER : ", round_number)
        print("=" * 60)
        party, enemy = battle_round(party, enemy)
        round_number += 1
    return (party, enemy)

def choose_target(party):
    alive = []
    for player in party:
        if is_alive(player):
            alive.append(player)
    if not alive:
        return None

    return random.choice(alive)

def enemy_turn(enemy, party):
    target = choose_target(party)
    if target is None:
        return None
    else:
        player_turn(enemy, target)
    return target

def pause():
    next = input("")
    return next


def give_loot(party, enemy):
    if enemy['hp'] <= 0:
        alive_party = remove_dead(party)

        # test to see if anyone is still alive
        if alive_party:
            gold_reward = enemy.get("gold_reward", 0)
            gold_per_player = gold_reward // len(alive_party)

            # # give a potion to the first party member that is still alive
            # first_alive = alive_party[0]
            # first_alive["inventory"].append("potion")
            # first_alive["inventory"].sort()
            # print(f'Loot found : potion -> {first_alive["name"]}')

            for player in alive_party:
                player["gold"] += gold_per_player
                print(f"{player['name']} received {gold_per_player} gold !")
                pause()
            print(f"Total party gold : {sum(player["gold"] for player in party)}")
            return True
    else :
        return False

def choose_random_enemy():
    rand = random.choice(enemies)
    enemy=copy.deepcopy(rand)
    return enemy

def party_battle_flow(party, enemy):
    print("=" * 60)
    print(f"A wild {enemy["name"]} has appeared !")
    battle(party, enemy)
    if party_is_alive(party):
        give_loot(party, enemy)
    else:
        print("You have been defeated.")
    return remove_dead(party)

def rest_at_campfire(party):
    remove_dead(party)
    if party_is_alive(party):
        heal_amount = 30
        for player in party:
            print("=" * 60)
            print(f"{player['name']} has {player['hp']} HP")
            print(f"{player['name']} has healed {heal_amount} HP!")
            pause()
            player["hp"] += heal_amount
            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]
            print(f"{player['name']} : ", player["hp"],'/', player["max_hp"], "HP")
            print("=" * 60)
            pause()

def rarity_weight(day):
    starting_day = 1
    end_game = 100
    t = (day - starting_day) / (end_game - starting_day)
    t = max(0.0 , min(1.0, t))
    start = {
        "common": 80,
        "uncommon": 15,
        "rare": 5,
        "epic": 2,
        "legendary": 1,
        "mythic": 0.1,
        "evil": 0.05,
        "voidless": 0.01,
    }

    end = {
        "common": 0.01,
        "uncommon": 0.05,
        "rare": 0.1,
        "epic": 1,
        "legendary": 2,
        "mythic": 5,
        "evil": 15,
        "voidless": 80,
    }

    weights ={}

    for rarity in start:
        a = start[rarity]
        b = end[rarity]
        w = a + (b - a) * t
        weights[rarity] = w

    return weights

def visit_village(party, day):

    weights_dict = rarity_weight(day)
    rarities = ["common", "uncommon", "rare", "epic", "legendary", "mythic", "evil", "voidless"]
    weights = [weights_dict[r] for r in rarities]
    slots = 3
    rolled_rarities = random.choices(rarities, weights=weights, k=slots)
    todays_loot = []
    for r in rolled_rarities:
        loot =  [item for item in shop_items if item["rarity"] == r]
        choice = random.choice(loot)
        todays_loot.append(choice)


    print("Choose a buyer:")
    while True:
        for i, player in enumerate(party, start=1):
            print(f"{i}) {player['name']} (Gold: {player['gold']})")

        buyer_choice = input("Enter player number (or q to leave) : ").strip()
        if buyer_choice == "q":
            print("Thank you for visiting!")
            return

        if not buyer_choice.isdigit():
            print("Invalid player.")
            continue

        idx = int(buyer_choice) - 1
        if idx < 0 or idx >= len(party):
            print("Invalid player.")
            continue

        buyer = party[idx]

        while True:

            print("=" * 60)
            print(f"Hello {buyer['name']}, you have entered Dino's Tavern, what would you like?")
            print(f"Total gold for this player -> {buyer['gold']} gold")


            for x in range(len(todays_loot)):
                item = todays_loot[x]

                parts= []
                if item["attack"] != 0:
                    parts.append(f"+{item['attack']} atk")
                if item["defense"] != 0:
                    parts.append(f"+{item['defense']} def")
                if item["max_hp"] != 0:
                    parts.append(f"+{item['max_hp']} hp")

                stats_text = ", ".join(parts)

                if stats_text:
                    print(f"{x + 1}) {item['name']} ({item['price']} gold [{stats_text}])")
                else:
                    print(f"{x + 1}) {item['name']} ({item['price']} gold)")


            print("c) Change buyer")
            print("m) Return to menu")
            choice = input("Enter your choice, or (c) change buyer, (m) to return to menu: ").strip().lower()

            if choice == "c":
                break

            if choice == "m":
                print("Thank you for visiting")
                return

            if not choice.isdigit():
                print("Invalid choice!")
                pause()
                continue

            idx = int(choice) - 1
            if idx < 0 or idx >= len(todays_loot):
                print("That item number doesnt exist")
                pause()
                continue

            item = todays_loot[idx]

            if buyer["gold"] < item["price"]:
                print("Sorry, you don't have enough gold")
                pause()
                continue

            buyer["gold"] -= item["price"]
            name = item["name"]
            buyer["equipment"][name] = buyer['equipment'].get(name, 0) + 1
            buyer['attack'] += item['attack']
            buyer['defense'] += item['defense']
            buyer['max_hp'] += item['max_hp']
            print(f"{buyer['name']} has bought a(n) {item['name']} for {item['price']} gold !")
            print(f"{buyer['name']} now has {buyer['gold']} gold !")
            pause()


def main():

    global party

    print("1) New game")
    print("2) Load game")
    start_choice = input("> ").strip()

    day = 1

    if start_choice == "1":
        print("Welcome to Dino's Adventure (Press enter to continue)")
        pause()
        print("You can select your action choices with the numbers attributed to them (Press enter to continue)")
        pause()
        print("If no action is specified and nothing is happening press enter to go to the next event (Press enter to continue)")
        pause()
        print("Each action that you do within the main menu makes a day pass (Press enter to continue)")
        pause()
        print("Each day that passes the game gets harder and more loot is available (Press enter to continue)")
        pause()
        print("Have fun and try to survive as long as possible (Press enter to continue)")
        pause()

    elif start_choice == "2":
        loaded_day, loaded_party = load_game()
        if loaded_day is not None:
            day = loaded_day
            party = loaded_party

    else:
        print("Invalid choice!")

    while True:
        print("\n" + "=" * 60)
        print(f"Day : {day}")
        print("1) Battle")
        print("2) Rest at the Campfire")
        print("3) Visit Village")
        print("4) Check a player's stat page")
        print("5) Save & Quit")
        print("6) Quit without saving")
        choice = input("Enter your choice: ")
        if choice == "1":
            enemy = choose_random_enemy()
            party_battle_flow(party, enemy)
            day += 1
        elif choice == "2":
            rest_at_campfire(party)
            day += 1
        elif choice == "3":
            visit_village(party, day)
            day += 1
        elif choice == "4":
            print("Choose a player:")
            for i, player in enumerate(party, start=1):
                print(f"{i}) {player['name']}")
            choice = input("Enter player number: ")
            idx = int(choice) - 1
            if idx < 0 or idx >= len(party):
                print("Invalid player.")
                continue
            player = party[idx]
            print("=" * 60)
            print(f"{player['name']} : ", player["hp"],'/',player["max_hp"], "HP")
            print(f"Attack : {player["attack"]}")
            print(f"Defense : {player["defense"]}")
            print(f"Gold : {player['gold']}")
            print("=" * 60)
            pause()
            choice2 = input("Would you like to see the equipments of this player? (y/n) :")
            if choice2 == "y":
                for item, count in player["equipment"].items():
                    print(f"{item} x{count}")
                    pause()
            else :
                return

        elif choice == "5":
            save_game(day, party)
            print("Thank you for playing!")
            break
        elif choice == "6":
            sure = input("Are you sure you want to quit without saving? (y/n) : ")
            if sure == "y":
                print("Thank you for playing!")
                break
            elif sure == "n":
                return
            else:
                print("Invalid choice!")
        else:
            print("Invalid choice!")

SAVE_FILE = "savegame.json"

def save_game(day, party):
    data = {
        "day": day,
        "party": party,
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Game saved!")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        print("Game loaded!")
        return data["day"], data["party"]
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None, None

if __name__ == "__main__":
    main()