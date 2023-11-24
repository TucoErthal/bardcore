import pygame
import entity
import init_assets

### TRAP IDEAS ###
# Spike floor -> damage when stepped on
# Flamethrower -> turret that periodically shoots out fire
# Blade disc -> runs across the walls of a room
# Ping pong of death -> bounces around the room (maybe shooting projectiles?)



class spikeTrap():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.img = init_assets.spike_trap

    def collision_check(self):
        if entity.player.x+8 > self.x and entity.player.x+8 < self.x + self.width:
            if entity.player.y+8 > self.y and entity.player.y+8 < self.y + self.height:
                pass