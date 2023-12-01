import pygame
import music
import graphics


# INIT
window = graphics.Graphics()
clock = pygame.time.Clock()


# ENTITY SPRITES
projectile_sprite = pygame.image.load("assets/textures/projectile.png").convert_alpha()
crosshair = pygame.image.load("assets/textures/gui/mouse_crosshair.png")
miss_crosshair = pygame.image.load("assets/textures/gui/mouse_crosshair_miss.png")


explosion_sprite_1 = pygame.image.load("assets/textures/explosion1.png").convert_alpha()
explosion_sprite_2 = pygame.image.load("assets/textures/explosion2.png").convert_alpha()
explosion_sprite_3 = pygame.image.load("assets/textures/explosion3.png").convert_alpha()
explosion_sprite_4 = pygame.image.load("assets/textures/explosion4.png").convert_alpha()

player_sprite_left = pygame.image.load("assets/textures/player_left_A.png").convert_alpha()
player_sprite_right = pygame.image.load("assets/textures/player_right_A.png").convert_alpha()
player_sprite_down = pygame.image.load("assets/textures/player_down_A.png").convert_alpha()
player_sprite_up = pygame.image.load("assets/textures/player_up_A.png").convert_alpha()
player_sprite_dmg = pygame.image.load("assets/textures/player_dmg.png").convert_alpha()

player_dmg = pygame.image.load("assets/textures/player_dmg.png").convert_alpha


bell_sprite = pygame.image.load("assets/textures/bell.png").convert_alpha()
bell_dmg_sprite = pygame.image.load("assets/textures/belldmg.png").convert_alpha()

mage_sprite = pygame.image.load("assets/textures/mage.png").convert_alpha()
mage_dmg_sprite = pygame.image.load("assets/textures/magedmg.png").convert_alpha()

fire_sprite = pygame.image.load("assets/textures/fireguy.png").convert_alpha()
fire_dmg_sprite = pygame.image.load("assets/textures/fireguydmg.png").convert_alpha()

ghost_sprite = pygame.image.load("assets/textures/ghost.png").convert_alpha()
ghost_dmg_sprite = pygame.image.load("assets/textures/ghostdmg.png").convert_alpha()

skelly_sprite = pygame.image.load("assets/textures/Skelly.png").convert_alpha()
skelly_dmg_sprite = pygame.image.load("assets/textures/Skellydmg.png").convert_alpha()





# DOOR SPRITES

door_sprite = pygame.image.load("assets/textures/door.png").convert_alpha()
door_open_sprite = pygame.image.load("assets/textures/door_open.png").convert_alpha()

door_left_sprite = pygame.image.load("assets/textures/doorleft.png").convert_alpha()
door_left_open_sprite = pygame.image.load("assets/textures/doorleftopen.png").convert_alpha()

door_right_sprite = pygame.image.load("assets/textures/doorright.png").convert_alpha()
door_right_open_sprite = pygame.image.load("assets/textures/doorrightopen.png").convert_alpha()

door_down_sprite = pygame.image.load("assets/textures/doordown.png").convert_alpha()
door_down_open_sprite = pygame.image.load("assets/textures/doordownopen.png").convert_alpha()


# TRANSITION SPRITES

trans1 = pygame.image.load("assets/textures/gui/trans1.png")
trans2 = pygame.image.load("assets/textures/gui/trans2.png")
trans3 = pygame.image.load("assets/textures/gui/trans3.png")
trans4 = pygame.image.load("assets/textures/gui/trans4.png")
transparent = pygame.image.load("assets/textures/gui/transparent.png")



# TORCH SPRITES

torch1 = pygame.image.load("assets/textures/torch1.png")
torch2 = pygame.image.load("assets/textures/torch2.png")
torch3 = pygame.image.load("assets/textures/torch3.png")



# ROOM SPRITES

room1_sprite = pygame.image.load("assets/maps/room1.png").convert_alpha()
room2_sprite = pygame.image.load("assets/maps/room2.png").convert_alpha()
room3_sprite = pygame.image.load("assets/maps/room3.png").convert_alpha()
room4_sprite = pygame.image.load("assets/maps/room4.png").convert_alpha()
room5_sprite = pygame.image.load("assets/maps/room5.png").convert_alpha()
room6_sprite = pygame.image.load("assets/maps/room6.png").convert_alpha()


# GUI
rhythm_bar_bg = pygame.image.load("assets/textures/gui/rhythm_bar_bg.png")
rhythm_bar_0 = pygame.image.load("assets/textures/gui/rhythm_bar_0.png")
rhythm_bar_1 = pygame.image.load("assets/textures/gui/rhythm_bar_1.png")
rhythm_bar_fg = pygame.image.load("assets/textures/gui/rhythm_bar_fg.png")

# INITIATE MUSIC
soundtrack = music.Track("assets/audio/Bardcore.ogg", 80, 2)

shoot_sfx = pygame.mixer.Sound("assets/audio/shoot.ogg")
dash_sfx = pygame.mixer.Sound("assets/audio/dash.ogg")
dmg_sfx = pygame.mixer.Sound("assets/audio/damage.ogg")
explode_sfx = pygame.mixer.Sound("assets/audio/explosion.ogg")
player_dmg_sfx = pygame.mixer.Sound("assets/audio/player_dmg.ogg")
door_sfx = pygame.mixer.Sound("assets/audio/door.ogg")
whiff_sfx = pygame.mixer.Sound("assets/audio/whiff.ogg")