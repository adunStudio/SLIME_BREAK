from Framework.ADUN import Director, Node
import math


class Bullet(Node):
    speed = 1
    angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "bullet")
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


