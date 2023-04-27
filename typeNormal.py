from pokemon import Pokemon

class TypeNormal(Pokemon):
    def __init__(self, name="", hp=100, ap=12, defense=0):
        super().__init__(name, hp, ap, defense)
        self.name = "NormalType"



normal = TypeNormal()
normal.showinf()



