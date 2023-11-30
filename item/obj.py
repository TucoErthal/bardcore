class GameObject():
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    def collided(self, obj):
        from . import collision
        
        return collision.Collision.collided(self, obj)