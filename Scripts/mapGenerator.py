from PPlay.sprite import *
from Scripts.tile import Tile

#ToDo: 
# - Ver o tutorial na parte do mapa e colizao
# - Função para adicionar novos tiles

class MapGenerator:

    def __init__(self, map, default_tile):
        self.__tile_size = {'x': 64, 'y':64}
        self.__tiles = []

        self.__map_size = None
        self.__mat = None

        self.__tiles.append(Tile(default_tile))
        self.load(map)

        

    def add_tile(self, file, group = None):
        self.__tiles.append(Tile(file, group))

    def load(self, filename):
        imgMap = Sprite(filename)
        self.__map_size = imgMap.image.get_size()

        #Criando matriz de tamanho __map_size[0] por __map_size[1]
        self.__mat = [[0] * self.__map_size[1] for _ in range(self.__map_size[0])]
        
        for i in range(0, self.__map_size[0]):
            for j in range(0, self.__map_size[1]):
                color = imgMap.image.get_at((i, j))

                if color == (0, 0, 0):
                    self.__mat[i][j] = 0
                    
                elif color == (255, 255, 255):
                    self.__mat[i][j] = 1
                    
                else:
                    self.__mat[i][j] = -1

    def draw(self):
        for i in range(0, self.__map_size[0]):
            for j in range(0, self.__map_size[1]):
                code = self.__mat[i][j]
                tile_x = i * self.__tile_size["x"]
                tile_y = j * self.__tile_size["y"]
                try:
                    self.__tiles[code].set_position(tile_x, tile_y)
                    self.__tiles[code].draw()
                except:
                    self.__tiles[0].set_position(tile_x, tile_y)
                    self.__tiles[0].draw()

                

    #geter and setter
    def get_tile_set(self):
        return self.__tile_set