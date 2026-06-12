import random

bag = []
player = {}
box = []

def startup():
    player["arena_badges"] = 0
    player["top4_badges"] = 0
    print("Willkommen zu Pokémon!")
    print("Du bist ein Trainer und dein Ziel ist es, der beste Pokémon-Trainer zu werden.")
    print("Fange Pokémon, sammle Items und heile deine Pokémon, um stärker zu werden.")
    print("Wenn du eine Arena nicht schaffst hast du verloren")

    print("Bevor wir starten, wie ist dein Name?")
    trainer_name = input("Dein Name: ")

    print(f"\nHallo {trainer_name}!")
    starter = starter_pokemon()

    print("Wo möchtest du starten? (x, y)")
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            friend(x)
            print(f"Dein Trainer ist {friend(x)}")
            break
        except ValueError:
            print("Bitte gib nur Zahlen ein. Neuer Versuch.")
            
    print("Auf welcher Schwierigkeit möchtest du spielen? (1 (leicht) -3 (schwer))")
    
    while True:
        try:
            difficulty = int(input("Schwierigkeit: "))
            if difficulty < 1 or difficulty > 3:
                print("Bitte gib nur eine Zahl zwischen 1 und 3 ein. Neuer Versuch.")
            else:
                break
        except ValueError:
            print("Bitte gib nur Zahlen ein. Neuer Versuch.")
            
    print("Wie soll dein Rivale heißen?")
    rival_name = input("Name: ")

    print("\nMit wie viel Geld möchtest du starten?")

    while True:
        try:
            money = int(input("Geld: "))
            if money < 0:
                print("Bitte gib eine positive Zahl ein. Neuer Versuch.")
            else:
                break
        except ValueError:
            print("Bitte gib nur Zahlen ein. Neuer Versuch.")
            
    player["geld"] = money
    player["name"] = trainer_name
    player["trainer"] = friend(x)
    player["difficulty"] = difficulty
    player["starter"] = starter["name"]
    player["rival"] = rival_name

    print("Viel Spaß auf deiner Reise!\n")
    return trainer_name

def battle(player_pokemon, enemy_pokemon):

    print(f"\nEin wildes {enemy_pokemon['name']} erscheint!")

    while True:

        print("\n-------------------")
        print(f"{player_pokemon['name']} KP: {player_pokemon['health']}")
        print(f"{enemy_pokemon['name']} KP: {enemy_pokemon['health']}")

        print("\nWas möchtest du tun?")
        print("1. Angreifen")
        print("2. Heilen")
        print("3. Fliehen")

        choice = input("Auswahl: ")

        if choice == "1":

            damage = random.randint(8, 15)
            enemy_pokemon["health"] -= damage

            print(
                f"\n{player_pokemon['name']} macht "
                f"{damage} Schaden!"
            )

            if enemy_pokemon["health"] <= 0:
                print(f"{enemy_pokemon['name']} wurde besiegt!")
                return True

        elif choice == "2":

            if len(bag) == 0:
                print("\nDu hast keine Heilitems!")

            else:
                heal_pokemon()

        elif choice == "3":

            chance = random.randint(1, 100)

            if chance <= 50:
                print("\nDu bist erfolgreich geflohen!")
                return False
            else:
                print("\nFlucht fehlgeschlagen!")

        else:
            print("\nUngültige Eingabe!")
            continue

        enemy_damage = random.randint(5, 12)

        player_pokemon["health"] -= enemy_damage

        print(
            f"\n{enemy_pokemon['name']} macht "
            f"{enemy_damage} Schaden!"
        )

        if player_pokemon["health"] <= 0:
            print(f"\n{player_pokemon['name']} wurde besiegt!")
            return False

