from core.monster import Monster
import random

class Goblin(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.type="גובלין"

    def weapon(self):
        self.weapons=self.weapons[random.randint(0,2)]
    def speak(self):
        print(self.type,self.name,"מגיע, והוא עצבני!!!!")
    def attack(self):
        pass