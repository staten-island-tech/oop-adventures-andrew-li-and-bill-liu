import random
class dungeon:
    def __init__(self):
        self.moblist = []
        self.bosslist = []
        self.enemies = []
        self.hero = None
        self.enemy_limit = 1
        self.dungeon_depth = 1
        self.hero_setup()
    def hero_setup(self):
        name = input("Enter your hero's name: ")
        self.hero = Hero(name)
        self.hero.dungeon = self
        print(f"Welcome, {self.hero.name}, to the dungeon!")
    def spawn(self,x,y):
        t = x(level = y, target = self.hero, dungeon = self)
        self.enemies.append(t)
        print(t.stats())
    def normal_room(self):
        for i in range(1,self.enemy_limit + 1):
            self.spawn(random.choice(self.moblist), self.dungeon_depth)
    def boss_room(self):
        boss_of_choice = random.choice(self.bosslist)
        self.spawn(boss_of_choice, self.dungeon_depth)
        if self.enemy_limit < 5:
            self.enemy_limit += 1


    def newroom(self):
        print(f'floor {self.dungeon_depth}')
        if self.dungeon_depth % 10 == 0:
            self.boss_room()
        else:
            self.normal_room()
    def progress(self):
        self.dungeon_depth += 5
        self.newroom()
    
    def Hero_turn(self):
        self.hero.turns += 1
        self.hero.status_effects_tick()
        if self.hero.turns > 0:
            self.hero.action()
    def Enemy_turn(self):
        for i in self.enemies:
            i.status_effects_tick()
            i.attack()
    
    def run(self):
        self.newroom()
        while len(self.enemies) != 0:
            self.Hero_turn()
            self.Enemy_turn()
            if len(self.enemies) == 0:
                self.progress()
