from character import *
from utilities import *

class Hero(character):
    def __init__(self, name):
        self.weaponbuff = 0
        self.batkbuff = 0
        self.mxhpbuff = 0
        self.bdefbuff = 0
        super().__init__(level = 1, name = name, batk = (10 + self.weaponbuff) * self.batkbuff, bdef = 10 * self.bdefbuff, bhp = 40)
        self.turns = 0
        self.inventory = {
            'weapons':[{'name' : 'fists', 'dmgbuff': 2},{'name': 'Whalen Blade', 'dmgbuff':3000000}]
        }
        self.equipped = None
        self.brace = False
        self.equip(0)
    def take_damage(self, x):
        if self.braced == True:
            tanked = super().take_damage(x)
            self.braced = False
            self.defense = cut(self.bdef / 10)
            self.stat_update
            print("Your brace have stopped bracing, your defense has returned to normal.")
            return tanked
        else:
            return super().take_damage(x)
    
    def equip(self, x):
        try:
            item = self.inventory['weapons'][x]
        except:
            print("invalid weapon format")
            return
        self.weaponbuff = item['dmgbuff']
        self.equipped = item['name']
        self.stat_update()    
    def stat_update(self):
        self.mxhp = self.scale(self.bhp, 1.25) * self.mxhpbuff
        self.atk = self.scale(self.batk + self.weaponbuff, 1.05) + self.batkbuff
        self.defense = self.scale(self.bdef, 1.05) + self.bdefbuff
    def level_up(self):
        while self.exp >= self.expbound:
            self.exp -= self.expbound
            self.level += 1
            self.stat_update()
            self.hp = self.mxhp
            self.expbound = self.scale(self.expbound, 1.05)
            print(f"{self.name} leveled up! Now level {self.level}!")
    def gain_exp(self,exp):
        self.exp += exp
        self.level_up()
    def attack(self):
        selected = False
        attacked = False
        for i, enemy in enumerate(self.dungeon.enemies):
            print(f"{i}: {enemy.name} {enemy.hp}hp/{enemy.mxhp}hp {enemy.atk}atk {enemy.defe}def")
        while attacked == False:
            who = input('Who do you attack? :')
            try:
                target = self.dungeon.enemies[who]
                selected = True
            except:
                print('Invalid enemy selected.')
            if selected == True:
                dmg = cut(self.atk) 
                dmg_done = target.take_damage(dmg)
                print(f"You have a attacked {target.name}, dealing {dmg_done} damage, their hp is now {target.hp}/{target.mxhp}")
                attacked = True
    def brace(self):
        if self.braced == False:
            self.braced = True
            self.turns -= 2
            self.defense *= 10
            print("You are bracing for incoming attacks, your defense has increased significantly for this next strike.")
        if self.braced == True:
            print("You are already bracing!")
    def inventory(self):
        item_selected = False
        for i, weapon in (self.inv['weapons']):
            print(f"{i}: {weapon['name']} {weapon['dmgbuff']} dmg")
        while item_selected == False:
            chosen = input('Choose a weapon')
            try:
                self.equip(chosen)
                item_selected = True
            except:
                print('Invalid Option')
        
    def action(self):
         while self.turns > 0 and self.alive == True:
            act = input("|1.) attack| |2.) brace| |3.) inv| |4.) stats| |5.) status| |6.) Wait| :")
            if act == "1":
                self.attack()
            if act == '2':
                self.brace()
            if act == '3':
                self.inventory()
            if act == '4':
                print(f"{self.stats()}, Equipped: {self.equipped}, EXP: {self.exp}/{self.expbound}, Turns left: {self.turns}")
            if act == '5':
                self.turns -= 1 
            if act not in ["1", "2", "3", "4",'5']:
                print("Invalid action!")
