## ============================================================================
## PART 1: DATA IMPORT
## ============================================================================

import random
import copy
import json
from colorama import *
from UI.mainmenu import mainloop


with open("data/enemies.json", "r", encoding="utf-8") as f:
    enemies = json.load(f)

with open("data/shop_items.json", "r", encoding="utf-8") as f:
    shop_items = json.load(f)

with open("data/players.json", "r", encoding="utf-8") as f:
    party_template = json.load(f)

with open("data/crits.json", "r", encoding="utf-8") as f:
    crits_raw = json.load(f)

crits = {int(k): v for k, v in crits_raw.items()}

with open("data/spells.json", "r", encoding="utf-8") as f:
    spells = json.load(f)

with open("data/bosses.json", "r", encoding="utf-8") as f:
    bosses = json.load(f)

## ============================================================================
## PART 2: CORE BATTLE FUNCTIONS
## ============================================================================

def calculate_damage(attacker, defender):
    base_damage = attacker["attack"] * (1 + (attacker.get("strength", 0) / 25 )) - defender["defense"]
    if base_damage <= 0:
        base_damage = 0
    return round(max(1, base_damage))


def apply_damage(attacker, defender):

    if random.random() < dodge_chance(defender):
        print(f"{defender['name']} has",Style.BRIGHT,Fore.YELLOW,"dodged the attack !",Style.RESET_ALL)
        return 0

    damage = calculate_damage(attacker, defender)
    p = crit_chance(attacker)
    layers = int(p)
    extra = p - layers

    if random.random() < extra:
        layers += 1

    if layers > 0:
        text = crits.get(layers, f"{layers}x critical hit!")
        print(text)
        pause()
        damage *= 2

    defender["hp"] = defender["hp"] - damage
    if defender["hp"] <= 0:
        defender["hp"] = 0
    return round(damage)

def dodge_chance(player):
    agility = player.get("agility", 0)
    cap = 0.35
    scaling = 40
    return cap * (agility / (agility + scaling)) if agility > 0 else 0

def crit_chance(player):
    agility = player.get("agility", 0)
    return agility / 100

def spell_crit_chance(player):
    intelligence = player.get("intelligence", 0)
    return intelligence / 100

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
    if player["inventory"].get('potion', 0) > 0:
        player["hp"] += heal_amount
        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]
        player["inventory"]['potion'] -= 1
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

def use_spell(player, spell):
    if player["mana"] < spell["mana_cost"]:
        print("You don't have enough",Style.BRIGHT,Fore.BLUE,"mana!",Style.RESET_ALL)
        return
    else:
        player["mana"] -= spell["mana_cost"]
        return spell["damage"]

