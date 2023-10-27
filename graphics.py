import pygame
import random
pygame.init()

class Graphics:

    def __init__(self):
        self.native_w, self.native_h = 320, 240
        self.native_screen = pygame.Surface((self.native_w, self.native_h))

        self.window = pygame.display.set_mode(flags = pygame.FULLSCREEN)

        self.window_w, self.window_h = pygame.display.get_window_size()
        self.upscaling_factor =  self.window_h / self.native_h

        self.camera_x, self.camera_y = 0, 0
        self.screenshake_duration = 0
        self.screenshake_intensity = 0
    
    def update(self):        

        if self.screenshake_duration > 0:
            self.screenshake_duration -= 1

        upscaled_resolution = (self.native_w * self.upscaling_factor, self.native_h * self.upscaling_factor)
        upscaled_image = pygame.transform.scale(self.native_screen, upscaled_resolution)
        self.window.blit(upscaled_image, ((self.window_w - (self.native_w * self.upscaling_factor)) / 2, 0))

        pygame.display.flip()
        self.native_screen.fill((255, 255, 255))

    def render(self, image, coordinates = (0, 0)):
        screenshake_x_multiplier = (1 if self.screenshake_duration > 0 else 0) * self.screenshake_intensity        
        screenshake_y_multiplier = (1 if self.screenshake_duration > 0 else 0) * self.screenshake_intensity
        coordinates = (coordinates[0] - self.camera_x + random.random() * screenshake_x_multiplier), (coordinates[1] - self.camera_y + (random.random() * screenshake_y_multiplier))
        self.native_screen.blit(image, coordinates)

    def move_camera_to(self, x, y):
        self.camera_x = x
        self.camera_y = y

    def move_camera_by(self, x, y):
        self.camera_x += x
        self.camera_y += y
   
    def screenshake(self, duration = 60, intensity = 4):
        self.screenshake_duration = duration
        self.screenshake_intensity = intensity