from pico2d import *


class Core:
    __instnace = None

    window_width = 16 * 80
    window_height = 9 * 80
    mouse_x, mouse_y = (0, 0)
    current_time = 0
    frame_time = 0
    CURSOR = True
    LATTICE = True
    fps = 60
    running = None
    stack = None
    asset = {}
    level = {}
    mouse = None
    events = None
    INPUT =\
    {
        "LEFT": False,
        "RIGHT": False,
        "UP": False,
        "DOWN": False,
        "LEFT_CLICK": False,
        "RIGHT_CLICK": False,
        "ESC": False,
        "1": False,
        "2": False,
        "3": False,
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
        self.current_time = get_time()
        self.running = True
        self.stack = [scene]

        scene.enter()

        while self.running:

            self.frame_time = get_time() - self.current_time
            self.current_time += self.frame_time

            self.events = get_events()
            self.handle_events(self.events)
            self.stack[-1].handle_events(self.events)

            self.stack[-1].update(self.frame_time)

            clear_canvas()
            self.stack[-1].draw()
            if self.mouse is not None:
                self.mouse.update()
                self.mouse.draw()
            update_canvas()

        while len(self.stack) > 0:
            self.stack[-1].exit()
            self.stack.pop()

    def pre_image_load(self, assets):
        for name in assets:
            self.asset[name] = load_image("Asset/" + name + ".png")

    def pre_level_load(self, data):
        for name in data:
            self.level[name] = data[name]

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
                elif event.key == SDLK_DOWN or event.key == SDLK_ESCAPE:
                    self.INPUT["ESC"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_DOWN or event.key == SDLK_1:
                    self.INPUT["1"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_DOWN or event.key == SDLK_2:
                    self.INPUT["2"] = (event.type == SDL_KEYDOWN)
                elif event.key == SDLK_DOWN or event.key == SDLK_3:
                    self.INPUT["3"] = (event.type == SDL_KEYDOWN)

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

    def get_current_scene(self):
        return self.stack[-1]

    def get_prev_scene(self):
        if len(self.stack) > 2:
            return self.stack[-2]

        return None

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


# Singleton Object
Director = Core()
