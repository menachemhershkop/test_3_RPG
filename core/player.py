from core.fighters import Fighters
import random

from cube.cube import Cube


class Player(Fighters):
    def __init__(self, name):
        super().__init__(name)
        self.power=random.randint(10,15)
        self.speed=random.randint(0,5)
        self.armor_rating=random.randint(2,8)
        self.profession=["לוחם", "מרפא"]
        self.profession=self.profession[random.randint(0,1)]
    def add_power(self):

        if self.profession=="לוחם":
            self.power+=2
        else:
            self.hp+=10
    def speak(self):
        print(self.name, "מגיע...")
    def attack(self):
        def attack(self,armor, hp):
            while True:
                self.speak()
                cube = Cube().rool(20) + self.speed
                if cube > armor:
                    damage = Cube().rool(6) + self.power
                    hp -= damage
                else:
                    break