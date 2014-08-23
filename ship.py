import pygame


class Ship(object):
	def __init__(self):
		self.loc = {'x': 100, 'y': 100}
		self.rot = 0
		
	def draw(self, screen):
		pygame.draw.line(screen, (255, 255, 255), (self.loc['x'], self.loc['y']),
			(self.loc['x']+100, self.loc['y']))
		
	def update(self):
		pass