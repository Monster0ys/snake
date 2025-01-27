import pygame
pygame.init()
LEFT="LEFT"
RIGHT="RIGHT"
UP="UP"
DOWN="DOWN"
opposite_direction={
    LEFT:RIGHT,
    RIGHT:LEFT,
    UP:DOWN,
    DOWN:UP
}

class Snake_stick():
    def __init__(self,x:int,y:int,horizontal:bool=True):
        self.x:int=x
        self.y:int=y
        self.horizontal:bool=horizontal
W = 500
H = 500
W_SNAKE=4
lines:list[Snake_stick]=[]
for i in range(50):
    lines.append(Snake_stick(W//2-i, H//2, False))

sc=pygame.display.set_mode((W, H))
WHITE=(255, 255, 255)
BLUE=(0,0,255)

FPS=60
clock=pygame.time.Clock()

speed=1
direction =[RIGHT]
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
                
    if len(direction)>1 and opposite_direction[direction[1]] not in direction_changes:
        direction_changes.insert(0, direction.pop(0))
        if direction[0] == LEFT:
            for i in range(W_SNAKE):
                lines[i]=Snake_stick(lines[W_SNAKE].x-W_SNAKE+i, lines[W_SNAKE].y, False)
                lines[W_SNAKE+1+i]=Snake_stick(lines[W_SNAKE].x+1+i, lines[W_SNAKE].y, False)
            lines[W_SNAKE].horizontal=False
        elif direction[0] == RIGHT:
            for i in range(W_SNAKE):
                lines[i]=Snake_stick(lines[W_SNAKE].x+W_SNAKE-i, lines[W_SNAKE].y, False)
                lines[W_SNAKE+1+i]=Snake_stick(lines[W_SNAKE].x-1-i, lines[W_SNAKE].y, False)
            lines[W_SNAKE].horizontal=False
        elif direction[0] == UP:
            for i in range(W_SNAKE):
                lines[i]=Snake_stick(lines[W_SNAKE].x, lines[W_SNAKE].y-W_SNAKE+i, True)
                lines[W_SNAKE+1+i]=Snake_stick(lines[W_SNAKE].x, lines[W_SNAKE].y+1+i, True)
            lines[W_SNAKE].horizontal=True
        elif direction[0] == DOWN:
            for i in range(W_SNAKE):
                lines[i]=Snake_stick(lines[W_SNAKE].x, lines[W_SNAKE].y+W_SNAKE-i, True)
                lines[W_SNAKE+1+i]=Snake_stick(lines[W_SNAKE].x, lines[W_SNAKE].y-1-i,True)
            lines[W_SNAKE].horizontal=True
    else:
        direction_changes.insert(0, None)
    direction_changes.pop()
    if direction[0] == LEFT:
        lines.insert(0,Snake_stick((lines[0].x-1+W)%W,(lines[0].y+H)%H, False))
    elif direction[0] ==RIGHT:
        lines.insert(0,Snake_stick((lines[0].x+1+W)%W,(lines[0].y+H)%H, False))
    elif direction[0] ==UP:
        lines.insert(0,Snake_stick((lines[0].x+W)%W,(lines[0].y-1+H)%H, True))
    elif direction[0] ==DOWN:
        lines.insert(0,Snake_stick((lines[0].x+W)%W,(lines[0].y+1+H)%H, True))
    lines.pop()

    sc.fill(WHITE)
    for i in range(len(lines)):
        if lines[i].horizontal:
            pygame.draw.line(sc, BLUE, [lines[i].x+W_SNAKE, lines[i].y], [lines[i].x-W_SNAKE, lines[i].y])
        else:
            pygame.draw.line(sc, BLUE, [lines[i].x, lines[i].y+W_SNAKE], [lines[i].x, lines[i].y-W_SNAKE])
    # pygame.draw.rect(sc, BLUE, (x, y, 15, 15))
    pygame.display.update()

    clock.tick(FPS)