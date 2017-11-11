from abc import *
from Framework.core import Director
import math


class Node(metaclass=ABCMeta):
    level = None
    image = None
    red_image = None
    direction = None
    frameEx = 0
    speed = 0

    x, y = (0, 0)
    width, height = (0, 0)
    half_width, half_height = (0, 0)
    frame = 0
    frame_x = 0

    def __init__(self, name):
        self.level = Director.level[name]
        self.init()

    def init(self):
        if self.level["red_image"]:
            self.red_image = Director.asset[self.level["red_image"]]

        if self.level["direction"]:
            self.direction = self.level["direction"]

        if self.direction is not None:
            self.image = Director.asset[self.level["image"] + "_" + self.direction[0]]
        else:
            self.image = Director.asset[self.level["image"]]

        self.x = self.level["x"]
        self.y = self.level["y"]

        self.frameEx = self.level["frameEx"]

        self.speed = self.level["speed"]

        self.width = self.image.w
        self.height = self.image.h
        self.half_width = self.width / 2
        self.half_height = self.height / 2

        self.frame_x =  math.floor(self.width / self.frameEx)

    @abstractmethod
    def update(self, frame_time):
        pass

    @abstractmethod
    def draw(self):
        pass

    def set_direction_image(self, angle):
        if self.direction is not None:
            self.image = Director.asset[self.level["image"] + "_" + self.direction[int(angle)]]

    # AABB 방식
    def intersect(self, node):
        left_a, bottom_a, right_a, top_a = (self.x - self.width / self.frameEx / 2, self.y - self.half_height, self.x + self.width / self.frameEx / 2, self.y + self.half_height)
        left_b, bottom_b, right_b, top_b = (node.x - node.width / node.frameEx / 2, node.y - node.half_height, node.x + node.width / node.frameEx / 2, node.y + self.half_height)

        if left_a > right_b:
            return False
        if right_a < left_b:
            return False
        if top_a < bottom_b:
            return False
        if bottom_a > top_b:
            return False

        return True

    # Circle 방식
    def inWith(self, r, node):
        dist = math.sqrt(math.pow(self.x - node.x, 2) + math.pow(self.y - node.y, 2))
        return dist <= r