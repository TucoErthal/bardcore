import math
import item.obj
from item.init_assets import *
from item.timer import Timer
from item.projectile import Projectile

import pygame

class Entity(item.obj.GameObject):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        super().__init__(x, y, w, h)

        self.immuneTimer = Timer()
        self.immuneTimer.set_max_time(1)

        self.hurt = 0
        self.hp = 0

    def draw(self, sprite):
        window.render(sprite, (self.x, self.y))

    def set_hp(self, val):
        self.hp = val

    def get_hit(self):
        if self.immuneTimer.ringing():
            self.hurt = 30
            self.set_hp(self.hp - 1)
            self.immuneTimer.restart()
            window.screenshake(10,4)

class Player(Entity):
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        super().__init__(x, y, w, h)
        self.hp = 4
        self.velocity = pygame.math.Vector2()
        self.dash_timer = 0
        self.isDead = False

        

        self.player_sprite_left = item.init_assets.player_sprite_left
        self.player_sprite_right = item.init_assets.player_sprite_right
        self.player_sprite_down = item.init_assets.player_sprite_down
        self.player_sprite_up = item.init_assets.player_sprite_up
        self.player_sprite_dead = item.init_assets.player_sprite_dmg # coloca o sprite certo aqui
        self.dmg_sprite = item.init_assets.player_sprite_dmg # coloca o sprite certo aqui

        self.curr_sprite = self.player_sprite_down
        self.lest_sprite = self.curr_sprite
        self.can_control = False

        self.w = self.curr_sprite.get_rect().width
        self.h = self.curr_sprite.get_rect().height

        self.counter = 0
        self.timer = 0
        self.scene_delay = False
        self.transition_counter = 0
        self.transition_frame = transparent

    def input(self, current_keys):
        if self.can_control:
            if current_keys[pygame.K_s]:
                self.velocity.y += 1
            
            if current_keys[pygame.K_w]:
                self.velocity.y -= 1
                
            if current_keys[pygame.K_d]:
                self.velocity.x += 1
            
            if current_keys[pygame.K_a]:
                self.velocity.x -= 1

            try:
                self.velocity = self.velocity.normalize()
            except:
                pass
        if self.dash_timer > 0:
            self.velocity.x *= (1.15 *self.dash_timer)
            self.velocity.y *= (1.15 * self.dash_timer)
        self.dash_timer -= 1

        self.x += self.velocity.x
        self.y += self.velocity.y
        self.velocity.x, self.velocity.y = 0, 0

        self.dash_timer

    def get_hit(self):
        if self.immuneTimer.ringing():
            self.hurt = 30
            self.set_hp(self.hp - 1)
            self.immuneTimer.restart()
            window.screenshake(10,4)
            player_dmg_sfx.play()

    def set_hp(self, val):
        if self.hp <= 0:
            self.die()
        self.hp = val

    def die(self):
        self.isDead = True
        self.can_control = False
        self.curr_sprite = self.player_sprite_dead

    def is_dead(self):
        if self.isDead == True:
            if self.counter < 120:
                    self.counter += 1

            if self.counter == 120:
                self.transition_frame = transparent

                if self.scene_delay == False:
                    self.timer = pygame.time.get_ticks()
                    self.scene_delay = True
                    self.transition_counter = 180

                if self.transition_counter < 60:
                    player.x = 66*16
                    player.y = 175*16
            else:
                self.warp = False

            if self.transition_counter == 0:
                self.scene_delay = False

            if self.transition_counter > 0:
                self.transition_counter -= 1

            if self.scene_delay == True and pygame.time.get_ticks() - self.timer >= 500:
                if self.transition_counter > 160:
                    pass
                elif self.transition_counter > 150:
                    self.transition_frame = trans1
                elif self.transition_counter > 140:
                    self.transition_frame = trans2
                elif self.transition_counter > 130:
                    self.transition_frame = trans3
                elif self.transition_counter > 30:
                    self.transition_frame = trans4
                elif self.transition_counter > 20:
                    self.transition_frame = trans3
                elif self.transition_counter > 10:
                    self.transition_frame = trans2
                elif self.transition_counter > 0:
                    self.transition_frame = trans1        
                    player.can_control = True
                    self.isDead = False
                    player.hp = 4

    def draw(self):
        sin = (window.camera_y + window.mouse_y - item.entity.player.y)
        cos = (window.camera_x + window.mouse_x - item.entity.player.x)
        
        if abs(sin) >= abs(cos):
            self.curr_sprite = player_sprite_down if sin >= 0 else player_sprite_up
        else:
            self.curr_sprite = player_sprite_right if cos >= 0 else player_sprite_left

        if self.hurt > 0:
            self.curr_sprite = self.dmg_sprite
            self.hurt -= 1

        super().draw(self.curr_sprite)

