from character import *
from utilities import *
class Mob(character):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target):
        super().__init__(level=level, name=name, bhp=bhp, batk=batk, bdef=bdef)
        self.exp=exp
        self.exp_drop=self.scale(self.exp, 1.2)
        self.target=target
        self.dungeon=dungeon
    def attack(self):
        dmg = self.target.take_damage(cut(self.atk))
        print(dmg)
    def take_damage(self, damage):
        dmg = super().take_damage(damage)
        if self.alive==False:
            self.dungeon.enemies.remove(self)
        return dmg
class wxa(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Xiyang Amalgamate", bhp= 4, batk=3, bdef=2, exp=4, target=target, dungeon=dungeon)
class wgs(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Goo Skelly", bhp= 3, batk=11, bdef=0, exp=5, target=target, dungeon=dungeon)
class wmg(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Massive Giant", bhp= 11, batk=11, bdef=11, exp=11, target=target, dungeon=dungeon)
class whr(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Hairless Rat", bhp= 2, batk=1, bdef=2, exp=2, target=target, dungeon=dungeon)
class wgc(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Nuclear Cochroach", bhp= 3, batk=1.5, bdef=11, exp=6, target=target, dungeon=dungeon)
class wdc(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Whalen Dumb Clanker", bhp= 1, batk=1, bdef=1, exp=1, target=target, dungeon=dungeon)
class xfp(Mob):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Xiyang Files Person", bhp= 3, batk=4.67, bdef=3, exp=5, target=target, dungeon=dungeon)

list_mobs = [wxa, wgs, wmg, whr, wgc, wdc, xfp]