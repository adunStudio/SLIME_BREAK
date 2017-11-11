from pico2d import *
from Framework.core import Director
from Framework.scene import Scene
from Object.player import Player


class BattleScene(Scene):
    time = 0

    player = None

    def enter(self):
        self.player = Player()
        pass

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

        self.player.update(frame_time)

        pass

    def draw(self):
        self.player.draw()
