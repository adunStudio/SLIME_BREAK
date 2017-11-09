from pico2d import *
from Framework.core import Director
from Framework.scene import Scene
from Scene.titleScene import TitleScene


class StartScene(Scene):
    time = 0

    def enter(self):
        self.image = Director.asset['kpu_credit']

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        pass

    def update(self, frame_time):
        self.time += frame_time

        if self.time >= 3:
            Director.push_scene(TitleScene())

    def draw(self):
        self.image.draw(Director.window_width / 2, Director.window_height / 2)
