import pygame
import random

from PyGE.Objects.ObjectBase import ObjectBase
from PyGE.Objects.Text import Text
from PyGE.Screens.Room import Room
from PyGE.Globals.Cache import get_image
from PyGE.Misc.AlarmClock import AlarmClock
import PyGE.utils as utils
import source.GlobalVariable as GlobalVariable


class EnemyHandler(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent:'Room'):
        args["@x"], args["@y"] = (-10, -10)
        ObjectBase.__init__(self, screen, args, parent)

        self.spawn_countdown = AlarmClock(1)
        self.spawn_countdown.start()
        self.difficulty_timer = AlarmClock(1)
        self.difficulty_timer.start()

    def oncreate(self):
        GlobalVariable.score = 0
        GlobalVariable.wave = 1

    def update(self, pressed_keys):
        if self.spawn_countdown.finished:
            self.spawn_countdown.restart()
            self.add_object("Enemy", {}, -31, random.randint(0, self.screen.get_height() - 32))
            if self.difficulty_timer.finished:
                self.difficulty_timer.restart()
                self.spawn_countdown = AlarmClock(1 - GlobalVariable.wave/18)
                self.spawn_countdown.start()
                if GlobalVariable.wave < 15:
                    GlobalVariable.wave += 1
                    print(GlobalVariable.wave)



class Enemy(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent:'Room'):
        ObjectBase.__init__(self, screen, args, parent)

        self.image = get_image("enemy")
        self.drawable = self.image

        self.w, self.h = self.image.get_size()

        self.angle = 0

        self.drawable = self.rotate_object(self.image, self.angle)
        self.velocity = 100 + GlobalVariable.wave*5

        self.scoreboard = self.get_all_type("Text")[0]     # type: Text

        self.screen_c_w, self.screen_c_h = utils.get_surface_center(self.screen)

    def update(self, pressed_keys):
        self.move_angle_time(self.velocity)

    def oncollide(self, obj:'ObjectBase'):
        if obj.object_type == "Bullet":
            self.delete(self)
            self.delete(obj)

            self.change_score(100)

    def onscreenleave(self):
        self.delete(self)
        self.change_room("gameover")

    def draw(self):
        self.draw_to_screen(item=self.drawable)

    def change_score(self, delta:int):
        GlobalVariable.score += delta
        self.scoreboard.set_text("Score: {}".format(GlobalVariable.score))
