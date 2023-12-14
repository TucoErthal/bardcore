import pygame
import music
import graphics
import input


# INIT
window = graphics.Graphics()
clock = pygame.time.Clock()
input_manager = input.InputManager(window)

# ENTITY SPRITES
projectile_sprite = pygame.image.load("assets/textures/projectile.png").convert_alpha()
crosshair         = pygame.image.load("assets/textures/gui/mouse_crosshair.png")
miss_crosshair    = pygame.image.load("assets/textures/gui/mouse_crosshair_miss.png")


explosion_sprite_1 = pygame.image.load("assets/textures/explosion1.png").convert_alpha()
explosion_sprite_2 = pygame.image.load("assets/textures/explosion2.png").convert_alpha()
explosion_sprite_3 = pygame.image.load("assets/textures/explosion3.png").convert_alpha()
explosion_sprite_4 = pygame.image.load("assets/textures/explosion4.png").convert_alpha()

player_sprite_left  = pygame.image.load("assets/textures/player_left_A.png").convert_alpha()
player_sprite_right = pygame.image.load("assets/textures/player_right_A.png").convert_alpha()
player_sprite_down  = pygame.image.load("assets/textures/player_down_A.png").convert_alpha()
player_sprite_up    = pygame.image.load("assets/textures/player_up_A.png").convert_alpha()

player_sprite_left_dash  = pygame.image.load("assets/textures/player_left_dash.png").convert_alpha()
player_sprite_right_dash = pygame.image.load("assets/textures/player_right_dash.png").convert_alpha()
player_sprite_down_dash  = pygame.image.load("assets/textures/player_down_dash.png").convert_alpha()
player_sprite_up_dash    = pygame.image.load("assets/textures/player_up_dash.png").convert_alpha()
player_sprite_dmg        = pygame.image.load("assets/textures/player_dmg.png").convert_alpha()

player_dmg = pygame.image.load("assets/textures/player_dmg.png").convert_alpha()

string_img = pygame.image.load("assets/textures/string.png").convert_alpha()



bell_sprite     = pygame.image.load("assets/textures/bell.png").convert_alpha()
bell_dmg_sprite = pygame.image.load("assets/textures/belldmg.png").convert_alpha()

mage_sprite     = pygame.image.load("assets/textures/mage.png").convert_alpha()
mage_dmg_sprite = pygame.image.load("assets/textures/magedmg.png").convert_alpha()

fire_sprite     = pygame.image.load("assets/textures/fireguy.png").convert_alpha()
fire_dmg_sprite = pygame.image.load("assets/textures/fireguydmg.png").convert_alpha()

ghost_sprite     = pygame.image.load("assets/textures/ghost.png").convert_alpha()
ghost_dmg_sprite = pygame.image.load("assets/textures/ghostdmg.png").convert_alpha()

skelly_sprite     = pygame.image.load("assets/textures/Skelly.png").convert_alpha()
skelly_dmg_sprite = pygame.image.load("assets/textures/Skellydmg.png").convert_alpha()


# BOSS

boss_idle1   = pygame.image.load("assets/textures/boss_Idle.png")
boss_dmg     = pygame.image.load("assets/textures/boss_dmg.png")
boss_Impact  = pygame.image.load("assets/textures/boss_Impact.png")
boss_PreJump = pygame.image.load("assets/textures/boss_PreJump.png")
boss_Attack  = pygame.image.load("assets/textures/boss_Attack.png")


# DOOR SPRITES

door_sprite      = pygame.image.load("assets/textures/door.png").convert_alpha()
door_open_sprite = pygame.image.load("assets/textures/door_open.png").convert_alpha()
door_lock_sprite = pygame.image.load("assets/textures/doorlock.png").convert_alpha()

door_left_sprite      = pygame.image.load("assets/textures/doorleft.png").convert_alpha()
door_left_open_sprite = pygame.image.load("assets/textures/doorleftopen.png").convert_alpha()
door_left_lock_sprite = pygame.image.load("assets/textures/doorleftlock.png").convert_alpha()

door_right_sprite      = pygame.image.load("assets/textures/doorright.png").convert_alpha()
door_right_open_sprite = pygame.image.load("assets/textures/doorrightopen.png").convert_alpha()
door_right_lock_sprite = pygame.image.load("assets/textures/doorrightlock.png").convert_alpha()

door_down_sprite      = pygame.image.load("assets/textures/doordown.png").convert_alpha()
door_down_open_sprite = pygame.image.load("assets/textures/doordownopen.png").convert_alpha()
door_down_lock_sprite = pygame.image.load("assets/textures/doordownlock.png").convert_alpha()


# TRANSITION SPRITES

trans1      = pygame.image.load("assets/textures/gui/trans1.png")
trans2      = pygame.image.load("assets/textures/gui/trans2.png")
trans3      = pygame.image.load("assets/textures/gui/trans3.png")
trans4      = pygame.image.load("assets/textures/gui/trans4.png")
transparent = pygame.image.load("assets/textures/gui/transparent.png")

