from Framework.ADUN import Director, Node
import math
from pico2d import *
import random

class Bullet(Node):
    speed = 20
    angle = 0
    damage = 10
    name = ""

    def __init__(self, x, y, angle=False, name="bullet_a", damage=10):
        Node.__init__(self, name)
        self.x = x
        self.y = y - 15
        self.name = name
        self.damage = damage
        if not angle:
            dist_y = Director.get_mouse_y() - self.y
            dist_x = Director.get_mouse_x() - self.x
            self.angle = math.atan2(dist_y, dist_x)
        else:
            self.angle = angle

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self):
        if self.name == "bullet_c":
            self.image.rotate_draw(self.angle, self.x, self.y, self.width / 2, self.height / 2)

        else:
            self.image.rotate_draw(self.angle, self.x, self.y, self.width, self.height)


