import pygame

blockSize, mapSize, margin = 15, 600, 30
x, y = margin, margin

black, white, snakeColor = (0,0,0), (255,255,255), (255,0,255)

pygame.init()
win = pygame.display.set_mode((mapSize,mapSize))
pygame.display.set_caption("Snake Game")

run = True

def drawGrid(win, color):
    gridlineCount = (mapSize-(2*margin))//blockSize + 1
    for i in range(gridlineCount):
        pygame.draw.line(win, color, (margin + i*blockSize, margin), (margin + i*blockSize, mapSize-margin), 1)
        pygame.draw.line(win, color, (margin, margin + i*blockSize), (mapSize-margin, margin + i*blockSize), 1)
        

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=blockSize
    elif keys[pygame.K_RIGHT]:
        x+=blockSize
    elif keys[pygame.K_UP]:
        y-=blockSize
    elif keys[pygame.K_DOWN]:
        y+=blockSize
    
    win.fill(black)
    
    pygame.draw.rect(win, snakeColor, (x, y, blockSize, blockSize))   
    drawGrid(win, white)
    
    pygame.display.update()
    pygame.time.delay(70)

    
pygame.quit()