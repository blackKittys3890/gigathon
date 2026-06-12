import random

bag = []
player = {}
box = []
player["schritte"] = 0
MIN_X, MAX_X = -100, 100
MIN_Y, MAX_Y = -100, 100


def startup():
    global x, y
    player["arena_badges"] = 0
    player["top4_badges"] = 0
    player["schritt"] = 0

    print("Willkommen zu Pokémon!")
    print("Du bist ein Trainer und dein Ziel ist es, der beste Pokémon-Trainer zu werden.")
    print("Fange Pokémon, sammle Items und heile deine Pokémon, um stärker zu werden.")
    print("Wenn du eine Arena nicht schaffst, hast du verloren.")

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

    print("Auf welcher Schwierigkeit möchtest du spielen? (1 (leicht) - 3 (schwer))")
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
    player["x"] = x
    player["y"] = y
    player["trainer"] = friend(x)
    player["difficulty"] = difficulty
    player["starter"] = starter["name"]
    player["rival"] = rival_name

    print("\n=== Expeditionsstart ===")
    print(f"Name der Expedition: {trainer_name}")
    print(f"Startposition: ({x}, {y})")
    print(f"Anfangsressource (Geld): {money}")
    print(f"Grenzen der Welt: x = {MIN_X} bis {MAX_X}, y = {MIN_Y} bis {MAX_Y}")
    print("Endbedingung: Das Spiel endet, wenn du alle Orden sammelst oder eine Arena verlierst.")

    print("Viel Spaß auf deiner Reise!\n")
    return trainer_name

def reisen():
    global MIN_X, MAX_X, MIN_Y, MAX_Y

    player["schritt"] += 1
    print(f"\n--- Schritt {player['schritt']}: Bewegung ---")

    print(f"Alte Position: ({player['x']}, {player['y']})")
    print(f"Geld: {player['geld']}")

    richtung = input("In welche Richtung möchtest du gehen? (N, S, O, W): ").lower()
    while richtung not in ["n", "s", "o", "w"]:
        print("Ungültige Richtung! Bitte wähle N, S, O oder W.")
        richtung = input("In welche Richtung möchtest du gehen? (N, S, O, W): ").lower()

    while True:
        try:
            schritte = int(input("Wie viele Schritte möchtest du gehen? "))
            if schritte <= 0:
                print("Bitte gib eine positive Zahl ein.")
                continue
            break
        except ValueError:
            print("Bitte gib nur Zahlen ein.")

    print(f"Aktion: {schritte} Schritte nach {richtung.upper()}")

    new_x, new_y = player["x"], player["y"]
    if richtung == "n":
        new_y += schritte
    elif richtung == "s":
        new_y -= schritte
    elif richtung == "o":
        new_x += schritte
    elif richtung == "w":
        new_x -= schritte

    if new_x < MIN_X:
        new_x = MIN_X
        print(f"Grenzüberschreitung: Du kannst nicht weiter nach Westen gehen! (Grenze: x = {MIN_X})")
    elif new_x > MAX_X:
        new_x = MAX_X
        print(f"Grenzüberschreitung: Du kannst nicht weiter nach Osten gehen! (Grenze: x = {MAX_X})")

    if new_y < MIN_Y:
        new_y = MIN_Y
        print(f"Grenzüberschreitung: Du kannst nicht weiter nach Süden gehen! (Grenze: y = {MIN_Y})")
    elif new_y > MAX_Y:
        new_y = MAX_Y
        print(f"Grenzüberschreitung: Du kannst nicht weiter nach Norden gehen! (Grenze: y = {MAX_Y})")

    player["x"], player["y"] = new_x, new_y
    print(f"Neue Position: ({player['x']}, {player['y']})")

    print("\nZustand der Pokémon:")
    for pokemon in box:
        print(f"{pokemon['name']}: {pokemon['health']} KP")

    random_events(player["trainer"])

def battle(player_pokemon, enemy_pokemon):
    print(f"\n--- Schritt {player['schritt']}: Kampf gegen {enemy_pokemon['name']} ---")
    print(f"Vor dem Kampf:")
    print(f"{player_pokemon['name']}: {player_pokemon['health']} KP")
    print(f"{enemy_pokemon['name']}: {enemy_pokemon['health']} KP")

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
            print(f"\n{player_pokemon['name']} macht {damage} Schaden!")

            if enemy_pokemon["health"] <= 0:
                print(f"{enemy_pokemon['name']} wurde besiegt!")
                player["schritt"] += 1
                return True

        elif choice == "2":
            if len(bag) == 0:
                print("\nDu hast keine Heilitems!")
            else:
                heal_pokemon()
                player["schritt"] += 1

        elif choice == "3":
            chance = random.randint(1, 100)
            if chance <= 50:
                print("\nDu bist erfolgreich geflohen!")
                player["schritt"] += 1
                return False
            else:
                print("\nFlucht fehlgeschlagen!")

        else:
            print("\nUngültige Eingabe!")
            continue

        enemy_damage = random.randint(5, 12)
        player_pokemon["health"] -= enemy_damage
        print(f"\n{enemy_pokemon['name']} macht {enemy_damage} Schaden!")

        if player_pokemon["health"] <= 0:
            print(f"\n{player_pokemon['name']} wurde besiegt!")
            player["schritt"] += 1
            return False

