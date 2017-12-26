from Framework.ADUN import Director, Node
from Object.basetower import BaseTower
from pico2d import *
import random


class FlameTower(BaseTower):

    bullet = "bullet_c"
    damage = 1

    def __init__(self, x, y):
        BaseTower.__init__(self, "flame", 10, 100, Director.fps / 20)
        self.x = x
        self.y = y
        self.money = 100

    def update(self):
        BaseTower.update(self)



