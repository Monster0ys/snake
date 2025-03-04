import pygame
import random

pygame.init()

LEFT=(-1,0)
RIGHT=(1,0)
UP=(0,-1)
DOWN=(0,1)

W = 500
H = 500
FPS=60
W_SNAKE=4
snake_must_grow=40

WHITE=(255, 255, 255)
BLUE=(0,0,255)
RED=(255,0,0)

sc=pygame.display.set_mode((W, H))
sc.fill(WHITE)
clock=pygame.time.Clock()

def opposite(dir):
    return tuple(-i for i in dir)

class Snake_stick():
    def __init__(self,x:int,y:int,horizontal:bool=True):
        self.x:int=x
        self.y:int=y
        self.horizontal:bool=horizontal
    def draw(self,color):
        pygame.draw.line(sc,color,self.get_pos(1),self.get_pos(-1))
    def get_pos(self,n):
        return [self.x+W_SNAKE*int(self.horizontal)*n, self.y+W_SNAKE*int(not self.horizontal)*n]
                                  
lines:list[Snake_stick]=[Snake_stick(W//2-i, H//2, False) for i in range(10)]

direction =[RIGHT]
food=pygame.Rect(random.randint(0,W-(W_SNAKE*2+1)),random.randint(0,H-(W_SNAKE*2+1)),W_SNAKE*2+1,W_SNAKE*2+1)
direction_changes = [None for _ in range(W_SNAKE*2)]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction[-1] != RIGHT:
                direction.append(LEFT)
            elif event.key == pygame.K_RIGHT and direction[-1] != LEFT:
                direction.append(RIGHT)
            elif event.key == pygame.K_UP and direction[-1] != DOWN:
                direction.append(UP)
            elif event.key == pygame.K_DOWN and direction[-1] != UP:
                direction.append(DOWN)
                
    if len(direction)>1 and opposite(direction[1]) not in direction_changes:
        direction_changes.insert(0, direction.pop(0))
        for i in range(W_SNAKE):
            lines[i]=Snake_stick(lines[W_SNAKE].x+(W_SNAKE-i)*direction[0][0], lines[W_SNAKE].y+(W_SNAKE-i)*direction[0][1], direction[0][0]==0)
            lines[W_SNAKE+1+i]=Snake_stick(lines[W_SNAKE].x-(1+i)*direction[0][0], lines[W_SNAKE].y-(1+i)*direction[0][1], direction[0][0]==0)
        lines[W_SNAKE].horizontal=direction[0][0]==0
    else:
        direction_changes.insert(0, None)
    direction_changes.pop()
    lines.insert(0,Snake_stick((lines[0].x+direction[0][0]+W)%W,(lines[0].y+direction[0][1]+H)%H, direction[0][0]==0))
    if food.clipline(lines[0].get_pos(-1),lines[0].get_pos(1)):
        pygame.draw.rect(sc, WHITE, food)
        food=pygame.Rect(random.randint(0,W-(W_SNAKE*2+1)),random.randint(0,H-(W_SNAKE*2+1)),W_SNAKE*2+1,W_SNAKE*2+1)
        snake_must_grow=9
    if snake_must_grow>0:
        snake_must_grow-=1
    else:
        lines[-1].draw(WHITE)
        lines.pop()
    pygame.draw.rect(sc, RED, food)
    for line in lines:
        line.draw(BLUE)
    
    pygame.display.update()

    clock.tick(FPS)