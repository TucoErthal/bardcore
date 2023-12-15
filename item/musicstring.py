from item.init_assets import *
from item.entity import *

class String():
    def __init__(self, x, y):
        self.x = x * 16
        self.y = y * 16
        self.counter = 0
        self.string_img = string_img

        self.timer = 0
        self.string_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent


    def draw(self):
        self.counter += 1

        if self.counter == 10:
            self.y += 1
        elif self.counter == 20:
            self.y += 2
        elif self.counter == 30:
            self.y += 1
        elif self.counter == 40:
            self.y -= 1
        elif self.counter == 50:
            self.y -= 2
        elif self.counter == 60:
            self.y -= 1
            self.counter = 0

        window.render(self.string_img, (self.x, self.y))

        if player.x+16 > self.x and player.x+16 < self.x + 32:
            if player.y+8 > self.y and player.y+8 < self.y + 32:
                player.can_control = False
                self.transition_frame = transparent

                if self.string_delay == False:
                    self.timer = pygame.time.get_ticks()
                    string_sfx.play()
                    self.string_delay = True
                    self.transition_counter = 120

                
        else:
            self.warp = False

        if self.transition_counter == 0:
            self.string_delay = False

        if self.transition_counter > 0:
            self.transition_counter -= 1

        if self.string_delay == True and pygame.time.get_ticks() - self.timer >= 500:
            if self.transition_counter > 100:
                pass
            elif self.transition_counter > 90:
                self.transition_frame = trans1
            elif self.transition_counter > 80:
                self.transition_frame = trans2
            elif self.transition_counter > 70:
                self.string_img = transparent
                self.transition_frame = trans3
            elif self.transition_counter > 30:
                self.transition_frame = trans4
            elif self.transition_counter > 20:
                self.transition_frame = trans3
            elif self.transition_counter > 10:
                self.transition_frame = trans2
            elif self.transition_counter > 0:
                self.transition_frame = trans1        
                player.can_control = True

    def transition(self):
        if self.string_delay == True:
            window.render(self.transition_frame,(item.entity.player.x-660, item.entity.player.y-500))