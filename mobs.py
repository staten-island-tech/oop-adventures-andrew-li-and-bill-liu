from character import *
from utilities import *
from weapons import *
class Mob(character):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, drops):
        super().__init__(level=level, name=name, bhp=bhp, batk=batk, bdef=bdef)
        self.exp=exp
        self.exp_drop=self.scale(self.exp, 1.2)
        self.target=target
        self.dungeon=dungeon
        self.drops = drops
    def attack(self):
        dmg = self.target.take_damage(cut(self.atk))
        print(f"{self.name} has attacked {self.target.name}, dealing {dmg} dmg, {self.target.name}'s hp is now {self.target.hp}/{self.target.mxhp}hp")
    def take_damage(self, damage):
        dmg = super().take_damage(damage)
        if self.alive==False:
            self.on_death()
        return dmg
    def drop_exp(self):
        self.target.gain_exp(self.exp_drop)
        return self.exp_drop

    def loot_drop(self):
        if self.drops != None:
            for object in self.drops:
                item = find_item(self.weapons_list, object, id = True)
                if proc_chance(object['chance']) == True:
                    if item is None:
                        continue 
                        
                    self.target.obtain_weapon(self.weapon_setter(item))

        


    def on_death(self):
        self.drop_exp()
        self.loot_drop()
        self.dungeon.enemies.remove(self)



class wxa(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Xiyang Amalgamate", bhp= 4, batk=3, bdef=2, exp=4, target=target, dungeon=dungeon, drops = None)
class wgs(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Goo Skelly", bhp= 3, batk=11, bdef=0, exp=5, target=target, dungeon=dungeon, drops = None)
class wmg(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Massive Giant", bhp= 11, batk=11, bdef=11, exp=11, target=target, dungeon=dungeon, drops = None)
class whr(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Hairless Rat", bhp= 2, batk=1, bdef=2, exp=2, target=target, dungeon=dungeon, drops = None)
class wgc(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Nuclear Cochroach", bhp= 3, batk=1.5, bdef=11, exp=6, target=target, dungeon=dungeon, drops = None)
class wdc(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Dumb Clanker", bhp= 1, batk=1, bdef=1, exp=1, target=target, dungeon=dungeon, drops = None)
class xfp(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Xiyang Files Person", bhp= 3, batk=4.67, bdef=3, exp=5, target=target, dungeon=dungeon, drops = None)


class test_mob(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="test mob", bhp= 4, batk=3, bdef=2, exp=4, target=target, dungeon=dungeon, drops = [{'name':'test sword', 'id': 3, 'chance':100}])
