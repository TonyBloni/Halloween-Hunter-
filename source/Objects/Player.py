import pygame

from PyGE.Objects.ObjectBase import ObjectBase
from PyGE.Screens.Room import Room
from PyGE.Globals.Cache import get_image
from PyGE.Misc.AlarmClock import AlarmClock
import PyGE.utils as utils


class Player(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent:'Room'):
        ObjectBase.__init__(self, screen, args, parent)

        self.angle = 90
        self.velocity = 300

        self.number = self.get_mandatory_arguement("number", int)

        self.image = self.rotate_object(get_image("player{}".format(self.number)))

        self.w, self.h = self.image.get_size()

        self.shot_cool_down = AlarmClock(0.125)
        self.shot_cool_down.start()

    @property
    def bullet_y(self):
        return self.y + (self.h / 2)
    
    def oncollide(self, obj: 'ObjectBase'):
        if obj.object_type =="Enemy":
            self.change_room("gameover")

    def draw(self):
        self.draw_to_screen(self.image)

    def update(self, pressed_keys):
        # print(len(self.siblings))

        if (pressed_keys[pygame.K_w] == 1 and self.number == 1) or (pressed_keys[pygame.K_UP] == 1 and self.number == 2):
            self.time_move(0, self.velocity)
            self.boundary_check()

        if (pressed_keys[pygame.K_s] == 1 and self.number == 1) or (pressed_keys[pygame.K_DOWN] == 1 and self.number == 2):
            self.time_move(0, -self.velocity)
            self.boundary_check()
        
        #COPY THIS
        if (pressed_keys[pygame.K_a] == 1 and self.number == 1) or (pressed_keys[pygame.K_LEFT] == 1 and self.number == 2):
            self.time_move(-self.velocity, 0)
            if self.x >= self.screen_w-self.w or self.x <= 0:
                self.undo_last_move()

        if (pressed_keys[pygame.K_d] == 1 and self.number == 1) or (pressed_keys[pygame.K_RIGHT] == 1 and self.number == 2):
            self.time_move(self.velocity, 0)
            if self.x >= self.screen_w-self.w or self.x <= 0:
                self.undo_last_move()
        #TO THIS

        if (self.shot_cool_down.finished) and (pressed_keys[pygame.K_SPACE] == 1):
                self.add_object("Bullet", {"angle": self.angle + 90}, x=self.x, y=self.bullet_y)
                self.shot_cool_down.restart()

    def boundary_check(self):
        if not utils.rect_a_in_b(self.rect, self.screen.get_rect()):
            self.undo_last_move()

    def onkeydown(self, unicode, key, modifier, scancode):
        if key == 27:
            self.change_room("menu")