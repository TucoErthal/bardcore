from item.projectile import *
import sys
import math
import random
import item.enemylist
from item.entity import *
from item.itemlist import *
from item.init_assets import *
from item.enemylist import *
from item.cutscene import *
from gui import *

play_button = Button(16,  96, 80, 24, "PLAY", lambda: start_game())
quit_button = Button(16, 144, 80, 24, "QUIT", lambda: pygame.QUIT())
start = 0

def start_game():
    global start
    start = 1


in_game = False
enemies2  = []
enemies3  = []
enemies4  = []
enemies5  = []
enemies6  = []
enemies7  = []
enemies8  = []
enemies9  = []
enemies10 = []
enemies11 = []
enemies12 = []
enemies13 = []
enemies14 = []
enemies15 = []
enemies16 = []

strings_collected = []

#listname.append(item.enemylist.Bell(500,500))

def spawnEnemies():
    #enemiesX.append(item.enemylist.Name(x,y))
    ...

spawnEnemies()

current_room = room0
projectiles = []
frame_state = 0
crosshair_state = 1
crosshair_timer = 0


#----- ENEMIES -----#

def enemyDraw(enemy_list):
    for enemy in enemy_list:
        enemy.draw()
        #enemy.update(current_room)
        if enemy.dead_time < 0:
            enemy_list.remove(enemy)
        if enemy.hp > 0:
            enemy.update(current_room)

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


def level0():
    global current_room
    global start
    room0.draw_menu()

    play_button.update()
    quit_button.update()

    if start == 1:
        transition_to_game.logic()
        pygame.mouse.set_visible(False)
        player.x = 46*16
        player.y = 175*16

        transition_to_game.transition()
        if transition_to_game.transition_counter == 40:
            current_room = room1


def level1():
    global current_room
    room1.draw()

    player.draw()

    torch1_1.draw()

    intro.logic()
    transition_to_game.logic()

    intro.transition()
    transition_to_game.transition()

    if intro.transition_counter == 40:
        current_room = room2


def level2():
    global current_room
    global in_game
    in_game = 1
    room2.draw()

    door2U.draw(2)
    door3D.draw(2)

    player.draw()
    projDraw(enemies2)

    torch2_1.draw()

    door2U.transition()
    door3D.transition()

    intro.logic()
    intro.transition()

    if door2U.transition_counter == 40:
        current_room = door2U.target_room

    


def level3():
    global current_room
    room3.draw()

    door3U.draw(3,enemies3)
    door3D.draw(3,enemies3)
    door4D.draw(3)
    door2U.draw(3)

    enemyDraw(enemies3)
    player.draw()
    projDraw(enemies3)


    torch3_1.draw()
    torch3_2.draw()

    door3U.transition()
    door3D.transition()
    door4D.transition()
    door2U.transition()

    if door3U.transition_counter == 40:
        current_room = door3U.target_room
    if door3D.transition_counter == 40:
        current_room = door3D.target_room


def level4():
    global current_room
    room4.draw()

    door4U.draw(4,enemies4)
    door4L.draw(4,enemies4)
    door4R.draw(4,enemies4)
    door4D.draw(4,enemies4)
    door3U.draw(4)
    door5R.draw(4)
    door9L.draw(4)
    door13D.draw(4)
    string1.draw()
    string2.draw()

    player.draw()
    enemyDraw(enemies4)
    projDraw(enemies4)

    torch4_1.draw()
    torch4_2.draw()
    torch4_3.draw()
    torch4_4.draw()

    door4U.transition()
    door4L.transition()
    door4R.transition()
    door4D.transition()
    door3U.transition()
    door5R.transition()
    door9L.transition()
    door13D.transition()
    string1.transition()
    string2.transition()

    if door4U.transition_counter == 40:
        current_room = door4U.target_room
    elif door4L.transition_counter == 40:
        current_room = door4L.target_room
    elif door4R.transition_counter == 40:
        current_room = door4R.target_room
    elif door4D.transition_counter == 40:
        current_room = door4D.target_room


def level5():
    global current_room
    room5.draw()

    door5U.draw(5,enemies5)
    door5R.draw(5,enemies5)
    door4L.draw(5)
    door6D.draw(5)

    for i in room5spikes:
        i.draw()
    for i in room5conveyors:
        i.draw()

    player.draw()
    enemyDraw(enemies5)
    projDraw(enemies5)

    fire1_5.draw(room5)

    torch5_1.draw()
    torch5_2.draw()

    door5U.transition()
    door5R.transition()
    door4L.transition()
    door6D.transition()

    if door5U.transition_counter == 40:
        current_room = door5U.target_room
    elif door5R.transition_counter == 40:
        current_room = door5R.target_room


