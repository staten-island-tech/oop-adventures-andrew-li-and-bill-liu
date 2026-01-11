from dungeon import *
from utilities import *

class game_runner:
    def __init__(self):
        self.dungeons = duns
        self.dungeon_choice = None
        self.hero = None
        self.end = False
    def dungeon_choose(self):
        chosen = False
        while chosen == False:
            choice = ask(self.dungeons, prompt = 'Choose a dungeon :')
            if choice != None:
                self.dungeon_choice = choice
                chosen = True
                return choice

    def run_system(self):
        while self.end == False:  # loop to allow replaying dungeons
            map_class = self.dungeon_choose()
            dungeon_instance = map_class(hero = self.hero)
            dungeon_instance.run()
        
            self.hero = dungeon_instance.hero

            again = input("\nDo you want to play another dungeon? (y/n): ").lower()
            if again != 'y':
                print("Thanks for playing!")
                break

runner = game_runner()
runner.run_system()