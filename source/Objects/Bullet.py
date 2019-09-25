import pygame

from PyGE.Objects.ObjectBase import ObjectBase
from PyGE.Screens.Room import Room
from PyGE.Globals.Cache import get_image

class Bullet(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent:'Room'):
        ObjectBase.__init__(self, screen, args, parent)
        self.angle = self.get_mandatory_arguement("angle", float)
        self.velocity = self.get_optional_arguement("velocity", 400, float)
        
        self.image = get_image("bullet") 

    def draw(self):
        self.draw_to_screen(self.image)

    def update(self, pressed_keys):
        self.move_angle_time(self.velocity)

    def onscreenleave(self):
        self.delete(self)