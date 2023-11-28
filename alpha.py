import projectile
import sys
import math
import item.enemylist
from item.entity import *
from item.itemlist import *
from item.init_assets import *
from item.enemylist import *

enemies = []
projectiles = []
frame_state = 0
player_direction_facing = player_sprite_down

pygame.mouse.set_visible(False)

#----- ENEMIES -----#

def enemyDraw():
    for i in enemies:
        i.draw()
        if i.dead_time < 0:
            enemies.remove(i)

def projDraw():
    for note in projectiles:
        note.lifetime -= 1
        note.update()
        window.render(projectile_sprite, (note.x, note.y))
        if note.lifetime <= 0:
            projectiles.remove(note)

        if note.check_wall_collision(room_1):
            note.lifetime = 0

        for i in enemies:
            if note.check_collision(i):
                dmg_sfx.play()
                note.lifetime = 0






#---------- LEVELS ----------#

def level1():
    room_1.draw()
    room_1_door_up.draw()
    room_1_door_left.draw()
    room_1_door_right.draw()

    enemyDraw()

    window.render(player_direction_facing, (player.x, player.y))

    torch_1_1.draw()
    torch_1_2.draw()
    torch_1_3.draw()

    projDraw()

    room_1_door_up.transition()
    room_1_door_left.transition()
    room_1_door_right.transition()

    window.render_crosshair()



















while True:
    clock.tick(60)
    soundtrack.tick()

    for i in enemies:
        if i.hp > 0:
            i.follow()


        window.crosshair.set_duration(2 * soundtrack.get_delta_beat())



    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()


    if current_keys[pygame.K_f] and not(last_keys[pygame.K_f]):
        enemies.append(item.enemylist.Bell())
   

    if current_keys[pygame.K_s]:
        item.entity.player.y += 1
        player_direction_facing = player_sprite_down
    
    if current_keys[pygame.K_w]:
        item.entity.player.y -= 1
        player_direction_facing = player_sprite_up
        
    if current_keys[pygame.K_d]:
        item.entity.player.x += 1
        player_direction_facing = player_sprite_right
    
    if current_keys[pygame.K_a]:
        item.entity.player.x -= 1
        player_direction_facing = player_sprite_left



    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        window.screenshake()
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()

    if current_mouse[0] and not(last_mouse[0]):
        #if soundtrack.is_on_beat(0.2):
            sin = (window.camera_y + window.mouse_y - item.entity.player.y)
            cos = (window.camera_x + window.mouse_x - item.entity.player.x)
            angle = math.atan2(sin, cos)

            #pygame.draw.line(background_sprite, (0, 255, 0), (player.x, player.y), (window.camera_x + window.mouse_x, window.camera_y + window.mouse_y), 10)
            #print("player_pos =", player.x, player.y)
            projectiles.append(projectile.Projectile(item.entity.player.x, item.entity.player.y, 8, 8, 3, angle, 200))
            shoot_sfx.play()
        #else:
            #window.screenshake(20,4)

    last_keys = current_keys
    last_mouse = current_mouse


    # GRAPHICS
    window.camera_focus(item.entity.player)
    window.mouse_offset()




    # DRAW SCREEN #
    level1()



    

    window.update()
















