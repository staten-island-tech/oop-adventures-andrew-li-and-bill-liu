import random
from hero import *
class dungeon:
    def __init__(self):
        self.moblist = []
        self.bosslist = []
        self.enemies = []
        self.hero = None
        self.enemy_limit = 1
        self.dungeon_depth = 1
        self.dungeon_options = ["Whalen Champain"]
        self.hero_setup()
    def Whalen_Champain(self):
        self.moblist.append()
        self.bosslist.append
    def hero_setup(self):
        name = input("Enter your hero's name: ")
        self.hero = Hero(name)
        self.hero.dungeon = self
        print(f"Welcome, {self.hero.name}, to the dungeon!")
    def dungeon_chooser(self):
        selected = False
        for i, name in enumerate(self.dungeon_options):
            print(f"{i} : {name}")
        while selected == False:
            chosen = input("Choose")
            if chosen == '0':
                self.Whalen_Champain()
    def spawn(self,x,y):
        t = x(level = y, target = self.hero, dungeon = self)
        self.enemies.append(t)
        print(t.stats())
    def normal_room(self):
        for i in range(1,self.enemy_limit + 1):
            self.spawn(random.choice(self.moblist), self.dungeon_depth)
    def boss_room(self):
        boss = random.choice(self.bosses) 
        self.spawn(boss, self.dungeon_depth)
        if self.enemy_limit < 5:
            self.enemy_limit += 1


    def newroom(self):
        print(f'floor {self.dungeon_depth}')
        if self.dungeon_depth % 10 == 0:
            self.boss_room()
        else:
            self.normal_room()
    def progress(self):
        self.dungeon_depth += 1
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
        while len(self.enemies) != 0:
            self.Hero_turn()
            self.Enemy_turn()
            if len(self.enemies) == 0:
                self.progress()