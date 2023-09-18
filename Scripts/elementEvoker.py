from enum import Enum
from PPlay.sprite import Sprite
import pygame


class   el_id(Enum):
    AGUA = 0
    FOGO = 1
    TERRA = 2 
    AR = 3


class el_evoker:
    def __init__(self):
        #self.window = pygame.display.get_surface()
        self.__element = [
            Sprite("Images\\agua.png"),
            Sprite("Images\\fogo.png"),
            Sprite("Images\\terra.png"),
            Sprite("Images\\ar.png")
        ]


        self.x = 20
        self.y = 20
        self.on_screen = []

    def add_on_screen(self, id):
        self.on_screen.append(id)


    def pop_on_screen(self):
        self.on_screen.pop(0)

    def event(self, event):
        if event.key == pygame.K_1:
            self.add_on_screen(el_id.AGUA)
            #reset timer
        elif event.key == pygame.K_2:
            self.add_on_screen(el_id.TERRA)
            #reset timer
        elif event.key == pygame.K_3:
            self.add_on_screen(el_id.FOGO)
            #reset timer
        elif event.key == pygame.K_4:
            self.add_on_screen(el_id.AR)
            #reset timer

    def draw(self):
        offset = 0
        for el in self.on_screen:
            indice_el = el.value
            element = self.__element[indice_el]
            element.set_position(self.x + offset, self.y)
            element.draw()
            offset += element.width + 5