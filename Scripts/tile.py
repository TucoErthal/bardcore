from PPlay.sprite import Sprite
from Scripts.E_tile_group import Tile_group

class Tile(Sprite):
    
    def __init__(self, file, group = Tile_group.DEFAULT):
        super().__init__(file)
        self._group = group