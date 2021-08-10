import pygame

class Player:
	# Player position
	position = pygame.Vector2()
	position.xy = 295, 100

	# Player velocity & Acceleration
	velocity = pygame.Vector2()
	velocity.xy = 3, 0
	acceleration = 0.1

	# Player sprites
	rightSprite = pygame.image.load('data/gfx/player.png')
	leftSprite = pygame.transform.flip(rightSprite, True, False)

	# The current Player sprite
	currentSprite = rightSprite
