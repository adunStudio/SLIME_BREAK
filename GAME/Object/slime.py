from Framework.ADUN import Director, Node
import random
import math


class Slime(Node):
    image = None
    time = 60
    hp = random.randint(30, 60)
    angle = 0
    base = None
    speed = 1.5

    def __init__(self, x, y, base):
        Node.__init__(self, "slime")
        self.base = base
        self.x = x
        self.y = y
        dist_y = base.y - self.y
        dist_x = base.x - self.x
        self.angle = math.atan2(dist_y, dist_x)
        self.frame_x = math.floor(self.width / 4)

    def update(self):
        self.time += 1

        if not self.inWith(50, self.base):
            self.x += math.cos(self.angle) * self.speed
            self.y += math.sin(self.angle) * self.speed

        if self.time < 30:
            if self.image == Director.asset["slime"] and random.randint(0, 3) == 1:
                self.image = Director.asset['slime_red']
            else:
                self.image = Director.asset['slime']
        else:
            self.image = Director.asset['slime']

        self.frame = (self.frame + 0.1) % 4

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)

    def set_red(self):
        self.time = 0
