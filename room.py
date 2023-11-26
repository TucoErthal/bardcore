import entity
import init_assets

class generateRoom():
    def __init__(self, room_img, x, y):
        self.room_img = room_img

        self.width = self.room_img.get_rect().width
        self.height = self.room_img.get_rect().height
        
        self.x = x
        self.y = y

        self.x1 = 32 + self.x
        self.y1 = 84 + self.y
        self.x2 = self.width - 32 + self.x
        self.y2 = self.height - 32 + self.y


    def collision_check(self):
        if entity.player.x <= self.x1:
            entity.player.x = self.x1
            
        if entity.player.x > self.x2:
            entity.player.x = self.x2
            
        if entity.player.y < self.y1:
            entity.player.y = self.y1
        
        if entity.player.y > self.y2:
            entity.player.y = self.y2

    def change_frame(self, new_frame):
        self.room_img = new_frame
    
    def draw_room(self):
        init_assets.window.render(self.room_img,(self.x,self.y))