player = Player(200, 200, 16, 16)


# DO NOT TOUCH
# When creating new enemies, go to enemylist.py
# When initializing enemies, go to their specific room!

class Enemy(Entity):
        def __init__(self, sprite, dmg_sprite, x, y, speed, hp):
            super().__init__()
            self.x = x * 16
            self.y = y * 16

            self.sprite = sprite
            self.dmg_sprite = dmg_sprite
            self.immuneTimer.set_max_time(0)

            self.w = self.sprite.get_rect().width
            self.h = self.sprite.get_rect().height

            self.speed = speed
            self.follow_distance = 50
            self.hurt = 0
            self.hp = hp

            self.dead_time = 120
            self.spread = 0.4
            self.projSpd = 1

            self.isShooter = False
            self.isSpreadShooter = False

            self.projectiles = []
            self.t_shoot = Timer(1)

            self.sin = (player.y - self.y)
            self.cos = (player.x - self.x)
            self.angle = math.atan2(self.sin, self.cos)

        # Go to where the player is but stops at a distance
        def follow(self):
            self.sin = (player.y - self.y)
            self.cos = (player.x - self.x)
            self.angle = math.atan2(self.sin, self.cos)
            
            distance = math.sqrt(self.sin**2 + self.cos**2)
            if distance > self.follow_distance:
                self.move()
        
        # Move in the direction of self.angle
        def move(self):
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)


        def update(self, room):
            self.follow()

            if self.isShooter:
                if self.t_shoot.ringing():
                    self.t_shoot.start()
                    self.shoot()

                for t in self.projectiles:
                    t.update()
                    t.check_collision(player)
                    t.check_wall_collision(room)

                    if t.lifetime <= 0:
                        self.projectiles.remove(t)

            if self.isSpreadShooter:
                if self.t_shoot.ringing():
                    self.t_shoot.start()
                    self.shoot()

                for t in self.projectiles:
                    t.update()
                    t.check_collision(player)
                    t.check_wall_collision(room)

                    if t.lifetime <= 0:
                        self.projectiles.remove(t)

            if self.collided(player):
                player.get_hit()
                
        def shoot(self):
            p = Projectile(self.x+(self.w/2), self.y+(self.h/2), angle = self.angle)
            self.projectiles.append(p)

        def spradShoot(self):
            p1 = Projectile(self.x+(self.w/2), self.y+(self.h/2), angle = self.angle + self.spread, speed= self.projSpd)
            p2 = Projectile(self.x+(self.w/2), self.y+(self.h/2), angle = self.angle, speed= self.projSpd)
            p3 = Projectile(self.x+(self.w/2), self.y+(self.h/2), angle = self.angle - self.spread, speed= self.projSpd)
            self.projectiles.append(p1)
            self.projectiles.append(p2)
            self.projectiles.append(p3)

        def draw(self):
            if self.hp > 0:    
                if self.hurt > 0:
                    window.render(self.dmg_sprite, (self.x, self.y))
                    self.hurt -= 1
                else:
                    window.render(self.sprite, (self.x, self.y))
            else:
                self.dead_time -=1

                if self.dead_time == 45:
                    explode_sfx.play()

                if self.dead_time > 20:
                    window.render(self.dmg_sprite, (self.x, self.y))
                elif self.dead_time > 15:
                    window.render(explosion_sprite_1, (self.x,self.y))
                elif self.dead_time > 10:
                    window.render(explosion_sprite_2, (self.x,self.y))
                elif self.dead_time > 5:
                    window.render(explosion_sprite_3, (self.x,self.y))
                else:
                    window.render(explosion_sprite_4, (self.x,self.y))

            for t in self.projectiles:
                t.draw()


