from core.monster import Monster
import random

from cube.cube import Cube


class Orc(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.type="אורק"
        self.speed=random.randint(0,5)
        self.power=random.randint(10,15)
        self.armor_rating=random.randint(2,8)
        self.weapons = self.weapons[random.randint(0, 2)]
    # def weapon(self):
    #     self.weapons=self.weapons[random.randint(0,2)]
    def speak(self):
        print(self.type,self.name,"מגיע, והוא עצבני!!!!")
    def attack(self, armor, hp):
        while True:
            self.speak()
            cube = Cube().rool(20) + self.speed
            if cube > armor:
                damage = (Cube().rool(6) + self.power) * pow_damage(self.weapons)
                hp -= damage
            else:
                break