__author__ = 'fil'

import random
import math
import pygame
import utils

def setup_asteroid_spines(obj):
    for i in range(0, obj.SPINES):
        i = random.randint(1, 40) + 20
        obj.aryspines.append(i)

class Asteroid(object):
    def __init__(self, game, level, loc):
        self.GAME = game
        self.loc = {'x': loc['x'], 'y': loc['y']}
        self.rot = 0
        self.speed = random.randint(1,10)/10
        self.aryspines = []
        self.SPINES = 8
        setup_asteroid_spines(self)

    def draw(self, screen):
        if self.loc['x'] < self.GAME.offset['x'] or\
            self.loc['x'] > self.GAME.offset['x'] + self.GAME.screen_width or\
            self.loc['y'] < self.GAME.offset['y'] or\
            self.loc['y'] > self.GAME.offset['y'] + self.GAME.screen_height:
            return

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

    def get_triangles(self):
        arytris = []

        for i in range(0, len(self.aryspines)-1):
            thetai = i * (2 * math.pi/len(self.aryspines)) + self.rot
            j = i + 1
            thetaj = j * (2 * math.pi/len(self.aryspines)) + self.rot
            sizei = self.aryspines[i]
            sizej = self.aryspines[j]
            pt1 = {'x': self.loc['x'] + sizei * math.sin(thetai),
                   'y': self.loc['y'] + sizei * math.cos(thetai)}
            pt2 = {'x': self.loc['x'] + sizej * math.sin(thetaj),
                   'y': self.loc['y'] + sizej * math.cos(thetaj)}
            pt3 = {'x': self.loc['x'], 'y': self.loc['y']}
            arytris.append([pt1, pt2, pt3])

        thetai = (len(self.aryspines)-1) * (2 * math.pi/len(self.aryspines)) + self.rot
        thetaj = self.rot
        sizei = self.aryspines[len(self.aryspines)-1]
        sizej = self.aryspines[0]
        pt1 = {'x': self.loc['x'] + sizei * math.sin(thetai),
               'y': self.loc['y'] + sizei * math.cos(thetai)}
        pt2 = {'x': self.loc['x'] + sizej * math.sin(thetaj),
               'y': self.loc['y'] + sizej * math.cos(thetaj)}
        pt3 = {'x': self.loc['x'], 'y': self.loc['y']}
        arytris.append([pt1, pt2, pt3])
        return arytris

    def check_collision(self, obj):
        arypts = obj.get_points()
        arytris = self.get_triangles()
        for i in arypts:
            for j in arytris:
                if utils.is_point_inside_triangle(j, i):
                    #print('A hit')
                    return True

        return False
