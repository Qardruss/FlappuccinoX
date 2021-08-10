import pygame

class Bean: 
	def __init__(self):
		# Load the bean sprite
		self.sprite = pygame.image.load('data/gfx/bean.png')

		# Handle the position of the bean
		self.position = pygame.Vector2()
		self.position.xy