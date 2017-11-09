import json
from pico2d import *
from Framework.core import Director
from Scene.startScene import StartScene

image_data_file = open("./json/image.json", "r")
level_data_file = open("./json/level.json", "r")

open_canvas(Director.window_width, Director.window_height)

Director.show_cursor(True)
Director.show_lattice(True)

Director.pre_image_load(json.load(image_data_file))
Director.pre_level_load(json.load(level_data_file))
image_data_file.close()
level_data_file.close()

Director.set_fps(100)

Director.run(StartScene())

close_canvas()
