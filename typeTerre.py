from pokemon import Pokemon

class TypeTerre(Pokemon):
    def __init__(self, name="", hp=100, ap=12, defense=0):
        super().__init__(name, hp, ap, defense)
        self.name = "EarthType"
        self.hp = 100
        self.ap = 15
        self.defense = 15


feu = TypeTerre()
feu.showinf()