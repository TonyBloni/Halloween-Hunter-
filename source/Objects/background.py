import pygame

from PyGE.Objects.ObjectBase import ObjectBase
from PyGE.Screens.Room import Room
from PyGE.Globals.Cache import get_image
from PyGE.Misc.AlarmClock import AlarmClock
import PyGE.utils as utils


class Background(ObjectBase):
    def __init__(self, screen:pygame.Surface, args: dict, parent:'Room'):
        ObjectBase.__init__(self, screen, args, parent)

        
        self.image = get_image("background")       


    def draw(self):
        self.draw_to_screen(self.image)

   