## Stuart McIntosh
## Year 12 Software Design and Development Software Major Project
## Due Date: 09/05/2014

import pygame, random, time, array
pygame.init()


#The variable running the Game while Loop
Game = True

#-Screen
Height = 500
Width = 500

#Colours used in the program, in (R, G, B) format
black = (0, 0, 0)
white = (255, 255, 255)

#Controls the on screen image display and movement
#Car
car = pygame.sprite.Sprite()
car.image = pygame.image.load('pretendcar.gif') #<-- 'pretendcar.gif' to be replaced with actual image later, once a suitable picture is found
car.rect = car.image.get_rect()
car_group = pygame.sprite.GroupSingle(car)
#Tile setup
tileSize = car.rect.width
numTileWide = Width / tileSize
numTileHigh = Height / tileSize

screenX = numTileWide * tileSize
screenY = numTileHigh * tileSize
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Stuart McIntosh-Yr 12 SDD Major Project")


#Manages the text to display on screen, including colour and font
textToDisplay = "Hello"
font = pygame.font.Font(None, 40)
onScreenText = font.render(textToDisplay, True, black)
onScreenText_display = onScreenText.get_rect(centerx=screenX/2, centery=screenY/2)

#-Random Number Generation
##ranNum = random.randint(0, 9)
##number = str(ranNum)

#-Game Loop
while Game == True:
    for event in pygame.event.get():
    #Quit Game
        #Close Button
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.KEYDOWN:
            #Escape Key
            if event.key == pygame.K_ESCAPE:
                Game = False
                
        #Character Movement
            #Move Up-Up Arrow
            if event.key == pygame.K_UP:
                if car.rect.top > 0:
                    car.rect.top -= tileSize
                    
            #Move Down-Down Arrow
            if event.key == pygame.K_DOWN:
                if car.rect.bottom < screenX:                 
                    car.rect.bottom += tileSize
                    
            #Move Right-Right Arrow
            if event.key == pygame.K_RIGHT:
                if car.rect.right < screenY:
                    car.rect.right += tileSize
                    
            #Move Left-Left Arrow
            if event.key == pygame.K_LEFT:
                 if car.rect.left> 0:
                    car.rect.left -= tileSize

    screen.fill(white)
    car_group.draw(screen)
    screen.blit(onScreenText, onScreenText_display)
    pygame.display.update()
    
pygame.quit()


