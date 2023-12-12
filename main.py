from item.projectile import *
import sys
import math
import item.enemylist
from item.entity import *
from item.itemlist import *
from item.init_assets import *
from item.enemylist import *


enemies2 = []
enemies3 = []
enemies4 = []
enemies5 = []
enemies6 = []


#listname.append(item.enemylist.Bell(500,500))

def spawnEnemies():
    enemies2.append(item.enemylist.Ghost(3,35))
    enemies3.append(item.enemylist.Bell(68,30))
    enemies4.append(item.enemylist.Fireguy(38,6))
    enemies4.append(item.enemylist.Fireguy(41,6))
    enemies5.append(item.enemylist.Skelly(3,50))
    enemies5.append(item.enemylist.Skelly(18,50))
    enemies5.append(item.enemylist.Bell(10,63))
    enemies6.append(item.enemylist.Mage(32,57))
    enemies6.append(item.enemylist.Mage(32,63))
    enemies6.append(item.enemylist.Mage(40,57))
    enemies6.append(item.enemylist.Mage(40,63))

spawnEnemies()

current_room = room1
projectiles = []
frame_state = 0
crosshair_state = 1
crosshair_timer = 0

pygame.mouse.set_visible(False)

#----- ENEMIES -----#

def enemyDraw(enemy_list):
    for enemy in enemy_list:
        enemy.draw()
        enemy.follow()
        if enemy.dead_time < 0:
            enemy_list.remove(enemy)
        if enemy.hp > 0:
            enemy.update()

def projDraw(enemy_list):
    for note in projectiles:
        note.lifetime -= 1
        note.update()
        window.render(projectile_sprite, (note.x, note.y))
        if note.lifetime <= 0:
            projectiles.remove(note)

        if note.check_wall_collision(current_room):
            note.lifetime = 0

        for i in enemy_list:
            if note.check_collision(i):
                dmg_sfx.play()
                note.lifetime = 0













#---------- LEVELS ----------#

# level template:
'''
def levelX():
    global current_room
    roomX.draw()

    doors.draw(X)

    enemyDraw(enemiesX)

    player.draw()

    torches.draw()

    projDraw(enemiesX)

    doors.transition()

    window.render_crosshair(crosshair_state)

    if doors.transition_counter == 40:
        current_room = doors.target_room
'''








def level1():
    global current_room
    room1.draw()

    door1U.draw(1)
    door1L.draw(1)
    door1R.draw(1)
    door2R.draw(1)
    door3L.draw(1)
    door4D.draw(1)

    spkTrap1_1.draw()

    wallTrapL.draw(room1)
    wallTrapD.draw(room1)
    wallTrapU.draw(room1)
    wallTrapR.draw(room1)

    player.draw()

    torch1_1.draw()
    torch1_2.draw()
    torch1_3.draw()


    projDraw(enemies2)

    door1U.transition()
    door1L.transition()
    door1R.transition()
    door4D.transition()
    door2R.transition()
    door3L.transition()

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

    door2R.draw(2)
    door2D.draw(2)
    door1L.draw(2)
    door5U.draw(2)

    enemyDraw(enemies2)

    player.draw()

    torch2_1.draw()
    torch2_2.draw()
    torch2_3.draw()
    torch2_4.draw()
    torch2_5.draw()

    projDraw(enemies2)

    door2R.transition()
    door2D.transition()
    door1L.transition()
    door5U.transition()

    window.render_crosshair(crosshair_state)

    if door2R.transition_counter == 40:
        current_room = door2R.target_room
    elif door2D.transition_counter == 40:
        current_room = door2D.target_room

def level3():
    global current_room
    room3.draw()

    door3L.draw(3)
    door1R.draw(3)

    enemyDraw(enemies3)

    player.draw()

    torch3_1.draw()
    torch3_2.draw()

    projDraw(enemies3)

    door3L.transition()
    door1R.transition()

    window.render_crosshair(crosshair_state)

    if door3L.transition_counter == 40:
        current_room = door3L.target_room


def level4():
    global current_room
    room4.draw()
    
    door4D.draw(4)
    door1U.draw(4)

    enemyDraw(enemies4)

    player.draw()

    torch4_1.draw()

    projDraw(enemies4)

    door4D.transition()
    door1U.transition()

    window.render_crosshair(crosshair_state)

    if door4D.transition_counter == 40:
        current_room = door4D.target_room


