from Framework.ADUN import Director, Node
import math


class Character(Node):
    image = None
    speed = 3
    max_cool_time = Director.fps / 6
    cool_time = 0
    angle = 0
    mouse_angle = 0
    see_angle = 0
    gun = None

    def __init__(self):
        Node.__init__(self, "character_down", 4)
        self.x = 50
        self.y = 50
        self.frame_x = math.floor(self.width / 4)

    def update(self):
        if self.cool_time < self.max_cool_time:
            self.cool_time += 1

        dist_y = Director.get_mouse_y() - self.y
        dist_x = Director.get_mouse_x() - self.x
        self.angle = math.atan2(dist_y, dist_x)
        self.mouse_angle = self.angle * (180 / math.pi) + 180
        self.see_angle = ((self.mouse_angle + 22.5) / 45) % 8
        self.set_direction(int(self.see_angle))

        self.frame = (self.frame + 0.1) % 4

        if self.gun is not None:
            self.gun.x = self.x
            self.gun.y = self.y
            self.gun.set_direction(int(self.see_angle))

    def draw(self):
        if int(self.see_angle) == 6 or int(self.see_angle) == 7 or int(self.see_angle) == 5:
            self.gun.draw()
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * self.frame_x, 0, self.frame_x, self.height, self.x, self.y)
            self.gun.draw()

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

    def set_gun(self, gun):
        self.gun = gun

    def enable_shot(self):
        if self.cool_time == self.max_cool_time:
            self.cool_time = 0
            return True
        else:
            return False


