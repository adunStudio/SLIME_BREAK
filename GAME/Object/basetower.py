from Framework.ADUN import Director, Node
from pico2d import *
import random


class BaseTower(Node):
    money = 0
    name = ""
    angle = 0;
    see_angle = 0
    monster = None
    range = 160
    max_cool_time = 0
    cool_time = 0

    def __init__(self, name, money, range=160, max_cool_time = Director.fps / 3):
        Node.__init__(self, name + "_right")
        self.name = name
        self.money = money
        self.range = range
        self.max_cool_time = max_cool_time

    def update(self):
        if self.cool_time < self.max_cool_time:
            self.cool_time += 1

        if self.monster is not None:
            dist_y = self.monster.y - self.y
            dist_x = self.monster.x - self.x
            self.angle = math.atan2(dist_y, dist_x)
            self.see_angle = int((((self.angle * (180 / math.pi) + 180) + 22.5) / 45) % 8)
            self.set_direction(self.see_angle)

    def draw(self):
        self.image.draw(self.x, self.y)

    def void_monster(self, monsters):
        if self.monster is None:
            return True
        if not self.inWith(self.range, self.monster):
            self.monster = None
            return True
        if self.monster not in monsters:
            self.monster = None
            return True

        return False

    def check_by_able(self, money):
        if money >= self.money:
            self.image = Director.asset[self.name + "_right"]
        else:
            self.image = Director.asset[self.name + "_by_disable"]

    def set_monster(self, monster):
        if self.inWith(self.range, monster):
            self.monster = monster

    def set_direction(self, angle):
        switch_case = {
            0: Director.asset[self.name + "_left"],
            1: Director.asset[self.name + "_down_left"],
            2: Director.asset[self.name + "_down"],
            3: Director.asset[self.name + "_down_right"],
            4: Director.asset[self.name + "_right"],
            5: Director.asset[self.name + "_up_right"],
            6: Director.asset[self.name + "_up"],
            7: Director.asset[self.name + "_up_left"],
        }
        self.image = switch_case[angle]

    def enable_shot(self):
        if self.monster is not None and self.cool_time == self.max_cool_time:
            self.cool_time = 0
            return True
        else:
            return False




