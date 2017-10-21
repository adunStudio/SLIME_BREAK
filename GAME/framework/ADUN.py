from pico2d import *
from abc import *


class Core:
    running = None
    stack = None

    def push_scene(self, scene):
        if len(self.stack) > 0:
            self.stack[-1].pause()

        self.stack.append(scene)
        scene.enter()

    def pop_scene(self):
        if len(self.stack) > 0:
            self.stack[-1].exit()
            self.stack.pop()

        if len(self.stack) > 0:
            self.stack[-1].resume()

    def change_scene(self, scene):
        self.pop_scene()
        self.stack.append(scene)
        scene.enter()

    def quit(self):
        self.running = False

    def run(self, scene):
        self.running = True
        self.stack = [scene]

        scene.enter()

        while self.running:
            self.stack[-1].handle_events(get_events())
            self.stack[-1].update()
            self.stack[-1].draw()

        while len(self.stack) > 0:
            self.stack[-1].exit()
            self.stack.pop()


class Scene(metaclass=ABCMeta):

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Node(metaclass=ABCMeta):
    x, y = (0, 0)
    width, height = (0, 0)
    frame = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass