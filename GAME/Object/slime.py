from Framework.ADUN import Director, Node
import random
import math


class Slime(Node):
    image = None
    explode_mode = False
    time = 60
    hp = random.randint(30, 60)
    angle = 0
    base = None
    speed = 1.5

    def __init__(self, x, y, base):
        Node.__init__(self, "slime", 4)
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
        else:
            if not self.explode_mode:
                self.set_explode()

        if self.time < 30:
            if not self.explode_mode:
                if self.image == Director.asset["slime"] and random.randint(0, 3) == 1:
                    self.image = Director.asset['slime_red']
                else:
                    self.image = Director.asset['slime']
            else:
                if self.image == Director.asset["slime_explode"] and random.randint(0, 3) == 1:
                    self.image = Director.asset['slime_explode_red']
                else:
                    self.image = Director.asset['slime_explode']
        else:
            if not self.explode_mode:
                self.image = Director.asset['slime']
            else:
                self.image = Director.asset['slime_explode']

        if not self.explode_mode:
            self.frame = (self.frame + 0.1) % 4
        else:
            self.frame = (self.frame + 0.15) % 9

    def draw(self):
        if not self.explode_mode:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y + 20)

    def set_red(self):
        self.time = 0

    def set_explode(self):
        self.image = Director.asset["slime_explode"]
        self.explode_mode = True
        self.frame = 0
        self.init(8)
        self.frame_x = math.floor(self.width / 8)
        #self.y += 20
        #self.x += 1
