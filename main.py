import pygame
from random import randint

blockSize, mapSize, margin = 20, 25, 50
winSize = (2 * margin) + (blockSize * mapSize)
black, white, snakeColor, foodColor = (0,0,0), (255,255,255), (255,0,255), (0, 255, 0)

pygame.init()
win = pygame.display.set_mode((winSize,winSize))
pygame.display.set_caption("Snake Game")



class Box:
    def __init__(self, pos=[0, 0], color=snakeColor):
        self.pos   = pos
        self.color = color


    def draw(self):
        xPos = margin + (self.pos[0] * blockSize)
        yPos = margin + (self.pos[1] * blockSize)
        pygame.draw.rect(win, self.color, (xPos, yPos, blockSize, blockSize))

    def move(self, deltaX, deltaY):
        self.pos[0]+=deltaX
        self.pos[1]+=deltaY

    def __eq__(self, other):
        return self.pos == other.pos


class Snake:
    def __init__(self):
        self.body = [Box()]
        self.lastPop = None

    def draw(self):
        for box in self.body:
            box.draw()

    def move(self, deltaX, deltaY):
        newPos = self.body[0].pos[:] # Deep copy of position
        newPos[0]+=deltaX
        newPos[1]+=deltaY
        self.body.insert(0, Box(pos=newPos))
        self.lastPop = self.body[-1]
        self.body.pop(-1)
    
    def eat(self):
        self.body.append(self.lastPop)
        


def drawGrid(color):
    for i in range(mapSize + 1):
        pygame.draw.line(win, color, (margin + i*blockSize, margin), (margin + i*blockSize, winSize-margin), 1)
        pygame.draw.line(win, color, (margin, margin + i*blockSize), (winSize-margin, margin + i*blockSize), 1)


def checkCollision(snake, food):
    aux = False
    if food in snake.body:
        aux = True
        print('collided')
        while food in snake.body:
            food.pos = [randint(0, mapSize-1), randint(0, mapSize-1)]
    return aux



pressedKeys = []
snake = Snake()
food = Box(pos=[4, 4], color=foodColor)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pressedKeys.append(event.key)
        if event.type == pygame.KEYUP:
            pressedKeys.remove(event.key)
    if pressedKeys:
        if pressedKeys[-1] == pygame.K_LEFT:
            snake.move(-1, 0)
        elif pressedKeys[-1] == pygame.K_RIGHT:
            snake.move(1, 0)
        elif pressedKeys[-1] == pygame.K_UP:
            snake.move(0, -1)
        elif pressedKeys[-1] == pygame.K_DOWN:
            snake.move(0, 1)

    if checkCollision(snake, food):
        snake.eat()

    win.fill(black)
    food.draw()
    snake.draw()
    drawGrid(white)


    pygame.display.update()
    pygame.time.delay(100)


pygame.quit()