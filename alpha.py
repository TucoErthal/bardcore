import projectile
import sys
import math
import enemylist
import entity
import roomlist
from init_assets import *

enemies = []
projectiles = []
frame_state = 0

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


    # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG #
    if current_keys[pygame.K_f] and not(last_keys[pygame.K_f]):
        enemies.append(enemylist.Bell())
    if current_keys[pygame.K_g]:
        enemies.append(enemylist.Shroom())
    if current_keys[pygame.K_h]:
        enemies.append(enemylist.Cat())
    if current_keys[pygame.K_j]:
        enemies.append(enemylist.Mage())
    if current_keys[pygame.K_k]:
        enemies.append(enemylist.Goblin())
    if current_keys[pygame.K_c]:
        enemies.append(enemylist.Fireguy())
    if current_keys[pygame.K_v]:
        enemies.append(enemylist.Ghost())
    if current_keys[pygame.K_b]:
        enemies.append(enemylist.Sleepy())


    player_direction_facing = player_sprite_down
    if current_keys[pygame.K_d]:
        entity.player.x += 1
        player_direction_facing = player_sprite_left
    
    if current_keys[pygame.K_a]:
        entity.player.x -= 1
        player_direction_facing = player_sprite_right
    
    if current_keys[pygame.K_s]:
        entity.player.y += 1
        player_direction_facing = player_sprite_down
    
    if current_keys[pygame.K_w]:
        entity.player.y -= 1
        player_direction_facing = player_sprite_up

    if current_keys[pygame.K_SPACE] and not(last_keys[pygame.K_SPACE]):
        window.screenshake()
    
    if current_keys[pygame.K_ESCAPE]:
        sys.exit()
    
    if current_mouse[0] and not(last_mouse[0]):
        #if soundtrack.is_on_beat(0.2):
            sin = (window.camera_y + window.mouse_y - entity.player.y)
            cos = (window.camera_x + window.mouse_x - entity.player.x)
            angle = math.atan2(sin, cos)

            #pygame.draw.line(background_sprite, (0, 255, 0), (player.x, player.y), (window.camera_x + window.mouse_x, window.camera_y + window.mouse_y), 10)
            #print("player_pos =", player.x, player.y)
            projectiles.append(projectile.Projectile(entity.player.x, entity.player.y, 8, 8, 3, angle, 200))
        #else:
            #window.screenshake(20,4)

    last_keys = current_keys
    last_mouse = current_mouse



    for i in enemies:
        for j in enemies:
            if i == j:
                continue
            if i.x == j.x and i.y == j.y:
                i.x += 32
                i.y += 32


    


    # GRAPHICS
    window.camera_focus(entity.player)
    window.mouse_offset()


    if frame_state == 0:
        frame_state = 1
        roomlist.first_room.change_frame(first_room_sprite_B)

    if frame_state == 1:
        frame_state = 2
        roomlist.first_room.change_frame(first_room_sprite_C)

    if frame_state == 2:
        frame_state = 3
        roomlist.first_room.change_frame(first_room_sprite_B)

    if frame_state == 3:
        frame_state = 0
        roomlist.first_room.change_frame(first_room_sprite_A)

    roomlist.first_room.draw_room()



    roomlist.first_room.collision_check()
    window.render(player_direction_facing, (entity.player.x, entity.player.y))

    for i in enemies:
        if i.hp > 0:
            if i.hurt > 0:
                window.render(i.dmg_sprite, (i.x, i.y))
                i.hurt -= 1
            else:
                window.render(i.sprite, (i.x, i.y))
        else:
            window.render(i.dead_sprite, (i.x, i.y))


    roomlist.first_room_door.warp()

    window.render_crosshair()

    for note in projectiles:
        note.lifetime -= 1
        note.update()
        window.render(projectile_sprite, (note.x, note.y))
        if note.lifetime <= 0:
            projectiles.remove(note)

        if note.check_wall_collision(roomlist.first_room):
            note.lifetime = 0

        for i in enemies:    
            if note.check_collision(i):
                note.lifetime = 0

    window.update()