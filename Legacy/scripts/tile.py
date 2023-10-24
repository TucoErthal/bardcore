from PPlay.sprite import Sprite

class Tile(Sprite):
    
    def __init__(self, file, color):
        super().__init__(file)
        self.__color = color

    def get_color(self):
        return self.__color