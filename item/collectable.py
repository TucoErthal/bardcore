from item.init_assets import *
from item.obj import GameObject

 
collectables = []


class Collectable(GameObject):
    def __init__(self, x, y):
        x = x*16
        y = y*16

        self.sprite = heart1

        self.x = x
        self.y = y

        self.w = self.sprite.get_rect().width
        self.h = self.sprite.get_rect().height

        self.collidable = True
        self.drawable = True

    def draw(self):
        if self.drawable:
            window.render(self.sprite, (self.x, self.y))

        self.update()

    def update(self):
        if self.collided(player):
            player.heal()
            self.collidable = False
            self.drawable = False
