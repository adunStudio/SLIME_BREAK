from Framework.ADUN import Director, Node


class Base(Node):
    def __init__(self, x, y):
        Node.__init__(self, "base")
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def set_red(self):
        pass

