import pygame
from scripts.timer import *
from scripts.key_list import Key_list
from enum import Enum

class   key_image_id(Enum):
    AGUA = 0
    FOGO = 1
    TERRA = 2 
    AR = 3

class Combo_manager:
    def __init__(self):
        

        self.__current_combo = Key_list()

        self.__valid_combo = [
            [1, 1, 2, 1],
            [1, 2, 1, 4],
            [2, 1, 1, 3]
        ]

    def inputs(self, event):
        sec_idex = self.__current_combo.get_len()
        for combo in range(len(self.__valid_combo)):
            if event.key == pygame.K_1 and self.__valid_combo[combo][sec_idex] == 1:
                self.__current_combo.add_key(key_image_id.AGUA)
                print(sec_idex)
                break
            elif event.key == pygame.K_2 and self.__valid_combo[combo][sec_idex] == 2:
                self.__current_combo.add_key(key_image_id.TERRA)
                break
            elif event.key == pygame.K_3 and self.__valid_combo[combo][sec_idex] == 3:
                self.__current_combo.add_key(key_image_id.FOGO)
                break
            elif event.key == pygame.K_4 and self.__valid_combo[combo][sec_idex] == 4:
                self.__current_combo.add_key(key_image_id.AR)
                break
        
    def draw(self):
        self.__current_combo.draw()

    def update(self):
        if self.__current_combo.get_time() >= 1:
            self.__current_combo.clear()