__author__ = 'fil'

import pygame
from stars import Star
from asteroid import Asteroid
from enemy import EnemyShip
from utils import is_point_inside_rect
from levels.worldnames import WorldNames
import math

class RedSpace(object):
    def __init__(self, game, size):
        self.width = size['x']
        self.height = size['y']
        self.game_assets = []
        self.GAME = game
        self.player = game.player
        self._setup()

        self.blue_exit = {'x': game.width-400, 'y': game.height-400,
                          'w': 300, 'h': 300, 'exit_world': WorldNames.BLUESPACE,
                          'exit_x': 200, 'exit_y': 200}

    def _setup(self):
        for i in range(0, 400):
            self.game_assets.append(Star(self.GAME))

        self.game_assets.append(EnemyShip(self.GAME, [{'x': 50, 'y': 500, 'rot': 3*math.pi/2} ,
                         {'x': 500, 'y': 500, 'rot': math.pi/2} ]))

        self.game_assets.append(EnemyShip(self.GAME, [{'x': 700, 'y': 600, 'rot': math.pi/2} ,
                         {'x': 10, 'y': 600, 'rot': 3*math.pi/2} ]))

        for i in range(2, 5):
            for j in range(2, 5):
                loc = {'x': i * 400, 'y': j * 400}
                self.game_assets.append(Asteroid(self.GAME, self, loc))

    def draw(self, screen):
        #Red space is red (obviously)
        screen.fill((60, 0, 0))

        ox = self.GAME.offset['x']
        oy = self.GAME.offset['y']

        pygame.draw.rect(screen, (0, 0, 60), (self.blue_exit['x']-ox, self.blue_exit['y']-oy,
                                            self.blue_exit['w'], self.blue_exit['h']))

        for item in self.game_assets:
            item.draw(screen)

    def update(self):

        if is_point_inside_rect(self.blue_exit, self.GAME.player.loc):
            self.GAME.player.exit = self.blue_exit
        else:
            self.GAME.player.exit = None

        for item in self.game_assets:
            item.update()