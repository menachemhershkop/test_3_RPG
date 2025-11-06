from core.monster import Monster
import random
from fight import pow_damage

from cube.cube import Cube


class Goblin(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.type="גובלין"
        self.hp=20
        self.speed=random.randint(5,10)
        self.power=random.randint(5,10)
        self.armor_rating=1
        self.weapons = self.weapons[random.randint(0, 2)]
    # def weapon(self):
    #     self.weapons=self.weapons[random.randint(0,2)]
    def speak(self):
        print(self.type,self.name,"מגיע, והוא עצבני!!!!")
    def attack(self, armor, hp):
        while True:
            self.speak()
            cube=Cube().rool(20)+self.speed
            if cube > armor:
                damage=(Cube().rool(6)+self.power)*pow_damage(self.weapons)
                hp-=damage
            else:
                break