def level6():
    global current_room
    room6.draw()

    door6L.draw(6,enemies6)
    door6D.draw(6,enemies6)
    door5U.draw(6)
    door7R.draw(6)

    for i in room6spikes:
        i.draw()

    player.draw()
    enemyDraw(enemies6)
    projDraw(enemies6)

    for i in room6fire:
        i.draw(room6)

    torch6_1.draw()
    torch6_2.draw()
    torch6_3.draw()
    torch6_4.draw()

    door6L.transition()
    door6D.transition()
    door5U.transition()
    door7R.transition()

    if door6L.transition_counter == 40:
        current_room = door6L.target_room
    elif door6D.transition_counter == 40:
        current_room = door6D.target_room


def level7():
    global current_room
    room7.draw()

    door7U.draw(7,enemies7)
    door7R.draw(7,enemies7)
    door6L.draw(7)
    door8D.draw(7)

    for i in room7spikes:
        i.draw()

    player.draw()
    enemyDraw(enemies7)
    projDraw(enemies7)

    for i in room7fire:
        i.draw(room7)

    torch7_1.draw()
    torch7_2.draw()

    door7U.transition()
    door7R.transition()
    door6L.transition()
    door8D.transition()

    if door7U.transition_counter == 40:
        current_room = door7U.target_room
    elif door7R.transition_counter == 40:
        current_room = door7R.target_room


def level8():
    global current_room
    room8.draw()

    door8D.draw(8,enemies8)
    door7U.draw(8)

    for i in room8spikes:
        i.draw()

    player.draw()
    enemyDraw(enemies8)
    projDraw(enemies8)

    for i in room8fire:
        i.draw(room8)

    if 1 not in strings_collected:
        string1.draw()

    torch8_1.draw()
    torch8_2.draw()

    door8D.transition()
    door7U.transition()
    string1.transition()

    if door8D.transition_counter == 40:
        current_room = door8D.target_room
    if string1.transition_counter == 80:
        strings_collected.append(2)
    if string1.transition_counter == 60:
        current_room = room4


def level9():
    global current_room
    room9.draw()

    door9L.draw(9,enemies9)
    door9R.draw(9)
    door4R.draw(9)
    door10L.draw(9)

    player.draw()
    enemyDraw(enemies9)
    projDraw(enemies9)

    torch9_1.draw()
    torch9_2.draw()
    torch9_3.draw()
    torch9_4.draw()
    torch9_5.draw()
    torch9_6.draw()

    door9L.transition()
    door9R.transition()
    door4R.transition()
    door10L.transition()

    if door9L.transition_counter == 40:
        current_room = door9L.target_room
    elif door9R.transition_counter == 40:
        current_room = door9R.target_room


def level10():
    global current_room
    room10.draw()

    door10U.draw(10,enemies10)
    door10L.draw(10,enemies10)
    door9R.draw(10)
    door11D.draw(10)

    player.draw()
    enemyDraw(enemies4)
    projDraw(enemies4)

    torch10_1.draw()
    torch10_2.draw()

    door10U.transition()
    door10L.transition()
    door9R.transition()
    door11D.transition()

    if door10U.transition_counter == 40:
        current_room = door10U.target_room
    elif door10L.transition_counter == 40:
        current_room = door10L.target_room


def level11():
    global current_room
    room11.draw()

    door11U.draw(11,enemies11)
    door11D.draw(11,enemies11)
    door10U.draw(11)
    door12D.draw(11)

    player.draw()
    enemyDraw(enemies11)
    projDraw(enemies11)

    torch11_1.draw()
    torch11_2.draw()
    torch11_3.draw()
    torch11_4.draw()

    door11U.transition()
    door11D.transition()
    door10U.transition()
    door12D.transition()

    if door11U.transition_counter == 40:
        current_room = door11U.target_room
    elif door11D.transition_counter == 40:
        current_room = door11D.target_room


def level12():
    global current_room
    room12.draw()

    door12D.draw(12,enemies12)
    door11U.draw(12)

    player.draw()
    enemyDraw(enemies12)
    projDraw(enemies12)

    if 2 not in strings_collected:
        string2.draw()

    torch12_1.draw()
    torch12_2.draw()

    door12D.transition()
    door11U.transition()

    if door12D.transition_counter == 40:
        current_room = door12D.target_room
    if string2.transition_counter == 80:
        strings_collected.append(2)
    if string2.transition_counter == 60:
        current_room = room4


