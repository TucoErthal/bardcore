from item.entity import *
from item.init_assets import *
from item.timer import Timer
from item.path import Path
from item.point import Point

ATTACK = 0
FOLLOW = 1
IMPACT = 2
PREPERING = 4

class Boss(Enemy):
    def __init__(self, x, y):
        super().__init__(boss_idle1, boss_dmg, x, y, 0.1, 16)
        self.defalt_spd = self.speed
        self.follow_distance = 70
        self.defalt_follow_distance = self.follow_distance

        self.gx = self.x 
        self.gy = self.y - 48

        self.target = Point(self.x, self.y)
        self.start_cords = Point(self.x, self.y)

        self.h =  self.h - 48

        self.spt_follow = boss_idle1
        self.spt_attack = boss_Attack
        self.spt_prepare = boss_PreJump
        self.spt_impact = boss_Impact

        self.t_attack = Timer(0.5)
        self.t_follow = Timer(5)
        self.t_impact = Timer(0.5)
        self.t_prepare = Timer(0.5)

        self.state = ATTACK
        self.hitbox = True

    def set_target(self):
        tx = player.x-16
        ty = player.y-16
        self.target = Point(tx, ty)
        self.start_cords = Point(self.x, self.y)

    def follow2Attack(self):
        self.t_follow.start()  
        self.t_follow.pouse()  
        self.t_attack.start()  
        self.t_prepare.restart()

        self.set_target()
        self.sprite = self.spt_prepare
        self.state = PREPERING

        self.speed = self.defalt_spd
        self.follow_distance = 0


    def attack2Follow(self):
        self.t_attack.start()
        self.t_attack.pouse()
        self.t_follow.start()
        self.t_impact.restart()

        self.sprite = self.spt_impact
        self.state = IMPACT

        self.speed = self.defalt_spd*3
        self.hitbox = True
        self.follow_distance = self.defalt_follow_distance

    def goTo_target(self):
        point = Path.interpolate_2d(self.start_cords, self.target, self.t_attack.get_time()/self.t_attack.max_time)
        self.x = point.x
        self.y = point.y

    def follow(self):
        self.sin = (player.y - self.y-16)
        self.cos = (player.x - self.x-16)
        self.angle = math.atan2(self.sin, self.cos)
        
        distance = math.sqrt(self.sin**2 + self.cos**2)
        if distance > self.follow_distance:
            self.move()

    def update(self):
        if self.state == ATTACK:
            self.goTo_target()
            if self.t_attack.ringing():
                self.attack2Follow()
        elif self.state == FOLLOW:
            self.follow()
            if self.t_follow.ringing():
                self.follow2Attack()
        elif self.state == IMPACT:
            self.hitbox = True
            if self.t_impact.ringing():
                self.sprite = self.spt_follow
                self.t_impact.start()
                self.state = FOLLOW
        elif self.state == PREPERING:
            if self.t_prepare.ringing():
                self.sprite = self.spt_attack
                self.t_prepare.start()
                self.t_attack.start()
                self.hitbox = False
                self.state = ATTACK

        if self.collided(player) and self.hitbox:
            player.get_hit()

        self.gx = self.x 
        self.gy = self.y - 48


    def draw(self):
        if self.hp > 0:    
            if self.hurt > 0:
                window.render(self.dmg_sprite, (self.gx, self.gy))
                self.hurt -= 1
            else:
                window.render(self.sprite, (self.gx, self.gy))
        else:
            self.dead_time -=1

            if self.dead_time == 45:
                explode_sfx.play()

            if self.dead_time > 20:
                window.render(self.dmg_sprite, (self.gx, self.gy))
            elif self.dead_time > 15:
                window.render(explosion_sprite_1, (self.gx,self.gy))
            elif self.dead_time > 10:
                window.render(explosion_sprite_2, (self.gx,self.gy))
            elif self.dead_time > 5:
                window.render(explosion_sprite_3, (self.gx,self.gy))
            else:
                window.render(explosion_sprite_4, (self.gx,self.gy))