def apply_spell_damage(spell, attacker, defender):
    damage = spell["damage"]
    p = spell_crit_chance(attacker)
    layers = int(p)
    extra = p - layers

    if random.random() < extra:
        layers += 1

    if layers > 0:
        text = crits.get(layers, f"{layers}x critical hit!")
        print(text)
        pause()
        damage *= 2

    defender["hp"] = defender["hp"] - damage
    if defender["hp"] <= 0:
        defender["hp"] = 0
    return round(damage)

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
    if was_alive:
        print("1) Attack")
        print("2) Cast a spell")
        print("3) Use an item")
        print("4) Try to escape")
        choice = input('Which action do you want to do ?')
        if choice == "1" :
            dmg = apply_damage(attacker, defender)
            print("=" * 60)
            print(Fore.GREEN,Style.BRIGHT,f"{attacker['name']}", Style.RESET_ALL, "has dealt",Fore.RED,Style.BRIGHT,round(dmg),Style.RESET_ALL, f"damage to {defender['name']}")
            print(Fore.RED,Style.BRIGHT,f"{defender['name']}",Style.RESET_ALL, ":", Fore.RED,Style.BRIGHT,round(defender["hp"]),'/',round(defender["max_hp"]),Style.RESET_ALL, "HP")
            print("=" * 60)
        elif choice == "2" :
            print("You currently have",Fore.BLUE,Style.BRIGHT,f"{attacker['mana']}",Style.RESET_ALL," mana")
            print("1) Fireball |",Fore.RED,Style.BRIGHT,"Damage : 45",Style.RESET_ALL,"|",Fore.BLUE,Style.BRIGHT,"Mana cost : 50",Style.RESET_ALL)
            print("2) Icequake |",Fore.RED,Style.BRIGHT,"Damage : 30",Style.RESET_ALL,"|",Fore.BLUE,Style.BRIGHT,"Mana cost : 35",Style.RESET_ALL)
            print("3) Back")
            choice2 = input("Which spell do you want to cast ? ")
            if choice2 == "1" :
                dmg = apply_spell_damage(spells[0], attacker, defender)
                print("=" * 60)
                print(Fore.GREEN,Style.BRIGHT,f"{attacker['name']}",Style.RESET_ALL, "has cast Fireball and dealt",Fore.RED,Style.BRIGHT,round(dmg),Style.RESET_ALL, f"damage to {defender['name']}")
                print(Fore.GREEN,Style.BRIGHT,f"{defender['name']}",Style.RESET_ALL, ":", Fore.RED,Style.BRIGHT,round(defender["hp"]),'/',round(defender["max_hp"]),Style.RESET_ALL, "HP")
                print("=" * 60)
            elif choice2 == "2" :
                dmg = apply_spell_damage(spells[1], attacker, defender)
                print("=" * 60)
                print(Fore.GREEN,Style.BRIGHT,f"{attacker['name']}",Style.RESET_ALL, "has cast Icequake and dealt",Fore.RED,Style.BRIGHT,round(dmg),Style.RESET_ALL, f"damage to {defender['name']}")
                print(Fore.GREEN,Style.BRIGHT, f"{defender['name']}", Style.RESET_ALL, ":", Fore.RED, Style.BRIGHT,round(defender["hp"]), '/', round(defender["max_hp"]), Style.RESET_ALL, "HP")
                print("=" * 60)
            elif choice2 == "3" :
                return
        elif choice == "3" :
            print("1) Potion | Heal amount : 30")
            print("2) Back")
            choice3 = input("Which item do you want to use ? ")
            if choice3 == "1" :
                if attacker["hp"] == attacker["max_hp"]:
                    print("You are already at full health!")
                    return
                elif "potion" in attacker["inventory"]:
                    use_potion(attacker, 30)
                    print("=" * 60)
                    print(Fore.GREEN,Style.BRIGHT,f"{attacker['name']}",Style.RESET_ALL,"has used a potion and healed for",Fore.GREEN,Style.BRIGHT,"30",Style.RESET_ALL,"HP!")
                    print("=" * 60)
                else:
                    print("You don't have a potion!")
                    return
            elif choice3 == "2" :
                return
        elif choice == "4" :
            ans = input("Are you sure you want to try to run away ? y/n")
            if ans == 'y':
                print("=" * 60)
                print(f"{attacker['name']} has run away from the battle!")
                print("=" * 60)
                return defender["hp"]
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
        dmg = round(apply_damage(enemy, target))
        print("=" * 60)
        print(f"{enemy["name"]} has dealt",Style.BRIGHT,Fore.RED,f"{dmg}",Style.RESET_ALL,"damage to",Style.BRIGHT,Fore.GREEN,f"{target['name']}",Style.RESET_ALL,"!")
        print(f"{target['name']} : ",Style.BRIGHT,Fore.RED,target["hp"],'/', target["max_hp"],Style.RESET_ALL,"HP")
        print("=" * 60)

    return target

def pause():
    next = input("Press Enter to continue...")
    return next

def check_level_up(player):
    while player["xp"] >= xp_to_level(player["level"]):
        cost = xp_to_level(player["level"])
        player["xp"] -= cost
        player["level"] += 1
        player["max_hp"] += 5
        player["stat_points"] += 3
        print(Style.BRIGHT,Fore.GREEN,f"{player['name']}",Style.RESET_ALL,f" has leveled up to Lv. {player['level']}!")
    return player

def give_loot(party, enemy):
    if enemy['hp'] <= 0:
        alive_party = remove_dead(party)

        # test to see if anyone is still alive
        if alive_party:
            gold_reward = enemy.get("gold_reward", 0)
            gold_per_player = gold_reward // len(alive_party)

            xp_reward = enemy.get("xp_reward", 0)

            # # give a potion to the first party member that is still alive
            # first_alive = alive_party[0]
            # first_alive["inventory"].append("potion")
            # first_alive["inventory"].sort()
            # print(f'Loot found : potion -> {first_alive["name"]}')

            for player in alive_party:
                player["gold"] += gold_per_player
                print(Style.BRIGHT,Fore.GREEN,f"{player['name']}",Style.RESET_ALL,f"received {gold_per_player}",Style.BRIGHT,Fore.YELLOW,"gold",Style.RESET_ALL,"!")
                player["xp"] += xp_reward
                print(Style.BRIGHT,Fore.GREEN,f"{player['name']}",Style.RESET_ALL,f"received {xp_reward} xp !")
                check_level_up(player)
                pause()
            print("Total party gold :",Style.BRIGHT,Fore.YELLOW,f"{sum(player["gold"] for player in party)}",Style.RESET_ALL)
            return True
    else :
        return False

