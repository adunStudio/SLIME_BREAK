from pico2d import *
from abc import *

class Core:
    __instnace = None

    window_width = 16 * 80
    window_height = 9 * 80
    mouse_x, mouse_y = (0, 0)
    CURSOR = True
    LATTICE = True
    fps = 60
    running = None
    stack = None
    asset = {}
    mouse = None
    events = None
    INPUT =\
    {
        "LEFT": False,
        "RIGHT": False,
        "UP": False,
        "DOWN": False,
        "LEFT_CLICK": False,
        "RIGHT_CLICK": False
    }

    @staticmethod
    def getInstnace():
        if Core.__instnace is not None:
            Core()
        return Core.__instnace

    def __init__(self):
        if Core.__instnace is not None:
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
            if self.mouse is not None:
                self.mouse.update()
                self.mouse.draw()
            update_canvas()
            delay(1 / self.fps)

        while len(self.stack) > 0:
            self.stack[-1].exit()
            self.stack.pop()

    def pre_load(self, assets):
        for name in assets:
            self.asset[name] = load_image("Asset/" + name + ".png")

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.x, self.window_height - event.y

            if event.type == SDL_MOUSEBUTTONDOWN or event.type == SDL_MOUSEBUTTONUP:
                if event.button == SDL_BUTTON_LEFT:
                    self.INPUT["LEFT_CLICK"] = (event.type == SDL_MOUSEBUTTONDOWN)
                elif event.button == SDL_BUTTON_RIGHT:
                    self.INPUT["RIGHT_CLICK"] = (event.type == SDL_MOUSEBUTTONDOWN)

            if event.type == SDL_QUIT:
                Director.quit()

            if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT or event.key == SDLK_d:
                    self.INPUT["RIGHT"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_LEFT or event.key == SDLK_a:
                    self.INPUT["LEFT"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_UP or event.key == SDLK_w:
                    self.INPUT["UP"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_DOWN or event.key == SDLK_s:
                    self.INPUT["DOWN"] = (event.type == SDL_KEYDOWN)

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def set_mouse(self, mouse):
        if self.mouse is None:
            self.mouse = mouse

    def set_mouse_type(self, type):
        if self.mouse is not None:
            self.mouse.set_type(type)

    def show_cursor(self, show):
        if show:
            show_cursor()
        else:
            hide_cursor()

        self.CURSOR = show

    def show_lattice(self, show):
        if show:
            show_lattice()
        else:
            hide_lattice()

        self.LATTICE = show

    def set_fps(self, fps):
        self.fps = fps


class Scene(metaclass=ABCMeta):

    image = None

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
    half_width, half_height = (0, 0)
    frame = 0
    frame_x = 1
    frame_Ex = 1

    def __init__(self, image_name, frame_Ex = 1):
        self.image = Director.asset[image_name]
        self.init(frame_Ex)


    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def init(self, frame_Ex):
        self.width = self.image.w
        self.height = self.image.h
        self.half_width = self.width / 2
        self.half_height = self.height / 2
        self.frame_Ex = frame_Ex

    # AABB 방식
    def intersect(self, node):
        left_a, bottom_a, right_a, top_a = (self.x - self.width / self.frame_Ex / 2, self.y - self.half_height, self.x + self.width / self.frame_Ex / 2, self.y + self.half_height)
        left_b, bottom_b, right_b, top_b = (node.x - node.width / node.frame_Ex / 2, node.y - node.half_height, node.x + node.width / node.frame_Ex / 2, node.y + self.half_height)

        if left_a > right_b:
            return False
        if right_a < left_b:
            return False
        if top_a < bottom_b:
            return False
        if bottom_a > top_b:
            return False

        return True

    # Circle 방식
    def inWith(self, r, node):
        dist = math.sqrt(math.pow(self.x - node.x, 2) + math.pow(self.y - node.y, 2))
        return dist <= r



Director = Core()
