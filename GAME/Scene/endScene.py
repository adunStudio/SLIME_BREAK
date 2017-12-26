from pico2d import *
from Framework.ADUN import Director
import Scene.titleScene2




class EndScene():

    time = 60 * 2.5
    font = None
    score = 0
    name = ""

    def __init__(self, score):
        self.score = score
        self.font = load_font("Asset/ENCR10B.TTF", 32 * 5)
        self.font2 = load_font("Asset/ENCR10B.TTF", 32 * 3)


    def enter(self):
        Director.set_mouse_type("pointer")
        self.image = Director.asset['basebreak']

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self, events):

        for event in events:
            if event.type == SDL_KEYDOWN:
                asc = event.key
                print(asc)
                if asc:
                    if asc == 13 and len(self.name) >= 3:
                        pass
                        #Director.pop_scene()
                        #Director.change_scene(Scene.titleScene.TitleScene())
                        Director.push_scene(Scene.titleScene2.TitleScene())
                        #Director.pop_scene()

                    elif(asc == 8 and len(self.name) >= 1):

                        self.name = self.name[:-1]
                    elif(((48<=asc and asc <= 57) or (97 <= asc and asc <= 122))  and len(self.name) <= 8):
                        self.name += str(chr(event.key) )

        pass

    def update(self):
        self.time -= 1

        if self.time <= 0:
            self.time = 60 * 2.5

            #Director.push_scene(TitleScene())

    def draw(self):
        self.image.draw(Director.window_width / 2, Director.window_height / 2)
        self.font.draw(700, 340, str(self.score), (0, 0, 0))
        self.font2.draw(700, 180, str(self.name), (100, 255, 0))
