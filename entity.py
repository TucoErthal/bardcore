import math
import obj
player = obj.GameObject(64, 64, 16, 16)


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

        def get_hit(self):
            self.hurt = 5
            self.hp -= 1