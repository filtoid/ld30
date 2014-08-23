import pygame
import math

class Ship(object):
	def __init__(self):
		self.loc = {'x': 100, 'y': 100}
		self.rot = 0
		
	def draw(self, screen):
		
		pt1 = [20 * math.sin(self.rot) + self.loc['x'], 20 * math.cos(self.rot) + self.loc['y']]
		pt2 = [10 * math.sin(self.rot +  (3*(math.pi)/4)) + self.loc['x'], 
				10 * math.cos(self.rot + (3 *(math.pi)/4)) + self.loc['y']]
		pt3 = [10 * math.sin(self.rot +  (5*(math.pi)/4)) + self.loc['x'], 
				10 * math.cos(self.rot + (5 *(math.pi)/4)) + self.loc['y']]
		
		pygame.draw.line(screen, (255, 255, 255), (pt1[0], pt1[1]),
			(pt2[0],pt2[1]))
		pygame.draw.line(screen, (255, 255, 255), (pt2[0], pt2[1]),
			(self.loc['x'], self.loc['y']))
		pygame.draw.line(screen, (255, 255, 255), (self.loc['x'], self.loc['y']),
			(pt3[0],pt3[1]))
		pygame.draw.line(screen, (255, 255, 255), (pt3[0], pt3[1]),
			(pt1[0],pt1[1]))
		
	def update(self):
		pass