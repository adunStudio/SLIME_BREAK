from Framework.ADUN import Director, Node
from pico2d import *
import random
import math


class SlimePong(Node):
    def __init__(self, x, y):
        Node.__init__(self, "slime_1")
        self.x = x
        self.y = y

        self.num = random.randint(1, 4)

        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y
        self.x3 = x
        self.y3 = y

        self.a1 = 0
        self.a2 = 0
        self.a3 = 0

        self.angle = 0
        self.scale = self.image.w
        self.death = False

    def update(self):


        self.a1 += 0.2
        self.a2 -= 0.3
        self.a3 += 0.1

        self.x1 = self.x  - 10 + math.cos(self.a1) * 3
        self.y1 = self.y  + 10 + math.sin(self.a1) * 3

        self.x2 = self.x + 10 + math.cos(self.a2) * 13
        self.y2 = self.y - 10 + math.sin(self.a2) * 13

        self.x3 = self.x + math.cos(self.a3) * -13
        self.y3 = self.y + math.sin(self.a3) * -13


        self.angle += 1
        self.scale = min(self.scale + 0.2, 48)

        if self.scale >= 48:
            self.death = True

        self.frame = (self.frame + 0.2) % 10

    def draw(self):
        if self.num >= 1:
            self.image.rotate_draw(self.angle, self.x1, self.y1, self.scale, self.scale)
        if self.num >= 2:
            self.image.rotate_draw(self.angle, self.x2, self.y2, self.scale, self.scale)
        if self.num >= 3:
            self.image.rotate_draw(self.angle, self.x3, self.y3, self.scale, self.scale)


