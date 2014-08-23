import sys, pygame
import time
from ship import Ship

screen = None
game_assets = []

def draw_assets():
	if screen is None:
		return
	
	screen.fill( (60,0,0) )
	
	for item in game_assets:
		item.draw(screen)
	

def update_assets():
	for item in game_assets:
		item.update()


def game_setup():
	game_assets.append( Ship() )


if __name__ == '__main__':
	#Main game loop
	pygame.init()
	
	w = 1024
	h = 1024
	size = (w, h)
	screen = pygame.display.set_mode(size)
	
	Quit = False
	
	game_setup()
	
	while Quit is not True:

		update_assets()
		draw_assets()
		
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
					Quit = True