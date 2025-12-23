import random
class dungeon:
    def __init__(self, mobs, bosses):
        self.mobs = mobs
        self.bosses = bosses
        self.floor = 1
        self.room_max = 3
    def roomfill(self):
            enemies = []
            for i in range(self.room_max):
                enemies.append(random.choice(self.mobs))
            return enemies
    def new_room(self):
            enemies = self.roomfill()

tower = dungeon(['zombie','skeleton','bat','xiyang'], [])
tower.new_room()
                               