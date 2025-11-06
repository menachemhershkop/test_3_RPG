from cube.cube import Cube


class First_fighter:
    def roll(self,player,monster):
        player_roll=Cube().rool(6)+player.speed
        monster_roll=Cube().rool(6)+monster.speed
        if player_roll < monster_roll:
            return monster.attack(player.armor_rating,player.hp)
        else:
            return player.attack(monster.armor_rating,monster.hp)