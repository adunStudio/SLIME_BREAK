import json
from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene
from Object.mouse import Mouse

image_data_file = open("./json/image.json", "r")
sound_data_file = open("./json/sound.json", "r")

open_canvas(Director.window_width, Director.window_height)

Director.show_cursor(False)
Director.show_lattice(True)

Director.pre_load(json.load(image_data_file))
Director.pre_sound_load(json.load(sound_data_file))

image_data_file.close()
sound_data_file.close()

Director.set_mouse(Mouse())

Director.set_fps(130)

Director.run(StartScene())

close_canvas()
