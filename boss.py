from mobs import *
from utilities import *
import random
class Boss(Mob):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, attacks, charge_rate):
        super().__init__(level=level, name=name, bhp=bhp, batk=batk, bdef=bdef, exp=exp, dungeon=dungeon, target=target)
        self.charge_rate=charge_rate
        self.attacks=attacks
        self.move_charge=0
        self.selected_move=None
        self.selected_move_scale=0
        self.move_released=False
        self.move_special=None
        self.move_damage_type=None

    def select_move(self):
        move=random.choice(self.attacks)
        self.charge=0
        self.move_charge=move['charge']
        self.selected_move=move['move']
        self.selected_move_scale=move['scale']
        self.move_special=move['special']

    def move_release(self):
        dmg=int(int(self.atk)* self.selected_move_scale)
        while self.charge>=self.move_charge:
            x=self.target.take_damage(dmg)
            print(f"{self.name} has attacked {self.target} with {self.selected_move} deeling {x} dmg\n Your current hp is now {self.target.hp}/{self.target.mxhp}")
            self.move_released=True
            if self.move_special is not None:
                for effects in self.move_special:
                    effects()
            if self.target.alive==False:
                exit()

    def attack(self):
        if self.selected_move==None:
            self.selected_move()
        if self.selected_move is not None and self.charge<=self.move_charge:
            self.charge+=self.charge_rate
        if self.charge>= self.move_charge:
            self.move_released()
            self.selected_move=None

class Whalen(Boss):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, attacks, charge_rate):
        super().__init__(level, name="Whalen", bhp=500, batk=50, bdef=50, exp=100, dungeon=dungeon, target=target, attacks={'name':'Little Boy', 'charge':5, 'scale':4, 'special':[self.radiation]}, charge_rate=1)
    def radiation(self):
        self.charge+=1
        self.target.hp-=15
        self.bhp*1.15
class XIyang(Boss):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, attacks, charge_rate):
        super().__init__(level=level, name="Xiyang", bhp=600, batk=70, bdef=10, exp=125, dungeon=dungeon, target=target, attacks=[{'name':'melt', 'charge':5, 'scale':4,}, {'name':'fire', 'charge':3, 'scale':2, 'special':'burn'}], charge_rate=1)
class Mecha_Whalen(Boss):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, attacks, charge_rate):
        super().__init__(level=level, name="Mecha Whalen", bhp=1000, batk=75, bdef=100, exp=200, dungeon=dungeon, target=target, attacks={'name':'Big Man', 'charge':8, 'scale':5, 'special':[self.radiation]}, charge_rate=1)
    def radiation(self):
        self.charge+=2
        self.target.hp-=25
        self.bhp*1.2
    

list_boss = [Whalen, XIyang, Mecha_Whalen]