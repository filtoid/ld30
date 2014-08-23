import pygame
import math
import time
from missile import Missile

class ShipState(object):
    def __init__(self):
        self.ALIVE = 0
        self.DYING = 1
        self.DEAD = 2

SHIPSTATE = ShipState()

class Shard(object):
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.pt1['x'], self.pt1['y']),
                         (self.pt2['x'], self.pt2['y']))

    def update(self):
        pass

class Ship(object):
    def __init__(self, GAME):
        self.loc = {'x': 100, 'y': 100}
        self.rot = 0

        self.GAME = GAME
        self.MAX_SPEED = 2
        self.status = SHIPSTATE.ALIVE

        self.time_between_shots = 1000
        self.speed = 0
        self.acc = 0.01
        self.dec = 0.02
        self.fric = 0.005
        self.last_shot = 0
        self.missiles = []
        self.gun_point = self.loc

        self.dying_count = 100
        self.pieces = []

    def draw(self, screen):

        if self.status == SHIPSTATE.DYING:

            return

        for m in self.missiles:
            m.draw(screen)

        ox = self.GAME.offset['x']
        oy = self.GAME.offset['y']
        pt1 = [20 * math.sin(self.rot) + self.loc['x'] - ox, 20 * math.cos(self.rot) + self.loc['y'] - oy]
        self.gun_point = pt1
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

        if self.status == SHIPSTATE.DYING:

            return

        for m in self.missiles:
            m.update()

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
        else:
            self.speed -= self.fric
            if self.speed < 0:
                self.speed = 0

        if keys[pygame.K_SPACE]:
            if (time.time()*1000) > self.last_shot + self.time_between_shots:
                self.missiles.append(Missile(self.GAME, self, self.gun_point, self.rot))
                self.last_shot = time.time()*1000

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
            noy = self.GAME.height - self.GAME.screen_height

        self.GAME.set_offset(nox, noy)
        self.GAME.check_collisions(self)

    def check_collision(self, obj):
        # Can't hit player ship
        return False

    def remove_missile(self, m):
        if m in self.missiles:
            self.missiles.remove(m)

    def get_points(self):
        pt1 = {'x': self.loc['x'] + 20 * math.sin(self.rot),
               'y': 20 * math.cos(self.rot) + self.loc['y']}
        pt2 = {'x': 12 * math.sin(self.rot + (3 * math.pi / 4)) + self.loc['x'],
               'y': 12 * math.cos(self.rot + (3 * math.pi / 4)) + self.loc['y']}
        pt3 = {'x': 12 * math.sin(self.rot + (5 * math.pi / 4)) + self.loc['x'],
               'y': 12 * math.cos(self.rot + (5 * math.pi / 4)) + self.loc['y']}

        return [pt1, pt2, pt3]

    def kill(self):
        self.status = SHIPSTATE.DYING
        self.pieces.append()

    def has_been_hit(self, obj):
        self.kill()