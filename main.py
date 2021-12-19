from fpoints import *
from sci_cal2 import *
import random
import pygame as pg
import pygame.gfxdraw
pg.init()
win = pg.display.set_mode((1200,700))
pg.display.set_caption('Graphing Calculator')
run = True

points = []

colours = [(0,128,255),(153,0,0),(102,204,0),(153,0,153),(255,255,0)]
functions = [f(y) for y in functions]
for i in functions:
    points.append(i.generate_points())
def filled_aacircle(win,x,y,r,colour):
    pg.gfxdraw.aacircle(win,x,y,r,colour)
    pg.gfxdraw.filled_circle(win,x,y,r,colour)

def plot_graph(points,count):
        for i in range(len(points)):
            c = colours[i]
            for j in points[i][0:count]:
                #pg.gfxdraw.pixel(win,int(i[0]*50)+600,int(i[1]*50)+350,(0,0,0))
                filled_aacircle(win,j[0],j[1],1,c)

numFont = pg.font.Font('freesansbold.ttf',15)
def num_text(x,y,num):
    numText = numFont.render("{num}".format(num = num),True,(0,0,0))
    win.blit(numText,((x*50+600),(-y*50+350)))

def drawGrid():
    for x in range(0,24):
        pg.gfxdraw.vline(win,x*50,0,700,(153,153,153))
    for y in range(0,14):
        pg.gfxdraw.hline(win,0,1200,y*50,(153,153,153))
    #y-axis
    pg.gfxdraw.hline(win,0,1200,350,(153,0,0))
    #x-axis
    pg.gfxdraw.vline(win,600,0,700,(153,0,0))





def numberLineX():
    for i in range(-12,13):
        num_text(i,0,i)

def numberLineY():
    for i in range(-7,8):
        num_text(0,i,i)

keyFont = pg.font.Font('freesansbold.ttf',25)
keyState = 'Hidden'
keyString = 'Show Key'
def keyBut(text):
    pg.draw.rect(win,(155,0,0),(50,50,200,35),0)
    keyText = keyFont.render("{text}".format(text = text),True,(255,255,255))
    win.blit(keyText,(85,55))

def showKey():
    if keyState == 'Shown':
        pg.draw.rect(win,(255,255,255),(50,85,200,200),0)
        pg.draw.rect(win,(155,0,0),(50,85,200,200),2)

        for i in range(len(functions)):
            pg.draw.rect(win,(0,0,0),(65,95+i*35,35,30),2)
            #pg.gfxdraw.hline(win,65,110,(95+i*35)+20,colours[i])
            pg.draw.rect(win,colours[i],(65,95+i*35+13,35,2),0)

            showKeyFont = pg.font.Font('freesansbold.ttf',15)
            showKeyText = showKeyFont.render("y = {text}".format(text = (functions[i].func).replace('{x}','x')),True,(0,0,0))
            win.blit(showKeyText,(105,95+i*35+7))


def reDrawWindow():
    win.fill((255,255,255))
    drawGrid()
    numberLineX()   
    numberLineY()
    
    keyBut(keyString)
    showKey()

def distance(x1,y1,x2,y2):
    return pow(pow((x2-x1),2) + pow((y2-y1),2),0.5)
 
def show_pos(win,x,y):
    pg.gfxdraw.box(win,(x,y,5,10),(255,0,0))

left = 0
right = 0
n = 0
count = 0
start = False
while run:
    reDrawWindow()
    if start:
        plot_graph(points,count)
        n += 1
        count += 1*n
    pg.display.update()
    x,y = pygame.mouse.get_pos()
    if keyState == 'Hidden':
        keyString = 'Show Key'
    else:
        keyString = 'Hide Key'
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and 50 <= x <= 250 and 50 <= y <= 85:
                if keyState == 'Hidden':
                    keyState = 'Shown'
                else:
                    keyState = 'Hidden'
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                start = True
                


          
pg.quit()


