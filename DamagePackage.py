from enum import Enum

class DamageType(Enum):
    physical = 0
    fire = 1
    ice = 2
    nature = 3
    shadow = 4
    light = 5

class DamagePackage:
    
    def __init__(self, damagetype, damagepercent):
        self.damageType = damagetype
        self.damagePercent = damagepercent

    def InterpretJson(self, content):
        dt = content["damageType"]
        dp = content["percent"]

        return DamagePackage(dt, dp)