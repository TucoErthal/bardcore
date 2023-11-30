import math
import item.obj
from item.init_assets import *
from item.timer import Timer


class Entity(item.obj.GameObject):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        super().__init__(x, y, w, h)

        self.immuneTimer = Timer()
        self.immuneTimer.max_time = 5

        self.hurt = 0
        self.hp = 0

    def draw(self, sprite):
        window.render(sprite, (self.x, self.y))

    def get_hit(self): # Mudar nome
        if self.immuneTimer.ringing():
            self.hurt = 5
            self.hp -= 1
        print("aaaaaaah osso doi :(")
        print(self.hp)

class Player(Entity):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        super().__init__(x, y, w, h)
        self.hp = 10

        self.player_sprite_left = item.init_assets.player_sprite_left
        self.player_sprite_right = item.init_assets.player_sprite_right
        self.player_sprite_down = item.init_assets.player_sprite_down
        self.player_sprite_up = item.init_assets.player_sprite_up

        self.curr_sprite = self.player_sprite_down
        self.can_control = True

        self.w = self.curr_sprite.get_rect().width
        self.h = self.curr_sprite.get_rect().height

    def input(self, current_keys):
        if self.can_control:
            if current_keys[pygame.K_s]:
                self.y += 1
                self.curr_sprite = self.player_sprite_down
            
            if current_keys[pygame.K_w]:
                self.y -= 1
                self.curr_sprite = self.player_sprite_up
                
            if current_keys[pygame.K_d]:
                self.x += 1
                self.curr_sprite = self.player_sprite_right
            
            if current_keys[pygame.K_a]:
                self.x -= 1
                self.curr_sprite = self.player_sprite_left

    def draw(self):
        super().draw(self.curr_sprite)



player = Player(624, 496, 16, 16)


# DO NOT TOUCH
# When creating new enemies, go to enemylist.py
# When initializing enemies, go to their specific room!

class Enemy(Entity):
        def __init__(self, sprite, dmg_sprite, dead_sprite, x, y, speed, hp):
            super().__init__()
            self.x = x
            self.y = y

            self.sprite = sprite
            self.dmg_sprite = dmg_sprite
            self.dead_sprite = dead_sprite

            self.w = self.sprite.get_rect().width
            self.h = self.sprite.get_rect().height

            self.speed = speed
            self.follow_distance = 50
            self.hurt = 0
            self.hp = hp

            self.dead_time = 120

        def follow(self):
            self.sin = (player.y - self.y)
            self.cos = (player.x - self.x)
            self.angle = math.atan2(self.sin, self.cos)
            
            distance = math.sqrt(self.sin**2 + self.cos**2)
            if distance > self.follow_distance:
                self.move()
        
        def move(self):
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)


        def update(self):
            self.follow()

            if self.collided(player):
                player.get_hit()

        def draw(self):
            if self.hp > 0:    
                if self.hurt > 0:
                    window.render(self.dmg_sprite, (self.x, self.y))
                    self.hurt -= 1
                else:
                    window.render(self.sprite, (self.x, self.y))
            else:
                self.dead_time -=1

                if self.dead_time == 45:
                    explode_sfx.play()

                if self.dead_time > 20:
                    window.render(self.dead_sprite, (self.x, self.y))
                elif self.dead_time > 15:
                    window.render(explosion_sprite_1, (self.x,self.y))
                elif self.dead_time > 10:
                    window.render(explosion_sprite_2, (self.x,self.y))
                elif self.dead_time > 5:
                    window.render(explosion_sprite_3, (self.x,self.y))
                else:
                    window.render(explosion_sprite_4, (self.x,self.y))