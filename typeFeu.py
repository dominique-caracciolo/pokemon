from pokemon import Pokemon

class TypeFeu(Pokemon):
    def __init__(self, name="", hp=100, ap=12, defense=0):
        super().__init__(name, hp, ap, defense)
        self.name = "FireType"
        self.hp = 80
        self.ap = 20
        self.defense = 12


feu = TypeFeu()
feu.showinf()