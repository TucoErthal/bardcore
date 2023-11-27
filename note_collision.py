

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