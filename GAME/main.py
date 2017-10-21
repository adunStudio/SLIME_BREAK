from pico2d import *
from Framework.ADUN import Director
from Scene.startScene import StartScene

open_canvas()

Director.pre_load(["character", "slime", "kpu_credit", "title", "mouse_pointer"])

Director.run(StartScene())

close_canvas()
