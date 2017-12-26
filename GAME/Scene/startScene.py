from pico2d import *
from Framework.ADUN import Director, Scene
from Scene.titleScene import TitleScene
from Scene.gameScene import GameScene

class StartScene(Scene):
    time = 60 * 2.5

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

    def update(self):
        self.time -= 1

        if self.time <= 0:
            self.time = 60 * 2.5
            Director.push_scene(TitleScene())

    def draw(self):
        self.image.draw(Director.window_width / 2, Director.window_height / 2)
