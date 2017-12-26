from Framework.ADUN import Director, Node
from Object.basetower import BaseTower
from pico2d import *
import random


class CannonTower(BaseTower):
    bullet = "bullet_b"
    damage = 10

    def __init__(self, x, y):
        BaseTower.__init__(self, "cannon", 10)
        self.money = 30

        self.x = x
        self.y = y

    def update(self):
        BaseTower.update(self)



