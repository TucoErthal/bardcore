from item.entity import *
from item.init_assets import *
from item.path import *
# (sprite, hurt_sprite, dead_sprite, x, y, speed, HP)


class Bell(Enemy):
    def __init__(self, x, y):
        super().__init__(bell_sprite, bell_dmg_sprite, x, y, 0.2, 20)

    def update(self, room):
        super().update(room)
        if self.collided(player):
            player.get_hit()
        else:
            self.move()

class Mage(Enemy):
    def __init__(self, x, y):
        super().__init__(mage_sprite, mage_dmg_sprite, x, y, 0, 10)

        self.isSpreadShooter = True
        self.t_shoot.set_max_time(3)

    def update(self, room):
        super().update(room)
        if self.collided(player):
            player.get_hit()


class Ghost(Enemy):
    def __init__(self, x, y):
        super().__init__(ghost_sprite, ghost_dmg_sprite, x, y, 0.5, 12)

    def update(self, room):
        super().update(room)
        if self.collided(player):
            player.get_hit()
        else:
            self.move()

class Skelly(Enemy):
    def __init__(self, x, y):
        super().__init__(skelly_sprite, skelly_dmg_sprite, x, y, 0, 16)

        self.isShooter = True

    def update(self, room):
        super().update(room)
        if self.collided(player):
            player.get_hit()