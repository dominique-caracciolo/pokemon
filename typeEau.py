from pokemon import Pokemon

class TypeEau(Pokemon):
    def __init__(self, name="", hp=100, ap=12, defense=0):
        super().__init__(name, hp, ap, defense)
        self.name = "WaterType"
        self.hp = 100
        self.ap = 18
        self.defense = 13


eau = TypeEau()
eau.showinf()