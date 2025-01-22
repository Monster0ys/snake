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

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        x=(x-speed+W)%W
    elif keys[pygame.K_RIGHT]:
        x=(x+speed+W)%W
    elif keys[pygame.K_UP]:
        y=(y-speed+H)%H
    elif keys[pygame.K_DOWN]:
        y=(y+speed+H)%H

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 15, 15))
    pygame.display.update()

    clock.tick(FPS)