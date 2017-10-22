from Framework.ADUN import Director, Node
from pico2d import *
import random


class Coin(Node):
    angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "coin", 8)
        self.x = x
        self.y = y
        self.frame_x = math.floor(self.width / 8)

    def update(self):
        self.frame = (self.frame + 0.3) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)

    def go_to(self, player):
        dist_y = player.y - self.y
        dist_x = player.x - self.x
        self.angle = math.atan2(dist_y, dist_x)
        self.x += math.cos(self.angle) * 4
        self.y += math.sin(self.angle) * 5




