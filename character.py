from utilities import *
class character:
    def __init__(self, level, name, bhp, batk, bdef):
        self.name=name
        self.level=level
        self.bhp=bhp
        self.batk=batk
        self.bdef=bdef
        self.atk=self.scale(self.batk, 1.05)
        self.mxhp=self.scale(self.bhp, 1.25)
        self.hp = self.mxhp
        self.defe=self.scale(self.bdef, 1.05)
        self.alive=True
        self.dungeon = None
    def scale(self, scale, factor, x=None):
        try:
            return cut(scale*(factor **(self.level-1)))
        except:
            return cut(scale*(factor**(x-1)))
    def take_damage(self, damage):
        dmg_after_def =cut((damage*(100/(100+self.defe))))
        if self.hp<=0:
            self.alive=False
            print(f"{self.name} has died")
        return dmg_after_def
    def stats(self):
        return(f"{self.name}, {self.level}, {self.hp}/{self.mxhp}, {self.defe}, {self.atk}")
    
