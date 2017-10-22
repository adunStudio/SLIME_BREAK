from Framework.ADUN import Director, Node
from pico2d import *
import random


class Explode(Node):
    time = 0

    def __init__(self, x, y, type, time):
        Node.__init__(self, "explode" + type)
        self.time = time
        self.x = x
        self.y = y
        self.frame_x = math.floor(self.width / 3)
        self.a , self.b, self.c, self.d = (random.randint(-15, 15), random.randint(-15, 15), random.randint(-15, 15), random.randint(-15, 15))

    def update(self):
        self.time -= 1
        self.frame = (self.frame + 0.1) % 3

    def draw(self):
        if int(self.frame) == 0:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
        elif int(self.frame) == 1:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x + self.a,
                                 self.y + self.b)
        elif int(self.frame) == 2:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x + self.c, self.y + self.d)


