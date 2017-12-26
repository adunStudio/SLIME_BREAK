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
from Object.redslime import RedSlime
from Object.item import Item
from Object.cannontower import CannonTower
from Object.flametower import FlameTower
from Object.map import Map

import random


class GameScene(Scene):
    time = 0
    monsters = []
    bullets = []
    explodes = []
    waves = []
    coins = []
    menus = []
    items = []
    towers = []
    map1 = None
    map2 = None

    player = None
    base = None
    selected_item = None

    mode = ""
    ATTACK_MODE = "attack_mode"
    CREATE_MODE = "create_mode"

    score = 0
    score_font = None

    def enter(self):
        self.score_font = load_font("Asset/ENCR10B.TTF", 32)
        self.map1 = Map("json/map1.json")
        self.map2 = Map("json/map2.json")
        Director.set_mouse_type("attack")
        Director.sounds['bgm'].set_volume(64)
        Director.sounds['bgm'].repeat_play()
        self.base = Base(Director.window_width / 2, Director.window_height - 200)
        self.player = Character()
        self.player.set_gun(Gun(self.player.x, self.player.y))
        self.menus.append(CannonTower(50, 80))
        self.menus.append(FlameTower(150, 83))
        for menu in self.menus:
            self.items.append(Item(menu.name, menu.money))
        self.mode = self.ATTACK_MODE

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):
        if Director.INPUT["LEFT_CLICK"]:
            if self.mode == self.ATTACK_MODE and self.player.enable_shot():
                Director.sounds['shot'].set_volume(32)
                Director.sounds['shot'].play(1)
                self.bullets.append(Bullet(self.player.x, self.player.y))

            elif self.mode == self.CREATE_MODE and self.selected_item.able:
                if self.selected_item.name == "cannon":
                    self.towers.append(CannonTower(self.selected_item.x, self.selected_item.y))
                if self.selected_item.name == "flame":
                    self.towers.append(FlameTower(self.selected_item.x, self.selected_item.y))
                self.player.money -= self.selected_item.money
                self.selected_item = None
                self.mode = self.ATTACK_MODE

        for i in ["1", "2"]:
            if Director.INPUT[i]:
                if self.player.money >= self.items[int(i) - 1].money:
                    self.mode = self.CREATE_MODE
                    self.selected_item = self.items[int(i) - 1]

        if Director.INPUT["ESC"] or Director.INPUT["RIGHT_CLICK"]:
            self.mode = self.ATTACK_MODE

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

        if self.mode == self.CREATE_MODE:
            self.selected_item.update(self.base, self.towers)

        self.base.update()

        self.check_mouse_type()

        self.bullet_update()

        self.explode_update()

        self.wave_update()

        self.coin_update()

        self.tower_update()

        self.player.update()

        self.monster_update()

        self.item_update()

    def draw(self):

        self.map1.draw()

        for tower in self.towers:
            tower.draw()

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

        for menu in self.menus:
            menu.draw()

        if self.mode == self.CREATE_MODE:
            self.selected_item.draw()

        self.score_font.draw(1050, 700, "Score: " + str(self.score), (0, 0, 0))

    def add_monster(self):
        r = random.randint (0, 4)

        if random.randint(0, 10) > 3:
            if r == 0:  # 왼쪽
                self.monsters.append(Slime(-10, random.randint(0, Director.window_height), self.base))
            elif r == 1:  # 오른쪽
                self.monsters.append(Slime(Director.window_width, random.randint(0, Director.window_height), self.base))
            else:  # 아래
                self.monsters.append(Slime(random.randint(0, Director.window_width), -10, self.base))
        else:
            if r == 0:  # 왼쪽
                self.monsters.append(RedSlime(-10, random.randint(0, Director.window_height), self.base))
            elif r == 1:  # 오른쪽
                self.monsters.append(RedSlime(Director.window_width, random.randint(0, Director.window_height), self.base))
            else:  # 아래
                self.monsters.append(RedSlime(random.randint(0, Director.window_width), -10, self.base))



    def check_mouse_type(self):
        for monster in self.monsters:
            if monster.intersect(Director.mouse):
                Director.set_mouse_type("attack_red")

        if self.mode == self.CREATE_MODE:
            Director.set_mouse_type("pointer")

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
                    monster.hp -= bullet.damage
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

            if bullet.x < 0 or Director.window_width < bullet.x or bullet.y < 0 or Director.window_height < bullet.y:
                self.bullets.remove(bullet)

    def explode_update(self):
        for explode in self.explodes:
            explode.update()
            if explode.time < 0:
                self.explodes.remove(explode)
                if(explode.type == 'explode1'):
                    Director.sounds['slime_explosion'].play(1)
                    self.base.hp -= 10

    def monster_update(self):
        for monster in self.monsters:
            monster.update()
            if monster.hp <= 0:
                self.monsters.remove(monster)
                Director.sounds['slime_death'].play(1)
                self.waves.append(Shockwave(monster.x, monster.y))
                if not monster.explode_mode and random.randint(1, 10) >= 4:
                    self.coins.append(Coin(monster.x, monster.y))
                else:
                    self.score += 10

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

            if coin.inWith(70, self.player):
                coin.go_to(self.player)

            if coin.inWith(3, self.player):
                self.coins.remove(coin)
                self.player.money += coin.money
                Director.sounds['coin'].play(1)

    def item_update(self):
        for menu in self.menus:
            menu.check_by_able(self.player.money)

    def tower_update(self):
        for tower in self.towers:
            if tower.void_monster(self.monsters):
                for monster in self.monsters:
                    tower.set_monster(monster)
            tower.update()
            if tower.enable_shot():
                #self.bullets.append(tower.get_bullet())
                self.bullets.append(Bullet(tower.x, tower.y + 20, tower.angle, tower.bullet, tower.damage))








