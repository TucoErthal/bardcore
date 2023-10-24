import pygame


class Level:
    def __init__(self):

        # Display surface
        self.display_surface = pygame.display.get_surface()


        # Setup de grupos de sprites

        self.sprites_visiveis = pygame.sprite.Group()
        self.sprites_obstaculos = pygame.sprite.Group()

    def run(self):
        
        # update e desenhar os sprites no jogo

        pass