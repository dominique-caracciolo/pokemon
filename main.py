from pokemon import Pokemon
from combat import Combat
import json
import os
import random

def start():
    with open("pokemon.json", "r") as f:
        data = json.load(f)

    print("Voici la liste des Pokémons :")
    for pokemon_data in data:
        pokemon = Pokemon(pokemon_data["_Pokemon__name"], pokemon_data["_Pokemon__hp"], pokemon_data["ap"], pokemon_data["defense"],pokemon_data["type"])
        print(pokemon_data["_Pokemon__name"])

    while True:
        pokemon_nom = input("Entrez le nom du Pokémon que vous souhaitez utiliser : ")
        pokemon1 = None
        for pokemon_data in data:
            if pokemon_data["_Pokemon__name"] == pokemon_nom:
                pokemon1 = Pokemon(pokemon_data["_Pokemon__name"], pokemon_data["_Pokemon__hp"], pokemon_data["ap"], pokemon_data["defense"],pokemon_data["type"])
                break
        if pokemon1 is None:
            print(f"Le Pokémon {pokemon_nom} n'existe pas, veuillez réessayer.")
            continue
        else:
            break

    pokemon2_data = random.choice(data)
    pokemon2 = Pokemon(pokemon2_data["_Pokemon__name"], pokemon2_data["_Pokemon__hp"], pokemon2_data["ap"], pokemon2_data["defense"], pokemon2_data["type"])

    combat = Combat(pokemon1, pokemon2)

    while True:
        if combat.verifier_fin_combat():
            pokemon_gagnant = combat.verifier_fin_combat()
            print(f"{pokemon_gagnant} remporte le combat !")
            ajouter_pokemon_au_pokedex(pokemon2)
            break
        combat.attaquer(pokemon1, pokemon2)
        combat.attaquer(pokemon2, pokemon1)

def add_pokemon():
    with open("pokemon.json", "r") as f:
        data = json.load(f)

    print("Entrez les informations pour ajouter un nouveau Pokemon :")
    nom = input("Nom : ")
    max_hp = int(input("Points de vie : "))
    ap = int(input("Points d'attaque : "))
    defense = int(input("Points de défense : "))
    type = input(("Type du pokemon = "))

    nouveau_pokemon = Pokemon(nom, max_hp, ap, defense,type)
    data.append(nouveau_pokemon.__dict__)

    with open("pokemon.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Le Pokemon {nom} a été ajouté avec succès !")

def pokemon():
    with open("pokemon.json", "r") as f:
        data = json.load(f)

    for pokemon_data in data:
        pokemon = Pokemon(pokemon_data["_Pokemon__name"], pokemon_data["_Pokemon__hp"], pokemon_data["ap"], pokemon_data["defense"],pokemon_data["type"])
        pokemon.showinf()
        print("===")


import json

def ajouter_pokemon_au_pokedex(pokemon):
    pokedex = []
    # Charger la liste de tous les pokémons depuis le fichier pokemon.json
    with open("pokemon.json", "r") as f:
        pokemons = json.load(f)

    # Chercher le Pokémon ajouté dans la liste
    def ajouter_pokemon_au_pokedex(pokemon):
    # Charger la liste de tous les pokémons depuis le fichier pokemon.json
        with open("pokemon.json", "r") as f:
            pokemons = json.load(f)

    # Chercher le Pokémon ajouté dans la liste
    for p in pokemons:
        if p["_Pokemon__name"] == pokemon.get_name():
            # Copier toutes les informations du Pokémon dans un nouvel objet JSON
            nouveau_pokemon = {}
            nouveau_pokemon["nom"] = p["_Pokemon__name"]
            nouveau_pokemon["hp"] = pokemon.get_max_hp()
            nouveau_pokemon["ap"] = p["ap"]
            nouveau_pokemon["defense"] = p["defense"]
            nouveau_pokemon["type"] = p["type"]

            # Charger la liste des Pokémon enregistrés dans le pokedex.json
            with open("pokedex.json", "r+") as f:
                try:
                    pokedex = json.load(f)
                except json.JSONDecodeError:
                    pokedex = []

            # Ajouter le nouveau Pokemon au pokedex.json si il n'existe pas deja
            if not any(p["nom"] == pokemon.get_name() for p in pokedex):
                pokedex.append(nouveau_pokemon)

                # Enregistrer le pokedex mis à jour dans le fichier pokedex.json
                with open("pokedex.json", "w") as f:
                    json.dump(pokedex, f, indent=4)

                print(f"Le Pokemon {pokemon.get_name()} a été ajouté au pokedex avec succès!")
            else:
                print(f"Le Pokemon {pokemon.get_name()} est déjà enregistré dans le pokedex.")



# if os.stat("pokemon.json").st_size == 0:
#     data = []
# else:
#     data = json.load(f)
# with open("pokemon.json", "w") as f:
#     f.write("[]")
# if not os.path.isfile("pokemon.json"):
#     with open("pokemon.json", "r+") as f:
#         f.write("[]")



while True:
    print("""
    Menu :
    1 - Lancer une partie
    2 - Ajouter un Pokemon
    3 - Accéder a la liste Pokemon
    4 - Quitter
    """)
    choix = input("Que voulez-vous faire ? ")
    if choix == "1":
        start()
    elif choix == "2":
        add_pokemon()
    elif choix == "3":
        pokemon()
    elif choix == "4":
        break
    else:
        print("Choix invalide, veuillez réessayer.") 
