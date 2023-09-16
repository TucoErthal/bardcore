from PPlay.window import *
from Scripts.mapGenerator import MapGenerator

class Game:
    
    def __init__(self):
        #Constantes
        self.__height = 460
        self.__width = 802
        self.FPS = 60

        #Pygame/PPlay Setup
        self.window = Window(self.__width, self.__height)
        self.keyboard = self.window.get_keyboard()
        self.clock = pygame.time.Clock()

        #Initialize Game Objects
        self.map = MapGenerator("Images\\map.png", "Images\\missing_texture.png")
        #self.map.add_tile("Images\\grass_top.png")

    def events(self):
        #Eventos
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

    def draw(self):
        self.window.set_background_color([0,12,24])
        self.clock.tick(self.FPS)

        self.map.draw()

    def update(self):
        self.window.update()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()    

game = Game()
game.run()