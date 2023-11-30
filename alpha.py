import projectile
import sys
import math
import item.enemylist
from item.entity import *
from item.itemlist import *
from item.init_assets import *
from item.enemylist import *

enemies = []
current_room = room1
projectiles = []
frame_state = 0
crosshair_state = 1
crosshair_timer = 0
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

        if note.check_wall_collision(current_room):
            note.lifetime = 0

        for i in enemies:
            if note.check_collision(i):
                dmg_sfx.play()
                note.lifetime = 0













#---------- LEVELS ----------#

def level1():
    global current_room
    room1.draw()

    door1U.draw()
    door1L.draw()
    door1R.draw()

    enemyDraw()

    player.draw()

    torch1_1.draw()
    torch1_2.draw()
    torch1_3.draw()

    projDraw()

    door1U.transition()
    door1L.transition()
    door1R.transition()

    window.render_crosshair(crosshair_state)
    
    if door1U.transition_counter == 40:
        current_room = door1U.target_room
    elif door1L.transition_counter == 40:
        current_room = door1L.target_room
    elif door1R.transition_counter == 40:
        current_room = door1R.target_room



def level2():
    global current_room
    room2.draw()
    door2R.draw()

    enemyDraw()

    player.draw()

    torch2_1.draw()
    torch2_2.draw()
    torch2_3.draw()
    torch2_4.draw()
    torch2_5.draw()

    projDraw()

    door2R.transition()

    window.render_crosshair(crosshair_state)

    if door2R.transition_counter == 40:
        current_room = door2R.target_room



def level3():
    global current_room
    room3.draw()
    door3L.draw()

    enemyDraw()

    player.draw()

    torch3_1.draw()
    torch3_2.draw()

    projDraw()

    door3L.transition()

    window.render_crosshair(crosshair_state)

    if door3L.transition_counter == 40:
        current_room = door3L.target_room


def level4():
    global current_room
    room4.draw()
    door4D.draw()

    enemyDraw()

    player.draw()

    torch4_1.draw()

    projDraw()

    door4D.transition()

    window.render_crosshair(crosshair_state)

    if door4D.transition_counter == 40:
        current_room = door4D.target_room









while True:
    clock.tick(60)
    soundtrack.tick()

    for i in enemies:
        if i.hp > 0:
            i.update()


        window.crosshair.set_duration(2 * soundtrack.get_delta_beat())



    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()

    # DEBUG #
    if current_keys[pygame.K_f] and not(last_keys[pygame.K_f]):
        enemies.append(item.enemylist.Bell())

    player.input(current_keys)



    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        window.screenshake()
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()

    if crosshair_timer > 0:
        crosshair_timer -= 1
        crosshair_state = 0
    else:
        crosshair_state = 1

    if current_mouse[0] and not(last_mouse[0]):
        if soundtrack.is_on_beat(0.2):
            sin = (window.camera_y + window.mouse_y - item.entity.player.y)
            cos = (window.camera_x + window.mouse_x - item.entity.player.x)
            angle = math.atan2(sin, cos)

            projectiles.append(projectile.Projectile(item.entity.player.x, item.entity.player.y, 8, 8, 3, angle, 200))
            shoot_sfx.play()
        else:
            window.screenshake(20,8)
            crosshair_timer = 60

    last_keys = current_keys
    last_mouse = current_mouse


    # GRAPHICS
    window.camera_focus(item.entity.player)
    window.mouse_offset()










    # DRAW SCREEN #
    if current_room.id == 1:
        level1()

    elif current_room.id == 2:
        level2()
        
    elif current_room.id == 3:
        level3()

    elif current_room.id == 4:
        level4()




    window.update()