# TRAPS
 
spike_trap_0 = pygame.image.load("assets/textures/spike_trap_0.png")
spike_trap_1 = pygame.image.load("assets/textures/spike_trap_1.png")

templeTrap_U = pygame.image.load("assets/textures/templeTrap_U.png")
templeTrap_D = pygame.image.load("assets/textures/templeTrap_D.png")
templeTrap_L = pygame.image.load("assets/textures/templeTrap_L.png")
templeTrap_R = pygame.image.load("assets/textures/templeTrap_R.png")

fireball_U = pygame.image.load("assets/textures/fireballup.png")
fireball_D = pygame.image.load("assets/textures/fireballdown.png")
fireball_L = pygame.image.load("assets/textures/fireballleft.png")
fireball_R = pygame.image.load("assets/textures/fireballright.png")

convR1 = pygame.image.load("assets/textures/convR1.png")
convR2 = pygame.image.load("assets/textures/convR2.png")
convR3 = pygame.image.load("assets/textures/convR3.png")

convL1 = pygame.image.load("assets/textures/convL1.png")
convL2 = pygame.image.load("assets/textures/convL2.png")
convL3 = pygame.image.load("assets/textures/convL3.png")

convU1 = pygame.image.load("assets/textures/convU1.png")
convU2 = pygame.image.load("assets/textures/convU2.png")
convU3 = pygame.image.load("assets/textures/convU3.png")

convD1 = pygame.image.load("assets/textures/convD1.png")
convD2 = pygame.image.load("assets/textures/convD2.png")
convD3 = pygame.image.load("assets/textures/convD3.png")


enemyBall = pygame.image.load("assets/textures/enemy_ball.png")


# TORCH SPRITES

torch1 = pygame.image.load("assets/textures/torch1.png")
torch2 = pygame.image.load("assets/textures/torch2.png")
torch3 = pygame.image.load("assets/textures/torch3.png")



# ROOM SPRITES

room0_sprite  = pygame.image.load("assets/maps/room0.png").convert_alpha()
room1_sprite  = pygame.image.load("assets/maps/room1.png").convert_alpha()
room2_sprite  = pygame.image.load("assets/maps/room2.png").convert_alpha()
room3_sprite  = pygame.image.load("assets/maps/room3.png").convert_alpha()
room4_sprite  = pygame.image.load("assets/maps/room4.png").convert_alpha()
room5_sprite  = pygame.image.load("assets/maps/room5.png").convert_alpha()
room6_sprite  = pygame.image.load("assets/maps/room6.png").convert_alpha()
room7_sprite  = pygame.image.load("assets/maps/room7.png").convert_alpha()
room8_sprite  = pygame.image.load("assets/maps/room8.png").convert_alpha()
room9_sprite  = pygame.image.load("assets/maps/room9.png").convert_alpha()
room10_sprite = pygame.image.load("assets/maps/room10.png").convert_alpha()
room11_sprite = pygame.image.load("assets/maps/room11.png").convert_alpha()
room12_sprite = pygame.image.load("assets/maps/room12.png").convert_alpha()
room13_sprite = pygame.image.load("assets/maps/room13.png").convert_alpha()
room14_sprite = pygame.image.load("assets/maps/room14.png").convert_alpha()
room15_sprite = pygame.image.load("assets/maps/room15.png").convert_alpha()
room16_sprite = pygame.image.load("assets/maps/room16.png").convert_alpha()


# GUI
select_sprite = pygame.image.load("assets/textures/gui/select.png")
rhythm_bar_bg = pygame.image.load("assets/textures/gui/rhythm_bar_bg.png")
rhythm_bar_0  = pygame.image.load("assets/textures/gui/rhythm_bar_0.png")
rhythm_bar_1  = pygame.image.load("assets/textures/gui/rhythm_bar_1.png")
rhythm_bar_fg = pygame.image.load("assets/textures/gui/rhythm_bar_fg.png")

# INITIATE MUSIC
soundtrack = music.Track("assets/audio/Bardcore.ogg", 80, 2)

shoot_sfx1         = pygame.mixer.Sound("assets/audio/shoot1.ogg")
shoot_sfx2         = pygame.mixer.Sound("assets/audio/shoot2.ogg")
shoot_sfx3         = pygame.mixer.Sound("assets/audio/shoot3.ogg")
dash_sfx           = pygame.mixer.Sound("assets/audio/dash.ogg")
dmg_sfx            = pygame.mixer.Sound("assets/audio/damage.ogg")
explode_sfx        = pygame.mixer.Sound("assets/audio/explosion.ogg")
player_dmg_sfx     = pygame.mixer.Sound("assets/audio/player_dmg.ogg")
door_sfx           = pygame.mixer.Sound("assets/audio/door.ogg")
whiff_sfx          = pygame.mixer.Sound("assets/audio/whiff.ogg")
string_sfx         = pygame.mixer.Sound("assets/audio/stringsfx.ogg")
cell_explosion_sfx = pygame.mixer.Sound("assets/audio/cell_explosion.ogg")