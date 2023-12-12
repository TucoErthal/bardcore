from item.entity import *
from item.timer import *
from item.obj import *

from item.init_assets import boss_idle1
from item.init_assets import boss_Impact
from item.init_assets import boss_PreJump
from item.init_assets import boss_Jump
from item.init_assets import boss_Shadow

from item.init_assets import window
from item.sprite import Sprite


FOLLOW = 0
ATTACK = 1


class Boss(Enemy):
    def __init__(self, x, y):
        x = x*16
        y = y*16

        self.spt_idle1      = Sprite(boss_idle1,    x, y)
        self.spt_dmg1       = Sprite(boss_idle1,    x, y)

        self.curr_sprite = self.spt_idle1

        super().__init__(self.curr_sprite.get_sprite(), self.spt_dmg1.get_sprite(), x, y, 50, 10)
        
        self.spt_Impact     = Sprite(boss_Impact,   x, y)
        self.spt_PreJump    = Sprite(boss_PreJump,  x, y)
        self.spt_Jump       = Sprite(boss_Jump,     x, y)
        self.spt_Shadow     = Sprite(boss_Shadow,   x, y-(2*16))

        self.w = self.spt_idle1.w
        self.h = self.spt_idle1.h


        self.collidable = True

        self.state = FOLLOW

        self.attackTimer = Timer(3)


    def draw(self):
        self.curr_sprite.draw()

    def update(self):
        super().update()

    
