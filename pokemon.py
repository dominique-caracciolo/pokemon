import json
class Pokemon:
    def __init__(self,name = "", hp=100, ap = 0, defense=0, type="", max_hp=100):
        self.__name = name
        self.__hp = hp
        self.ap = ap
        self.defense = defense
        self.type = type
        self.__max_hp = max_hp

    def set_hp(self,new_hp):
        self.__hp = new_hp
    def set_name(self,new_name):
        self.__name = new_name
    def set_max_hp(self,max_hp):
        self.__max_hp = max_hp

    def get_max_hp(self):
        return self.__max_hp
    def get_name(self):
        return self.__name
    def get_hp(self):
        return self.__hp
    def get_ap(self):
        return self.ap
    def get_defense(self):
        return self.defense
    def get_type(self):
        return self.type


    def showinf(self):
        print("Nom =",self.get_name())
        print("Vie =",self.get_hp())
        print("Puissance d'attaque =",self.get_ap())
        print("defense = ",self.get_defense())
        print("Type du pokemon = ",self.get_type())

# def add_pokemon():
#     with open("pokemon.json", "r") as f:
#         data = json.load(f)

pokemon = Pokemon()