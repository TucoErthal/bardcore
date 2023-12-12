import item.entity
from item.init_assets import *

from item.obj import GameObject
from item.timer import Timer
from item.projectile import *
### TRAP IDEAS ###
# Spike floor -> damage when stepped on                                         Feita
# Flamethrower -> turret that periodically shoots out fire                      Feita
# Blade disc -> runs across the walls of a room
# Ping pong of death -> bounces around the room (maybe shooting projectiles?)

UP = 'u'
RIGHT = 'r'
DOWN = 'd'
LEFT = 'l'





# Atiram no ritimo da musica
# Sprites sao place holder
#update dentro de draw para consistencia com o resto do codigo
class WallTrap(GameObject):
    def __init__(self, x, y, dire = RIGHT):
        super().__init__()
        
        self.x = x*16
        self.y = y*16

        self.direction = dire

        self.tiros = []



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
        if self.tiroCadence.ringing() and soundtrack.is_on_beat():
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
        angel = 0
        

        if self.direction == UP:
            angle = 1.5708 # 90°
        elif self.direction == LEFT:
            angle = 0
        elif self.direction == DOWN:
            angle = 4.71239 # 270° 
        elif self.direction == RIGHT:
            angle = 3.14159 # 180°

        tiro = Projectile(self.tiro_spawn[0], self.tiro_spawn[1], 8, 8, 3, angle, 200)
        tiro.curr_sprite = enemyBall
        self.tiros.append(tiro)

class spikeTrap(GameObject):
    def __init__(self, x, y):
        super().__init__()

        self.img_0 = item.init_assets.spike_trap_0
        self.img_1 = item.init_assets.spike_trap_1

        self.curr_sprite = self.img_0

        self.x = x*16
        self.gy = y*16      # for draw fuction
        self.y = self.gy+16       # for the collided fuction
        self.w = self.img_0.get_rect().width
        self.h = self.img_0.get_rect().height/2

        self.animationTimer = Timer(1)

    def draw(self):
        window.render(self.curr_sprite, (self.x, self.gy))
        self.update()

    def update(self):
        player = item.entity.player

        if self.animationTimer.ringing():
            if self.curr_sprite != self.img_0:
                self.curr_sprite = self.img_0
                
            if self.collided(player):
                self.curr_sprite = self.img_1
                player.get_hit()
                self.animationTimer.restart()
            

