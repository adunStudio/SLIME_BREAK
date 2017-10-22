from Framework.ADUN import Director, Node
import math


class Base(Node):
    crystal = None
    crystal_x, crystal_y = (0, 0)

    def __init__(self, x, y):
        Node.__init__(self, "base")
        self.x = x
        self.y = y
        self.crystal = Director.asset['crystal']
        self.frame_x = math.floor(self.crystal.w / 4)
        self.crystal_x = self.x
        self.crystal_y = self.y + self.crystal.h

    def update(self):
        self.frame = (self.frame + 0.1) % 4

    def draw(self):
        self.image.draw(self.x, self.y)
        self.crystal.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.crystal.h, self.crystal_x, self.crystal_y)

    def set_red(self):
        pass

