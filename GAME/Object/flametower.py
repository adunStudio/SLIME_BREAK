from Framework.ADUN import Director, Node
from pico2d import *
import random


class FlameTower(Node):
    money = 50
    name = "flame"
    angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "flame_right")
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def check_enable(self, money):
        if money >= self.money:
            self.image = Director.asset["flame_right"]
        else:
            self.image = Director.asset["flame_disable"]



