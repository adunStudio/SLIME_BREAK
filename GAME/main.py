from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene

open_canvas()

Director.pre_load(["3_south", "3_north", "3_side", "3_diagdown", "3_diagup", "slime", "kpu_credit", "title", "mouse_pointer"])

Director.run(StartScene())

close_canvas()
