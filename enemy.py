__author__ = 'fil'

from ship import ShipState
import math
import pygame

class EnemyShip(object):
    def __init__(self, game, path):
        self.GAME = game
        self.status = ShipState.ALIVE
        self.path_ary = path

        self.loc = {'x': self.path_ary[0]['x'], 'y': self.path_ary[0]['y']}
        self.cur_path_num = 0
        self.pieces = []
        self.missiles = []
        self.rot = self.path_ary[0]['rot']
        self.turn_speed = 0.01
        self.SPEED = 0.2

    def draw(self, screen):

        if self.status == ShipState.DYING:
            for shard in self.pieces:
                shard.draw(screen, self.GAME.offset)
            return

        for m in self.missiles:
            m.draw(screen)

        ox = self.GAME.offset['x']
        oy = self.GAME.offset['y']
        pt1 = [20 * math.sin(self.rot) + self.loc['x'] - ox, 20 * math.cos(self.rot) + self.loc['y'] - oy]

        self.gun_point = {'x': pt1[0], 'y': pt1[1]}

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
        ch = {'x': self.path_ary[self.cur_path_num]['x'],
              'y': self.path_ary[self.cur_path_num]['y'],
              'rot': self.path_ary[self.cur_path_num]['rot']}

        if self.rot != ch['rot']:
            if self.rot < ch['rot']:
                self.rot += self.turn_speed
                if self.rot >= math.pi * 2:
                    self.rot -= math.pi * 2

                if self.rot >= ch['rot']:
                    self.rot = ch['rot']
            else:
                self.rot -= self.turn_speed
                if self.rot < 0:
                    self.rot += math.pi * 2

                if self.rot <= ch['rot']:
                    self.rot = ch['rot']

        else:
            if self.loc['x'] < ch['x']:
                self.loc['x'] += self.SPEED
                if self.loc['x'] >= ch['x']:
                    self.loc['x'] = ch['x']
            elif self.loc['x'] > ch['x']:
                self.loc['x'] -= self.SPEED
                if self.loc['x'] <= ch['x']:
                    self.loc['x'] = ch['x']

            if self.loc['y'] < ch['y']:
                self.loc['y'] += self.SPEED
                if self.loc['y'] >= ch['y']:
                    self.loc['y'] = ch['y']
            elif self.loc['y'] > ch['y']:
                self.loc['y'] -= self.SPEED
                if self.loc['y'] <= ch['y']:
                    self.loc['y'] = ch['y']

            if self.loc['x'] == ch['x'] and self.loc['y'] == ch['y']:
               self.cur_path_num += 1
                if self.cur_path_num >= len(self.path_ary):
                    self.cur_path_num = 0

                print(self.path_ary)

    def check_collision(self, obj):
        return False