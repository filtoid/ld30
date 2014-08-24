import sys, pygame
from levels.redspace import RedSpace
from levels.bluespace import BlueSpace
from levels.worldnames import WorldNames

from ship import Ship

screen = None
game_assets = []
GAME = None

game_worlds = []

# Global Constants
w = 600
h = 600

class Game(object):
    def __init__(self):
        self.width = 2000
        self.height = 2000
        self.screen_width = w
        self.screen_height = h
        self.offset = {'x': 0, 'y': 0}
        self.safe_zone = [{'x': 0, 'y': 0}, {'x': 400, 'y': 400}]
        self.player =  Ship(self)

        game_worlds.append(RedSpace(self, {'x': self.width, 'y': self.height}))
        game_worlds.append(BlueSpace(self, {'x': self.width, 'y': self.height}))

        self.current_level = game_worlds[0]

    def draw_assets(self):
        if screen is None:
            return

        self.current_level.draw(screen)
        self.player.draw(screen)

    def set_offset(self, x, y):
        self.offset = {'x': x, 'y': y}

    def update_assets(self):
        self.player.update()
        self.current_level.update()

    def change_level(self, level, player_loc=None):
        self.current_level = self.get_worlds_list()[level]
        if player_loc is None:
            self.player.loc = {'x': 100, 'y': 100}
        else:
            self.player.loc = {'x': player_loc['x'], 'y': player_loc['y']}
    def check_collisions(self, obj):
        for item in self.current_level.game_assets:

            # Optimisation don't figure out collisions for object that's nowhere near
            if not (max(item.loc['x'],obj.loc['x']) - min(item.loc['x'],obj.loc['x'])) \
                    > self.screen_width/2:

                if item.check_collision(obj):
                    obj.has_been_hit(item)
                    return True

        return False

    def get_worlds_list(self):
        return game_worlds


if __name__ == '__main__':
    # Main game loop
    pygame.init()

    size = (w, h)
    from pygame.locals import *
    flags = DOUBLEBUF

    screen = pygame.display.set_mode(size, flags)

    Quit = False
    GAME = Game()

    while Quit is not True:
        GAME.update_assets()
        GAME.draw_assets()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    Quit = True
