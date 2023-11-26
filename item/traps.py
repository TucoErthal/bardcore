import item.entity
import item.init_assets

### TRAP IDEAS ###
# Spike floor -> damage when stepped on
# Flamethrower -> turret that periodically shoots out fire
# Blade disc -> runs across the walls of a room
# Ping pong of death -> bounces around the room (maybe shooting projectiles?)



class spikeTrap():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.img = item.init_assets.spike_trap

    def collision_check(self):
        if item.entity.player.x+8 > self.x and item.entity.player.x+8 < self.x + self.width:
            if item.entity.player.y+8 > self.y and item.entity.player.y+8 < self.y + self.height:
                pass
                #TODO