from utilities import *
from weapons import *
class character:
    def __init__(self, level, name, bhp, batk, bdef):
        self.name=name
        self.level=level
        self.bhp=bhp
        self.batk=batk
        self.bdef=bdef
        self.atk=self.scale(self.batk, 1.05)
        self.mxhp=self.scale(self.bhp, 1.05)
        self.hp = self.mxhp
        self.defe=self.scale(self.bdef, 1.05)
        self.min_tankable = 0.3
        self.alive=True
        self.dungeon = None
        self.weapons_list = lista_weapons
    
    def stat_update(self):
        self.atk = self.scale(self.batk, 1.05)
        self.mxhp = self.scale(self.bhp, 1.05)
        self.defe = self.scale(self.bdef, 1.05)
    
    
    def weapon_setter(self, x):
        weapon = {'id': x['id'], 'name':x['name'],'lvl':self.level, 'dmgbuff':self.scale(x['dmgbuff'], 1.05), 'scales':x['scales']}
        return weapon
    
    def scale(self, scale, factor, x=None):
        try:
            return cut(scale*(factor **(self.level-1)))
        except:
            return cut(scale*(factor**(x-1)))
   
    def take_damage(self, damage):
        dmg_after_def =cut((damage*(100/(100+self.defe))))
        dmg_after_def = max(dmg_after_def, damage * self.min_tankable)
        self.hp -= dmg_after_def
        if self.hp<=0:
            self.alive=False
            print(f"{self.name} has died")
        return dmg_after_def
    
    def stats(self):
        return(f"Name:{self.name}, lvl:{self.level}, Hp:{self.hp}/{self.mxhp}, Def:{self.defe}, Atk:{self.atk}")
    
