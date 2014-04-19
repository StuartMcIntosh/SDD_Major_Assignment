## Stuart McIntosh
## Year 12 Software Dessign and Development Software Major Project
## Due: 09/05/2014

import pygame, random, time

pygame.init()

#-Game Control
Game = True

#-Screen
Height = 500
Width = 500
screenSize = (Height, Width)

#-PyGame Window
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Stuart McIntosh-Yr 12 SDD Major Project")

#-Colours
black = (0, 0, 0)
white = (255, 255, 255)

#-Random Number Generation
##ranNum = random.randint(0, 9)
##number = str(ranNum)

#-On Screen Text
textToDisplay = "Hello, how are you?"
font = pygame.font.Font(None, 40)
onScreenText = font.render(textToDisplay, True, black)
onScreenText_display = onScreenText.get_rect(centerx=Width/2, centery=Height/2)

#-Game Loop
while Game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game = False
    
    screen.fill(white)
    screen.blit(onScreenText, onScreenText_display)
    pygame.display.update()
    
pygame.quit()
