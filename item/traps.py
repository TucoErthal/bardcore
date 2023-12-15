import item.entity
from item.init_assets import *

from item.obj import GameObject
from item.timer import Timer
from item.projectile import *


UP = 'u'
RIGHT = 'r'
DOWN = 'd'
LEFT = 'l'
player = item.entity.player





# Atiram no ritimo da musica
# Sprites sao place holder
#update dentro de draw para consistencia com o resto do codigo
class wallTrap(GameObject):
    def __init__(self, x, y, dire = RIGHT):
        super().__init__()
        
        self.x = x*16
        self.y = y*16

        self.direction = dire

        self.tiros = []

        self.current_frame_on_beat = 0


        self.tiroCadence = Timer(0.2)

        if self.direction == UP:
            self.curr_sprite = templeTrap_U
        elif self.direction == LEFT:
            self.curr_sprite = templeTrap_L
        elif self.direction == DOWN:
            self.curr_sprite = templeTrap_D
        elif self.direction == RIGHT:
            self.curr_sprite = templeTrap_R

        self.w = self.curr_sprite.get_rect().width
        self.h = self.curr_sprite.get_rect().height

        tiro_w = enemyBall.get_rect().width
        tiro_h = enemyBall.get_rect().height

        self.tiro_spawn = (self.x+((self.w-tiro_w)/2), self.y+((self.h-tiro_h)/2))

    def draw(self, room = -1):

        for t in self.tiros:
            t.draw()

        window.render(self.curr_sprite, (self.x, self.y))
        self.update(room)
        

    def update(self, room = -1):
        self.last_frame_on_beat = self.current_frame_on_beat
        self.current_frame_on_beat = soundtrack.is_on_beat()

        if self.tiroCadence.ringing() and (self.current_frame_on_beat and not(self.last_frame_on_beat)):
            self.fire()
            self.tiroCadence.restart()

        if room == -1:
            return
        
        for t in self.tiros:
            t.update()
            t.check_collision(item.entity.player)
            t.check_wall_collision(room)

            if t.lifetime <= 0:
                self.tiros.remove(t)

    def fire(self):        
        if self.direction == UP:
            angle = 1.5708 # 90°
        elif self.direction == LEFT:
            angle = 0
        elif self.direction == DOWN:
            angle = 4.71239 # 270° 
        elif self.direction == RIGHT:
            angle = 3.14159 # 180°

        tiro = Projectile(self.tiro_spawn[0]-2, self.tiro_spawn[1]-2, 2.5, angle, 200)

        if self.direction == UP:
            tiro.curr_sprite = fireball_D
        elif self.direction == LEFT:
            tiro.curr_sprite = fireball_R
        elif self.direction == DOWN:
            tiro.curr_sprite = fireball_U
        elif self.direction == RIGHT:
            tiro.curr_sprite = fireball_L

        self.tiros.append(tiro)
        fireball_sfx.play()

class spikeTrap(GameObject):
    def __init__(self, x, y):
        super().__init__()

        self.img_0 = item.init_assets.spike_trap_0
        self.img_1 = item.init_assets.spike_trap_1

        self.curr_sprite = self.img_0

        self.x = x*16
        self.gy = y*16              # for draw fuction
        self.y = self.gy+16         # for the collided fuction
        self.w = self.img_0.get_rect().width
        self.h = self.img_0.get_rect().height/2

        self.animationTimer = Timer(1)

    def draw(self):
        window.render(self.curr_sprite, (self.x, self.gy))
        self.update()

    def update(self):
        if self.animationTimer.ringing():
            if self.curr_sprite != self.img_0:
                self.curr_sprite = self.img_0
                
            if player.x+8 > self.x and player.x+8 < self.x+32:
                if player.y+8 > self.y and player.y+8 < self.y+16:
                    self.curr_sprite = self.img_1
                    player.get_hit()
                    self.animationTimer.restart()
            

# 1 = UP, 2 = LEFT, 3 = RIGHT, 4 = DOWN
class conveyorBelt():
    def __init__(self, x, y, direction):
        self.direction = direction
        self.x = x*16
        self.y = y*16
        self.timer = 0
        self.currentsprite = convU1

        if self.direction == 1:
            self.frame1 = convU1
            self.frame2 = convU2
            self.frame3 = convU3
        elif self.direction == 2:
            self.frame1 = convL1
            self.frame2 = convL2
            self.frame3 = convL3
        elif self.direction == 3:
            self.frame1 = convR1
            self.frame2 = convR2
            self.frame3 = convR3
        elif self.direction == 4:
            self.frame1 = convD1
            self.frame2 = convD2
            self.frame3 = convD3

    def draw(self):
        window.render(self.currentsprite, (self.x, self.y))
        self.update()

    def update(self):
        self.timer += 1

        if self.timer == 30:
            self.timer = 0
        elif self.timer < 10:
            self.currentsprite = self.frame1
        elif self.timer < 20:
            self.currentsprite = self.frame2
        elif self.timer < 30:
            self.currentsprite = self.frame3

        if (player.x+8 > self.x and player.x+8 < self.x+17) and (player.y+12 > self.y and player.y+12 < self.y+17):
            if self.direction == 1:
                player.y -= 1.8
            elif self.direction == 2:
                player.x -= 1.8
            elif self.direction == 3:
                player.x += 1.8
            elif self.direction == 4:
                player.y += 1.8