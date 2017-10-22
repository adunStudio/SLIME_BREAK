from Framework.ADUN import Director, Node
import math
from pico2d import *


class Bullet(Node):
    speed = 20
    angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "bullet")
        self.x = x
        self.y = y - 15
        dist_y = Director.get_mouse_y() - self.y
        dist_x = Director.get_mouse_x() - self.x
        self.angle = math.atan2(dist_y, dist_x)

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self):
        self.image.rotate_draw(self.angle, self.x, self.y, self.width, self.height)


