import random

bag = []
player = {}
box = []
MIN_X, MAX_X = -100, 100
MIN_Y, MAX_Y = -100, 100


def startup():
    global x, y
    player["arena_badges"] = 0
    player["top4_badges"] = 0
    player["schritt"] = 0
    player["game_over"] = False
    player["ereignisse"] = []

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
    print("Endbedingung: Das Spiel endet, wenn du alle Orden sammelst, eine Arena verlierst oder dir das Geld ausgeht.")

    print("Viel Spaß auf deiner Reise!\n")
    return trainer_name


def reisen():
    player["schritt"] += 1
    print(f"\n--- Schritt {player['schritt']}: Bewegung ---")

    print(f"Alte Position: ({player['x']}, {player['y']})")
    print(f"Geld vorher: {player['geld']}")
    
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
        print(f"  {pokemon['name']}: {pokemon['health']} KP")

    random_events(player["trainer"])
    print(f"Geld nach Schritt: {player['geld']}")


def battle(player_pokemon, enemy_pokemon):
    difficulty = player.get("difficulty", 2)
    if difficulty == 1:
        schaden_faktor = 0.75
    elif difficulty == 3:
        schaden_faktor = 1.5
    else:
        schaden_faktor = 1.0
    
    print(f"\n--- Kampf gegen {enemy_pokemon['name']} ---")
    print(f"Vor dem Kampf:")
    print(f"  {player_pokemon['name']}: {player_pokemon['health']} KP")
    print(f"  {enemy_pokemon['name']}: {enemy_pokemon['health']} KP")

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

        enemy_damage = int(random.randint(5, 12) * schaden_faktor)
        player_pokemon["health"] -= enemy_damage
        print(f"\n{enemy_pokemon['name']} macht {enemy_damage} Schaden!")

        if player_pokemon["health"] <= 0:
            print(f"\n{player_pokemon['name']} wurde besiegt!")
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
    box.append(new_pokemon)
    print(f"\nDu hast {new_pokemon['name']} gefangen! (+{new_pokemon['health']} KP)")
    player["ereignisse"].append(f"Pokémon {new_pokemon['name']} gefangen")


