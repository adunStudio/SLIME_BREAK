from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene
from Object.mouse import Mouse

open_canvas(Director.window_width, Director.window_height)

Director.show_cursor(False)
Director.show_lattice(True)

Director.pre_load([
    "character", "character_left", "character_right",
    "character_down", "character_down_left", "character_down_right",
    "character_up", "character_up_left", "character_up_right",
    "mg_left", "mg_right",
    "mg_down", "mg_down_left", "mg_down_right",
    "mg_up", "mg_up_left", "mg_up_right",
    "cannon_left", "cannon_right", "cannon_disable",
    "cannon_down", "cannon_down_left", "cannon_down_right",
    "cannon_up", "cannon_up_left", "cannon_up_right",
    "flame_left", "flame_right", "flame_disable",
    "flame_down", "flame_down_left", "flame_down_right",
    "flame_up", "flame_up_left", "flame_up_right",
    "mouse_pointer", "mouse_attack", "mouse_attack_red",
    "bullet", "explode1", "explode2", "shockwave",
    "slime", "slime_red", "slime_break", "slime_explode", "slime_explode_red",
    "base", "crystal",
    "coin",
    "kpu_credit", "title"])

Director.set_mouse(Mouse())

Director.set_fps(100)

Director.run(StartScene())

close_canvas()
