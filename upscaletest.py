import pygame
pygame.init()

native_w, native_h = 320, 240
native = pygame.Surface((native_w, native_h))

window = pygame.display.set_mode(flags = pygame.FULLSCREEN)
window_w, window_h = pygame.display.get_window_size()

upscaling_factor =  window_h/native_h
print("upscaling factor =", upscaling_factor)

image = pygame.image.load('assets/barrel.png')

while True:

    native.fill((255, 255, 255))
    native.blit(image, (0, 0))

    window.blit(pygame.transform.scale(native, (native_w*upscaling_factor, native_h*upscaling_factor)), ((window_w - (native_w*upscaling_factor))/2, 0))
    pygame.display.flip()