def starter_pokemon():
    starters = [
        {"name": "Bisasam", "health": 45, "typ": "Pflanze", "typ2": "Gift"},
        {"name": "Glumanda", "health": 39, "typ": "Feuer"},
        {"name": "Schiggy", "health": 44, "typ": "Wasser"},
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
        {"name": "Glumanda", "health": 39, "typ": "Feuer", "typ2": None, "evolution_stage": 1},
        {"name": "Schiggy", "health": 44, "typ": "Wasser", "typ2": None, "evolution_stage": 1},
        {"name": "Raupy", "health": 45, "typ": "Käfer", "typ2": None, "evolution_stage": 1},
        {"name": "Pikachu", "health": 35, "typ": "Elektro", "typ2": None, "evolution_stage": 1},
    ]

    new_pokemon = random.choice(pokemon_team)
    while new_pokemon["evolution_stage"] != 1:
        new_pokemon = random.choice(pokemon_team)

    box.append(new_pokemon)
    print(f"\nDu hast {new_pokemon['name']} gefangen!")

def legendary_pokemon():

    pokemon_team = [
        {
            "name": "Mewtu",
            "health": 106,
            "typ": "Psycho",
            "typ2": None,
            "evolution_stage": 1,
        },
        {
            "name": "Mew",
            "health": 100,
            "typ": "Psycho",
            "typ2": None,
            "evolution_stage": 1,
        },
        {
            "name": "Meltan",
            "health": 46,
            "typ": "Stahl",
            "typ2": None,
            "evolution_stage": 1,
        },
        {
            "name": "Melmetal",
            "health": 135,
            "typ": "Stahl",
            "typ2": None,
            "evolution_stage": 2,
        },
        {
            "name": "Arktos",
            "health": 90,
            "typ": "Eis",
            "typ2": "Flug",
            "evolution_stage": 1,
        },
        {
            "name": "Zapdos",
            "health": 90,
            "typ": "Elektro",
            "typ2": "Flug",
            "evolution_stage": 1,
        },
        {
            "name": "Lavados",
            "health": 90,
            "typ": "Feuer",
            "typ2": "Flug",
            "evolution_stage": 1,
        },
    ]

def find_item():
    items = [("Normale Potion", 20), ("Super Potion", 50), ("Hyper Potion", 120)]

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
        events = ["item", "item", "pokemon", "dangerous_field"]
    elif friend_name == "Ash":
        events = ["pokemon", "pokemon", "item", "dangerous_field"]
    else:  # Rocko
        events = ["item", "pokemon", "dangerous_field", "dangerous_field"]

    event = random.choice(events)

    if event == "pokemon":
        if len(box) == 6:
            print("\nDeine Box ist voll! Du kannst kein neues Pokémon fangen.")
            find_item()
        else:
            find_pokemon()

    elif event == "item":
        find_item()

    elif event == "dangerous_field":
        print(f"\n--- Schritt {player['schritt']}: Gefährliches Feld ---")
        print("Du betrittst ein gefährliches Feld! Alle Pokémon verlieren 10 KP.")
        for pokemon in box:
            pokemon["health"] -= 10
            if pokemon["health"] < 0:
                pokemon["health"] = 0
            print(f"{pokemon['name']}: {pokemon['health']} KP (Erklärung: -10 KP durch gefährliches Feld)")
        player["schritt"] += 1

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
        {"name": "weiter gehen"},
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
        return "Rocko"  # Fördert Eigenentscheidung
    elif x <= 0:
        return "Ash"  # Fördert Pokemons fangen
    else:
        return "Misty"  # Fördert Items finden

