import graphics
import pygame
import projectile
import music
import tucoanimation
import sys
import math


#---- CLASSES ----#
class GameObject():
    def __init__(self, x, y, w = 0, h = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Cat():
        def __init__(self, x, y, w = 32, h = 32):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.speed = 10
            self.follow_distance = 50
            self.hurt = 0
            self.hp = 30

        def follow(self):
            self.sin = (player.y - self.y)
            self.cos = (player.x - self.x)
            self.angle = math.atan2(self.sin, self.cos)
            
            distance = math.sqrt(self.sin**2 + self.cos**2)
            if distance > self.follow_distance:
                self.move()
        
        def move(self):
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)

        def get_hit(self):
            self.hurt = 30
            self.hp -= 1



# INITIATE GRAPHICS
window = graphics.Graphics()
player = GameObject(0, 0)
cats = []

for i in range(10):
    cats.append(Cat(32*i,32*i))
cat = Cat(16, 16)
projectiles = []


# SPRITE LOAD
projectile_sprite = pygame.image.load("assets/textures/projectile.png").convert_alpha()
background_sprite = pygame.image.load("assets/textures/graphics2.png").convert_alpha()
player_sprite = pygame.image.load("assets/textures/playerNES1A.png").convert_alpha()
cat_sprite = pygame.image.load("assets/textures/cat.png").convert_alpha()
cat_sad_sprite = pygame.image.load("assets/textures/catsad.png").convert_alpha()
cat_dead_sprite = pygame.image.load("assets/textures/catdead.png").convert_alpha()
cat_gore_sprite = pygame.image.load("assets/textures/catSUPERdead.png").convert_alpha()



# INITIATE MUSIC
soundtrack = music.Track("assets/Pong.ogg", 110, 4)
clock = pygame.time.Clock()





while True:
    clock.tick(60)
    soundtrack.tick()

    # ON BEAT EVENTS
    if soundtrack.is_frame_on_beat():
        if cat.hp > 0:
            cat.follow()

        window.crosshair.set_duration(2 * soundtrack.get_delta_beat())
        #print("JOGO EXECUTA ACOES SINCRONIZADAS COM O RITMO")
        #print(soundtrack.get_delta_beat())

    if cat.hp < -20:
        cat.follow()
        cat.speed = 10
        cat.follow_distance = 1


    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()

    if current_keys[pygame.K_d]:
        player.x += 1
    
    if current_keys[pygame.K_a]:
        player.x -= 1
    
    if current_keys[pygame.K_s]:
        player.y += 1
    
    if current_keys[pygame.K_w]:
        player.y -= 1

    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        window.screenshake()
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()
    
    if current_mouse[0] and not(last_mouse[0]):
        sin = (window.camera_y + window.mouse_y - player.y)
        cos = (window.camera_x + window.mouse_x - player.x)
        angle = math.atan2(sin, cos)
        
        background_sprite = pygame.image.load("assets/textures/graphics2.png").convert_alpha()

        #pygame.draw.line(background_sprite, (0, 255, 0), (player.x, player.y), (window.camera_x + window.mouse_x, window.camera_y + window.mouse_y), 10)
        #print("player_pos =", player.x, player.y)
        projectiles.append(projectile.Projectile(player.x, player.y, 8, 8, 3, angle, 200))

    last_keys = current_keys
    last_mouse = current_mouse


    



    # GRAPHICS
    window.camera_focus(player)
    window.mouse_offset()

    window.render(background_sprite, (0, 0))
    window.render(player_sprite, (player.x, player.y))

    if cat.hp > 0:
        if cat.hurt > 0:
            window.render(cat_sad_sprite, (cat.x, cat.y))
            cat.hurt -= 1
        else:
            window.render(cat_sprite, (cat.x, cat.y))
    elif cat.hp > -20:
        window.render(cat_dead_sprite, (cat.x, cat.y))
    else:
        window.render(cat_gore_sprite, (cat.x, cat.y))
    

    window.render_crosshair()

    for obj in projectiles:
        obj.lifetime -= 1
        obj.update()
        window.render(projectile_sprite, (obj.x, obj.y))
        if obj.lifetime <= 0:
            projectiles.remove(obj)
        if obj.check_collision(cat):
            obj.lifetime = 0

    window.update()