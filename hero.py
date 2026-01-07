from character import *
from utilities import *
class character:
    pass 
class Hero(character):
    def __init__(self, name):
        self.weaponbuff = 0
        self.batkbuff = 0
        self.mxhpbuff = 0
        self.bdefbuff = 0
        super().__init__(level = 1, name = name, batk = (10 + self.weaponbuffkbuff) * self.batkbuff, bdef = 10 * self.bdefbuff, bhp = 40)
        self.turns = 0
        self.inventory = {
            'weapons':[{'name': 'Whalen Blade', 'dmgbuff':3000000}],
            'consumeables':[]
        }
    def stat_update(self):
        self.mxhp = self.scale(self.bhp, 1.25) * self.mxhp_buff
        self.atk = self.scale(self.batk + self.weapon_buff, 1.05) + self.atk_buff
        self.defense = self.scale(self.bdef, 1.05) + self.def_buff
    def attack(self):
        attacked = False
        for i, enemy in enumerate(self.dungeon.enemies):
            print(f"{i}: {enemy.name} {enemy.hp}hp/{enemy.mxhp}hp {enemy.atk}atk {enemy.defe}def")
        while attacked == False:
            who = input('Who do you attack? :')
            if 

