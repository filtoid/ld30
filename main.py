import sys, pygame
import time
from ship import Ship
from stars import Star
from asteroid import Asteroid

screen = None
game_assets = []
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
        self.safe_zone = [{'x': 0, 'y': 0}, {'x': 400, 'y': 400}]

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
        for i in range(0, 400):
            game_assets.append(Star(GAME))
        for i in range(0, 40):
            game_assets.append(Asteroid(GAME))

    def check_collisions(self, obj):
        for item in game_assets:
            if item.check_collision(obj):
                return True
        return False


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
