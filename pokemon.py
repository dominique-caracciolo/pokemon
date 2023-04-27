class Pokemon:
    def __init__(self,name = "", hp=100, ap = 12, defense=0):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.defense = defense

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_ap(self):
        return self.ap
    def get_defense(self):
        return self.defense

    def showinf(self):
        print(self.get_name())
        print(self.get_hp())
        print(self.get_ap())
        print(self.get_defense())

pokemon = Pokemon()



