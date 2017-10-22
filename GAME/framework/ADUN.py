from pico2d import *
from abc import *

class Core:
    __instnace = None

    window_width = 16 * 80
    window_height = 9 * 80
    running = None
    stack = None
    asset = {}
    mouse = None
    events = None
    KEYBOARD =\
    {
        "LEFT": False,
        "RIGHT": False,
        "UP": False,
        "DOWN": False
    }

    @staticmethod
    def getInstnace():
        if Core.__instnace == None:
            Core()
        return Core.__instnace

    def __init__(self):
        if Core.__instnace != None:
            raise Exception("this class is a singleton!")
        else:
            Core.__instnace == self

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
        if self.mouse is None:
            self.mouse = Mouse()

        self.running = True
        self.stack = [scene]

        scene.enter()

        while self.running:
            self.events = get_events()
            self.handle_events(self.events)
            self.stack[-1].handle_events(self.events)
            self.stack[-1].update()
            clear_canvas()
            self.stack[-1].draw()
            self.mouse.draw()
            update_canvas()

        while len(self.stack) > 0:
            self.stack[-1].exit()
            self.stack.pop()

    def pre_load(self, assets):
        for name in assets:
            self.asset[name] = load_image("Asset/" + name + ".png")

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.mouse.x, self.mouse.y = event.x, self.window_height - event.y

            if event.type == SDL_QUIT:
                Director.quit()

            if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT or event.key == SDLK_d:
                    self.KEYBOARD["RIGHT"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_LEFT or event.key == SDLK_a:
                    self.KEYBOARD["LEFT"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_UP or event.key == SDLK_w:
                    self.KEYBOARD["UP"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_DOWN or event.key == SDLK_s:
                    self.KEYBOARD["DOWN"] = (event.type == SDL_KEYDOWN)

    def get_mouse_x(self):
        return self.mouse.x

    def get_mouse_y(self):
        return self.mouse.y


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
    image = None
    x, y = (0, 0)
    width, height = (0, 0)
    frame = 0
    frame_x = 0

    def __init__(self, image_name):
        self.image = Director.asset[image_name]
        self.width = self.image.w
        self.height = self.image.h

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Mouse(Node):
    image = None
    x, y = (0, 0)
    pointer = None

    def __init__(self):
        Node.__init__(self, "mouse_pointer")
        self.pointer = Director.asset["mouse_pointer"]

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
    pass

Director = Core()
