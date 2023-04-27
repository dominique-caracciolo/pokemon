import json
class Pokemon:
    def __init__(self,name = "", hp=100, ap = 0, defense=0):
        self.__name = name
        self.__hp = hp
        self.ap = ap
        self.defense = defense

    def set_hp(self,new_hp):
        self.__hp = new_hp
    def set_name(self,new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    def get_hp(self):
        return self.__hp
    def get_ap(self):
        return self.ap
    def get_defense(self):
        return self.defense

    def showinf(self):
        print("Nom =",self.get_name())
        print("Vie =",self.get_hp())
        print("Puissance d'attaque =",self.get_ap())
        print("deffence = ",self.get_defense())

# def add_pokemon():
#     with open("pokemon.json", "r") as f:
#         data = json.load(f)




pokemon = Pokemon()


