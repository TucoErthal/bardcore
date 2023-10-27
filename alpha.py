import graphics
import pygame
import music
import tucoanimation
import sys

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# INITIATE GRAPHICS
window = graphics.Graphics()
player = GameObject(0, 0)
cat = GameObject(16, 16)

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
    
    last_keys = current_keys

    # GRAPHICS
    window.camera_focus(player)
    window.mouse_offset()

    window.render(pygame.image.load('assets/textures/graphics.png'), (0, 0))
    window.render(pygame.image.load('assets/textures/playerNES1A.png'), (player.x, player.y))
    window.render(pygame.image.load('assets/textures/cat.png'), (cat.x, cat.y))

    window.render_crosshair()

    window.update()