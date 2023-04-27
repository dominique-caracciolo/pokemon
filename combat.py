import random
from pokemon import Pokemon

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def est_en_vie(self, pokemon):
        return pokemon.get_hp() > 0
        
    def verifier_fin_combat(self):
        if not self.est_en_vie(self.pokemon1):
            return self.pokemon2.get_name()
        elif not self.est_en_vie(self.pokemon2):
            return self.pokemon1.get_name()
        else:
            return None
        
    def attaquer(self, attaquant, defenseur):
        if random.randint(0, 1) == 1:
            degats = attaquant.get_ap() - defenseur.get_defense()
            if degats < 0:
                degats = 0
            defenseur.set_hp(defenseur.get_hp() - degats)
            print(f"{attaquant.get_name()} attaque {defenseur.get_name()} et inflige {degats} points de dégâts.")
        else:
            print(f"{attaquant.get_name()} rate son attaque.")

pikachu = Pokemon("Pikachu", 100, 10, 5)
bulbizarre = Pokemon("Bulbizarre", 100, 8, 7)
combat = Combat(pikachu, bulbizarre)

while True:
    if combat.verifier_fin_combat():
        print(f"{combat.verifier_fin_combat()} remporte le combat !")
        break
    combat.attaquer(pikachu, bulbizarre)
    combat.attaquer(bulbizarre, pikachu)