import random as rand

import DamagePackage

class Enemy:
    def __init__(self):
        self.id = 0
        self.name = 0

        self.health = 0
        self.maxhealth = 0

        self.attacks = []

        self.resistances = []

    def InterpretJson(self, content):
        self.id = content["id"]
        self.name = content["name"]
        self.health = content["health"]

        for i in range(len(content["attacks"])):
            self.attacks.append(Attack.InterpretJson(content["attacks"][i]))

        for i in range(len(content["resistances"])):
            package = content["resistances"][i]["dealDamage"]
            self.resistances.append(DamagePackage.InterpretJson(package))   #DamagePackage(package["dealDamage"]["damageType"], package["dealDamage"]["percent"])

class Attack:

    def __init__(self, occurance, package):
        self.occurance = occurance
        self.package = package

    def InterpretJson(self, content):
        o = content["occurance"]
        p = DamagePackage(content["dealDamage"]["damageType"], content["dealDamage"]["percent"])
        return Attack(o, p)
