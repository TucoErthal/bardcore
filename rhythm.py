from PPlay.window import *
from PPlay.sprite import *
from scripts.music import *
import pygame

# CREATE WINDOW
screen_w, screen_h = 1280, 720
window = Window(screen_w, screen_h)
window.set_title("Bardcore 🤘")
keyboard = window.get_keyboard()

good = Sprite("assets/textures/gui/good.png")
good.set_position((screen_w-good.width)/2, (screen_h-good.height)/2)

miss = Sprite("assets/textures/gui/miss.png")
miss.set_position((screen_w-miss.width)/2, (screen_h-miss.height)/2)

# MUSIC
pong = Track(window, "assets/Pong.ogg", 110, 4)

# MASTER CLOCK (FPS)
clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pong.on_beat(0.175):
                good.draw()
            else:
                miss.draw()
                pygame.mixer.Sound("assets/miss.ogg").play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    window.update()
