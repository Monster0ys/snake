import pygame
pygame.init()

class Snake_stick():
    def __init__(self,x:int,y:int,horizontal:bool=True):
        self.x:int=x
        self.y:int=y
        self.horizontal:bool=horizontal
W = 500
H = 500
w_snake=4
lines:list[Snake_stick]=[]
for i in range(50):
    lines.append(Snake_stick(W//2-i, H//2, False))

sc=pygame.display.set_mode((W, H))
WHITE=(255, 255, 255)
BLUE=(0,0,255)

FPS=60
clock=pygame.time.Clock()

speed=1
direction ="RIGHT"


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction="LEFT"
                for i in range(w_snake):
                    lines[i].x=lines[w_snake].x-w_snake+i
                    lines[i].y=lines[w_snake].y
                    lines[w_snake+1+i].x=lines[w_snake].x+1+i
                    lines[w_snake+1+i].y=lines[w_snake].y
                    lines[i].horizontal=False
                    lines[w_snake+1+i].horizontal=False
                lines[w_snake].horizontal=False
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction="RIGHT"
                for i in range(w_snake):
                    lines[i].x=lines[w_snake].x+w_snake-i
                    lines[i].y=lines[w_snake].y
                    lines[w_snake+1+i].x=lines[w_snake].x-1-i
                    lines[w_snake+1+i].y=lines[w_snake].y
                    lines[i].horizontal=False
                    lines[w_snake+1+i].horizontal=False
                lines[w_snake].horizontal=False
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction="UP"
                for i in range(w_snake):
                    lines[i].x=lines[w_snake].x
                    lines[i].y=lines[w_snake].y-w_snake+i
                    lines[w_snake+1+i].x=lines[w_snake].x
                    lines[w_snake+1+i].y=lines[w_snake].y+1+i
                    lines[i].horizontal=True
                    lines[w_snake+1+i].horizontal=True
                lines[w_snake].horizontal=True
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction="DOWN"
                for i in range(w_snake):
                    lines[i].x=lines[w_snake].x
                    lines[i].y=lines[w_snake].y+w_snake-i
                    lines[w_snake+1+i].x=lines[w_snake].x
                    lines[w_snake+1+i].y=lines[w_snake].y-1-i
                    lines[i].horizontal=True
                    lines[w_snake+1+i].horizontal=True
                lines[w_snake].horizontal=True

    if direction == "LEFT":
        lines.insert(0,Snake_stick(lines[0].x-1,lines[0].y, False))
    elif direction =="RIGHT":
        lines.insert(0,Snake_stick(lines[0].x+1,lines[0].y, False))
    elif direction =="UP":
        lines.insert(0,Snake_stick(lines[0].x,lines[0].y-1, True))
    elif direction =="DOWN":
        lines.insert(0,Snake_stick(lines[0].x,lines[0].y+1, True))
    lines.pop()

    sc.fill(WHITE)
    for i in range(len(lines)):
        if lines[i].horizontal:
            pygame.draw.line(sc, BLUE, [lines[i].x+w_snake, lines[i].y], [lines[i].x-w_snake, lines[i].y])
        else:
            pygame.draw.line(sc, BLUE, [lines[i].x, lines[i].y+w_snake], [lines[i].x, lines[i].y-w_snake])
    # pygame.draw.rect(sc, BLUE, (x, y, 15, 15))
    pygame.display.update()

    clock.tick(FPS)