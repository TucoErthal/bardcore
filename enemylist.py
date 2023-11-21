from entity import *
from init_assets import *

# (sprite, hurt_sprite, dead_sprite, x, y, width, height, speed, HP)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(goblin_sprite, goblin_dmg_sprite, goblin_dead_sprite,0, 0, 16, 16, 3, 8)

class Bell(Enemy):
    def __init__(self):
        super().__init__(bell_sprite, bell_dmg_sprite, bell_dead_sprite,0, 0, 32, 32, 0.8, 50)

class Mage(Enemy):
    def __init__(self):
        super().__init__(mage_sprite, mage_dmg_sprite, mage_dead_sprite,0, 0, 24, 24, 2, 20)

class Cat(Enemy):
    def __init__(self):
        super().__init__(cat_sprite, cat_dmg_sprite, cat_dead_sprite, 0, 0, 32, 32, 1, 20)

class Shroom(Enemy):
    def __init__(self):
        super().__init__(shroom_sprite, shroom_dmg_sprite, shroom_dead_sprite,0, 0, 32, 32, 2.4, 12)

class Fireguy(Enemy):
    def __init__(self):
        super().__init__(fire_sprite, fire_dmg_sprite, fire_dead_sprite,0, 0, 12, 12, 3.2, 4)

class Ghost(Enemy):
    def __init__(self):
        super().__init__(ghost_sprite, ghost_dmg_sprite, ghost_dead_sprite,0, 0, 24, 24, 2, 24)

class Sleepy(Enemy):
    def __init__(self):
        super().__init__(sleep_sprite, sleep_dmg_sprite, sleep_dead_sprite,0, 0, 16, 16, 0.4, 16)