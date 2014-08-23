import pygame
import math
# import main

class Ship(object):
    def __init__(self, GAME):
        self.loc = {'x': 100, 'y': 100}
        self.rot = 0
        self.GAME = GAME

        self.MAX_SPEED = 2
        self.speed = 0
        self.acc = 0.01
        self.dec = 0.02

    def draw(self, screen):

        ox = self.GAME.offset['x']
        oy = self.GAME.offset['y']
        pt1 = [20 * math.sin(self.rot) + self.loc['x'] - ox , 20 * math.cos(self.rot) + self.loc['y'] - oy]
        pt2 = [12 * math.sin(self.rot + (3 * math.pi / 4)) + self.loc['x'] - ox,
               12 * math.cos(self.rot + (3 * math.pi / 4)) + self.loc['y'] - oy]
        pt3 = [12 * math.sin(self.rot + (5 * math.pi / 4)) + self.loc['x'] - ox,
               12 * math.cos(self.rot + (5 * math.pi / 4)) + self.loc['y'] - oy]

        pygame.draw.line(screen, (255, 255, 255), (pt1[0], pt1[1]),
                         (pt2[0], pt2[1]))
        pygame.draw.line(screen, (255, 255, 255), (pt2[0], pt2[1]),
                         (self.loc['x']-ox, self.loc['y']-oy))
        pygame.draw.line(screen, (255, 255, 255), (self.loc['x']-ox, self.loc['y']-oy),
                         (pt3[0], pt3[1]))
        pygame.draw.line(screen, (255, 255, 255), (pt3[0], pt3[1]),
                         (pt1[0], pt1[1]))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rot += 0.01

        if keys[pygame.K_d]:
            self.rot -= 0.01

        if keys[pygame.K_w]:
            self.speed += self.acc
            if self.speed > self.MAX_SPEED:
                self.speed = self.MAX_SPEED
        elif keys[pygame.K_s]:
            self.speed -= self.dec
            if self.speed < 0:
                self.speed = 0

        # Update rotation
        if self.rot > 2 * math.pi:
            self.rot -= 2 * math.pi
        elif self.rot < 0:
            self.rot -= 2 * math.pi

        # Update location
        if self.speed > 0:
            self.loc['x'] += self.speed * (math.sin(self.rot))
            self.loc['y'] += self.speed * (math.cos(self.rot))

        if self.loc['x'] > self.GAME.width:
            self.loc['x'] = self.GAME.width
        if self.loc['y'] > self.GAME.height:
            self.loc['y'] = self.GAME.height
        if self.loc['x'] < 0:
            self.loc['x'] = 0
        if self.loc['y'] < 0:
            self.loc['y'] = 0

        # Update the screen offset
        nox = 0
        noy = 0
        if self.loc['x'] > (self.GAME.screen_width/2):
            nox = self.loc['x'] - (self.GAME.screen_width/2)

        if self.loc['x'] > self.GAME.width - (self.GAME.screen_width/2):
            nox = self.GAME.width - self.GAME.screen_width

        if self.loc['y'] > (self.GAME.screen_height/2):
            noy = self.loc['y'] - (self.GAME.screen_height/2)

        if self.loc['y'] > self.GAME.height - (self.GAME.screen_height/2):
            nox = self.GAME.height - self.GAME.screen_height

        self.GAME.set_offset(nox, noy)