def legendary_pokemon():
    legendaries = [
        {"name": "Mewtu", "health": 106, "typ": "Psycho", "evolution_stage": 1},
        {"name": "Mew", "health": 100, "typ": "Psycho", "evolution_stage": 1},
        {"name": "Arktos", "health": 90, "typ": "Eis", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Zapdos", "health": 90, "typ": "Elektro", "typ2": "Flug", "evolution_stage": 1},
        {"name": "Lavados", "health": 90, "typ": "Feuer", "typ2": "Flug", "evolution_stage": 1},
    ]
    
    new_pokemon = random.choice(legendaries)
    box.append(new_pokemon)
    print(f"\n⭐ LEGENDÄRES POKÉMON! ⭐")
    print(f"Du hast {new_pokemon['name']} gefangen! (+{new_pokemon['health']} KP)")
    player["ereignisse"].append(f"Legendäres Pokémon {new_pokemon['name']} gefangen")


def find_item():
    items = [("Normale Potion", 20), ("Super Potion", 50), ("Hyper Potion", 120)]
    item = random.choice(items)
    bag.append(item)
    print(f"\nDu hast {item[0]} gefunden! (+{item[1]} KP Heilung)")
    player["ereignisse"].append(f"Item {item[0]} gefunden")


def heal_pokemon():
    if len(bag) == 0:
        print("\nDeine Medizintasche ist leer!")
        return

    print("\nDeine Medizintasche:")
    for i, item in enumerate(bag, start=1):
        print(f"{i}. {item[0]} (+{item[1]} KP)")

    try:
        item_choice = int(input("\nWelches Item benutzen? "))
        item = bag[item_choice - 1]
    except (ValueError, IndexError):
        print("Ungültige Auswahl!")
        return

    print("\nDeine Pokémon:")
    for i, pokemon in enumerate(box, start=1):
        print(f"{i}. {pokemon['name']} - KP: {pokemon['health']}")

    try:
        pokemon_choice = int(input("\nWelches Pokémon heilen? "))
        pokemon = box[pokemon_choice - 1]
    except (ValueError, IndexError):
        print("Ungültige Auswahl!")
        return

    pokemon["health"] += item[1]
    print(f"\n{pokemon['name']} wurde um {item[1]} KP geheilt!")
    print(f"Neue KP: {pokemon['health']}")
    bag.remove(item)


def random_events(friend_name):
    if friend_name == "Misty":
        events = ["item", "item", "pokemon", "dangerous_field", "legendary"]
    elif friend_name == "Ash":
        events = ["pokemon", "pokemon", "item", "dangerous_field", "pokemon"]
    else:
        events = ["item", "pokemon", "dangerous_field", "dangerous_field", "dangerous_field"]

    event = random.choice(events)

    print(f"\n--- Ereignis auf Schritt {player['schritt']} ---")
    
    if event == "pokemon":
        if len(box) >= 6:
            print("\nDeine Box ist voll! Du kannst kein neues Pokémon fangen.")
            find_item()
        else:
            find_pokemon()
            
    elif event == "legendary":
        if len(box) >= 6:
            print("\nDeine Box ist voll! Du kannst kein legendäres Pokémon fangen.")
        else:
            legendary_pokemon()
            
    elif event == "item":
        find_item()
        
    elif event == "dangerous_field":
        print("⚠️ Du betrittst ein gefährliches Feld! Alle Pokémon verlieren 10 KP.")
        print("Erklärung: Gefährliche Felder sind mit Dornen oder Stacheldraht übersät und verletzen deine Pokémon.")
        for pokemon in box:
            pokemon["health"] -= 10
            if pokemon["health"] < 0:
                pokemon["health"] = 0
            print(f"  {pokemon['name']}: {pokemon['health']} KP")
        player["ereignisse"].append("Gefährliches Feld betreten -10 KP für alle Pokémon")


def next_step(trainer_name):
    while True:
        actions_list = [
            {"name": "Pokémon heilen"},
            {"name": "Pokémon fangen"},
            {"name": "weiter gehen (nächste Arena)"},
        ]

        print("\nWas ist deine nächste Aktion?")
        for i, action in enumerate(actions_list, start=1):
            print(f"{i}. {action['name']}")

        try:
            choice = int(input("\nDeine Wahl (1-3): "))
            if choice < 1 or choice > 3:
                print("Bitte gib nur eine Zahl zwischen 1 und 3 ein.")
                continue
        except ValueError:
            print("Bitte gib nur Zahlen ein.")
            continue

        action = actions_list[choice - 1]

        if action["name"] == "Pokémon heilen":
            heal_pokemon()
        elif action["name"] == "Pokémon fangen":
            if len(box) >= 6:
                print("\nDeine Box ist voll! Du kannst kein neues Pokémon fangen.")
            else:
                find_pokemon()
        else:
            arena(trainer_name)
            break


def friend(x):
    if x >= 5:
        return "Rocko"
    elif x <= 0:
        return "Ash"
    else:
        return "Misty"


arena_leiter = {
    "Rocko": [{"name": "Kleinstein", "health": 40}, {"name": "Onix", "health": 35}],
    "Misty": [{"name": "Sterndu", "health": 30}, {"name": "Starmie", "health": 60}],
    "Major Bob": [{"name": "Voltobal", "health": 40}, {"name": "Raichu", "health": 60}, {"name": "Pikachu", "health": 35}],
    "Erika": [{"name": "Sarazenia", "health": 45}, {"name": "Tangela", "health": 65}, {"name": "Giflor", "health": 75}],
    "Koga": [{"name": "Smogon", "health": 40}, {"name": "Sleimok", "health": 105}, {"name": "Smogon", "health": 40}, {"name": "Smogmog", "health": 65}],
    "Sabrina": [{"name": "Kadabra", "health": 40}, {"name": "Pantimos", "health": 40}, {"name": "Omot", "health": 70}, {"name": "Simsala", "health": 55}],
    "Pyro": [{"name": "Fukano", "health": 55}, {"name": "Ponita", "health": 50}, {"name": "Gallopa", "health": 65}, {"name": "Arkani", "health": 90}],
    "Giovanni": [{"name": "Onix", "health": 35}, {"name": "Rihorn", "health": 80}, {"name": "Kangama", "health": 105}],
}

top4_leiter = {
    "Lorelei": [{"name": "Jugong", "health": 90}, {"name": "Austos", "health": 50}, {"name": "Lahmus", "health": 95}, {"name": "Rossana", "health": 65}, {"name": "Lapras", "health": 130}],
    "Bruno": [{"name": "Onix", "health": 35}, {"name": "Nockchan", "health": 50}, {"name": "Kicklee", "health": 50}, {"name": "Onix", "health": 35}, {"name": "Machomei", "health": 90}],
    "Agathe": [{"name": "Gengar", "health": 60}, {"name": "Golbat", "health": 75}, {"name": "Alpollo", "health": 45}, {"name": "Arbok", "health": 60}, {"name": "Gengar", "health": 60}],
    "Siegfried": [{"name": "Garados", "health": 95}, {"name": "Dragonir", "health": 61}, {"name": "Dragonir", "health": 61}, {"name": "Aerodactyl", "health": 80}, {"name": "Dragoran", "health": 91}],
    "rival_placeholder": [{"name": "Tauboss", "health": 83}, {"name": "Simsala", "health": 55}, {"name": "Rizeros", "health": 105}, {"name": "Kokowei", "health": 95}, {"name": "Garados", "health": 95}, {"name": "Glurak", "health": 78}],
}


def top4(trainer_name):
    print("\n🌟 Du betrittst die Top 4 🌟")
    
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
        print("Du hast alle Top 4 besiegt! Herzlichen Glückwunsch zum Titel!")
        return True

    if top4_name == player["rival"]:
        gegner_team = top4_leiter["rival_placeholder"]
        print(f"\nDein Rivale {top4_name} fordert dich heraus!")
    else:
        gegner_team = top4_leiter[top4_name]
        print(f"\nTop 4 - {top4_name} fordert dich heraus!")

    for enemy_pokemon in gegner_team:
        print(f"\n{top4_name} setzt {enemy_pokemon['name']} ein!")

        if len(box) == 0:
            print("Du hast keine Pokémon!")
            print("\n💀 GAME OVER - Du hast verloren! 💀")
            player["game_over"] = True
            return False

        player_pokemon = box[0]
        gewonnen = battle(player_pokemon, enemy_pokemon)

        if not gewonnen:
            print(f"\n💀 GAME OVER - Du hast gegen {top4_name} verloren! 💀")
            player["game_over"] = True
            return False
        else:
            print(f"\n✨ Du hast {enemy_pokemon['name']} besiegt! ✨")

    print(f"\n🏆 Du hast {top4_name} besiegt! 🏆")
    print("Du erhältst einen Top 4 Orden!")
    player["top4_badges"] += 1
    return True


def arena(trainer_name):
    print("\n🏟️ Du betrittst die Arena 🏟️")

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
        print("Du hast alle 8 Arena Orden! Du darfst zu den Top 4!")
        return

    print(f"{arena_name} fordert dich heraus!")

    gegner_team = arena_leiter[arena_name]

    for enemy_pokemon in gegner_team:
        print(f"\n{arena_name} setzt {enemy_pokemon['name']} ein!")

        if len(box) == 0:
            print("Du hast keine Pokémon!")
            print("\n💀 GAME OVER - Du hast verloren! 💀")
            player["game_over"] = True
            return

        player_pokemon = box[0]
        gewonnen = battle(player_pokemon, enemy_pokemon)

        if not gewonnen:
            print(f"\n💀 GAME OVER - Du hast gegen {arena_name} verloren! 💀")
            player["game_over"] = True
            return
        else:
            print(f"\n✨ Du hast {enemy_pokemon['name']} besiegt! ✨")

    print(f"\n🏆 Du hast {arena_name} besiegt! 🏆")
    print("Du erhältst einen Arenaorden!")
    player["arena_badges"] += 1

    if player["arena_badges"] < 8:
        next_step(trainer_name)


def abschluss(trainer_name):
    print("\n" + "=" * 50)
    print("📊 SPIELZUSAMMENFASSUNG 📊")
    print("=" * 50)
    print(f"Trainer: {trainer_name}")
    print(f"Trainer-Typ: {player.get('trainer', '?')}")
    print(f"Rivale: {player.get('rival', '?')}")
    print(f"Starter-Pokémon: {player.get('starter', '?')}")
    print(f"\n📍 Endposition: ({player.get('x', '?')}, {player.get('y', '?')})")
    print(f"💰 Verbleibendes Geld: {player.get('geld', 0)}")
    print(f"🎮 Zurückgelegte Schritte: {player.get('schritt', 0)}")
    print(f"\n🏅 Arenasiege: {player.get('arena_badges', 0)}/8")
    print(f"⭐ Top4-Siege: {player.get('top4_badges', 0)}/5")
    print(f"\n🐾 Pokémon im Team: {len(box)}")
    for pokemon in box:
        print(f"   - {pokemon['name']} ({pokemon['health']} KP)")
    print(f"\n💊 Items gesammelt: {len(bag)}")
    for item in bag:
        print(f"   - {item[0]} (+{item[1]} KP)")
    if player.get("ereignisse"):
        print(f"\n📋 Ereignisse während der Reise:")
        for i, ereignis in enumerate(player["ereignisse"][-10:], 1):
            print(f"   {i}. {ereignis}")
    print("=" * 50)
    
    if player.get("top4_badges", 0) >= 5:
        print("\n👑 HERZLICHEN GLÜCKWUNSCH! Du bist der neue Pokémon-Champion! 👑")
    else:
        print("\n💀 Spiel beendet - Viel Glück beim nächsten Versuch! 💀")
    
    print("=" * 50)


if __name__ == "__main__":
    while True:
        bag.clear()
        box.clear()
        player.clear()

        trainer_name = startup()
        game_over = False

        while player["arena_badges"] < 8 and not game_over:
            reisen()
            
            if player["geld"] <= 0:
                print("\n💰 Dir ist das Geld ausgegangen! Du kannst keine Reise mehr fortsetzen.")
                game_over = True
                player["game_over"] = True
            
            if player.get("game_over"):
                game_over = True

        if not game_over and player["arena_badges"] >= 8:
            print("\n🎉 Glückwunsch! Du hast alle 8 Arena-Orden gesammelt! 🎉")
            print("Du darfst nun gegen die Top 4 antreten!\n")
            
            while player["top4_badges"] < 5 and not player.get("game_over", False):
                top4(trainer_name)   # ← HIER wurde trainer_name hinzugefügt!

        if player.get("game_over", False) or player["top4_badges"] >= 5:
            abschluss(trainer_name)

        print("\n🔄 Möchtest du nochmal spielen? (j/n)")
        again = input("Auswahl: ").strip().lower()
        if again != "j":
            print("Danke fürs Spielen! Auf Wiedersehen!")
            break