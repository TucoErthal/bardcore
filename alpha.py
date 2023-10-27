import graphics
import pygame
import projectile
import music
import tucoanimation
import sys
import math

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# INITIATE GRAPHICS
window = graphics.Graphics()
player = GameObject(0, 0)
cat = GameObject(16, 16)
projectiles = []

# SPRITE LOAD
projectile_sprite = pygame.image.load("assets/textures/projectile.png").convert_alpha()
background_sprite = pygame.image.load("assets/textures/graphics2.png").convert_alpha()
player_sprite = pygame.image.load("assets/textures/playerNES1A.png").convert_alpha()
cat_sprite = pygame.image.load("assets/textures/cat.png").convert_alpha()

# INITIATE MUSIC
soundtrack = music.Track("assets/Pong.ogg", 110, 4)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    soundtrack.tick()

    # ON BEAT EVENTS
    if soundtrack.is_frame_on_beat():
        window.crosshair.set_duration(2 * soundtrack.get_delta_beat())
        #print("JOGO EXECUTA ACOES SINCRONIZADAS COM O RITMO")
        #print(soundtrack.get_delta_beat())

    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()

    if current_keys[pygame.K_d]:
        #window.move_camera_by(1, 0)
        player.x += 1
    
    if current_keys[pygame.K_a]:
        #window.move_camera_by(-1, 0)
        player.x -= 1
    
    if current_keys[pygame.K_s]:
        #window.move_camera_by(0, 1)
        player.y += 1
    
    if current_keys[pygame.K_w]:
        #window.move_camera_by(0, -1)
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
        print("player_pos =", player.x, player.y)
        projectiles.append(projectile.Projectile(player.x, player.y, 4, angle, 200))

    last_keys = current_keys
    last_mouse = current_mouse

    # GRAPHICS
    window.camera_focus(player)
    window.mouse_offset()

    window.render(background_sprite, (0, 0))
    window.render(player_sprite, (player.x, player.y))
    window.render(cat_sprite, (cat.x, cat.y))

    window.render_crosshair()

    for obj in projectiles:
        obj.lifetime -= 1
        obj.update()
        window.render(projectile_sprite, (obj.x, obj.y))
        if obj.lifetime <= 0:
            projectiles.pop(0)
            print(obj, "destroyed")

    window.update()