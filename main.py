import projectile
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


#listname.append(item.enemylist.Bell(500,500))

def spawnEnemies():
    enemies2.append(item.enemylist.Ghost(64,560))
    enemies2.append(item.enemylist.Ghost(128,560))
    enemies2.append(item.enemylist.Ghost(192,560))
    enemies3.append(item.enemylist.Bell(1104,496))
    enemies4.append(item.enemylist.Fireguy(592,96))
    enemies4.append(item.enemylist.Fireguy(608,96))

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

def level1():
    global current_room
    room1.draw()

    door1U.draw(1)
    door1L.draw(1)
    door1R.draw(1)

    door2R.draw(1)
    door3L.draw(1)
    door4D.draw(1)

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

    door1L.draw(2)

    enemyDraw(enemies2)

    player.draw()

    torch2_1.draw()
    torch2_2.draw()
    torch2_3.draw()
    torch2_4.draw()
    torch2_5.draw()

    projDraw(enemies3)

    door2R.transition()

    door1L.transition()

    window.render_crosshair(crosshair_state)

    if door2R.transition_counter == 40:
        current_room = door2R.target_room



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

    window.crosshair.set_duration(2 * soundtrack.get_delta_beat())



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
            sin = (window.camera_y + window.mouse_y - item.entity.player.y)
            cos = (window.camera_x + window.mouse_x - item.entity.player.x)
            angle = math.atan2(sin, cos)

            player.x += math.cos(angle) * 32
            player.y += math.sin(angle) * 32
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

    draw_gui()

    window.update()