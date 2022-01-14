from os import path
import random
import pygame
from pygame.constants import K_LEFT, K_RIGHT
pygame.init()

w = 900
h = 600

clock = pygame.time.Clock()
fps = 60

sc = pygame.display.set_mode((w, h))
pygame.display.set_caption('CATCHER')


fone = pygame.image.load('fone.jpg')
fonePlace = fone.get_rect(center=(w//2, h//2))

telega = pygame.image.load('New Piskel.png')
telegaPlace = telega.get_rect(center=(11, 560))

redBall = pygame.image.load('red_ball.png')
redBallPlace = redBall.get_rect(center=(0, 0))

blueBall = pygame.image.load('blue_ball.png')
blueBallPlace = blueBall.get_rect(center=(0, 0))

greenBall = pygame.image.load('green_ball.png')
greenBallPlace = greenBall.get_rect(center=(0, 0))

speed = 8
telegaSpeed = 11

redFlag = False
blueFlag = False
greenFlag = False

randPlace = 0
k = 0
randBall = random.randint(1, 3)

f1 = pygame.font.Font(None, 36)
text1 = f1.render(str(k), True, (180, 0, 0))

gameOver = False    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        if telegaPlace.x > 10:
            telegaPlace.x -= telegaSpeed
    if key[K_RIGHT]:
        if telegaPlace.x < 700:
            telegaPlace.x += telegaSpeed

    
    if randBall == 1:
        if redBallPlace.y < 600:
            redFlag = True
            blueFlag = False
            greenFlag = False
            redBallPlace.x = randPlace
            redBallPlace.y += speed
        else:
            redBallPlace.y = 0
            randPlace = random.randint(0, 850)
            redBallPlace.x = randPlace

            randBall = random.randint(1, 3)

    if randBall == 2:
        if blueBallPlace.y < 600:
            redFlag = False
            blueFlag = True
            greenFlag = False
            blueBallPlace.x = randPlace
            blueBallPlace.y += speed
        else:
            blueBallPlace.y = 0
            randPlace = random.randint(0, 850)
            blueBallPlace.x = randPlace

            randBall = random.randint(1, 3)

    if randBall == 3:
        if greenBallPlace.y < 600:
            redFlag = False
            blueFlag = False
            greenFlag = True
            greenBallPlace.x = randPlace
            greenBallPlace.y += speed
        else:
            greenBallPlace.y = 0
            randPlace = random.randint(0, 850)
            greenBallPlace.x = randPlace

            randBall = random.randint(1, 3)


    if telegaPlace.collidepoint(redBallPlace.center):
        redBallPlace.y = 0
        randPlace = random.randint(0, 850)
        redBallPlace.x = randPlace
        k += 10
        print('You win:' + str(k))

        randBall = random.randint(1, 3)
        text1 = f1.render(str(k), True, (180, 0, 0))    

    #Blue
    if telegaPlace.collidepoint(blueBallPlace.center):
        blueBallPlace.y = 0
        randPlace = random.randint(0, 850)
        blueBallPlace.x = randPlace
        k += 15
        print('You win:' + str(k))

        randBall = random.randint(1, 3)
        text1 = f1.render(str(k), True, (180, 0, 0))

    
    #green
    if telegaPlace.collidepoint(greenBallPlace.center):
        greenBallPlace.y = 0
        randPlace = random.randint(0, 850)
        greenBallPlace.x = randPlace
        k += 5
        print('You win:' + str(k)) 

        randBall = random.randint(1, 3)
        text1 = f1.render(str(k), True, (180, 0, 0))       

    sc.blit(fone, fonePlace)
    sc.blit(telega, telegaPlace)
    
    if redFlag == True:
        sc.blit(redBall, redBallPlace)
    if blueFlag == True:
        sc.blit(blueBall, blueBallPlace)
    if greenFlag == True:
        sc.blit(greenBall, greenBallPlace)

    sc.blit(text1, (10, 50))

    pygame.display.update()
    clock.tick(fps)          