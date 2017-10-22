from Framework.ADUN import Director, Node


class Mouse(Node):
    pointer = None

    def __init__(self):
        Node.__init__(self, "mouse_pointer")
        self.pointer = Director.asset["mouse_pointer"]
        self.attack = Director.asset["mouse_attack"]
        self.attack_red = Director.asset["mouse_attack_red"]

    def update(self):
        self.x, self.y = (Director.get_mouse_x(), Director.get_mouse_y())

    def draw(self):
        if self.image == self.pointer:
            self.image.draw(self.x + self.half_width, self.y - self.half_height)
        else:
            self.image.draw(self.x, self.y)

    def set_type(self, type):
        switch_case = {
            "pointer": self.pointer,
            "attack": self.attack,
            "attack_red": self.attack_red
        }
        self.image = switch_case[type]