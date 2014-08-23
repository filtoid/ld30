import sys, pygame
import time
from ship import Ship
from stars import Star

screen = None
game_assets = []
#key_manager = []
GAME = None

# Global Constants
w = 1024
h = 1024

class Game(object):
    def __init__(self):
        self.width = 4000
        self.height = 4000
        self.screen_width = w
        self.screen_height = h
        self.offset = {'x': 0, 'y': 0}

    def draw_assets(self):
        if screen is None:
            return

        screen.fill((60, 0, 0))

        for item in game_assets:
            item.draw(screen)

    def set_offset(self, x, y):
        self.offset = {'x': x, 'y': y}

    def update_assets(self):
        for item in game_assets:
            item.update()

    def game_setup(self):
        game_assets.append(Ship(GAME))
        game_assets.append(Star(GAME))


if __name__ == '__main__':
    # Main game loop
    pygame.init()

    size = (w, h)
    screen = pygame.display.set_mode(size)

    Quit = False
    GAME = Game()
    GAME.game_setup()

    while Quit is not True:

        GAME.update_assets()
        GAME.draw_assets()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    Quit = True
                #if key not in key_manager:
                #    key_manager.append(key)

            #elif event.type == pygame.KEYUP:
            #    if key in key_manager:
            #        key_manager.remove(key)