def level5():
    global current_room
    room5.draw()

    door5U.draw(5)
    door5R.draw(5)
    door2D.draw(5)
    door6L.draw(5)

    enemyDraw(enemies5)

    player.draw()

    torch5_1.draw()
    torch5_2.draw()

    projDraw(enemies5)

    door5U.transition()
    door5R.transition()
    door2D.transition()
    door6L.transition()

    window.render_crosshair(crosshair_state)

    if door5U.transition_counter == 40:
        current_room = door5U.target_room
    elif door5R.transition_counter == 40:
        current_room = door5R.target_room


def level6():
    global current_room
    room6.draw()

    door6L.draw(6)
    door5R.draw(6)

    enemyDraw(enemies6)

    player.draw()

    torch6_1.draw()
    torch6_2.draw()
    torch6_3.draw()
    torch6_4.draw()

    projDraw(enemies6)

    door6L.transition()
    door5R.transition()

    window.render_crosshair(crosshair_state)

    if door6L.transition_counter == 40:
        current_room = door6L.target_room





















def draw_gui():
    top_bar = pygame.Surface((320, 32))
    top_bar.fill((0, 0, 0))

    beat_bar = pygame.Surface((256, 16))
    beat_bar.blit(rhythm_bar_bg, (0, 0))

    beat_bar_progress_width = 128 * soundtrack.current_beat_in_bar
    beat_bar.blit(rhythm_bar_1 if soundtrack.is_on_beat() else rhythm_bar_0, (0, 0), (0, 0, beat_bar_progress_width, 16))

    beat_bar_forgiveness_width = 128 * soundtrack.forgiveness    
    latency_offset = 128 * soundtrack.latency_beats

    beat_bar.fill((0, 0, 0), ((000 - beat_bar_forgiveness_width/2 + latency_offset - 1), 12, beat_bar_forgiveness_width + 2, 3))
    beat_bar.fill((80, 80, 80), ((000 - beat_bar_forgiveness_width/2 + latency_offset), 12, beat_bar_forgiveness_width, 3))

    beat_bar.fill((0, 0, 0), ((128 - beat_bar_forgiveness_width/2 + latency_offset - 1), 12, beat_bar_forgiveness_width + 2, 3))
    beat_bar.fill((80, 80, 80), ((128 - beat_bar_forgiveness_width/2 + latency_offset), 12, beat_bar_forgiveness_width, 3))

    beat_bar.fill((0, 0, 0), ((256 - beat_bar_forgiveness_width/2 + latency_offset - 1), 12, beat_bar_forgiveness_width + 2, 3))
    beat_bar.fill((80, 80, 80), ((256 - beat_bar_forgiveness_width/2 + latency_offset), 12, beat_bar_forgiveness_width, 3))

    beat_bar.blit(rhythm_bar_fg, (0, 0))
    top_bar.blit(beat_bar, (32, 8))

    window.render_ui(top_bar, (0, 0))





















while True:
    clock.tick(60)
    soundtrack.tick()



    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()


    if current_keys[pygame.K_UP] and not(last_keys[pygame.K_UP]):
        soundtrack.forgiveness += 0.01       

    if current_keys[pygame.K_DOWN] and not(last_keys[pygame.K_DOWN]):
        soundtrack.forgiveness -= 0.01

    if current_keys[pygame.K_RIGHT] and not(last_keys[pygame.K_RIGHT]):
        soundtrack.latency_seconds += 0.01    

    if current_keys[pygame.K_LEFT] and not(last_keys[pygame.K_LEFT]):
        soundtrack.latency_seconds -= 0.01


    player.input(current_keys)



    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        if soundtrack.is_on_beat():
            player.dash_timer = 8
            dash_sfx.play()
        else:
            window.screenshake(20,8)
            crosshair_timer = 60
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()

    if crosshair_timer > 0:
        crosshair_timer -= 1
        crosshair_state = 0
    else:
        crosshair_state = 1

    if current_mouse[0] and not(last_mouse[0]):
        if soundtrack.is_on_beat():
            sin = (window.camera_y + window.mouse_y - item.entity.player.y)
            cos = (window.camera_x + window.mouse_x - item.entity.player.x)
            angle = math.atan2(sin, cos)

            projectiles.append(Projectile(item.entity.player.x, item.entity.player.y, 8, 8, 3, angle, 200))
            shoot_sfx.play()
        else:
            window.screenshake(20,8)
            whiff_sfx.play()
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

    elif current_room.id == 5:
        level5()

    elif current_room.id == 6:
        level6()

    draw_gui()

    window.update()