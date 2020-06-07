import pygame
import random
import time

pygame.init()

gameDisplay=pygame.display.set_mode((600,600))

pygame.display.set_caption("Flappy Bird")

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
aquamarine2=(118,238,198)

topx=300
topy=0

bottomx=300
bottomy=400

birdx=100
birdy=300

bottomychange=200
topychange=200

score=0

clock=pygame.time.Clock()

changedet=random.randint(0,1)

gameOver=False
gg=False

background=pygame.image.load("flappybackground.jpg")
background=pygame.transform.scale(background,(800,800))

flappybird=pygame.image.load("flappybird.png")
flappybird=pygame.transform.scale(flappybird,(40,40))

pipedown=pygame.image.load("flappypipedown.png")
pipedown=pygame.transform.scale(pipedown,(300,200))

pipeup=pygame.image.load("flappypipeup.png")
pipeup=pygame.transform.scale(pipeup,(300,200))

def text(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Comic Sans MS', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))
    

def textAriel(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Ariel', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))

pygame.display.update()
while True:

    pygame.display.update()
    textAriel(str(int(score*0.5)), 570,580,black,10)
    gameDisplay.blit(background,(0,0))

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT: 
            pygame.quit()
            quit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and gameOver==False:
                birdy-=40

    clock.tick(200)

    if changedet==0 and topx==500 and gameOver==False: 
        topychange=random.randint(200,375)
        bottomychange=random.randint(150,525-topychange)
        pipedown=pygame.transform.scale(pipedown,(300,bottomychange))
        pipeup=pygame.transform.scale(pipeup,(300,topychange))
        print(topychange, "and", bottomychange)
        changedet=1

    elif changedet==1 and topx==500 and gameOver==False:
        bottomychange=random.randint(200,375)
        topychange=random.randint(150,525-bottomychange)
        pipedown=pygame.transform.scale(pipedown,(300,bottomychange))
        pipeup=pygame.transform.scale(pipeup,(300,topychange))
        print(topychange, "and", bottomychange)
        changedet=0
        
    
    gameDisplay.blit(pipedown,(bottomx,600-bottomychange))
    gameDisplay.blit(flappybird,(birdx,birdy))
    gameDisplay.blit(pipeup,(topx,topy))
    if topx>-200 and bottomx>-200 and gameOver==False:
        topx=topx-1
        bottomx-=1
    elif topx==-200 and bottomx==-200 and gameOver==False:
        topx=500
        bottomx=500
    if birdy<=560 and gameOver==False:
        birdy+=1

    if (topy<=birdy<=topy+topychange-5 and topx+110<=birdx+20<=topx+190) or (600-bottomychange<=birdy+20<=600 and bottomx+110<=birdx+20<=bottomx+190) or birdy==0 or birdy==560:
        textAriel("Game Over", 400, 300, black, 30)
        textAriel("Your Score:", 400,325,black,20)
        textAriel((str(int(score*0.5))), 400,350,black,20)
        gameOver=True
        gg=True
    elif (birdx+20==topx+200 and birdy>topy+topychange) or (birdx==bottomx+200 and birdy<600-bottomychange):
        score+=1
        print(score)

    textAriel(str(int(score*0.5)), 570,580,white,20)
