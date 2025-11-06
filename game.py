import random

from core.fight.first_fighter import First_fighter
from core.goblin import Goblin
from core.orc import Orc
from core.player import Player
from cube.cube import Cube


class Game:
    def start(self):
        # player=self.player()
        self.show_menu()
    def player(self):
        name = input("הכנס את שמך: ")
        player = Player(name)
        player.add_power()
        return player
    def show_menu(self):
        print("לחץ 1 עבור מלחמה, לחץ 2 עבור יציאה")

    def choose_random_monster(self):
        monsters=[Orc,Goblin]
        choice_monster=random.choice(monsters)
        monster=choice_monster("נוני")
        print(monster.type)
        return monster
    def battle(self,player,monster):
        first=First_fighter
        first.roll(player,monster)
        while True:
            if not player.hp:
                print("המפלצת שבעה, תודה על הארוחה")
                break
            if not monster.hp:
                print("אומץ לבבך ישאר אגדה לדורות...")
                break
    def roll_dice(self,sides):
        return Cube().rool(sides)
