import projectile
import sys
import math
import enemylist
import entity
from init_assets import *

enemies = []
projectiles = []


while True:
    clock.tick(60)
    soundtrack.tick()

    # NEEDS FIXING
    for i in enemies:
        for j in enemies:
            if i.hp > 0:
                if i.x > j.x and i.x < j.x + j.w:
                    continue
                if i.y > j.y and i.y < j.y + j.h:
                    continue
                i.follow()


        window.crosshair.set_duration(2 * soundtrack.get_delta_beat())
        #print("JOGO EXECUTA AÇÕES SINCRONIZADAS COM O RITMO")
        #print(soundtrack.get_delta_beat())


    # INPUT
    events = pygame.event.get()
    current_keys = pygame.key.get_pressed()
    current_mouse = pygame.mouse.get_pressed()


    # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG #
    if current_keys[pygame.K_f]:
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
            
            background_sprite = pygame.image.load("assets/textures/graphics2.png").convert_alpha()

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

    window.render(background_sprite, (0, 0))
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


    

    window.render_crosshair()

    for note in projectiles:
        note.lifetime -= 1
        note.update()
        window.render(projectile_sprite, (note.x, note.y))
        if note.lifetime <= 0:
            projectiles.remove(note)

        for i in enemies:    
            if note.check_collision(i):
                note.lifetime = 0

    window.update()