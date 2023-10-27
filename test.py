import pygame
import math

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

player = pygame.Rect(screen_rect.centerx, screen_rect.centery, 0, 0)
start = pygame.math.Vector2(player.center)

SPEED = 5

all_bullets = []

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True


while is_running:

    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
        

        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            distance_x = mouse_x - player.x
            distance_y = mouse_y - player.y
            
            angle = math.atan2(distance_y, distance_x)
            
            # speed_x, speed_y can be `float` but I don't convert to `int` to get better position
            speed_x = SPEED * math.cos(angle)
            speed_y = SPEED * math.sin(angle)
            
            # I copy `player.x, player.y` because I will change these values directly on list
            all_bullets.append([player.x, player.y, speed_x, speed_y])
            
        # --- objects events ---

            # empty

    # --- updates ---

    # move using speed - I use indexes to change directly on list
    for item in all_bullets:
        # speed_x, speed_y can be `float` but I don't convert to `int` to get better position
        item[0] += item[2]  # pos_x += speed_x
        item[1] += item[3]  # pos_y -= speed_y

    # --- draws ---

    screen.fill(BLACK)


    for pos_x, pos_y, speed_x, speed_y in all_bullets:
        # need to convert `float` to `int` because `screen` use only `int` values
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        pygame.draw.line(screen, (0,255,0), (pos_x, pos_y), (pos_x, pos_y))
        
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()