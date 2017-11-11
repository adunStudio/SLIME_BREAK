from Framework.core import Director
from Framework.node import Node
import math


class Player(Node):
    gun = None
    angle = 0
    mouse_angle = 0
    see_angle = 0
    money = 0

    def __init__(self):
        Node.__init__(self, "player")

    def update(self, frame_time):
        self.angle = math.atan2(Director.get_mouse_y() - self.y, Director.get_mouse_x() - self.x)
        self.mouse_angle = self.angle * (180 / math.pi) + 180
        self.see_angle = ((self.mouse_angle + 22.5) / 45) % 8

        self.set_direction_image(int(self.see_angle))

        if Director.INPUT["LEFT"]:
            self.x -= self.speed

        if Director.INPUT["RIGHT"]:
            self.x += self.speed

        if Director.INPUT["UP"]:
            self.y += self.speed

        if Director.INPUT["DOWN"]:
            self.y -= self.speed

        self.frame = (self.frame + 0.1) % 4

        if self.gun is not None:
            self.gun.x = self.x
            self.gun.y = self.y
            self.gun.set_direction(int(self.see_angle))

    def draw(self):
        if int(self.see_angle) == 6 or int(self.see_angle) == 7 or int(self.see_angle) == 5:
            #self.gun.draw()
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
            #self.gun.draw()

