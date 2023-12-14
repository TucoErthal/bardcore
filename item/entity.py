import math
import item.obj
from item.init_assets import *
from item.timer import Timer
from item.projectile import Projectile

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
        self.hp = 10
        self.x_velocity = 0
        self.y_velocity = 0
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
        self.can_control = True

        self.w = self.curr_sprite.get_rect().width
        self.h = self.curr_sprite.get_rect().height

    def input(self, current_keys):
        if self.can_control:
            if current_keys[pygame.K_s]:
                self.y_velocity += 1
            
            if current_keys[pygame.K_w]:
                self.y_velocity -= 1
                
            if current_keys[pygame.K_d]:
                self.x_velocity += 1
            
            if current_keys[pygame.K_a]:
                self.x_velocity -= 1

        if self.dash_timer > 0:
            self.x_velocity *= (2 *self.dash_timer)
            self.y_velocity *= (2 * self.dash_timer)
        self.dash_timer -= 1

        self.x += self.x_velocity
        self.y += self.y_velocity
        self.x_velocity, self.y_velocity = 0, 0

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

player = Player(624, 496, 16, 16)


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

            self.isShooter = False

            self.projectiles = []
            self.t_shoot = Timer(0.3)

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

            if self.collided(player):
                player.get_hit()
                
        def shoot(self):
            p = Projectile(self.x+(self.w/2), self.y+(self.h/2), angle = self.angle)
            self.projectiles.append(p)

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


