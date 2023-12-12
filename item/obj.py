class GameObject():
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.collidable = True


    def collided(self, obj):
        from . import collision
        
        if self.collidable:
            return collision.Collision.collided(self, obj)
        
        return False