from abc import *
from Framework.core import Director
import math


class Node(metaclass=ABCMeta):
    level = None
    image = None
    red_image = None

    x, y = (0, 0)
    width, height = (0, 0)
    half_width, half_height = (0, 0)
    frame = 0
    frame_x = 1
    frameEx = 1

    def __init__(self, name):
        self.level = Director.level[name]
        self.init()

    def init(self):
        self.image = self.level["image"]

        if self.level["red_image"] :
            self.red_image = self.level["red_image"]

        self.width = self.image.w
        self.height = self.image.h
        self.half_width = self.width / 2
        self.half_height = self.height / 2




    @abstractmethod
    def update(self, frame_time):
        pass

    @abstractmethod
    def draw(self):
        pass


    # AABB 방식
    def intersect(self, node):
        left_a, bottom_a, right_a, top_a = (self.x - self.width / self.frame_Ex / 2, self.y - self.half_height, self.x + self.width / self.frame_Ex / 2, self.y + self.half_height)
        left_b, bottom_b, right_b, top_b = (node.x - node.width / node.frame_Ex / 2, node.y - node.half_height, node.x + node.width / node.frame_Ex / 2, node.y + self.half_height)

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