arena_leiter = {
    "Rocko": [
        {"name": "Kleinstein", "health": 40, "typ": "Gestein"},
        {"name": "Onix", "health": 35, "typ": "Gestein"},
    ],
    "Misty": [
        {"name": "Sterndu", "health": 30, "typ": "Wasser"},
        {"name": "Starmie", "health": 60, "typ": "Wasser"},
    ],
    "Major Bob": [
        {"name": "Voltobal", "health": 40, "typ": "Elektro"},
        {"name": "Raichu", "health": 60, "typ": "Elektro"},
        {"name": "Pikachu", "health": 35, "typ": "Elektro"},
    ],
    "Erika": [
        {"name": "Sarazenia", "health": 45, "typ": "Pflanze"},
        {"name": "Tangela", "health": 65, "typ": "Pflanze"},
        {"name": "Giflor", "health": 75, "typ": "Pflanze"},
    ],
    "Koga": [
        {"name": "Smogon", "health": 40, "typ": "Gift"},
        {"name": "Sleimok", "health": 105, "typ": "Gift"},
        {"name": "Smogon", "health": 40, "typ": "Gift"},
        {"name": "Smogmog", "health": 65, "typ": "Gift"},
    ],
    "Sabrina": [
        {"name": "Kadabra", "health": 40, "typ": "Psycho"},
        {"name": "Pantimos", "health": 40, "typ": "Psycho"},
        {"name": "Omot", "health": 70, "typ": "Käfer", "typ2": "Gift"},
        {"name": "Simsala", "health": 55, "typ": "Psycho"},
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
        {"name": "Kangama", "health": 105, "typ": "Normal"},
    ],
}

top4_leiter = {
    "Lorelei": [
        {"name": "Jugong", "health": 90, "typ": "Wasser", "typ2": "Eis"},
        {"name": "Austos", "health": 50, "typ": "Wasser", "typ2": "Eis"},
        {"name": "Lahmus", "health": 95, "typ": "Wasser", "typ2": "Psycho"},
        {"name": "Rossana", "health": 65, "typ": "Eis", "typ2": "Psycho"},
        {"name": "Lapras", "health": 130, "typ": "Wasser", "typ2": "Eis"},
    ],
    "Bruno": [
        {"name": "Onix", "health": 35, "typ": "Gestein"},
        {"name": "Nockchan", "health": 50, "typ": "Kampf"},
        {"name": "Kicklee", "health": 50, "typ": "Kampf"},
        {"name": "Onix", "health": 35, "typ": "Gestein"},
        {"name": "Machomei", "health": 90, "typ": "Kampf"},
    ],
    "Agathe": [
        {"name": "Gengar", "health": 60, "typ": "Geist", "typ2": "Gift"},
        {"name": "Golbat", "health": 75, "typ": "Gift", "typ2": "Flug"},
        {"name": "Alpollo", "health": 45, "typ": "Geist", "typ2": "Gift"},
        {"name": "Arbok", "health": 60, "typ": "Gift"},
        {"name": "Gengar", "health": 60, "typ": "Geist", "typ2": "Gift"},
    ],
    "Siegfried": [
        {"name": "Garados", "health": 95, "typ": "Wasser", "typ2": "Flug"},
        {"name": "Dragonir", "health": 61, "typ": "Drache"},
        {"name": "Dragonir", "health": 61, "typ": "Drache"},
        {"name": "Aerodactyl", "health": 80, "typ": "Gestein", "typ2": "Flug"},
        {"name": "Dragoran", "health": 91, "typ": "Drache", "typ2": "Flug"},
    ],
    "rival_placeholder": [
        {"name": "Tauboss", "health": 83, "typ": "Normal", "typ2": "Flug"},
        {"name": "Simsala", "health": 55, "typ": "Psycho"},
        {"name": "Rizeros", "health": 105, "typ": "Boden", "typ2": "Gestein"},
        {"name": "Kokowei", "health": 95, "typ": "Pflanze", "typ2": "Psycho"},
        {"name": "Garados", "health": 95, "typ": "Wasser", "typ2": "Flug"},
        {"name": "Glurak", "health": 78, "typ": "Feuer", "typ2": "Flug"},
    ],
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

    if top4_name == player["rival"]:
        gegner_team = top4_leiter["rival_placeholder"]
    else:
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
            player["game_over"] = True  # <-- neu
            return

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
            player["game_over"] = True  # <-- neu
            return

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
    print(
        f"Dein Rivale war {player['rival']} und dein Trainer war {player['trainer']}."
    )

if __name__ == "__main__":
    while True:
        bag.clear()
        box.clear()
        player.clear()
        player["schritte"] = 0

        trainer_name = startup()

        game_over = False  # <-- neu

        while player["arena_badges"] < 8 and not game_over:
            reisen()
            if player.get("game_over"):  # <-- prüfen
                game_over = True

        if not game_over:
            top4()

        print("\nMöchtest du nochmal spielen? (j/n)")
        again = input("Auswahl: ").strip().lower()
        if again != "j":
            print("Danke fürs Spielen! Auf Wiedersehen!")
            break
