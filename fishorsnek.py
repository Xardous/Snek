 #credits to freecodecamp for assistance with some aspects
import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (7,155,253)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Return of Scylla')

#img = snake
#fishimg =  orange fish (1 point)
#rarefishimg = the blue fish (2 points)
#pufferfish = the pufferfish
img = pygame.image.load('/Users/tanishsatre/Desktop/pygame games/Resources/Images/Webp.net-resizeimage.png')
fishimg = pygame.image.load('/Users/tanishsatre/Desktop/pygame games/Resources/Images/orangefish.png')
rarefishimg = pygame.image.load('/Users/tanishsatre/Desktop/pygame games/Resources/Images/bluefish.png')
pufferfish = pygame.image.load('/Users/tanishsatre/Desktop/pygame games/Resources/Images/puffer.png')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = "right"

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            gameDisplay.fill(blue)
        message_to_screen("Return to the battle!",
                          black,
                          -100,
                          size="large")

        message_to_screen("Press C to continue or Q to give up.",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)

        


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            
   
        gameDisplay.fill(blue)
        message_to_screen(" Return Of Scylla",
                          green,
                          -100,
                          "large")
        message_to_screen("You have been awakened from your great slumber! eat all the fish as revenge!",
                          green,
                          -30)

        message_to_screen("The more fish you eat, the longer you get",
                          green,
                          10)

        message_to_screen("If you run into yourself, or the edges,oryou will die",
                          green,
                          50)
        
        message_to_screen("Blue fish give you twice as more length,eating the pufferfish will kill you.",
                          green,
                          30)

        message_to_screen("Press C to start or try again or Q to exit or P to pause.Made by Tanish",
                          green,
                          180)
    
        pygame.display.update()
        clock.tick(15)
        

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

FishApple = 30

def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-AppleThickness))
    randAppleY = round(random.randrange(0, display_height-AppleThickness))
    randAppleA = round(random.randrange(0, display_height-AppleThickness))
    randAppleB = round(random.randrange(0, display_height-AppleThickness))
    randAppleV = round(random.randrange(0, display_height-AppleThickness))
    randAppleU = round(random.randrange(0, display_height-AppleThickness))
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(blue)
            message_to_screen("RIP",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                        pause()
        

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(blue)

        
        

        gameDisplay.blit(fishimg,(randAppleX, randAppleY))
        gameDisplay.blit(rarefishimg,(randAppleA,randAppleB))
        gameDisplay.blit(pufferfish, (randAppleV,randAppleU))
        gameDisplay.blit(pufferfish, (randAppleV,randAppleU))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        
        snake(block_size, snakeList)

        
        pygame.display.update()



        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width-AppleThickness))
                randAppleY = round(random.randrange(0, display_height-AppleThickness))
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width-AppleThickness))
                randAppleY = round(random.randrange(0, display_height-AppleThickness))
                snakeLength += 1

        if lead_x > randAppleA and lead_x < randAppleA + AppleThickness or lead_x + block_size > randAppleA and lead_x + block_size < randAppleA + AppleThickness:

            if lead_y > randAppleB and lead_y < randAppleB + AppleThickness:
                randAppleA = round(random.randrange(0, display_width-AppleThickness))
                randAppleB = round(random.randrange(0, display_height-AppleThickness))
                snakeLength += 2

            elif lead_y + block_size > randAppleB and lead_y + block_size < randAppleB + AppleThickness:

                    randAppleA = round(random.randrange(0, display_width-AppleThickness))
                    randAppleB = round(random.randrange(0, display_height-AppleThickness))
                    snakeLength += 2

        if lead_x > randAppleV and lead_x < randAppleV + AppleThickness or lead_x + block_size > randAppleV and lead_x + block_size < randAppleV + AppleThickness:

            if lead_y > randAppleU and lead_y < randAppleU + AppleThickness:
                gameOver = True

            elif lead_y + block_size > randAppleU and lead_y + block_size < randAppleU + AppleThickness:
                gameOver = True

                    

            
                    

                    

                
                


        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()
