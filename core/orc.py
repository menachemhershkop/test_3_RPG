from core.monster import Monster
import random

class Orc(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.type="אורק"
        self.speed=random.randint(0,5)
        self.power=random.randint(10,15)
        self.armor_rating=random.randint(2,8)
    def weapon(self):
        self.weapons=self.weapons[random.randint(0,2)]
    def speak(self):
        print(self.type,self.name,"מגיע, והוא עצבני!!!!")
    def attack(self):
        pass