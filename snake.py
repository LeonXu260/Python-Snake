# Snake Game
# By LeonXu260
import pygame,random
from pygame.locals import *
from sys import exit
import math
 
#just some declarations
level=25 #5 easy 20 medium 50 hard
fps=20 #the higher the fps, the harder is the game
il=10 #the initial length of the snake
windowtiles=50 #number of blocks that fit on the screen. Count starts from 0. The bigger the number of tiles, the bigger will be the window
blockwidth=15 #size of one block in pixel. It may be snake body or food or obstacles
 
winsize=blockwidth*windowtiles
 
WHITE =(255, 255, 255)
BLACK =(  0,  0,  0)
RED   =(255,  0,  0)
GREEN =(  0, 255, 0)
DARKGREEN = ( 0, 255, 0)
DARKGRAY = ( 40, 40, 40)
BODYCOLOR =(100, 200, 150)
FOODCOLOR =(200,  23,  23)
OBSCOLOR  =( 23,  23, 200)
 
#direction of snake
left=-1,0
right=1,0
up=0,-1
down=0,1
 
snake=[(0,0)]*il
foodpos=(0,0)
newdirection=direction=right #snake is moving right by default
score=0
obstacles=[]
for i in range(1,level):
    lo=random.randrange(1,windowtiles),random.randrange(1,windowtiles) #last obstacle
    obstacles.append(lo)
    for j in range(1,random.randint(1,int(level/2))):
        if(random.randint(1,2) == 1):
            lo=(lo[0]+1,lo[1])
        else:
            lo=(lo[0],lo[1]+1)
        if( 0<lo[0]<=windowtiles and 0<lo[1]<=windowtiles ):
            obstacles.append(lo)
def rendertext(surface,text):
    font = pygame.font.Font(None, 22)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=surface.get_width()/2,y=winsize+blockwidth)
    surface.blit(text, textpos)
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('vtks encantar.ttf', 18)
    pygame.display.set_caption('Icy Snake')
    

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press UP, DOWN, LEFT, RIGHT arrow key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 500, WINDOWHEIGHT - 50)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
def matchcheat(cheatstr,code):
    if len(cheatstr)<len(code):
        return False
    if( cheatstr[-len(code):]==code):
        return True
    return False
cheat=""
if(__name__ == "__main__"):
    pygame.init()
    screen = pygame.display.set_mode((winsize,winsize+35))
    pygame.display.set_caption('Python Snake')
    dead=False
    clock = pygame.time.Clock()
    while dead==False:    
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if direction != down:
                        newdirection=up
                elif event.key == K_DOWN:
                    if direction != up:
                        newdirection=down
                elif event.key == K_LEFT:
                    if direction != right:
                        newdirection=left
                elif event.key == K_RIGHT:
                    if direction != left:
                        newdirection=right
                else:
                    cheat=cheat+event.unicode
                    if matchcheat(cheat,"getmorescore"):
                        score+=99999
                    elif matchcheat(cheat,"longlongsnake"):
                        snake=snake+snake[2:]*2
                    elif matchcheat(cheat,"doublemyscore"):
                        score*=2
                    elif matchcheat(cheat,"noobstacles"):
                        obstacles=[]
                    
        screen.fill(BLACK);
        #update the snake
        #check if there is food
        direction=newdirection
        if(foodpos == (0,0)):
            foodpos=random.randrange(1,windowtiles),random.randrange(1,windowtiles)
            while (foodpos in snake or foodpos in obstacles):
                foodpos=random.randrange(1,windowtiles),random.randrange(1,windowtiles)
        #update the snake
        head=snake[0]#head of snake
        head=(head[0]+direction[0],head[1]+direction[1])
        #wrap the snake around the window
        headx=windowtiles if head[0]<0 else 0 if head[0]>windowtiles else head[0]
        heady=windowtiles if head[1]<0 else 0 if head[1]>windowtiles else head[1]
        head=(headx,heady)
        if head in snake or head in obstacles:
            screen.fill(BLACK); #remove the score
            rendertext(screen,"You lose...Your score is "+str(score))
            dead=True
        else:
            if(head==foodpos):
                foodpos=0,0
                score+=5
                snake.append(head)
            rendertext(screen,"Score : "+str(score))
        snake=[head]+[snake[i-1] for i in range(1,len(snake))]
        #draw world
        pygame.draw.rect(screen,FOODCOLOR,(foodpos[0]*blockwidth,foodpos[1]*blockwidth,blockwidth,blockwidth),0)
        for block in snake:
            pygame.draw.rect(screen,BODYCOLOR,(block[0]*blockwidth,block[1]*blockwidth,blockwidth,blockwidth),0)
        for block in obstacles:
            pygame.draw.rect(screen,OBSCOLOR,(block[0]*blockwidth,block[1]*blockwidth,blockwidth,blockwidth),0)
        pygame.display.update()
    while True: #wait till the user clicks close button
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit();exit()

