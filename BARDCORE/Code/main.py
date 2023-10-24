
#----------- IMPORTAÇÕES -----------#

import pygame, sys
from settings import *
from level import Level



#----------- GAME CLASS -----------#

class Game:

	# SETUP DE PROPRIEDADES: inicializa-se o pygame, define as dimensões da tela,
	# define o nome da janela e define o relógio
	# self.level = Level inicializa a classe Level, em level.py

	def __init__(self):
		
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('BARDCORE')
		self.clock = pygame.time.Clock()

		self.level = Level()



	# GAMEPLAY LOOP: ocorre o get event do pygame para receber inputs,
	# preenche a tela de preto (por enquanto) e roda a classe Level


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()	