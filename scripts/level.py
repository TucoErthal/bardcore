from scripts.map import Map
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.camera import Camera


class Level:
    map = Map()
    player = Player()
    enemies = [] # Enemy()
    camera = Camera()
