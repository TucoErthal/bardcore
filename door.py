import entity
from init_assets import *

class generateDoor():
    def __init__(self, x, y, destination_x, destination_y, img1, img2):
        self.x = x
        self.y = y
        self.destination_x = destination_x
        self.destination_y = destination_y
        self.width = 32
        self.height = 32
        self.img1 = img1
        self.img2 = img2
        self.current_img = self.img1
        self.timer = 0
        self.door_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent

    def warp(self):

        window.render(self.current_img, (self.x,self.y))

        if entity.player.x+8 > self.x and entity.player.x+8 < self.x + self.width:
            if entity.player.y+8 > self.y and entity.player.y+8 < self.y + self.height:
                entity.player.x = self.x + 8
                entity.player.y = self.y + 12
                self.transition_frame = transparent

                if self.door_delay == False:
                    self.current_img = self.img2
                    self.timer = pygame.time.get_ticks()
                    self.door_delay = True
                    self.transition_counter = 120

                if self.transition_counter < 60:
                    entity.player.x = self.destination_x
                    entity.player.y = self.destination_y
                    self.current_img = self.img1
                
        if self.transition_counter == 0:
            self.door_delay = False

        if self.transition_counter > 0:
            self.transition_counter -= 1

        if self.door_delay == True and pygame.time.get_ticks() - self.timer >= 500:
            if self.transition_counter > 100:
                pass
            elif self.transition_counter > 90:
                self.transition_frame = trans1
            elif self.transition_counter > 80:
                self.transition_frame = trans2
            elif self.transition_counter > 70:
                self.transition_frame = trans3
            elif self.transition_counter > 30:
                self.transition_frame = trans4
            elif self.transition_counter > 20:
                self.transition_frame = trans3
            elif self.transition_counter > 10:
                self.transition_frame = trans2
            elif self.transition_counter > 0:
                self.transition_frame = trans1

