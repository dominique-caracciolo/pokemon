from pokemon import Pokemon
from combat import Combat
import json
import os

def start():
    pikachu = Pokemon("Pikachu", 100, 10, 5)
    bulbizarre = Pokemon("Bulbizarre", 100, 8, 7)
    combat = Combat(pikachu, bulbizarre)

    while True:
        if combat.verifier_fin_combat():
            print(f"{combat.verifier_fin_combat()} remporte le combat !")
            break
        combat.attaquer(pikachu, bulbizarre)
        combat.attaquer(bulbizarre, pikachu)

def add_pokemon():
    with open("pokemon.json", "r") as f:
        data = json.load(f)

    print("Entrez les informations pour ajouter un nouveau Pokemon :")
    nom = input("Nom : ")
    hp = int(input("Points de vie : "))
    ap = int(input("Points d'attaque : "))
    defense = int(input("Points de défense : "))
    nouveau_pokemon = Pokemon(nom, hp, ap, defense)
    data.append(nouveau_pokemon.__dict__)

    with open("pokemon.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Le Pokemon {nom} a été ajouté avec succès !")

def pokedex():
    with open("pokemon.json", "r") as f:
        data = json.load(f)

    for pokemon_data in data:
        pokemon = Pokemon(pokemon_data["_Pokemon__name"], pokemon_data["_Pokemon__hp"], pokemon_data["ap"], pokemon_data["defense"])
        pokemon.showinf()
        print("===")

if not os.path.isfile("pokemon.json"):
    with open("pokemon.json", "w") as f:
        f.write("[]")

while True:
    print("""
    Menu :
    1 - Lancer une partie
    2 - Ajouter un Pokemon
    3 - Accéder au Pokedex
    4 - Quitter
    """)
    choix = input("Que voulez-vous faire ? ")
    if choix == "1":
        start()
    elif choix == "2":
        add_pokemon()
    elif choix == "3":
        pokedex()
    elif choix == "4":
        break
    else:
        print("Choix invalide, veuillez réessayer.") 
