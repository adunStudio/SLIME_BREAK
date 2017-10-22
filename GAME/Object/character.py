from Framework.ADUN import Director, Node
import random
import math


class Character(Node):
    image = None
    speed = 1
    see_angle = 0

    def __init__(self):
        Node.__init__(self, "3_south")
        self.x = 50
        self.y = 50


    def update(self):
        self.see_angle = math.atan2(Director.get_mouse_y() - self.y, Director.get_mouse_x() - self.x) * 360
        print(self.see_angle)
    def draw(self):
        self.image.clip_draw(self.frame * self.width , 0, self.width, self.height, self.x, self.y)

    def randomMove(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
