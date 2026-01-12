from mobs import *
from utilities import *
from weapons import *
import random
class Boss(Mob):
    def __init__(self, level, name, bhp, batk, bdef, exp, dungeon, target, attacks, charge_rate, drops):
        super().__init__(level=level, name=name, bhp=bhp, batk=batk, bdef=bdef, exp=exp, dungeon=dungeon, target=target, drops = drops)
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
        while self.charge>=self.move_charge:
            dmg=int(int(self.atk)* self.selected_move_scale)
            x=self.target.take_damage(dmg)
            print(f"{self.name} has attacked {self.target.name} with {self.selected_move} deeling {x} dmg\n Your current hp is now {self.target.hp}/{self.target.mxhp}")
            self.move_released=True
            if self.move_special is not None:
                for effects in self.move_special:
                    effects()
            self.charge -= self.move_charge
            if self.target.alive==False:
                exit()

    def attack(self):
        if self.selected_move is None:
            self.select_move()

        self.charge += self.charge_rate
        print(f"{self.name} is charging {self.selected_move} : {self.charge}/{self.move_charge}")

        if self.charge >= self.move_charge:
            self.move_release()
            self.selected_move = None
            self.charge = 0
    def enrage(self,rate = 1.5, proc = 50):
        if proc_chance(proc) == True:
            self.batk *= rate
            self.stat_update()
    def action_delay(self, delay = 1, proc = 50):
        if proc_chance(proc) == True:
            self.target.turns -= delay

class Whalen(Boss):
    def __init__(self, level, target, dungeon):
        super().__init__(level, name="Whalen", bhp=500, batk=50, bdef=50, exp=100, dungeon=dungeon, target=target, attacks=[{'move':'Little Boy', 'charge':5, 'scale':4, 'special':[self.radiation]},{'move':'Big Man', 'charge':8, 'scale':5, 'special':[self.radiation]}], charge_rate=1, drops = [{'name':'Whalen Pro Max', 'id':5, 'chance':100'}]
    def radiation(self):
        dmg=int((self.atk * self.selected_move_scale)/2)
        self.target.take_damage(dmg)
        self.enrage()
class XIyang(Boss):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Xiyang", bhp=600, batk=70, bdef=10, exp=125, dungeon=dungeon, target=target, attacks=[{'move':'melt', 'charge':5, 'scale':4, 'special':None}, {'move':'fire', 'charge':3, 'scale':2, 'special':[self.burn]}], charge_rate=1, drops = None)
    def burn(self):
        dmg=int((self.atk * self.selected_move_scale)/2)
        self.target.take_damage(dmg)
        self.target.bdefbuff -= (self.target.bdefbuff *0.5)
        self.target.stat_update()
class Mecha_Whalen(Boss):
    def __init__(self, level, target, dungeon):
        super().__init__(level=level, name="Mecha Whalen", bhp=1000, batk=2, bdef=100, exp=200, dungeon=dungeon, target=target, attacks=[{'move':'Whalen Onslaught', 'charge':1, 'scale': 0.5, 'special':[self.enrage]}], charge_rate=3, drops = None)
    def enrage(self):
        super().enrage(rate = 2, proc = 90)
        if proc_chance(60) == True:
            self.charge_rate += 3
    

