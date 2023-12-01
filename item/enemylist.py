from item.entity import *
from item.init_assets import *

# (sprite, hurt_sprite, dead_sprite, x, y, speed, HP)


class Bell(Enemy):
    def __init__(self, x, y):
        super().__init__(bell_sprite, bell_dmg_sprite, x, y, 0.2, 50)

    def update(self):
        if self.collided(player):
            player.get_hit()
        else:
            self.move()

class Mage(Enemy):
    def __init__(self, x, y):
        super().__init__(mage_sprite, mage_dmg_sprite, x, y, 0.5, 20)

class Fireguy(Enemy):
    def __init__(self, x, y):
        super().__init__(fire_sprite, fire_dmg_sprite, x, y, 1, 4)

class Ghost(Enemy):
    def __init__(self, x, y):
        super().__init__(ghost_sprite, ghost_dmg_sprite, x, y, 0.5, 24)

    def update(self):
        if self.collided(player):
            player.get_hit()
        else:
            self.move()

class Skelly(Enemy):
    def __init__(self, x, y):
        super().__init__(skelly_sprite, skelly_dmg_sprite, x, y, 0.4, 16)