def starter_pokemon():
    starters = [
        {"name": "Bisasam", "health": 45, "typ": "Pflanze", "typ2": "Gift"},
        {"name": "Glumanda", "health": 39, "typ": "Feuer"},
        {"name": "Schiggy", "health": 44, "typ": "Wasser"}
    ]

    print("Wähle dein Starter-Pokémon:")

    for i, pokemon in enumerate(starters, start=1):
        print(f"{i}. {pokemon['name']} - KP: {pokemon['health']}")

    while True:
        try:
            choice = int(input("\nDeine Wahl (1-3): "))

            if choice < 1 or choice > 3:
                print("Bitte gib nur eine Zahl zwischen 1 und 3 ein. Neuer Versuch.")
            else:
                break 

        except ValueError:
            print("Bitte gib nur Zahlen ein. Neuer Versuch.")

    starter = starters[choice - 1]

    box.append(starter)
    player["starter"] = starter["name"]

    print(f"\nDu hast {starter['name']} als dein Starter-Pokémon gewählt!")
    return starter

def find_pokemon():

    pokemon_team = [

        {"name": "Bisasam", "health": 45, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Bisaknosp", "health": 60, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 2},
        {"name": "Bisaflor", "health": 80, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 3},

        {"name": "Glumanda", "health": 39, "typ": "Feuer", "typ2": None, "evolution_stage": 1},
        {"name": "Glutexo", "health": 58, "typ": "Feuer", "typ2": None, "evolution_stage": 2},
        {"name": "Glurak", "health": 78, "typ": "Feuer", "typ2": "Flug", "evolution_stage": 3},

        {"name": "Schiggy", "health": 44, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Schillok", "health": 59, "typ": "Wasser", "typ2": None, "evolution_stage": 2},
        {"name": "Turtok", "health": 79, "typ": "Wasser", "typ2": None, "evolution_stage": 3},

        {"name": "Raupy", "health": 45, "typ": "Käfer", "typ2": None, "evolution_stage": 1},
        {"name": "Safcon", "health": 50, "typ": "Käfer", "typ2": None, "evolution_stage": 2},
        {"name": "Smettbo", "health": 60, "typ": "Käfer", "typ2": "Flug", "evolution_stage": 3},

        {"name": "Hornliu", "health": 40, "typ": "Käfer", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Kokuna", "health": 45, "typ": "Käfer", "typ2": "Gift", "evolution_stage": 2},
        {"name": "Bibor", "health": 65, "typ": "Käfer", "typ2": "Gift", "evolution_stage": 3},

        {"name": "Taubsi", "health": 40, "typ": "Normal", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Tauboga", "health": 63, "typ": "Normal", "typ2": "Flug", "evolution_stage": 2},
        {"name": "Tauboss", "health": 83, "typ": "Normal", "typ2": "Flug", "evolution_stage": 3},

        {"name": "Rattfratz", "health": 30, "typ": "Normal", "typ2": None, "evolution_stage": 1},
        {"name": "Rattikarl", "health": 55, "typ": "Normal", "typ2": None, "evolution_stage": 2},

        {"name": "Habitak", "health": 40, "typ": "Normal", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Ibitak", "health": 65, "typ": "Normal", "typ2": "Flug", "evolution_stage": 2},

        {"name": "Rettan", "health": 35, "typ": "Gift", "typ2": None, "evolution_stage": 1},
        {"name": "Arbok", "health": 60, "typ": "Gift", "typ2": None, "evolution_stage": 2},

        {"name": "Pikachu", "health": 35, "typ": "Elektro", "typ2": None, "evolution_stage": 1},
        {"name": "Raichu", "health": 60, "typ": "Elektro", "typ2": None, "evolution_stage": 2},

        {"name": "Sandan", "health": 50, "typ": "Boden", "typ2": None, "evolution_stage": 1},
        {"name": "Sandamer", "health": 75, "typ": "Boden", "typ2": None, "evolution_stage": 2},

        {"name": "Nidoran♀", "health": 55, "typ": "Gift", "typ2": None, "evolution_stage": 1},
        {"name": "Nidorina", "health": 70, "typ": "Gift", "typ2": None, "evolution_stage": 2},
        {"name": "Nidoqueen", "health": 90, "typ": "Gift", "typ2": "Boden", "evolution_stage": 3},

        {"name": "Nidoran♂", "health": 46, "typ": "Gift", "typ2": None, "evolution_stage": 1},
        {"name": "Nidorino", "health": 61, "typ": "Gift", "typ2": None, "evolution_stage": 2},
        {"name": "Nidoking", "health": 81, "typ": "Gift", "typ2": "Boden", "evolution_stage": 3},

        {"name": "Piepi", "health": 70, "typ": "Fee", "typ2": None, "evolution_stage": 1},
        {"name": "Pixi", "health": 95, "typ": "Fee", "typ2": None, "evolution_stage": 2},

        {"name": "Vulpix", "health": 38, "typ": "Feuer", "typ2": None, "evolution_stage": 1},
        {"name": "Vulnona", "health": 73, "typ": "Feuer", "typ2": None, "evolution_stage": 2},

        {"name": "Pummeluff", "health": 115, "typ": "Normal", "typ2": "Fee", "evolution_stage": 1},
        {"name": "Knuddeluff", "health": 140, "typ": "Normal", "typ2": "Fee", "evolution_stage": 2},

        {"name": "Zubat", "health": 40, "typ": "Gift", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Golbat", "health": 75, "typ": "Gift", "typ2": "Flug", "evolution_stage": 2},

        {"name": "Myrapla", "health": 45, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Duflor", "health": 60, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 2},
        {"name": "Giflor", "health": 75, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 3},

        {"name": "Paras", "health": 35, "typ": "Käfer", "typ2": "Pflanze", "evolution_stage": 1},
        {"name": "Parasek", "health": 60, "typ": "Käfer", "typ2": "Pflanze", "evolution_stage": 2},

        {"name": "Bluzuk", "health": 60, "typ": "Käfer", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Omot", "health": 70, "typ": "Käfer", "typ2": "Gift", "evolution_stage": 2},

        {"name": "Digda", "health": 10, "typ": "Boden", "typ2": None, "evolution_stage": 1},
        {"name": "Digdri", "health": 35, "typ": "Boden", "typ2": None, "evolution_stage": 2},

        {"name": "Mauzi", "health": 40, "typ": "Normal", "typ2": None, "evolution_stage": 1},
        {"name": "Snobilikat", "health": 65, "typ": "Normal", "typ2": None, "evolution_stage": 2},

        {"name": "Enton", "health": 50, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Entoron", "health": 80, "typ": "Wasser", "typ2": None, "evolution_stage": 2},

        {"name": "Menki", "health": 40, "typ": "Kampf", "typ2": None, "evolution_stage": 1},
        {"name": "Rasaff", "health": 65, "typ": "Kampf", "typ2": None, "evolution_stage": 2},

        {"name": "Fukano", "health": 55, "typ": "Feuer", "typ2": None, "evolution_stage": 1},
        {"name": "Arkani", "health": 90, "typ": "Feuer", "typ2": None, "evolution_stage": 2},

        {"name": "Quapsel", "health": 40, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Quaputzi", "health": 65, "typ": "Wasser", "typ2": None, "evolution_stage": 2},
        {"name": "Quappo", "health": 90, "typ": "Wasser", "typ2": "Kampf", "evolution_stage": 3},

        {"name": "Abra", "health": 25, "typ": "Psycho", "typ2": None, "evolution_stage": 1},
        {"name": "Kadabra", "health": 40, "typ": "Psycho", "typ2": None, "evolution_stage": 2},
        {"name": "Simsala", "health": 55, "typ": "Psycho", "typ2": None, "evolution_stage": 3},

        {"name": "Machollo", "health": 70, "typ": "Kampf", "typ2": None, "evolution_stage": 1},
        {"name": "Maschock", "health": 80, "typ": "Kampf", "typ2": None, "evolution_stage": 2},
        {"name": "Machomei", "health": 90, "typ": "Kampf", "typ2": None, "evolution_stage": 3},

        {"name": "Knofensa", "health": 50, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Ultrigaria", "health": 65, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 2},
        {"name": "Sarzenia", "health": 80, "typ": "Pflanze", "typ2": "Gift", "evolution_stage": 3},

        {"name": "Tentacha", "health": 40, "typ": "Wasser", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Tentoxa", "health": 80, "typ": "Wasser", "typ2": "Gift", "evolution_stage": 2},

        {"name": "Kleinstein", "health": 40, "typ": "Gestein", "typ2": "Boden", "evolution_stage": 1},
        {"name": "Georok", "health": 55, "typ": "Gestein", "typ2": "Boden", "evolution_stage": 2},
        {"name": "Geowaz", "health": 80, "typ": "Gestein", "typ2": "Boden", "evolution_stage": 3},

        {"name": "Ponita", "health": 50, "typ": "Feuer", "typ2": None, "evolution_stage": 1},
        {"name": "Gallopa", "health": 65, "typ": "Feuer", "typ2": None, "evolution_stage": 2},

        {"name": "Flegmon", "health": 90, "typ": "Wasser", "typ2": "Psycho", "evolution_stage": 1},
        {"name": "Lahmus", "health": 95, "typ": "Wasser", "typ2": "Psycho", "evolution_stage": 2},

        {"name": "Magnetilo", "health": 25, "typ": "Elektro", "typ2": "Stahl", "evolution_stage": 1},
        {"name": "Magneton", "health": 50, "typ": "Elektro", "typ2": "Stahl", "evolution_stage": 2},

        {"name": "Porenta", "health": 52, "typ": "Normal", "typ2": "Flug", "evolution_stage": 1},

        {"name": "Dodu", "health": 35, "typ": "Normal", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Dodri", "health": 60, "typ": "Normal", "typ2": "Flug", "evolution_stage": 2},

        {"name": "Jurob", "health": 65, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Jugong", "health": 90, "typ": "Wasser", "typ2": "Eis", "evolution_stage": 2},

        {"name": "Sleima", "health": 80, "typ": "Gift", "typ2": None, "evolution_stage": 1},
        {"name": "Sleimok", "health": 105, "typ": "Gift", "typ2": None, "evolution_stage": 2},

        {"name": "Muschas", "health": 30, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Austos", "health": 50, "typ": "Wasser", "typ2": "Eis", "evolution_stage": 2},

        {"name": "Nebulak", "health": 30, "typ": "Geist", "typ2": "Gift", "evolution_stage": 1},
        {"name": "Alpollo", "health": 45, "typ": "Geist", "typ2": "Gift", "evolution_stage": 2},
        {"name": "Gengar", "health": 60, "typ": "Geist", "typ2": "Gift", "evolution_stage": 3},

        {"name": "Onix", "health": 35, "typ": "Gestein", "typ2": "Boden", "evolution_stage": 1},

        {"name": "Traumato", "health": 60, "typ": "Psycho", "typ2": None, "evolution_stage": 1},
        {"name": "Hypno", "health": 85, "typ": "Psycho", "typ2": None, "evolution_stage": 2},

        {"name": "Krabby", "health": 30, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Kingler", "health": 55, "typ": "Wasser", "typ2": None, "evolution_stage": 2},

        {"name": "Voltobal", "health": 40, "typ": "Elektro", "typ2": None, "evolution_stage": 1},
        {"name": "Lektrobal", "health": 60, "typ": "Elektro", "typ2": None, "evolution_stage": 2},

        {"name": "Owei", "health": 60, "typ": "Pflanze", "typ2": "Psycho", "evolution_stage": 1},
        {"name": "Kokowei", "health": 95, "typ": "Pflanze", "typ2": "Psycho", "evolution_stage": 2},

        {"name": "Tragosso", "health": 50, "typ": "Boden", "typ2": None, "evolution_stage": 1},
        {"name": "Knogga", "health": 60, "typ": "Boden", "typ2": None, "evolution_stage": 2},

        {"name": "Kicklee", "health": 50, "typ": "Kampf", "typ2": None, "evolution_stage": 1},
        {"name": "Nockchan", "health": 50, "typ": "Kampf", "typ2": None, "evolution_stage": 1},

        {"name": "Schlurp", "health": 90, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Smogon", "health": 40, "typ": "Gift", "typ2": None, "evolution_stage": 1},
        {"name": "Smogmog", "health": 65, "typ": "Gift", "typ2": None, "evolution_stage": 2},

        {"name": "Rihorn", "health": 80, "typ": "Boden", "typ2": "Gestein", "evolution_stage": 1},
        {"name": "Rizeros", "health": 105, "typ": "Boden", "typ2": "Gestein", "evolution_stage": 2},

        {"name": "Chaneira", "health": 250, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Tangela", "health": 65, "typ": "Pflanze", "typ2": None, "evolution_stage": 1},

        {"name": "Kangama", "health": 105, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Seeper", "health": 30, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Seemon", "health": 55, "typ": "Wasser", "typ2": None, "evolution_stage": 2},

        {"name": "Goldini", "health": 45, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Golking", "health": 80, "typ": "Wasser", "typ2": None, "evolution_stage": 2},

        {"name": "Sterndu", "health": 30, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Starmie", "health": 60, "typ": "Wasser", "typ2": "Psycho", "evolution_stage": 2},

        {"name": "Pantimos", "health": 40, "typ": "Psycho", "typ2": "Fee", "evolution_stage": 1},

        {"name": "Sichlor", "health": 70, "typ": "Käfer", "typ2": "Flug", "evolution_stage": 1},

        {"name": "Rossana", "health": 65, "typ": "Eis", "typ2": "Psycho", "evolution_stage": 1},

        {"name": "Elektek", "health": 65, "typ": "Elektro", "typ2": None, "evolution_stage": 1},

        {"name": "Magmar", "health": 65, "typ": "Feuer", "typ2": None, "evolution_stage": 1},

        {"name": "Pinsir", "health": 65, "typ": "Käfer", "typ2": None, "evolution_stage": 1},

        {"name": "Tauros", "health": 75, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Karpador", "health": 20, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Garados", "health": 95, "typ": "Wasser", "typ2": "Flug", "evolution_stage": 2},

        {"name": "Lapras", "health": 130, "typ": "Wasser", "typ2": "Eis", "evolution_stage": 1},

        {"name": "Ditto", "health": 48, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Evoli", "health": 55, "typ": "Normal", "typ2": None, "evolution_stage": 1},
        {"name": "Aquana", "health": 130, "typ": "Wasser", "typ2": None, "evolution_stage": 2},
        {"name": "Blitza", "health": 65, "typ": "Elektro", "typ2": None, "evolution_stage": 2},
        {"name": "Flamara", "health": 65, "typ": "Feuer", "typ2": None, "evolution_stage": 2},

        {"name": "Porygon", "health": 65, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Amonitas", "health": 35, "typ": "Gestein", "typ2": "Wasser", "evolution_stage": 1},
        {"name": "Amoroso", "health": 70, "typ": "Gestein", "typ2": "Wasser", "evolution_stage": 2},

        {"name": "Kabuto", "health": 30, "typ": "Gestein", "typ2": "Wasser", "evolution_stage": 1},
        {"name": "Kabutops", "health": 60, "typ": "Gestein", "typ2": "Wasser", "evolution_stage": 2},

        {"name": "Aerodactyl", "health": 80, "typ": "Gestein", "typ2": "Flug", "evolution_stage": 1},

        {"name": "Relaxo", "health": 160, "typ": "Normal", "typ2": None, "evolution_stage": 1},

        {"name": "Dratini", "health": 41, "typ": "Drache", "typ2": None, "evolution_stage": 1},
        {"name": "Dragonir", "health": 61, "typ": "Drache", "typ2": None, "evolution_stage": 2},
        {"name": "Dragoran", "health": 91, "typ": "Drache", "typ2": "Flug", "evolution_stage": 3},

    ]

    new_pokemon = random.choice(pokemon_team)

    while new_pokemon["evolution_stage"] != 1:
        new_pokemon = random.choice(pokemon_team)

    box.append(new_pokemon)

    print(f"\nDu hast {new_pokemon['name']} gefangen!")

def legendary_pokemon():
    
    pokemon_team = [
        {"name": "Mewtu", "health": 106, "typ": "Psycho", "typ2": None, "evolution_stage": 1},
        {"name": "Mew", "health": 100, "typ": "Psycho", "typ2": None, "evolution_stage": 1},
        {"name": "Meltan", "health": 46, "typ": "Stahl", "typ2": None, "evolution_stage": 1},
        {"name": "Melmetal", "health": 135, "typ": "Stahl", "typ2": None, "evolution_stage": 2},
        {"name": "Arktos", "health": 90, "typ": "Eis", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Zapdos", "health": 90, "typ": "Elektro", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Lavados", "health": 90, "typ": "Feuer", "typ2": "Flug", "evolution_stage": 1}
        
    ]

def find_item():
    items = [
        ("Normale Potion", 20),
        ("Super Potion", 50),
        ("Hyper Potion", 120)
    ]

    item = random.choice(items)

    bag.append(item)

    print(f"\nDu hast {item[0]} gefunden!")
    print(f"Heilung: {item[1]} KP")

def heal_pokemon():
    if len(bag) == 0:
        print("\nDeine Medizintasche ist leer!")
        return

    print("\nDeine Medizintasche:")

    for i, item in enumerate(bag, start=1):
        print(f"{i}. {item[0]} (+{item[1]} KP)")

    item_choice = int(input("\nWelches Item benutzen? "))
    item = bag[item_choice - 1]

    print("\nDeine Pokémon:")

    for i, pokemon in enumerate(box, start=1):
        print(f"{i}. {pokemon['name']} - KP: {pokemon['health']}")

    pokemon_choice = int(input("\nWelches Pokémon heilen? "))
    pokemon = box[pokemon_choice - 1]

    pokemon["health"] += item[1]

    print(f"\n{pokemon['name']} wurde um {item[1]} KP geheilt!")
    print(f"Neue KP: {pokemon['health']}")

    bag.remove(item)

def random_events(friend_name):

    if friend_name == "Misty":
        events = ["item", "item", "pokemon", "self"]

    elif friend_name == "Ash":
        events = ["pokemon", "pokemon", "item", "self"]

    else:  # Rocko
        events = ["item", "pokemon", "self", "self"]

    event = random.choice(events)

    if event == "pokemon":
        if len(box) == 6:
            print("\nDeine Box ist voll! Du kannst kein neues Pokémon fangen.")
            find_item()
        else:
            find_pokemon()

    elif event == "item":
        find_item()

    else:
        next_step()

def next_step():
    actions_list = [
        {"name": "Pokeom heilen"},
        {"name": "Pokemon fangen"},
        {"name": "weiter gehen"}
    ]

    print("Was ist deine nächste aktion?")

    for i, action in enumerate(actions_list, start=1):
        print(f"{i}. {action['name']}")

    while True:
        try:
            choice = int(input("\nDeine Wahl (1-3): "))

            if choice < 1 or choice > 3:
                print("Bitte gib nur eine Zahl zwischen 1 und 3 ein. Neuer Versuch.")
            else:
                break 

        except ValueError:
            print("Bitte gib nur Zahlen ein. Neuer Versuch.")

    actions = actions_list[choice - 1]

    if actions["name"] == "Pokeom heilen":
        heal_pokemon()
    elif actions["name"] == "Pokemon fangen":
        if len(box) == 6:
            print("\nDein Box ist voll! Du kannst kein neues Pokémon fangen.")
            next_step()
        find_pokemon()
    else:
        arena()

def friend(x):
    if x >= 5:
        return "Rocko" # Fördert Eigenentscheidung
    elif x <= 0:
        return "Ash" # Fördert Pokemons fangen
    else:
        return "Misty" # Fördert Items finden

arena_leiter = {
    "Rocko": [
        {"name": "Kleinstein", "health": 40, "typ": "Gestein"},
        {"name": "Onix", "health": 35, "typ": "Gestein"}
    ],

    "Misty": [
        {"name": "Sterndu", "health": 30, "typ": "Wasser"},
        {"name": "Starmie", "health": 60, "typ": "Wasser"}
    ],

    "Major Bob": [
        {"name": "Voltobal", "health": 40, "typ": "Elektro"},
        {"name": "Raichu", "health": 60, "typ": "Elektro"},
        {"name": "Pikachu", "health": 35, "typ": "Elektro"}
    ],

    "Erika": [
        {"name": "Sarazenia", "health": 45, "typ": "Pflanze"},
        {"name": "Tangela", "health": 65, "typ": "Pflanze"},
        {"name": "Giflor", "health": 75, "typ": "Pflanze"}
    ],

    "Koga": [
        {"name": "Smogon", "health": 40, "typ": "Gift"},
        {"name": "Sleimok", "health": 105, "typ": "Gift"},
        {"name": "Smogon", "health": 40, "typ": "Gift"},
        {"name": "Smogmog", "health": 65, "typ": "Gift"}
    ],

    "Sabrina": [
        {"name": "Kadabra", "health": 40, "typ": "Psycho"},
        {"name": "Pantimos", "health": 40, "typ": "Psycho"},
        {"name": "Omot", "health": 70, "typ": "Käfer", "typ2": "Gift"},
        {"name": "Simsala", "health": 55, "typ": "Psycho"}
    ],

    "Pyro": [
        {"name": "Fukano", "health": 55, "typ": "Feuer"},
        {"name": "Ponita", "health": 50, "typ": "Feuer"},
        {"name": "Gallopa", "health": 65, "typ": "Feuer"},
        {"name": "Arkani", "health": 90, "typ": "Feuer"},
    ],

    "Giovanni": [
        {"name": "Onix", "health": 35, "typ": "Gestein"},
        {"name": "Rihorn", "health": 80, "typ": "Boden"},
        {"name": "Kangama", "health": 105, "typ": "Normal"}
    ]
}

top4_leiter = {
    "Lorelei": [
        {"name": "Jugong", "health": 90, "typ": "Wasser", "typ2": "Eis"},
        {"name": "Austos", "health": 50, "typ": "Wasser", "typ2": "Eis"},
        {"name": "Lahmus", "health": 95, "typ": "Wasser", "typ2": "Psycho"},
        {"name": "Rossana", "health": 65, "typ": "Eis", "typ2": "Psycho"},
        {"name": "Lapras", "health": 130, "typ": "Wasser", "typ2": "Eis"}
    ],
    "Bruno": [
        {"name": "Onix", "health": 35, "typ": "Gestein"},
        {"name": "Nockchan", "health": 50, "typ": "Kampf"},
        {"name": "Kicklee", "health": 50, "typ": "Kampf"},
        {"name": "Onix", "health": 35, "typ": "Gestein"},
        {"name": "Machomei", "health": 90, "typ": "Kampf"}
    ],
    "Agathe": [
        {"name": "Gengar", "health": 60, "typ": "Geist", "typ2": "Gift"},
        {"name": "Golbat", "health": 75, "typ": "Gift", "typ2": "Flug"},
        {"name": "Alpollo", "health": 45, "typ": "Geist", "typ2": "Gift"},
        {"name": "Arbok", "health": 60, "typ": "Gift"},
        {"name": "Gengar", "health": 60, "typ": "Geist", "typ2": "Gift"}
    ],
    "Siegfried": [
        {"name": "Garados", "health": 95, "typ": "Wasser", "typ2": "Flug"},
        {"name": "Dragonir", "health": 61, "typ": "Drache"},
        {"name": "Dragonir", "health": 61, "typ": "Drache"},
        {"name": "Aerodactyl", "health": 80, "typ": "Gestein", "typ2": "Flug"},
        {"name": "Dragoran", "health": 91, "typ": "Drache", "typ2": "Flug"}
    ],
    f"player['rival']": [
        {"name": "Tauboss", "health": 83, "typ": "Normal", "typ2": "Flug"},
        {"name": "Simsala", "health": 55, "typ": "Psycho"},
        {"name": "Rizeros", "health": 105, "typ": "Boden", "typ2": "Gestein"},
        {"name": "Kokowei", "health": 95, "typ": "Pflanze", "typ2": "Psycho"},
        {"name": "Garados", "health": 95, "typ": "Wasser", "typ2": "Flug"},
        {"name": "Glurak", "health": 78, "typ": "Feuer", "typ2": "Flug"}
    ]
}

def top4():
    print("Du betrittst die Top 4...")
    if player["top4_badges"] == 0:
        top4_name = "Lorelei"
    elif player["top4_badges"] == 1:
        top4_name = "Bruno"
    elif player["top4_badges"] == 2:
        top4_name = "Agathe"
    elif player["top4_badges"] == 3:
        top4_name = "Siegfried"
    elif player["top4_badges"] == 4:
        top4_name = player["rival"]
    else:
        print("Du hast alle Top 4 Orden erreicht. Herzlichen Glückwunsch")

        
    gegner_team = top4_leiter[top4_name]

    for enemy_pokemon in gegner_team:

        print(f"\n{top4_name} setzt {enemy_pokemon['name']} ein!")

        if len(box) == 0:
            print("Du hast keine Pokémon!")
            print("GAME OVER")
            abschluss(trainer_name)

        player_pokemon = box[0]

        gewonnen = battle(player_pokemon, enemy_pokemon)

        if not gewonnen:
            print("\nDu hast die Arena verloren!")
            print("GAME OVER")
            abschluss(trainer_name)

        else:
            print(f"\nDu hast {top4_name} besiegt!")
            print("Du erhältst einen Top 4 Orden!")

    player["top4_badges"] += 1

def arena():
    print("\nDu betrittst die Arena...")

    if player["arena_badges"] == 0:
        arena_name = "Rocko"
    elif player["arena_badges"] == 1:
        arena_name = "Misty"
    elif player["arena_badges"] == 2:
        arena_name = "Major Bob"
    elif player["arena_badges"] == 3:
        arena_name = "Erika"
    elif player["arena_badges"] == 4:
        arena_name = "Koga"
    elif player["arena_badges"] == 5:
        arena_name = "Sabrina"
    elif player["arena_badges"] == 6:
        arena_name = "Pyro"
    elif player["arena_badges"] == 7:
        arena_name = "Giovanni"
    else:
        print("Du hast alle Arena Orden erreicht. Herzlichen Glückwunsch")

    print(f"{arena_name} fordert dich heraus!")

    gegner_team = arena_leiter[arena_name]

    for enemy_pokemon in gegner_team:

        print(f"\n{arena_name} setzt {enemy_pokemon['name']} ein!")

        if len(box) == 0:
            print("Du hast keine Pokémon!")
            print("GAME OVER")
            abschluss(trainer_name)

        player_pokemon = box[0]

        gewonnen = battle(player_pokemon, enemy_pokemon)

        if not gewonnen:
            print("\nDu hast die Arena verloren!")
            print("GAME OVER")
            abschluss(trainer_name)

        else:
            print(f"\nDu hast {arena_name} besiegt!")
            print("Du erhältst einen Arenaorden!")

    player["arena_badges"] += 1

def abschluss(trainer_name):
    print("\n===== SPIELZUSAMMENFASSUNG =====")
    
    
    for key, value in player.items():
        print(f"{key}: {value}")
    
    print(f"Danke {trainer_name} fürs Spielen!")
    print(f"Du hast {len(box)} Pokémon gefangen und {len(bag)} Items gesammelt.")
    print(f"Dein Geld: {player['geld']}")
    print(f"Du hast {player['arena_badges']} Arena Orden erreicht.")
    print(f"Dein Rivale war {player['rival']} und dein Trainer war {player['trainer']}.")

# Test
# Game logik
trainer_name = startup()
top4()

#a