import entity
from init_assets import *

class generateDoor():
    def __init__(self, x, y, destination_x, destination_y, img):
        self.x = x
        self.y = y
        self.destination_x = destination_x
        self.destination_y = destination_y
        self.width = 32
        self.height = 32
        self.img = img

    def warp(self):
        window.render(self.img, (self.x,self.y))
        if entity.player.x > self.x and entity.player.x < self.x + self.width:
            if entity.player.y > self.y and entity.player.y < self.y + self.height:
                entity.player.x = self.destination_x
                entity.player.y = self.destination_y
                print(1)