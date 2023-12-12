from item.obj import *

from item.init_assets import window

import pygame

class Sprite(GameObject):
    def __init__(self, asset, x = 0, y = 0):
        super().__init__()

        self.image = asset

        self.x = x
        self.y = y

        self.w = self.image.get_rect().width
        self.h = self.image.get_rect().height

        self.collidable = True



    def draw(self):
        window.render(self.image, (self.x, self.y))

    def get_sprite(self):
        return self.image