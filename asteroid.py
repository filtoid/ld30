__author__ = 'fil'

import random
import math
import pygame

def setup_asteroid_spines(obj):
    complete = False
    while complete == False:
        x = random.randint(0, obj.GAME.width)
        y = random.randint(0, obj.GAME.height)
        if not (x > obj.GAME.safe_zone[0]['x'] and x > obj.GAME.safe_zone[1]['x'] and \
            y > obj.GAME.safe_zone[0]['y'] and y < obj.GAME.safe_zone[1]['y']):
            obj.loc = {'x': x, 'y': y}
            complete = True

    for i in range(0, obj.SPINES):
        i = random.randint(1,40) + 20
        obj.aryspines.append(i)

class Asteroid(object):
    def __init__(self, game):
        self.GAME = game
        self.loc = {'x': 0, 'y': 0}
        self.rot = 0
        self.speed = random.randint(1,10)/10
        self.aryspines = []
        self.SPINES = 8
        setup_asteroid_spines(self)

    def draw(self, screen):
        ox =  self.GAME.offset['x']
        oy =  self.GAME.offset['y']

        for i in range(0, len(self.aryspines)-1):
            thetai = i * (2 * math.pi/len(self.aryspines)) + self.rot
            j = i + 1
            thetaj = j * (2 * math.pi/len(self.aryspines)) + self.rot

            sizei = self.aryspines[i]
            sizej = self.aryspines[j]
            pt1 = {'x': self.loc['x'] - ox + sizei * math.sin(thetai),
                   'y': self.loc['y'] - oy + sizei * math.cos(thetai) }
            pt2 = {'x': self.loc['x'] - ox + sizej * math.sin(thetaj),
                   'y': self.loc['y'] - oy + sizej * math.cos(thetaj) }
            color = (255, 255, 255)

            pygame.draw.line(screen, color, (pt1['x'], pt1['y']),
                             (pt2['x'], pt2['y']))

        thetai = (len(self.aryspines)-1) * (2 * math.pi/len(self.aryspines)) + self.rot
        thetaj = self.rot
        sizei = self.aryspines[len(self.aryspines)-1]
        sizej = self.aryspines[0]
        pt1 = {'x': self.loc['x'] - ox + sizei * math.sin(thetai),
               'y': self.loc['y'] - oy + sizei * math.cos(thetai) }
        pt2 = {'x': self.loc['x'] - ox + sizej * math.sin(thetaj),
               'y': self.loc['y'] - oy + sizej * math.cos(thetaj) }
        color = (255, 255, 255)

        pygame.draw.line(screen, color, (pt1['x'], pt1['y']),
                         (pt2['x'], pt2['y']))

    def update(self):
        pass

    def check_collision(self, obj):
        return False