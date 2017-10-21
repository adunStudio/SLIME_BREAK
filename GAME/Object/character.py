from Framework.ADUN import Director, Node
import random


class Character(Node):
    image = None

    def __init__(self):
        Node.__init__(self, "character")
        self.x = 50
        self.y = 50

    def update(self):
        self.randomMove()

    def draw(self):
        self.image.clip_draw(self.frame * self.width, 0, self.width, self.height, self.x, self.y)

    def randomMove(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
