from pico2d import *

from Framework.ADUN import Director, Scene
from Object.character import Character
from Object.gun import Gun
from Object.bullet import Bullet
from Object.slime import Slime


class GameScene(Scene):
    monsters = []
    bullets = []
    player = None

    def enter(self):
        Director.set_mouse_type("attack")

        for i in range(11):
            self.monsters.append(Slime())

        self.player = Character()
        self.player.set_gun(Gun(self.player.x, self.player.y))

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        if Director.INPUT["LEFT_CLICK"]:
            print(3)
            self.bullets.append(Bullet(self.player.x, self.player.y))

        if Director.INPUT["LEFT"]:
            self.player.x -= self.player.speed

        if Director.INPUT["RIGHT"]:
            self.player.x += self.player.speed

        if Director.INPUT["UP"]:
            self.player.y += self.player.speed

        if Director.INPUT["DOWN"]:
            self.player.y -= self.player.speed


        pass

    def update(self):
        Director.set_mouse_type("attack")
        for monster in self.monsters:
            if monster.intersect(Director.mouse):
                Director.set_mouse_type("attack_red")

        self.player.update()

        for monster in self.monsters:
            monster.update()

    def draw(self):
        for monster in self.monsters:
            monster.draw()

        for bullet in self.bullets:
            bullet.draw()

        self.player.draw()