def choose_random_enemy(day):
    if random.random() < boss_spawn_chance(day):
        weights_by_diff = boss_weight(day)
        diff = list(weights_by_diff.keys())
        difficulty_weights = [weights_by_diff[t] for t in diff]
        chosen_diff = random.choices(diff, weights=difficulty_weights, k=1)[0]

        chosen_one = [b for b in bosses if b.get("difficulty", 0) == chosen_diff]
        if not chosen_one:
            chosen_one = bosses

        boss = copy.deepcopy(random.choices(chosen_one, k=1)[0])
        boss["is_boss"] = True
        print("A boss has appeared! This enemy is much tougher than normal enemies.")
        return scale_enemy(boss, day)

    weights_by_tier = monster_weight(day)
    tiers = list(weights_by_tier.keys())
    tier_weights = [weights_by_tier[t] for t in tiers]
    chosen_tier = random.choices(tiers, weights=tier_weights, k=1)[0]

    chosen = [e for e in enemies if e.get("tier", 0) == chosen_tier]
    if not chosen:
        chosen = enemies

    enemy=copy.deepcopy(random.choice(chosen))

    return scale_enemy(enemy, day)

def scale_enemy(enemy, day):
    hp_scale = 1.05 ** (day - 1 )
    stat_scale = 1.03 ** (day - 1 )

    enemy["hp"] = int(enemy["hp"] * hp_scale)
    enemy["max_hp"] = int(enemy["max_hp"] * hp_scale)
    enemy["attack"] = int(enemy["attack"] * stat_scale)
    enemy["defense"] = int(enemy["defense"] * stat_scale)
    enemy["gold_reward"] = int(enemy["gold_reward"] * stat_scale)
    enemy["xp_reward"] = int(enemy["xp_reward"] * stat_scale)
    return enemy

def boss_spawn_chance(day, start_chance=0.01, cap=0.25, ramp_days=40):
    t = (day - 1) / ramp_days
    t = max(0.0 , min(1.0, t))
    chance = start_chance + (cap - start_chance) * t
    return chance

def party_battle_flow(party, enemy):
    print("=" * 60)
    print(f"A wild {enemy["name"]} has appeared !")
    print("It has",Style.BRIGHT,Fore.RED,f"{enemy["hp"]}/{enemy['max_hp']}",Style.RESET_ALL,"HP !")
    print("=" * 60)
    battle(party, enemy)
    if party_is_alive(party):
        give_loot(party, enemy)
        for player in party:
            player["mana"] = player["max_mana"]
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

def spell_check(player, spell):
    return player if player["mana"] >= spell["mana_cost"] else False

def xp_to_level(level):
    return 50 * level

def display_stat_page(player):
    print("Name : ",Style.BRIGHT,Fore.WHITE,f"{player['name']}",Style.RESET_ALL)
    print(f"Level : ",Style.BRIGHT,Fore.GREEN,f"{player['level']}",Style.RESET_ALL,)
    print(f"Experience : ",Style.BRIGHT,Fore.GREEN,f"{player['xp']}/{xp_to_level(player['level'])}",Style.RESET_ALL,)
    print(f"Health : ",Style.BRIGHT,Fore.RED,f"{player['hp']}/{player['max_hp']}",Style.RESET_ALL)
    print(f"Strength : ",Style.BRIGHT,Fore.RED,f"{player.get('strength', 0)}",Style.RESET_ALL)
    print(f"Defense : ",Style.BRIGHT,Fore.WHITE,f"{player.get('defense', 0)}",Style.RESET_ALL)
    print(f"Agility : ",Style.BRIGHT,Fore.GREEN,f"{player.get('agility', 0)}",Style.RESET_ALL)
    print(f"Intelligence : ",Style.BRIGHT,Fore.RED,f"{player.get('intelligence', 0)}",Style.RESET_ALL)
    print(f"Mana : ",Style.BRIGHT,Fore.BLUE,f"{player['mana']}/{player['max_mana']}",Style.RESET_ALL)
    print(f"Available Stat Points : ",Style.BRIGHT,Fore.GREEN,f"{player['stat_points']}",Style.RESET_ALL)
    return

