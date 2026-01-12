import random
from hero import *
from mobs import *
from boss import *
class Dungeon:
    def __init__(self, name, moblist, bosslist, hero = None):
        self.name = name
        self.moblist = moblist
        self.bosslist = bosslist
        self.enemies = []
        self.hero = hero
        self.enemy_limit = 1
        self.enemy_limit_max = 5
        self.dungeon_depth = 10
        self.descent_rate = 5
        self.dungeon_peak = len(self.bosslist) * 10
        self.dungeon_cleared = False
        self.room_cleared = False
        self.hero_setup()
    def hero_setup(self):
        if self.hero == None:
            name = input("Enter your hero's name: ")
            self.hero = Hero(name)
        self.hero.dungeon = self
        print(f"Welcome, {self.hero.name}, to the {self.name}!")
    def spawn(self,x,y):
        t = x(level = y, target = self.hero, dungeon = self)
        self.enemies.append(t)
        print(t.stats())
    def normal_room(self):
        level_to_use = max(self.dungeon_depth, self.hero.level)
        for i in range(self.enemy_limit):
            self.spawn(random.choice(self.moblist), level_to_use)
    def boss_room(self):
        level_to_use = max(self.dungeon_depth, self.hero.level)
        boss_number = (self.dungeon_depth // 10) - 1
        boss_index = boss_number % len(self.bosslist)
        self.spawn(self.bosslist[boss_index],level_to_use + 5)
        if self.enemy_limit < self.enemy_limit_max:
            self.enemy_limit += 1


    def newroom(self):
        self.enemies = []
        print(f'floor {self.dungeon_depth}')
        if self.dungeon_depth % 10 == 0:
            self.boss_room()
        else:
            self.normal_room()
    def progress(self):
        self.dungeon_depth += self.descent_rate
        if self.dungeon_depth > self.dungeon_peak:
            self.dungeon_depth = self.dungeon_peak
        self.newroom()
    
    def Hero_turn(self):
        self.hero.turns += 1
        if self.hero.turns > 0:
            self.hero.action()
    def Enemy_turn(self):
        for i in self.enemies:
            i.attack()
    
    def run(self):
        self.newroom()

        while self.dungeon_cleared != True:
            if self.hero.hp <= 0:
                print(f"{self.hero.name} has been defeated!")
                break

            self.Hero_turn()
            self.Enemy_turn()

            if len(self.enemies) == 0:
                self.room_cleared = True
                if self.dungeon_depth == self.dungeon_peak and self.room_cleared == True:
                    self.dungeon_cleared = True
                    print("Dungeon cleared!")
                    return
                self.progress()

class Whalen_Citadel(Dungeon):
    def __init__(self, hero):
        super().__init__(name="Whalen Citadel", moblist=[wxa, wgs, wmg, whr, wgc, wdc, xfp], bosslist=[Whalen, Mecha_Whalen],hero=hero)


class test_realm(Dungeon):
    def __init__(self, hero):
        super().__init__(name="test realm", moblist=[test_mob], bosslist=[test_mob],hero=hero)

class Xiyang_Desert(Dungeon):
    def __init__(self, hero):
        super().__init__(name="Xiyang Desert", moblist=[xsw, xuh, xmv], bosslist=[XIyang], hero=hero)


duns = [Whalen_Citadel, test_realm, Xiyang_Desert]