from pico2d import *
from framework import ADUN
from Scene import titleScene


class Scene(ADUN.Scene):
    core = None
    image = None
    time = 60 * 5

    def __init__(self, core):
        self.core = core

    def enter(self):
        open_canvas()
        self.image = load_image("Asset/kpu_credit.png")

    def exit(self):
        close_canvas()
        del self.image

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):

        for event in events:
            if event.type == SDL_QUIT:
                self.core.quit()

    def update(self):
        self.time -= 1

        if self.time <= 0:
            self.time = 60 * 2
            self.core.push_scene(titleScene.Scene(self.core))

    def draw(self):
        clear_canvas()
        self.image.draw(400, 300)
        update_canvas()
