import Enemy
import json

class Main:
    def __init__(self): #constructor
        self.inputText = ""
        self.enemies = []

    def Start(self):
        data = ""
        with open("Enemies/TestEnemy.json") as data_file:
            data = json.load(data_file)

        enemy = Enemy
        enemy.InterpretJson(data)
        self.enemies.append(enemy)
        #{'id': 'unique_id_goes_here', 'name': 'name_goes_here', 'health': 100, 'attacks': [{'occurance': 1, 'dealDamage': {'damageType': 0, 'percent': 1}}], 'resistances': [{'damageType': 1, 'percent': 1}]}
    
if __name__ == "__main__":
    main = Main()
    main.Start()
