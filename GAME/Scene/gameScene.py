from pico2d import *
from framework import ADUN
from Monster import slime


class Scene(ADUN.Scene):
    core = None
    monsters = []

    def __init__(self, core):
        self.core = core

    def enter(self):
        for i in range(11):
            self.monsters.append(slime.Slime())

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_QUIT:
                self.core.quit()

    def update(self):

        for monster in self.monsters:
            monster.update()

    def draw(self):
        clear_canvas()

        for monster in self.monsters:
            monster.draw()

        update_canvas()
