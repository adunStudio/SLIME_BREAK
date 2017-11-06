from pico2d import *
from Framework.ADUN import Director, Scene
from Scene.titleScene import TitleScene

class PauseScene(Scene):
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
        if Director.INPUT["LEFT_CLICK"]:
            Director.pop_scene()
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(Director.window_width / 2, Director.window_height / 2)