def spend_stat_points(player):
    print("You can spend your stat points to upgrade your character :")
    display_stat_page(player)
    choice = input("Enter the number of stat points you want to spend (or q to quit) : ").strip().lower()
    if choice == "q":
        return player
    if choice.isdigit():
        if int(choice) > player["stat_points"]:
            print("You don't have enough stat points!")
        else:
            player["stat_points"] -= int(choice)
            print("1) Max HP  | This increases your maximum health.")
            print("2) Attack  | This increases your base damage.")
            print("3) Defense  | This reduces the damage you receive.")
            print("4) Agility  | This increases your chance to dodge attacks and your critical strike chance for attacks.")
            print("5) Intelligence | This increases your critical hit rate with spells and your max mana.")
            choice2 = input("What do you want to spend them on ? ")
            if choice2 == "1":
                player["max_hp"] += int(choice)
                player["hp"] += int(choice)
                print("You have increased your max health by :", choice)
            elif choice2 == "2":
                player["attack"] += int(choice)
                print("You have increased your attack by :", choice)
            elif choice2 == "3":
                player["defense"] += int(choice)
                print("You have increased your defense by :", choice)
            elif choice2 == "4":
                player["agility"] += int(choice)
                print("You have increased your agility by :", choice)
            elif choice2 == "5":
                player["intelligence"] += int(choice)
                player["max_mana"] += int(choice)
                player["mana"] = player["max_mana"]
                print("You have increased your intelligence and your max mana by :", choice)
            else:
                print("Invalid choice!")


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

def monster_weight(day):
    starting_day = 1
    end_game = 100
    t = (day - starting_day) / (end_game - starting_day)
    t = max(0.0 , min(1.0, t))
    start = {
        1: 80,
        2: 15,
        3: 5,
        4: 2,
        5: 1,
        6: 0.1,
        7: 0.05,
        8: 0.01,
        9: 0.005,
        10: 0.001,
    }

    end = {
        1: 0.001,
        2: 0.005,
        3: 0.01,
        4: 0.05,
        5: 0.1,
        6: 1,
        7: 2,
        8: 5,
        9: 15,
        10: 80,
    }

    weights ={}

    for difficulty in start:
        a = start[difficulty]
        b = end[difficulty]
        w = a + (b - a) * t
        weights[difficulty] = w

    return weights

def boss_weight(day):
    starting_day = 1
    end_game = 100
    t = (day - starting_day) / (end_game - starting_day)
    t = max(0.0 , min(1.0, t))
    start = {
        1: 80,
        2: 15,
        3: 5,
        4: 2,
        5: 1,
        6: 0.1,
        7: 0.05,
        8: 0.01,
        9: 0.005,
        10: 0.001,
    }

    end = {
        1: 0.001,
        2: 0.005,
        3: 0.01,
        4: 0.05,
        5: 0.1,
        6: 1,
        7: 2,
        8: 5,
        9: 15,
        10: 80,
    }

    weights ={}

    for difficulty in start:
        a = start[difficulty]
        b = end[difficulty]
        w = a + (b - a) * t
        weights[difficulty] = w

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
            choice = input("Enter your choice, or (c) change buyer, (m) to return to menu : ").strip().lower()

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
            continue

    return


def main():

    global party


    print("1) New game")
    print("2) Load game")
    start_choice = input("> ").strip()

    day = 1

    if start_choice == "1":
        party = copy.deepcopy(party_template)
        print("Welcome to Dino's Adventure")
        pause()
        print("You can select your action choices with the numbers attributed to them")
        pause()
        print("If no action is specified and nothing is happening press enter to go to the next event")
        pause()
        print("Each action that you do within the main menu makes a day pass")
        pause()
        print("Each day that passes the game gets harder and more loot is available")
        pause()
        print("Have fun and try to survive as long as possible")
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
            enemy = choose_random_enemy(day)
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
            if not choice.isdigit():
                print("Choice invalid")
                continue
            idx = int(choice) - 1
            if idx < 0 or idx >= len(party):
                print("Invalid player.")
                continue

            player = party[idx]
            print("=" * 60)
            print(Fore.GREEN,Style.BRIGHT,f"Level : {player['level']}")
            print(Fore.GREEN,Style.BRIGHT,f"Available Stat Points : {player['stat_points']}")
            print(Fore.RED,Style.BRIGHT,f"{player['name']} : ", player["hp"],'/',player["max_hp"], "HP")
            print(Fore.RED,Style.BRIGHT,f"Attack : {player["attack"]}")
            print(Fore.WHITE,Style.BRIGHT,f"Defense : {player["defense"]}")
            print(Fore.YELLOW,Style.BRIGHT,f"Gold : {player['gold']}",Style.RESET_ALL)
            print("=" * 60)
            print("=" * 23, "- Equipments -", "=" * 23)
            for item, count in player["equipment"].items():
                print(f"{item} x{count}")
            pause()
            if player["stat_points"] > 0:
                choice2 = input("Would you like to spend your stat points ? (y/n) :")
                if choice2 == "y":
                    spend_stat_points(player)
                    pause()
            else :
                continue

        elif choice == "5":
            save_game(day, party)
            print("Thank you for playing!")
            break
        elif choice == "6":
            sure = input("Are you sure you want to quit without saving? (y/n) : ").strip().lower()
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
    mainloop()