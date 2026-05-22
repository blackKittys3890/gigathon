import random

bag = []
box = []

def starter_pokemon():
    starters = [
        {"name": "Bisasam", "health": 45, "typ": "Pflanze", "typ2": "Gift"},
        {"name": "Glumanda", "health": 39, "typ": "Feuer"},
        {"name": "Schiggy", "health": 44, "typ": "Wasser"}
    ]

    print("Wähle dein Starter-Pokémon:")

    for i, pokemon in enumerate(starters, start=1):
        print(f"{i}. {pokemon['name']} - KP: {pokemon['health']}")

    choice = int(input("\nDeine Wahl: "))
    starter = starters[choice - 1]

    box.append(starter)

    print(f"\nDu hast {starter['name']} als dein Starter-Pokémon gewählt!")

def find_pokemon():
    pokemon_team = [
        {"name": "Pikachu", "health": 35},
        {"name": "Glurak", "health": 120},
        {"name": "Bisasam", "health": 45}
    ]

    new_pokemon = random.choice(pokemon_team)

    box.append(new_pokemon)

    print(f"\nDu hast {new_pokemon['name']} gefangen!")

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
        print("\nDeine Tasche ist leer!")
        return

    print("\nDeine Tasche:")

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


# Test
starter_pokemon()
