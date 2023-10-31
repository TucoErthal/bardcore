import math

class Projectile:
    def __init__(self, x, y, w, h, speed, angle, lifetime):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.center_x = self.x + self.w/2
        self.center_y = self.y + self.h/2
        self.speed = speed
        self.angle = angle
        self.lifetime = lifetime

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def check_collision(self, target):
        print(1)
        if self.x > target.x and self.x < target.x + target.w:
            if self.y > target.y and self.y < target.y + target.h:
                target.get_hit()
                return 1
