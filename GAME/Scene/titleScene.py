from pico2d import *
from framework import ADUN
from Scene import gameScene


class Scene(ADUN.Scene):
    core = None
    image = None
    time = 60 * 2

    def __init__(self, core):
        self.core = core

    def enter(self):
        self.image = load_image("Asset/title.png")

    def exit(self):
        del self.image

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):

        for event in events:
            if event.type == SDL_QUIT:
                self.core.quit()
            else:
                if event.type == SDL_KEYDOWN:
                    self.core.change_scene(gameScene.Scene(self.core))

    def update(self):
        pass

    def draw(self):
        clear_canvas()
        self.image.draw(400, 300)
        update_canvas()
