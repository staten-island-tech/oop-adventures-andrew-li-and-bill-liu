class hero:
    def __init__(self, health, xp, inventory, items, money):
        self.health=health
        self.xp=xp
        self.level=1
        self.inventory=inventory
        self.items=items
        self.money=money
    def buying(self, options):
        options= {
            "name"=="sword",
            "cost"==50,
            "atk"==25
        }
        self.inventory.append(options)
        print(self.inventory)