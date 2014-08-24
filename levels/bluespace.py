__author__ = 'fil'

import pygame
from levels.worldnames import WorldNames
from utils import is_point_inside_rect
from stars import Star
from asteroid import Asteroid

class BlueSpace(object):
    def __init__(self, game, size):
        self.width = size['x']
        self.height = size['y']
        self.game_assets = []
        self.GAME = game
        self.player = game.player
        self.safe_zones = [{'x': 0, 'y': 0, 'w':400, 'h': 400},
                           {'x': 50, 'y': 50, 'w':300, 'h': 300}]
        self._setup()

        self.red_exit = {'x': 50, 'y': 50,
                          'w': 300, 'h': 300, 'exit_world': WorldNames.REDSPACE,
                          'exit_x': game.width-250, 'exit_y': game.height-250}

    def _setup(self):
        for i in range(0, 400):
            self.game_assets.append(Star(self.GAME))

        for i in range(2, 5):
            for j in range(2, 5):
                loc = {'x': i * 400, 'y': j * 400}
                self.game_assets.append(Asteroid(self.GAME, self, loc))

    def draw(self, screen):
        #Red space is red (obviously)
        screen.fill((0, 0, 60))

        ox = self.GAME.offset['x']
        oy = self.GAME.offset['y']

        pygame.draw.rect(screen, (60, 0, 0), (self.red_exit['x']-ox, self.red_exit['y']-oy,
                                        self.red_exit['w'], self.red_exit['h']))

        for item in self.game_assets:
            item.draw(screen)

    def update(self):

        if is_point_inside_rect(self.red_exit, self.GAME.player.loc):
            self.GAME.player.exit = self.red_exit
        else:
            self.GAME.player.exit = None

        for item in self.game_assets:
            item.update()
