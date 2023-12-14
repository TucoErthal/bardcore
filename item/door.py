import item.entity
from item.init_assets import *


# HOW TO USE:
# door_name = item.door.Door(args) -> initialize (do so on itemlist.py)
# door_name.draw()                 -> draw door on map (must be under player)
# door_name.transition()           -> transition animation (must be over everything)

# 1 = UP, 2 = LEFT, 3 = RIGHT, 4 = DOWN

class Door():
    def __init__(self, x, y, direction, current_id, target_room, door_type = 'lock'):
        self.x = x * 16
        self.y = y * 16
        self.door_type = door_type

        if direction == 1:
            self.destination_x = 0
            self.destination_y = -16*12
            self.img1 = door_sprite
            self.img2 = door_open_sprite
            self.img3 = door_lock_sprite

        elif direction == 2:
            self.destination_x = -16*9
            self.destination_y = 0
            self.img1 = door_left_sprite
            self.img2 = door_left_open_sprite
            self.img3 = door_left_lock_sprite
            
        elif direction == 3:
            self.destination_x = 16*9
            self.destination_y = 0
            self.img1 = door_right_sprite
            self.img2 = door_right_open_sprite
            self.img3 = door_right_lock_sprite

        else:
            self.destination_x = 0
            self.destination_y = 16*12
            self.img1 = door_down_sprite
            self.img2 = door_down_open_sprite
            self.img3 = door_down_lock_sprite





        self.width = 32
        self.height = 32
        self.current_img = self.img1
        self.timer = 0
        self.door_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent
        self.target_room = target_room
        self.current_id = current_id

    def draw(self, room_id, unlock_method = []):

        self.unlock_method = unlock_method

        if self.door_type == 'lock':
            self.current_img = self.img3
            if len(self.unlock_method) == 0:
                self.door_type = 'unlocked'
                self.current_img = self.img1
        elif self.door_type == 'string':
            self.current_img = self.img3
            if len(self.unlock_method) == 2:
                self.door_type = 'unlocked'
                self.current_img = self.img1

        if room_id == self.current_id:
            window.render(self.current_img, (self.x, self.y))

        if self.door_type == 'unlocked':
            if item.entity.player.x+16 > self.x and item.entity.player.x+16 < self.x + self.width:
                if item.entity.player.y+8 > self.y and item.entity.player.y+8 < self.y + self.height:
                    item.entity.player.can_control = False
                    self.transition_frame = transparent

                    if self.door_delay == False:
                        self.current_img = self.img2
                        self.timer = pygame.time.get_ticks()
                        door_sfx.play()
                        self.door_delay = True
                        self.transition_counter = 120

                    if self.transition_counter < 60:
                        item.entity.player.x += self.destination_x
                        item.entity.player.y += self.destination_y
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
            window.render(self.transition_frame,(item.entity.player.x-660, item.entity.player.y-500))