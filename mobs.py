from character import *
from utilities import *
class Mob(character):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon):
        super().__init__(level=level, name=name, bhp=bhp, batk=batk, bdef=bdef)
        self.exp=exp
        self.exp_drop=self.scale(self.exp, 1.2)
        self.target=target
        self.dungeon=dungeon