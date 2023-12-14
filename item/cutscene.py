from item.init_assets import *
from item.entity import *

class Cutscene():
    def __init__(self):
        self.counter = 0
        self.timer = 0
        self.scene_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent
        self.in_room = 1

    def logic(self):
        if self.in_room == 1:
            if self.counter < 120:
                self.counter += 1

            if self.counter == 120:
                self.transition_frame = transparent

                if self.scene_delay == False:
                    self.timer = pygame.time.get_ticks()
                    self.scene_delay = True
                    self.transition_counter = 180

                if self.transition_counter < 60:
                    player.x = 66*16
                    player.y = 175*16
            else:
                self.warp = False

            if self.transition_counter == 0:
                self.scene_delay = False

            if self.transition_counter > 0:
                self.transition_counter -= 1

            if self.scene_delay == True and pygame.time.get_ticks() - self.timer >= 500:
                if self.transition_counter > 160:
                    pass
                elif self.transition_counter > 150:
                    self.transition_frame = trans1
                elif self.transition_counter > 140:
                    self.transition_frame = trans2
                elif self.transition_counter > 130:
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
                elif self.transition_counter == 0:
                    self.in_room = 0
                if self.transition_counter == 110:
                    cell_explosion_sfx.play()


    def transition(self):
        if self.scene_delay == True:
            window.render(self.transition_frame,(item.entity.player.x-660, item.entity.player.y-500))
        