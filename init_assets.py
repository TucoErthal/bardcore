import pygame
import music
import graphics


# INIT
window = graphics.Graphics()
clock = pygame.time.Clock()


# SPRITE LOAD
projectile_sprite = pygame.image.load("assets/textures/projectile.png").convert_alpha()
background_sprite = pygame.image.load("assets/textures/graphics2.png").convert_alpha()

player_sprite_left = pygame.image.load("assets/textures/playerNES1A.png").convert_alpha()
player_sprite_right = pygame.image.load("assets/textures/playerNES2A.png").convert_alpha()
player_sprite_down = pygame.image.load("assets/textures/playerNES3A.png").convert_alpha()
player_sprite_up = pygame.image.load("assets/textures/playerNES4A.png").convert_alpha()


cat_sprite = pygame.image.load("assets/textures/cat.png").convert_alpha()
cat_dmg_sprite = pygame.image.load("assets/textures/catsad.png").convert_alpha()
cat_dead_sprite = pygame.image.load("assets/textures/catdead.png").convert_alpha()

goblin_sprite = pygame.image.load("assets/textures/goblin.png").convert_alpha()
goblin_dmg_sprite = pygame.image.load("assets/textures/goblinsad.png").convert_alpha()
goblin_dead_sprite = pygame.image.load("assets/textures/goblindead.png").convert_alpha()

shroom_sprite = pygame.image.load("assets/textures/shroom.png").convert_alpha()
shroom_dmg_sprite = pygame.image.load("assets/textures/shroom.png").convert_alpha()
shroom_dead_sprite = pygame.image.load("assets/textures/shroom.png").convert_alpha()

bell_sprite = pygame.image.load("assets/textures/bell.png").convert_alpha()
bell_dmg_sprite = pygame.image.load("assets/textures/bell.png").convert_alpha()
bell_dead_sprite = pygame.image.load("assets/textures/bell.png").convert_alpha()

mage_sprite = pygame.image.load("assets/textures/mage.png").convert_alpha()
mage_dmg_sprite = pygame.image.load("assets/textures/mage.png").convert_alpha()
mage_dead_sprite = pygame.image.load("assets/textures/mage.png").convert_alpha()

fire_sprite = pygame.image.load("assets/textures/fireguy.png").convert_alpha()
fire_dmg_sprite = pygame.image.load("assets/textures/fireguy.png").convert_alpha()
fire_dead_sprite = pygame.image.load("assets/textures/fireguy.png").convert_alpha()

ghost_sprite = pygame.image.load("assets/textures/ghost.png").convert_alpha()
ghost_dmg_sprite = pygame.image.load("assets/textures/ghost.png").convert_alpha()
ghost_dead_sprite = pygame.image.load("assets/textures/ghost.png").convert_alpha()

sleep_sprite = pygame.image.load("assets/textures/sleepy.png").convert_alpha()
sleep_dmg_sprite = pygame.image.load("assets/textures/sleepy.png").convert_alpha()
sleep_dead_sprite = pygame.image.load("assets/textures/sleepy.png").convert_alpha()

# INITIATE MUSIC
soundtrack = music.Track("assets/Pong.ogg", 110, 4)