def level13():
    global current_room
    room13.draw()

    door13U.draw(13,strings_collected)
    door13D.draw(13,enemies13)
    door4U.draw(13)
    door14D.draw(13)

    player.draw()
    enemyDraw(enemies13)
    projDraw(enemies13)

    door13U.transition()
    door13D.transition()
    door4U.transition()
    door14D.transition()

    if door13U.transition_counter == 40:
        current_room = door13U.target_room
    elif door13D.transition_counter == 40:
        current_room = door13D.target_room


def level14():
    global current_room
    room14.draw()

    door14U.draw(14,enemies14)
    door14D.draw(14,enemies14)
    door13U.draw(14)
    door15D.draw(14)

    player.draw()
    enemyDraw(enemies14)
    projDraw(enemies14)

    torch14_1.draw()
    torch14_2.draw()
    torch14_3.draw()
    torch14_4.draw()

    door14U.transition()
    door14D.transition()
    door13U.transition()
    door15D.transition()

    if door14U.transition_counter == 40:
        current_room = door14U.target_room
    elif door14D.transition_counter == 40:
        current_room = door14D.target_room


def level15():
    global current_room
    room15.draw()

    door15U.draw(15,enemies15)
    door15D.draw(15,enemies15)
    door14U.draw(15)
    door16D.draw(15)

    player.draw()
    enemyDraw(enemies15)
    projDraw(enemies15)

    torch15_1.draw()
    torch15_2.draw()
    torch15_3.draw()
    torch15_4.draw()

    door15U.transition()
    door15D.transition()
    door14U.transition()
    door16D.transition()

    if door15U.transition_counter == 40:
        current_room = door15U.target_room
    elif door15D.transition_counter == 40:
        current_room = door15D.target_room


def level16():
    global current_room
    room16.draw()

    door16D.draw(16,enemies16)
    door15U.draw(16)

    player.draw()
    enemyDraw(enemies16)
    projDraw(enemies16)

    torch16_1.draw()
    torch16_1.draw()

    door16D.transition()
    door15U.transition()

    if door16D.transition_counter == 40:
        current_room = door16D.target_room





















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

    window.render_crosshair(crosshair_state)





















while True:
    clock.tick(60)
    soundtrack.tick()

    # INPUT
    input_manager.update()
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


    if player.can_control:
        if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
            if soundtrack.is_on_beat():
                player.dash_timer = 8
                dash_sfx.play()
            else:
                window.screenshake(20,8)
                crosshair_timer = 60

        if current_mouse[0] and not(last_mouse[0]):
            if soundtrack.is_on_beat(2):
                sin = (window.camera_y + window.mouse_y - item.entity.player.y)
                cos = (window.camera_x + window.mouse_x - item.entity.player.x)
                angle = math.atan2(sin, cos)

                projectiles.append(Projectile(item.entity.player.x, item.entity.player.y, 3, angle, 200))
                
                random.choice([shoot_sfx1, shoot_sfx2, shoot_sfx3]).play()
            else:
                window.screenshake(20,8)
                whiff_sfx.play()
                crosshair_timer = 60
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()

    if crosshair_timer > 0:
        crosshair_timer -= 1
        crosshair_state = 0
    else:
        crosshair_state = 1


    last_keys = current_keys
    last_mouse = current_mouse


    # GRAPHICS
    window.camera_focus(item.entity.player)
    window.mouse_offset()




    # DRAW SCREEN #
    if current_room.id    == 0:
        level0()
    elif current_room.id  == 1:
        level1()
    elif current_room.id  == 2:
        level2()
    elif current_room.id  == 3:
        level3()
    elif current_room.id  == 4:
        level4()
    elif current_room.id  == 5:
        level5()
    elif current_room.id  == 6:
        level6()
    elif current_room.id  == 7:
        level7()
    elif current_room.id  == 8:
        level8()
    elif current_room.id  == 9:
        level9()
    elif current_room.id == 10:
        level10()
    elif current_room.id == 11:
        level11()
    elif current_room.id == 12:
        level12()
    elif current_room.id == 13:
        level13()
    elif current_room.id == 14:
        level14()
    elif current_room.id == 15:
        level15()
    elif current_room.id == 16:
        level16()

    player.is_dead()
    if player.transition_counter == 40:
        current_room = room2

    if in_game:
        draw_gui()
    window.update()