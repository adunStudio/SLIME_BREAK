from pico2d import *

from Framework.ADUN import Director, Scene
from Object.character import Character
from Object.slime import Slime


class GameScene(Scene):
    monsters = []
    player = None

    def enter(self):

        for i in range(11):
            self.monsters.append(Slime())

        self.player = Character()

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        if Director.KEYBOARD["LEFT"]:
            self.player.x -= self.player.speed

        if Director.KEYBOARD["RIGHT"]:
            self.player.x += self.player.speed

        if Director.KEYBOARD["UP"]:
            self.player.y += self.player.speed

        if Director.KEYBOARD["DOWN"]:
            self.player.y -= self.player.speed


        pass

    def update(self):

        self.player.update()

        for monster in self.monsters:
            monster.update()

    def draw(self):
        for monster in self.monsters:
            monster.draw()

        self.player.draw()

