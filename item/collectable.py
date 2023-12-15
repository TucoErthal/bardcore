from item.init_assets import *
from item.obj import GameObject

 
collectables = []


class Collectable(GameObject):
    def __init__(self, x, y):
        x = x
        y = y

        self.sprite = heart1

        self.x = x
        self.y = y

        self.w = self.sprite.get_rect().width
        self.h = self.sprite.get_rect().height

        self.collidable = True
        self.drawable = True

    def draw(self, player = 0):
        if self.drawable:
            window.render(self.sprite, (self.x, self.y))

        self.update(player)

    def update(self, player = 0):
        if player == 0:
            return
        if self.collided(player):
            player.heal()
            heal_sfx.play()
            self.collidable = False
            self.drawable = False
