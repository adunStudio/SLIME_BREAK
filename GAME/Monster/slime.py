from pico2d import *
from framework import ADUN
import random


class Slime(ADUN.Node):
    image = None

    def __init__(self):
        self.image = load_image("Asset/slime.png")
        self.width = self.image.w
        self.height = self.image.h

        self.x = random.randint(1, 300)
        self.y = random.randint(1, 300)

    def update(self):
        self.randomMove()

    def draw(self):
        self.image.clip_draw(self.frame * self.width, 0, self.width, self.height, self.x, self.y)

    def randomMove(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
