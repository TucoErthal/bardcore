import graphics
import pygame
import sys

window = graphics.Graphics()
image = pygame.image.load('assets/graphics.png')

current_keys = pygame.key.get_pressed()
while True:
    events = pygame.event.get()
    last_keys = current_keys
    current_keys = pygame.key.get_pressed()

    if current_keys[pygame.K_RIGHT]:
        window.move_camera_by(1, 0)
    
    if current_keys[pygame.K_LEFT]:
        window.move_camera_by(-1, 0)
    
    if current_keys[pygame.K_DOWN]:
        window.move_camera_by(0, 1)
    
    if current_keys[pygame.K_UP]:
        window.move_camera_by(0, -1)

    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        window.screenshake()
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()

    window.render(image, (0, 0))
    window.update()