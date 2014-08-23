__author__ = 'fil'

import pygame
import random

class Star(object):
    def __init__(self, GAME):
        self.GAME = GAME
        self.loc = {'x': random.randint(0, GAME.width), 'y': random.randint(0, GAME.height)}

    def draw(self, screen):
        pt1 = [self.loc['x']-1 - self.GAME.offset['x'], self.loc['y'] - 1 - self.GAME.offset['y']]
        pt2 = [self.loc['x']+1 - self.GAME.offset['x'], self.loc['y'] + 1 - self.GAME.offset['y']]
        pt3 = [self.loc['x']-1 - self.GAME.offset['x'], self.loc['y'] + 1 - self.GAME.offset['y']]
        pt4 = [self.loc['x']+1 - self.GAME.offset['x'], self.loc['y'] - 1 - self.GAME.offset['y']]

        pygame.draw.line(screen, (255, 255, 255), (pt1[0], pt1[1]),
                         (pt2[0], pt2[1]))

        pygame.draw.line(screen, (255, 255, 255), (pt3[0], pt3[1]),
                         (pt4[0], pt4[1]))

    def update(self):
        pass