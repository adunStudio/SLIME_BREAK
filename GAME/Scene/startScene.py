from pico2d import *
from Framework.ADUN import Director, Scene
from Scene.titleScene import TitleScene


class StartScene(Scene):
    core = None
    image = None
    time = 60 * 5

    def enter(self):
        self.image = Director.asset['kpu_credit']

    def exit(self):
        del self.image

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        pass

    def update(self):
        self.time -= 1

        if self.time <= 0:
            self.time = 60 * 2
            Director.push_scene(TitleScene())

    def draw(self):
        self.image.draw(400, 300)
