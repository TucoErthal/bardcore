from PPlay.window import *
from PPlay.sprite import *

_height = 460
_width = 802

wind = Window(_width, _height)

keyboard = wind.get_keyboard()


while True:
    wind.set_background_color([0,12,24])

   


    for event in pygame.event.get():
        #KeyDown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        #KeyUp    
        if event.type == pygame.KEYUP:
            pass  

        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    wind.update()