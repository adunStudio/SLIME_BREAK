from Framework.ADUN import Director, Node
from pico2d import *
import random


class SlimePong(Node):
    def __init__(self, x, y):
        Node.__init__(self, "slime_1")
        self.x = x
        self.y = y

    def update(self):
        self.frame = (self.frame + 0.2) % 10

    def draw(self):
        self.draw(self.x, self.y)


