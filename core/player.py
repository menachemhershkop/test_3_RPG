from core.fighters import Fighters
import random

class Player(Fighters):
    def __init__(self, name):
        super().__init__(name)
        self.power=random.randint(10,15)
        self.speed=random.randint(0,5)
        self.armor_rating=random.randint(2,8)
        self.profession=["לוחם", "מרפא"]
    def speak(self):
        print(self.name, "is cuming!")
    def attack(self):
        print(123)

