from abc import ABC, abstractmethod
import random
class Fighters(ABC):
    def __init__(self,name:str):
        self.name=name
        self.hp=50
        self.speed=None
        self.power=None
        self.armor_rating=None
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def attack(self):
        pass