from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene

open_canvas(Director.window_width, Director.window_height)

Director.pre_load([
    "character", "character_left", "character_right",
    "character_down", "character_down_left", "character_down_right",
    "character_up", "character_up_left", "character_up_right",
    "slime", "kpu_credit", "title", "mouse_pointer"])

Director.run(StartScene())

close_canvas()
