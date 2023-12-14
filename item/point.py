"""A Point class"""

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, target):
        dif = self.sub(target)

        return (dif.x**2 + dif.y**2)**0.5

    def sub(self, other):
        p = Point(self.x, self.y)
        p.x -= other.x
        p.y -= other.y

        return p


    def add(self, other):
        p = Point(self.x, self.y)
        p.x += other.x
        p.y += other.y

        return p

    def mult(self, other):
        p = Point(self.x, self.y)

        p.x *= other
        p.y *= other

        return p

    def __str__(self):
        return f'({round(self.x, 2)}, {round(self.y, 2)}) '

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
