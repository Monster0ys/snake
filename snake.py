import pygame
pygame.init()

W = 500
H = 500
sc=pygame.display.set_mode((W, H))
WHITE=(255, 255, 255)
BLUE=(0,0,255)

FPS=60
clock=pygame.time.Clock()

x = W // 2
y = H // 2
speed=1
direction ="RIGHT"

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction="LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction="RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction="UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction="DOWN"

    if direction == "LEFT":
        x=(x-speed+W)%W
    elif direction =="RIGHT":
        x=(x+speed+W)%W
    elif direction =="UP":
        y=(y-speed+H)%H
    elif direction =="DOWN":
        y=(y+speed+H)%H

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 15, 15))
    pygame.display.update()

    clock.tick(FPS)