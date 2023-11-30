import item.entity
from item.init_assets import *


# HOW TO USE:
# door_name = item.door.Door(args) -> initialize (do so on itemlist.py)
# door_name.draw()                 -> draw door on map (must be under player)
# door_name.transition()           -> transition animation (must be over everything)


class Door():
    def __init__(self, x, y, destination_x, destination_y, img1, img2, current_id, target_room):
        self.x = x * 16
        self.y = y * 16
        self.destination_x = destination_x * 16
        self.destination_y = destination_y * 16
        self.width = 32
        self.height = 32
        self.img1 = img1
        self.img2 = img2
        self.current_img = self.img1
        self.timer = 0
        self.door_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent
        self.target_room = target_room
        self.current_id = current_id

    def draw(self):
        window.render(self.current_img, (self.x,self.y))

        if item.entity.player.x+8 > self.x and item.entity.player.x+8 < self.x + self.width:
            if item.entity.player.y+8 > self.y and item.entity.player.y+8 < self.y + self.height:
                item.entity.player.can_control = False
                self.transition_frame = transparent

                if self.door_delay == False:
                    self.current_img = self.img2
                    self.timer = pygame.time.get_ticks()
                    self.door_delay = True
                    self.transition_counter = 120

                if self.transition_counter < 60:
                    item.entity.player.x = self.destination_x
                    item.entity.player.y = self.destination_y
                    self.current_img = self.img1
        else:
            self.warp = False


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
                item.entity.player.can_control = True

    def transition(self):
        if self.door_delay == True:
            window.render(self.transition_frame,(item.entity.player.x-330, item.entity.player.y-250))