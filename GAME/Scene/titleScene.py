from pico2d import *
from Framework.ADUN import Director, Scene
from Scene.gameScene import GameScene


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
            if event.type == SDL_KEYDOWN:
                Director.change_scene(GameScene())

    def update(self):

        pass

    def draw(self):
        self.image.draw(400, 300)
