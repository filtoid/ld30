__author__ = 'fil'

import pygame
import random

class Star(object):
    def __init__(self, game):
        self.GAME = game
        self.loc = {'x': random.randint(0, game.width), 'y': random.randint(0, game.height)}

    def draw(self, screen):
        if self.loc['x'] < self.GAME.offset['x'] or\
            self.loc['x'] > self.GAME.offset['x'] + self.GAME.screen_width or\
            self.loc['y'] < self.GAME.offset['y'] or\
            self.loc['y'] > self.GAME.offset['y'] + self.GAME.screen_height:
            return

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

    def check_collision(self, obj):
        # Can't hit a star
        return False