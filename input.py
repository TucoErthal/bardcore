import pygame

class InputManager:
    def __init__(self, window):

        self.window = window

        pygame.event.get()
        self.current_keys = pygame.key.get_pressed()
        self.current_mouse = pygame.mouse.get_pressed()
        self.current_cursor = pygame.mouse.get_pos()

        self.last_keys = self.current_keys
        self.last_mouse = self.current_mouse
        self.last_cursor = self.current_cursor

    def update(self):
        pygame.event.get()
        self.last_keys = self.current_keys
        self.current_keys = pygame.key.get_pressed()

        self.last_mouse = self.current_mouse
        self.current_mouse = pygame.mouse.get_pressed()

        self.last_cursor = self.current_cursor
        self.current_cursor = (self.window.mouse_x, self.window.mouse_y)

    def mouse1_pressed(self):
        return True if self.current_mouse[0] and not(self.last_mouse[0]) else False
        
    def mouse1_released(self):
        return True if self.last_mouse[0] and not(self.current_mouse[0]) else False

    def key_pressed(self, keycode):
        return True if self.current_keys[keycode] and not(self.last_keys[keycode]) else False
        
    def key_released(self, keycode):
        return True if self.last_keys[keycode] and not(self.current_keys[keycode]) else False
    
    def current_cursor_over(self, x, y, width, height):
        return True if x < self.current_cursor[0] < x + width and y < self.current_cursor[1] < y + height else False
    
    def last_cursor_over(self, x, y, width, height):
        return True if x < self.last_cursor[0] < x + width and y < self.last_cursor[1] < y + height else False
    
    def hovered_on(self, x, y, width, height):
        if x < self.current_cursor[0] < x + width and y < self.current_cursor[1] < y + height and\
        not (x < self.last_cursor[0] < x + width and y < self.last_cursor[1] < y + height):
            return True
        else:
            return False
        
    def hovered_off(self, x, y, width, height):
        if x < self.last_cursor[0] < x + width and y < self.last_cursor[1] < y + height and\
        not (x < self.current_cursor[0] < x + width and y < self.current_cursor[1] < y + height):
            return True
        else:
            return False