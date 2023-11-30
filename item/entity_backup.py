import math
import item.obj
from item.init_assets import *
player = item.obj.GameObject(624, 496, 16, 16)

# DO NOT TOUCH
# When creating new enemies, go to enemylist.py
# When initializing enemies, go to their specific room!



class Enemy():
        def __init__(self, sprite, dmg_sprite, dead_sprite, x, y, speed, hp):
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

        def get_hit(self): # Mudar nome 
            self.hurt = 5
            self.hp -= 1

        def draw(self): # Função adicionada
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
                
                    

