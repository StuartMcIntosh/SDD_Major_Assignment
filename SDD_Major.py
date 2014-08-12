## Stuart McIntosh
## Year 12 Software Design and Development Software Major Project
## Due Date: 12/05/2014

import pygame
pygame.init()

#Variables
#-To run the game loop
Display = True
Game = False
#-Screen
Height = 500
Width = 500
#-Colours used in the program, in (R, G, B) format
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((Height, Width))
screen.fill(white)
pygame.display.set_caption("Yr 12 SDD Major Project-Stuart McIntosh")

#Loads Car graphic for Display
##car = pygame.sprite.Sprite()
##car.image = pygame.image.load('car.png')
##car.rect = car.image.get_rect()
##car_group = pygame.sprite.GroupSingle(car)
##TILE_SIZE = car.rect.width
##numTileWide = Width / TILE_SIZE
##numTileHigh = Height / TILE_SIZE


#Welcome screen text
TextOne = 'Welcome To'
TextTwo = 'Learn Your Road Rules'
TextThree = '-A Game Of Knowledge-'
Continue = 'Press Space Key to Advance'

###Questions Text File
questionsfile = open('questions.txt', 'r')
questions = questionsfile.read()
##questionsfile.close

#Loading text to display
font = pygame.font.Font(None, 40)
##DisplayOne = font.render(TextOne, True, black)
##DisplayOne_View = DisplayOne.get_rect(centerx=Width/2, centery=80)
##DisplayTwo = font.render(TextTwo, True, black)
##DisplayTwo_View = DisplayTwo.get_rect(centerx=Width/2, centery=240)
##DisplayThree = font.render(TextThree, True, black)
##DisplayThree_View = DisplayThree.get_rect(centerx=Width/2, centery=160)
##DisplayContinue = font.render(Continue, True, black)
##DisplayContinue_View = DisplayContinue.get_rect(centerx=Width/2, centery=400)


###Questions Text File
questionsfile = open('questions.txt', 'r')
questions = questionsfile.read()
questionsfile.close

#Test Question/Answer
#-These are to demonstrate how the program will function
#--The final result would be to have the questions loaded from a external text file
#--However, I had trouble loading lines of the text file into an array
TestQuestion = 'Is it necessary to carry your license every time you drive?'
TestAnswerA = 'A-No, Being licensed is enough'
TestAnswerB ='B-Yes all the time'
TestAnswerC = 'C-No, Only for long trips'
UserAnswer = ''
UserPrompt = 'Press the A, B or C key relating to your answer'


#Again, we see how Pygame requires a lot to load text to the screen
font = pygame.font.Font(None, 25)
#-This is the question
DisplayQuestion = font.render(TestQuestion, True, black)
DisplayQuestion_View = DisplayQuestion.get_rect(centerx=Width/2, centery=50)
#-These are the answer options
DisplayA = font.render(TestAnswerA, True, black)
DisplayA_View = DisplayA.get_rect(centerx=Width/2, centery=150)
DisplayB = font.render(TestAnswerB, True, black)
DisplayB_View = DisplayB.get_rect(centerx=Width/2, centery=200)
DisplayC = font.render(TestAnswerC, True, black)
DisplayC_View = DisplayC.get_rect(centerx=Width/2, centery=250)
#-This is the prompt for users to enter there answer choice
font = pygame.font.Font(None, 20)
UserInput = font.render(UserPrompt, True, black)
UserInput_View = UserInput.get_rect(centerx=Width/2, centery=400)


#Win/Lose Screens
font = pygame.font.Font(None, 30)
Win = font.render('Congratulations, You Win!', True, black)
DisplayWin = Win.get_rect(centerx=Width/2, centery=Height/2)
Lose = font.render('Sorry, You Lose', True, black)
DisplayLose = Lose.get_rect(centerx=Width/2, centery=Height/2)

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
##    car_group.draw(screen)
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
        #Test Question Display
        screen.blit(DisplayQuestion, DisplayQuestion_View)
        screen.blit(DisplayA, DisplayA_View)
        screen.blit(DisplayB, DisplayB_View)
        screen.blit(DisplayC, DisplayC_View)
        screen.blit(UserInput, UserInput_View)
        #User Answer Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                UserAnswer = 'TestAnswerA'
            if event.key == pygame.K_b:
                UserAnswer = 'TestAnswerB'
            if event.key == pygame.K_c:
                UserAnswer = 'TestAnswerC'
        #Updates Game Screen Based on User Answer
        #-If User Answers correctly, Win screen is displayed
        if UserAnswer == 'TestAnswerB':
            screen.fill(white)
            screen.blit(Win, DisplayWin)
        #-If User Answers incorrectly, Lose screen is displayed
        elif UserAnswer == 'TestAnswerA' or UserAnswer == 'TestAnswerC':
            screen.fill(white)
            screen.blit(Lose, DisplayLose)
            
    pygame.display.update()
pygame.quit()
