import math

class Projectile:
    def __init__(self, x, y, speed, angle, lifetime):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.lifetime = lifetime

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)