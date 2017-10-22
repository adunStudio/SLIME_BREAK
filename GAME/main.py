from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene
from Object.mouse import Mouse

open_canvas(Director.window_width, Director.window_height)

Director.show_cursor(False)
Director.show_lattice(False)

Director.pre_load([
    "character", "character_left", "character_right",
    "character_down", "character_down_left", "character_down_right",
    "character_up", "character_up_left", "character_up_right",
    "mg_left", "mg_right",
    "mg_down", "mg_down_left", "mg_down_right",
    "mg_up", "mg_up_left", "mg_up_right",
    "mouse_pointer", "mouse_attack", "mouse_attack_red",
    "bullet", "explode1", "explode2", "shockwave",
    "slime", "slime_red", "slime_break",
    "base", "crystal",
    "kpu_credit", "title"])

Director.set_mouse(Mouse())

Director.set_fps(80)

Director.run(StartScene())

close_canvas()
