from character import *
from utilities import *
from weapons import *
class Hero(character):
    def __init__(self, name):
        self.weaponbuff = 0
        self.batkbuff = 0
        self.bhpbuff = 0
        self.mxhpbuff = 0
        self.bdefbuff = 0
        self.tbatk = 10
        self.tbdef = 1000000
        self.tbhp = 40
        super().__init__(level = 1, name = name, batk = (self.tbatk + self.weaponbuff) * (1 + self.batkbuff), bdef = self.tbdef * (1+self.bdefbuff), bhp = self.tbhp * (1+self.bhpbuff))
        self.turns = 0
        self.inventory = {
            'weapons':[]
        }
        self.obtain_weapon(self.weapons_list[0])
        self.obtain_weapon(self.weapons_list[1])
        self.equipped = None
        self.equipped_dict = None
        self.braced = False
        self.exp = 0
        self.exp_limit = 5
        self.expbound = self.scale(self.exp_limit, 1.05)
        self.levelcap = 200
        self.equip(1)
    
    def take_damage(self, x):
        if self.braced == True:
            tanked = super().take_damage(x)
            self.braced = False
            self.bdefbuff = 0
            self.stat_update()
            print("Your brace have stopped bracing, your defense has returned to normal.")
            return tanked
        else:
            return super().take_damage(x)
   
    def obtain_weapon(self, new_wep):
        new_wep = self.weapon_setter(new_wep)
        existing = find_item(self.inventory['weapons'], new_wep)
        if existing:
            if new_wep['lvl'] > existing['lvl'] or new_wep['dmgbuff'] > existing['dmgbuff']:
                self.inventory['weapons'].remove(existing)
                self.inventory['weapons'].append(new_wep)
                print(f"{self.name} have obatined a level:{new_wep['lvl']} {new_wep['name']}")
            else:
                print(f"{self.name} already has a better {new_wep['name']}.")
        else:
            self.inventory['weapons'].append(new_wep)
            print(f"{self.name} has obtained {new_wep['name']}")

    def equip(self, x):
        item = find_item(self.inventory['weapons'], x)
        if item == None:
            print("Invalid weapon choice.")
            return
        self.weaponbuff = item['dmgbuff']
        self.equipped = item['name']
        self.equipped_dict = item
        self.stat_update()
        print(f"You have equipped {self.equipped}.")

    def stat_update(self):
        self.weapon_update()
        self.batk = (self.tbatk + self.weaponbuff) * (1 + self.batkbuff)
        self.bdef = self.tbdef * (1+self.bdefbuff)
        self.bhp = self.tbhp * (1+self.bhpbuff)
        self.expbound = self.scale(self.exp_limit, 1.05)
        super().stat_update()
    def weapon_update(self):
        for i, weapon in enumerate(self.inventory['weapons']):
            if weapon['scales'] == True:
                base = find_item(self.weapons_list, weapon, id=True)
                if base:
                    self.inventory['weapons'][i] = self.weapon_setter(base)
        self.equip_junk()
    def equip_junk(self):
        if self.equipped:
            equipped_weapon = find_item(self.inventory['weapons'], {'name': self.equipped, 'id': self.equipped_dict['id']}, id=True)
            if equipped_weapon:
                self.weaponbuff = equipped_weapon['dmgbuff']
                self.equipped_dict = equipped_weapon


    
    
    def level_up(self):
        while self.exp >= self.expbound:
            self.exp -= self.expbound
            self.level += 1

            self.stat_update()
            self.hp = self.mxhp
            print(f"{self.name} leveled up! Now level {self.level}!")
    def gain_exp(self,exp):
        self.exp += exp
        self.level_up()
    
    
    def attack(self):
        attacked = False
        while attacked != True:
            for i, enemy in enumerate(self.dungeon.enemies):
                print(f"{i}: {enemy.name} {enemy.hp}/{enemy.mxhp} HP | {enemy.atk} ATK | {enemy.defe} DEF")
            who = input("Who do you attack? (number or 'x' to cancel): ")
            if who.lower() == 'x':
                return
            try:
                index = int(who)
                if 0 <= index < len(self.dungeon.enemies):
                    target = self.dungeon.enemies[index]
                    dmg = cut(self.atk)
                    dmg_done = target.take_damage(dmg)
                    print(f"You attacked {target.name}, dealing {dmg_done} damage. HP now: {target.hp}/{target.mxhp}")
                    self.turns -= 1
                    attacked = True
                    return
                else:
                    print("Invalid index.")
            except:
                print("Index pls")
    
    def brace(self):
        if self.braced == False:
            self.braced = True
            self.bdefbuff = 10
            self.stat_update()
            self.turns -= 2
            print("You are bracing for incoming attacks, your defense has increased significantly for this next strike.")
        elif self.braced == True:
            print("You are already bracing!")
    
    def inv(self):
        item = ask(self.inventory['weapons'], "Choose a weapon (or 'x' to cancel): ")
        if item:
            self.equip(item)
            self.turns -= 1      
    
    
    def action(self):
         while self.turns > 0 and self.alive == True:
            act = input("|1.) attack| |2.) brace| |3.) inv| |4.) stats| |5.) wait| :")
            if act == "1":
                self.attack()
            if act == '2':
                self.brace()
            if act == '3':
                self.inv()
            if act == '4':
                print(f"{self.stats()}, Equipped: {self.equipped}, EXP: {self.exp}/{self.expbound}, Turns left: {self.turns}")
            if act == '5':
                self.turns -= 1 
            if act not in ["1", "2", "3", "4",'5']:
                print("Invalid action!")
