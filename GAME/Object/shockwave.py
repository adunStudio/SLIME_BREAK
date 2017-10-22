from Framework.ADUN import Director, Node
from pico2d import *
import random


class Shockwave(Node):
    def __init__(self, x, y):
        Node.__init__(self, "shockwave")
        self.x = x
        self.y = y
        self.frame_x = math.floor(self.width / 9)

    def update(self):
        self.frame = (self.frame + 0.2) % 10

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)


