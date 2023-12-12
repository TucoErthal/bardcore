import pygame
from item.init_assets import *

font = pygame.font.SysFont(None, 24)

class Button:
    def __init__(self, x, y, width, height, text, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function

        self.sprite_index = 0 #0 = neutral, 1 = highlighted, 2 = clicked
        self.surface = pygame.surface.Surface((width, height))

    def update(self):
        if input_manager.current_cursor_over(self.x, self.y, self.width, self.height):

            if input_manager.mouse1_pressed():
                print("press")
                self.surface.fill((64, 64, 127))

            elif input_manager.mouse1_released():
                print("release")
                self.surface.fill((127, 127, 255))
                self.function()

            elif not(input_manager.last_cursor_over(self.x, self.y, self.width, self.height)):
                print("hover")
                self.surface.fill((127, 127, 255))
                
        else:
            self.surface.fill((127, 127, 127))

        text_surface = font.render(self.text, False, (255, 255, 255))
        self.surface.blit(text_surface, ((self.surface.get_width() - text_surface.get_width())/2, (self.surface.get_height() - text_surface.get_height())/2))
        window.render_ui(self.surface, (self.x, self.y))

    def render_text(self, text):
        pygame.font.SysFont()