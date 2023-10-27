import graphics
import pygame
import sys

window = graphics.Graphics()
image = pygame.image.load('assets/graphics.png')

class GameObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y

player = GameObject(0, 0)
cat = GameObject(16, 16)

current_keys = pygame.key.get_pressed()
while True:
    events = pygame.event.get()
    last_keys = current_keys
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

    window.camera_focus(player)
    window.mouse_offset()

    window.render(image, (0, 0))
    window.render(pygame.image.load('assets\playerNES1A.png'), (player.x, player.y))
    window.render(pygame.image.load('assets\cat.png'), (cat.x, cat.y))
    window.update()