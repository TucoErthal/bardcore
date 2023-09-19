from PPlay.sprite import Sprite
from scripts.timer import *

class Key_list:
    def __init__(self):
        #self.window = pygame.display.get_surface()
        self.__element = [
            Sprite("assets/agua.png"),
            Sprite("assets/fogo.png"),
            Sprite("assets/terra.png"),
            Sprite("assets/ar.png")
        ]
        self.__timer = Timer()

        self.__len = 0
        self.__max_len = 4

        self.__x = 20
        self.__y = 20
        self.__key_list = []

    def add_key(self, id):
        if self.__len < self.__max_len:
            self.__timer.start()
            self.__key_list.append(id)
            self.__len += 1
            return True
        else:
            return False

    def get_max_len(self):
        return self.__max_len

    def get_len(self):
        return self.__len

    def get_time(self):
        return self.__timer.get_time()

    def inputs(self, event):
        pass

    def clear(self):
        self.__timer.restart()
        self.__key_list = []

    def draw(self):
        offset = 0
        for el in self.__key_list:
            indice_el = el.value
            element = self.__element[indice_el]
            element.set_position(self.__x + offset, self.__y)
            element.draw()
            offset += element.width + 5

    def update(self):
        pass