import math
import obj
import pygame
player = obj.GameObject(0, 0)


class Enemy():
        def __init__(self, sprite, dmg_sprite, dead_sprite, x, y, w = 32, h = 32, speed = 10, hp = 30):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

            self.sprite = sprite
            self.dmg_sprite = dmg_sprite
            self.dead_sprite = dead_sprite

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
            self.hurt = 30
            self.hp -= 1