from PPlay.sprite import *
from Scripts.tile import Tile

#ToDo: 
# - Ver o tutorial na parte do mapa e colizao
# - Função para adicionar novos tiles

class Map:

    def __init__(self, map, default_tile):
        self.__tile_size = {'x': 64, 'y':64}
        self.__tiles = []

        self.__map_size = None
        self.__mat = None

        self.__map = map
        self.__tiles.append(Tile(default_tile, None))

        self.position = {'x': 0, 'y': 0}

    def add_tile(self, file, color):
        self.__tiles.append(Tile(file, color))
        return len(self.__tiles)

    def load(self):
        imgMap = Sprite(self.__map)
        self.__map_size = imgMap.image.get_size()

        #Criando matriz de tamanho __map_size[0] por __map_size[1]
        self.__mat = [[0] * self.__map_size[1] for _ in range(self.__map_size[0])]
        
        for i in range(0, self.__map_size[0]):
            for j in range(0, self.__map_size[1]):
                color = imgMap.image.get_at((i, j))

                for k in range(len(self.__tiles)):
                    print(f'tile {k} Color: {color} tile color: {self.__tiles}')
                    if color == self.__tiles[k].get_color():
                        self.__mat[i][j] = k

    def draw(self):
        try:
            for i in range(0, self.__map_size[0]):
                for j in range(0, self.__map_size[1]):
                    code = self.__mat[i][j]
                    tile_x = i * self.__tile_size["x"] - self.position['x']
                    tile_y = j * self.__tile_size["y"] - self.position['y']
                    try:
                        self.__tiles[code].set_position(tile_x, tile_y)
                        self.__tiles[code].draw()
                    except:
                        self.__tiles[0].set_position(tile_x, tile_y)
                        self.__tiles[0].draw()
        except:
            print("Algo deu errado. Talves vc tenha esquecido de charmar a funcao load()")
    
    def move_x(self, x):
        self.position['x'] += x

    def move_y(self, y):
        self.position['y'] += y

    #geter and setter