from Framework.ADUN import Director, Node
from pico2d import *
import random


class CannonTower(Node):
    money = 30
    name = "cannon"
    angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "cannon_right")
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def check_enable(self, money):
        if money >= self.money:
            self.image = Director.asset["cannon_right"]
        else:
            self.image = Director.asset["cannon_disable"]



