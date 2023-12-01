import pygame
import random
import tucoanimation
from PPlay.animation import *
import item.init_assets
pygame.init()

class Graphics:

    def __init__(self):
        self.native_w, self.native_h = 320, 240
        self.native_screen = pygame.Surface((self.native_w, self.native_h))

        self.window = pygame.display.set_mode(flags = pygame.FULLSCREEN)

        self.window_w, self.window_h = pygame.display.get_window_size()
        self.upscaling_factor =  self.window_h / self.native_h
        self.black_bar = (self.window_w - self.native_w * self.upscaling_factor)/2

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()[0] / self.upscaling_factor, pygame.mouse.get_pos()[1] / self.upscaling_factor

        self.camera_x, self.camera_y = 0, 0
        self.screenshake_duration = 0
        self.screenshake_intensity = 0

        self.crosshair = tucoanimation.Animation(15)
        self.crosshair.set_duration(100)
    
    def update(self):
        
        self.mouse_x = (pygame.mouse.get_pos()[0] - self.black_bar) / self.upscaling_factor
        self.mouse_y = (pygame.mouse.get_pos()[1]) / self.upscaling_factor
        
        if self.screenshake_duration > 0:
            self.screenshake_duration -= 1
        screenshake_x_multiplier = (1 if self.screenshake_duration > 0 else 0) * self.screenshake_intensity        
        screenshake_y_multiplier = (1 if self.screenshake_duration > 0 else 0) * self.screenshake_intensity

        upscaled_resolution = (self.native_w * self.upscaling_factor, self.native_h * self.upscaling_factor)
        upscaled_image = pygame.transform.scale(self.native_screen, upscaled_resolution)
        x = (self.window_w - (self.native_w * self.upscaling_factor))/2 + (random.random() * screenshake_x_multiplier)
        y = (random.random() * screenshake_y_multiplier)

        self.window.blit(upscaled_image, (x, y))
        pygame.display.flip()
        self.window.fill((0, 0, 0))
        self.native_screen.fill((0, 0, 0))

    def render(self, image, coordinates = (0, 0)):
        coordinates = (coordinates[0] - self.camera_x), (coordinates[1] - self.camera_y)
        self.native_screen.blit(image, coordinates)

    def render_ui(self, image, coordinates = (0, 0)):
        self.native_screen.blit(image, coordinates)
    
    def render_crosshair(self, state):
        if state == 1:
            self.render(item.init_assets.crosshair, (self.camera_x + self.mouse_x, self.camera_y + self.mouse_y))
        else:
            self.render(item.init_assets.miss_crosshair, (self.camera_x + self.mouse_x, self.camera_y + self.mouse_y))

    def move_camera_to(self, x, y):
        self.camera_x = x
        self.camera_y = y

    def move_camera_by(self, x, y):
        self.camera_x += x
        self.camera_y += y

    def camera_focus(self, target):
        self.camera_x = target.x - self.native_w/2
        self.camera_y = target.y - self.native_h/2

    def mouse_offset(self, multiplier = 0.2):
        x_offfset = self.mouse_x - self.native_w/2
        y_offfset = self.mouse_y - self.native_h/2
        self.move_camera_by(x_offfset*multiplier, y_offfset*multiplier)
   
    def screenshake(self, duration = 60, intensity = 8):
        self.screenshake_duration = duration
        self.screenshake_intensity = intensity