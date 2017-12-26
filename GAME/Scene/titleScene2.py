from pico2d import *
from Framework.ADUN import Director, Scene
from Scene.gameScene2 import GameScene


class TitleScene(Scene):
    def enter(self):
        self.image = Director.asset["title"]

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = event.y
                if 500 <= x and x <= 750:
                    if 470 <= y and y <= 570:
                        b = GameScene()
                        Director.change_scene(b)

    def update(self):
        pass

    def draw(self):
        self.image.draw(Director.window_width / 2, Director.window_height / 2)
