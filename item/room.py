import item.entity
from item.init_assets import *


# HOW TO USE:
# room_name = item.room.Room(args) -> initialize (do so on itemlist.py)
# room_name.draw()                 -> draws the room and checks collisions (must be under player)



class Room():
    def __init__(self, room_img, x, y, room_id):
        self.room_img = room_img

        self.width = self.room_img.get_rect().width
        self.height = self.room_img.get_rect().height
        
        self.x = x * 16
        self.y = y * 16

        self.x1 = 32 + self.x
        self.y1 = 84 + self.y
        self.x2 = self.width - 47 + self.x
        self.y2 = self.height - 47 + self.y
        self.id = room_id


    def draw(self):
        window.render(self.room_img,(self.x,self.y))
        if item.entity.player.x <= self.x1:
            item.entity.player.x = self.x1
            
        if item.entity.player.x > self.x2:
            item.entity.player.x = self.x2
            
        if item.entity.player.y < self.y1:
            item.entity.player.y = self.y1
        
        if item.entity.player.y > self.y2:
            item.entity.player.y = self.y2