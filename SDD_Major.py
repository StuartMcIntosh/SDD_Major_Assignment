## Stuart McIntosh
## Year 12 Software Design and Development Software Major Project
## Due Date: 09/05/2014

import pygame
pygame.init()

#Variables
# to run the game loop
Display = True
Game = False
#Screen
Height = 500
Width = 500
#Colours used in the program, in (R, G, B) format
black = (0, 0, 0)
white = (255, 255, 255)

car = pygame.sprite.Sprite()
car.image = pygame.image.load('car.png')
car.rect = car.image.get_rect()
car_group = pygame.sprite.GroupSingle(car)
TILE_SIZE = car.rect.width
numTileWide = Width / TILE_SIZE
numTileHigh = Height / TILE_SIZE
screen = pygame.display.set_mode((Height, Width))

##
TextOne = 'Welcome To'
TextTwo = 'Learn Your Road Rules'
TextThree = '-A Game Of Learning-'
Continue = 'Press Space Key to Advance'

font = pygame.font.Font(None, 40)
DisplayOne = font.render(TextOne, True, black)
DisplayOne_View = DisplayOne.get_rect(centerx=Width/2, centery=80)
DisplayTwo = font.render(TextTwo, True, black)
DisplayTwo_View = DisplayTwo.get_rect(centerx=Width/2, centery=240)
DisplayThree = font.render(TextThree, True, black)
DisplayThree_View = DisplayThree.get_rect(centerx=Width/2, centery=160)
DisplayContinue = font.render(Continue, True, black)
DisplayContinue_View = DisplayContinue.get_rect(centerx=Width/2, centery=400)
pygame.display.set_caption("Yr 12 SDD Major Project-Stuart McIntosh")
screen.fill(white)

###Questions Text File
##qtf = open('questions.txt', 'r')

TestQuestion = 'Is it necessary to carry your license every time you drive?'
TestAnswerA = 'A-No, Being licensed is enough'
TestAnswerB ='B-Yes all the time'
TestAnswerC = 'C-No, Only for long trips'
CorrectAnswer = 'B-Yes all the time'
UserAnswer = ''

font = pygame.font.Font(None, 25)
DisplayQuestion = font.render(TestQuestion, True, black)
DisplayQuestion_View = DisplayQuestion.get_rect(centerx=Width/2, centery=80)
DisplayA = font.render(TestAnswerA, True, black)
DisplayA_View = DisplayA.get_rect(centerx=Width/2, centery=240)
DisplayB = font.render(TestAnswerB, True, black)
DisplayB_View = DisplayB.get_rect(centerx=Width/2, centery=320)
DisplayC = font.render(TestAnswerC, True, black)
DisplayC_View = DisplayC.get_rect(centerx=Width/2, centery=400)


#-Game Loop
while Display == True:
    for event in pygame.event.get():
    #Quit Game
      #Close Button
        if event.type == pygame.QUIT:
            Display = False
        if event.type == pygame.KEYDOWN:
          #Escape Key
            if event.key == pygame.K_ESCAPE:
                Display = False
        
    screen.fill(white)
    car_group.draw(screen)
    screen.blit(DisplayOne, DisplayOne_View)
    screen.blit(DisplayTwo, DisplayTwo_View)
    screen.blit(DisplayThree, DisplayThree_View)
    screen.blit(DisplayContinue, DisplayContinue_View)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            screen.fill(white)
            Game = True

    if Game == True:
        screen.fill(white)
        screen.blit(DisplayQuestion, DisplayQuestion_View)
        screen.blit(DisplayA, DisplayA_View)
        screen.blit(DisplayB, DisplayB_View)
        screen.blit(DisplayC, DisplayC_View)


    pygame.display.update()

pygame.quit()
