from Framework.ADUN import Director, Node
from pico2d import *
import random


class Item(Node):
    name = ""
    money = 0
    able = False

    def __init__(self, name, money):
        Node.__init__(self, name + "_able")
        self.name = name
        self.money = money

    def update(self, base, towers):
        self.x = Director.get_mouse_x()
        self.y = Director.get_mouse_y()
        self.able = True
        self.image = Director.asset[self.name + "_able"]

        for tower in towers:
            if self.intersect(tower):
                self.able = False
                self.image = Director.asset[self.name + "_disable"]

        if self.intersect(base):
            self.able = False
            self.image = Director.asset[self.name + "_disable"]

    def draw(self):
        self.image.draw(self.x, self.y)

    def check_create_able(self, tower):
        pass




