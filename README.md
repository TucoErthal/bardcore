from PPlay.window import *
from PPlay.sprite import *
from music import *
import pygame

# CREATE WINDOW
screen_w, screen_h = 1280, 720
window = Window(screen_w, screen_h)
window.set_title("Bardcore ðŸ¤˜")
keyboard = window.get_keyboard()

# CREATE BALL
ball = Sprite("assets/ball.png")
ball.set_position((screen_w-ball.width)/2, (screen_h-ball.height)/2)

# MUSIC
pong = Track(window, "assets/Pong.ogg", 110, 4)

while True:

    pong.on_beat(0.2)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                ball.move_x(-screen_w/10*window.delta_time())
            if event.key == pygame.K_d:
                ball.move_x(screen_w/10*window.delta_time())
            if event.key == pygame.K_w:  
                ball.move_y(-screen_h/10*window.delta_time())
            if event.key == pygame.K_s:    
                ball.move_y(screen_h/10*window.delta_time())
            if event.key == pygame.K_ESCAPE:    
                pygame.quit()
                sys.exit()

    window.set_background_color((0,0,0))
    ball.draw()
    window.update()
