from item.point import *
from item.timer import *

class Path():
    def __init__(self, x, y):
        self.cords = Point(x, y)

        self.timer = Timer()
        self.timer.start()

        self.cords_List = [self.cords]
        self.curr_index = 0
        self.max_index = 0

        self.target = self.cords
        self.origin = self.cords

        self.frac = self.cords.dist(self.target)
        self.spd = 100


    def get_cords(self):
        return self.cords.x, self.cords.y

    def get_x(self):
        return self.cords.x
        
    def get_y(self):
        return self.cords.y

    def addCord(self, cord: Point):
        self.cords_List.append(cord)
        self.max_index += 1
        

    @staticmethod
    def interpolate_2d(origin: Point, destiny: Point, franc):
        if franc > 1:
            franc = 1

        dif = destiny.sub(origin)
        dif = dif.mult(franc)

        resp = origin.add(dif)

        return resp

    def setTarget(self, targ: Point):
        self.target = targ
        self.frac = self.cords.dist(self.target)

    def update(self):
        if self.target != self.cords:
            try:
                self.cords = self.interpolate_2d(self.origin, self.target, (self.timer.get_time()*self.spd)/self.frac)
            except:
                self.cords = self.interpolate_2d(self.origin, self.target, 1)
        else:
            self.timer.restart()
            self.setTarget(self.cords_List[self.curr_index])
            self.origin = self.cords
            if self.curr_index < self.max_index:
                self.curr_index += 1
            else:
                self.curr_index = 0
            print(f'New target: {self.target}')
        print(self.cords)


        