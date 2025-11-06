from core.fighters import Fighters


class Monster(Fighters):
    def __init__(self, name):
        super().__init__(name)
        self.weapons=["סכין","חרב","גרזן"]
    def speak(self):
       print(123)
    def attack(self):
       print(123)
