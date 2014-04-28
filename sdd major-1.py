## Stuart McIntosh
## Year 12 Software Design and Development Software Major Project
## Due Date: 09/05/2014

import pygame, random, time, array

pygame.init()

#Variable that runs the main Game Loop
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

#-Random Number Generation
ranNum = str(random.randint(0, 9))

#Manages the text to display on screen, including colour and font
textToDisplay = ranNum
font = pygame.font.Font(None, 40)
onScreenText = font.render(textToDisplay, True, black)
onScreenText_display = onScreenText.get_rect(centerx=screenX/2, centery=screenY/2)

#Movement
s = 'stop'
u = 'up'
r = 'right'
d = 'down'
l = 'left'
movedir = s


Questions Text File
qtf = open('questions.txt')
questions = array.array('c')
qs = str(qtf)
l = len(qs)
questions.fromfile(qtf, 375)
ql = list(qtf)




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
    #Arrow Key Movement
            #Up Key
            if event.key == pygame.K_UP:
                movedir = u
            #Right Key
            if event.key == pygame.K_RIGHT:
                movedir = r
            #Down Key
            if event.key == pygame.K_DOWN:
                movedir = d
            #Left Key
            if event.key == pygame.K_LEFT:
                movedir = l
        else:
            movedir = s

    if movedir == u:
        if car.rect.top > 0:
            car.rect.top -= 1
            time.sleep(0.005)
    if movedir == r:
         if car.rect.right < screenY:
             car.rect.right += 1
             time.sleep(0.005)
    if movedir == d:
        if car.rect.bottom < screenX:
            car.rect.bottom += 1
            time.sleep(0.005)
    if movedir == l:
          if car.rect.left > 0:
             car.rect.left -= 1
             time.sleep(0.005)

    screen.fill(white)
    car_group.draw(screen)
    screen.blit(onScreenText, onScreenText_display)
    pygame.display.update()
pygame.quit()

