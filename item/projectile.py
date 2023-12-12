import math

from item.init_assets import projectile_sprite
from item.init_assets import window

class Projectile:
    def __init__(self, x, y, w, h, speed, angle, lifetime):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.curr_sprite = projectile_sprite

        self.center_x = self.x + self.w/2
        self.center_y = self.y + self.h/2
        self.speed = speed
        self.angle = angle
        self.lifetime = lifetime

        self.direction = (math.cos(self.angle), math.sin(self.angle))

    def draw(self):
        window.render(self.curr_sprite, (self.x, self.y))

    def update(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def check_collision(self, target):
        if self.x > target.x and self.x < target.x + target.w:
            if self.y > target.y and self.y < target.y + target.h:
                target.get_hit()
                self.lifetime = 0
                return 1
            
    def check_wall_collision(self, room):
        if self.x < room.x1:
            self.lifetime = 0
            return 1
            
        if self.x > room.x2:
            self.lifetime = 0
            return 1
            
        if self.y < room.y1:
            self.lifetime = 0
            return 1
        
        if self.y > room.y2:
            self.lifetime = 0
            return 1