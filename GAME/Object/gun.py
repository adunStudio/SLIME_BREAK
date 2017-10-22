from Framework.ADUN import Director, Node


class Gun(Node):
    see_angle = 0

    def __init__(self, x, y):
        Node.__init__(self, "mg_down")
        self.x = x
        self.y = y

    def update(self):
      pass

    def draw(self):
        angle = self.see_angle

        # right
        if angle == 4:
            self.image.draw(self.x + 10, self.y - self.half_height / 2 - 7)
        # left
        if angle == 0:
            self.image.draw(self.x - 10, self.y - self.half_height / 2 - 7)
        # down
        if angle == 2:
            self.image.draw(self.x, self.y - self.half_height / 2 - 10)
        # up
        if angle == 6:
            self.image.draw(self.x, self.y + self.half_height / 2 + 5)
        # down_left
        if angle == 1:
            self.image.draw(self.x - 10, self.y - self.half_height / 2 - 6)
        # down_right
        if angle == 3:
            self.image.draw(self.x + 10, self.y - self.half_height / 2 - 6)
        # up_left
        if angle == 7:
            self.image.draw(self.x - 5, self.y - self.half_height / 2)
        # up_right
        if angle == 5:
            self.image.draw(self.x + 5, self.y - self.half_height / 2)

    def set_direction(self, angle):
        self.see_angle = angle

        switch_case = {
            0: Director.asset["mg_left"],
            1: Director.asset["mg_down_left"],
            2: Director.asset["mg_down"],
            3: Director.asset["mg_down_right"],
            4: Director.asset["mg_right"],
            5: Director.asset["mg_up_right"],
            6: Director.asset["mg_up"],
            7: Director.asset["mg_up_left"],
        }
        self.image = switch_case[angle]


