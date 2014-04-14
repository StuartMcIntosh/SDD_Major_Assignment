import pygame, random


#Game Setup
pygame.init()
#Screen
Width = 500
Height = Width
screen = pygame.display.set_mode((Height, Width))
pygame.display.set_caption("Stuart McIntosh-SDD Major Assignment")

#Variables
Game = True
white = (255, 255, 255)


#Game Loop
while Game == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				Game = False
	screen.fill(white)
	pygame.display.update()
	
pygame.quit()