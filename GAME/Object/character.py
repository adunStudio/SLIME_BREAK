from Framework.ADUN import Director, Node
import math


class Character(Node):
    image = None
    speed = 1
    mouse_angle = 0
    see_angle = 0

    def __init__(self):
        Node.__init__(self, "character_down")
        self.x = 50
        self.y = 50
        self.frame_x = int(self.width / 4)
        print(self.frame_x)

    def update(self):
        dist_y = Director.get_mouse_y() - self.y
        dist_x = Director.get_mouse_x() - self.x
        self.mouse_angle = math.atan2(dist_y, dist_x) * (180 / math.pi) + 180
        self.see_angle = ((self.mouse_angle + 22.5) / 45) % 8
        self.set_direction(int(self.see_angle))

    def draw(self):
        self.image.clip_draw(self.frame * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)

    def set_direction(self, angle):
        switch_case = {
            0: Director.asset["character_left"],
            1: Director.asset["character_down_left"],
            2: Director.asset["character_down"],
            3: Director.asset["character_down_right"],
            4: Director.asset["character_right"],
            5: Director.asset["character_up_right"],
            6: Director.asset["character_up"],
            7: Director.asset["character_up_left"],
        }
        self.image = switch_case[angle]



