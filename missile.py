__author__ = 'fil'

import pygame
import math


class Missile(object):
    def __init__(self, game, ship, loc, rot):
        self.loc = {'x': loc['x'], 'y': loc['y']}
        self.rot = rot
        self.SHIP = ship
        self.GAME = game
        self.SPEED = 4
        self.LENGTH = 3

    def draw(self, screen):
        pt1 = [self.loc['x'], self.loc['y']]
        pt2 = [self.LENGTH * math.sin(self.rot + math.pi) + self.loc['x'],
               self.LENGTH * math.cos(self.rot + math.pi) + self.loc['y']]
        pygame.draw.line(screen, (255, 255, 255), (pt1[0], pt1[1]),
                         (pt2[0], pt2[1]))

    def update(self):
        self.loc['x'] += self.SPEED * (math.sin(self.rot))
        self.loc['y'] += self.SPEED * (math.cos(self.rot))

        if self.loc['x'] > self.GAME.width or self.loc['x'] < 0 or \
                        self.loc['y'] > self.GAME.height or self.loc['y'] < 0:
            self.SHIP.remove_missile(self)

        if self.GAME.check_collisions(self):
            self.SHIP.remove_missile(self)

    def get_points(self, ox=0, oy=0):
        return [{'x': self.loc['x'] + ox, 'y': self.loc['y'] + oy}]

    def has_been_hit(self, obj):
        self.SHIP.remove_missile(self)