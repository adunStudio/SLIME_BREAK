from pico2d import *

from Framework.ADUN import Director, Scene
from Object.character import Character
from Object.base import Base
from Object.gun import Gun
from Object.bullet import Bullet
from Object.explode import Explode
from Object.shockwave import Shockwave
from Object.coin import Coin
from Object.slime import Slime
import random


class GameScene(Scene):
    time = 0
    monsters = []
    bullets = []
    explodes = []
    waves = []
    coins = []
    player = None
    base = None

    def enter(self):
        Director.set_mouse_type("attack")
        self.base = Base(Director.window_width / 2, Director.window_height - 200)
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
            if self.player.enable_shot():
                self.bullets.append(Bullet(self.player.x, self.player.y))

        if Director.INPUT["LEFT"]:
            self.player.x -= self.player.speed

        if Director.INPUT["RIGHT"]:
            self.player.x += self.player.speed

        if Director.INPUT["UP"]:
            self.player.y += self.player.speed

        if Director.INPUT["DOWN"]:
            self.player.y -= self.player.speed

    def update(self):
        self.time += 1
        Director.set_mouse_type("attack")

        if self.time > 60 * 2:
            self.add_monster()
            self.time = 0

        self.base.update()

        self.check_mouse_attack()

        self.bullet_update()

        self.explode_update()

        self.wave_update()

        self.coin_update()

        self.player.update()

        self.monster_update()

    def draw(self):
        self.base.draw()



        for monster in self.monsters:
            monster.draw()

        for bullet in self.bullets:
            bullet.draw()

        for explode in self.explodes:
            explode.draw()

        for wave in self.waves:
            wave.draw()

        self.player.draw()

        for coin in self.coins:
            coin.draw()

    def add_monster(self):
        self.monsters.append(Slime(random.randint(0, Director.window_width), random.randint(0, Director.window_height), self.base))

    def check_mouse_attack(self):
        for monster in self.monsters:
            if monster.intersect(Director.mouse):
                Director.set_mouse_type("attack_red")

    def bullet_update(self):
        for bullet in self.bullets:
            bullet.update()

            for monster in self.monsters:
                r = 25
                if monster.explode_mode:
                    r = 50

                if monster.inWith(r, bullet):
                    self.explodes.append(Explode(bullet.x, bullet.y, "2", 30))
                    monster.set_red()
                    monster.hp -= self.player.gun.damage
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

            if bullet.x < 0 or Director.window_width < bullet.x or bullet.y < 0 or Director.window_height < bullet.y:
                self.bullets.remove(bullet)

    def explode_update(self):
        for explode in self.explodes:
            explode.update()
            if explode.time < 0:
                self.explodes.remove(explode)

    def monster_update(self):
        for monster in self.monsters:
            monster.update()
            if monster.hp <= 0:
                self.monsters.remove(monster)
                self.waves.append(Shockwave(monster.x, monster.y))
                if not monster.explode_mode and random.randint(1, 10) >= 4:
                    self.coins.append(Coin(monster.x, monster.y))

            if monster.frame >= 8 and monster in self.monsters:
                self.monsters.remove(monster)
                #base.hp -=
                self.explodes.append(Explode(monster.x, monster.y, "1", 30))

    def wave_update(self):
        for wave in self.waves:
            wave.update()
            if wave.frame >= 9:
                self.waves.remove(wave)

    def coin_update(self):
        for coin in self.coins:
            coin.update()

            if coin.intersect(self.player):
                coin.go_to(self.player)

            if coin.inWith(3, self.player):
                self.coins.remove(coin)
                #self.player.money += coin.money








