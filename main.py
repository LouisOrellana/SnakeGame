import pygame
from random import randint
from time import time

blockSize, mapSize, margin = 20, 25, 50
winSize = (2 * margin) + (blockSize * mapSize)
black, white, snakeColor, foodColor = (0,0,0), (255,255,255), (255,0,255), (0, 255, 0)
menuColor = (255, 0, 100)
delay = 150

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

    def move(self, delta):
        newPos = self.body[0].pos[:] # Deep copy of position
        newPos[0]+=delta[0]
        newPos[1]+=delta[1]
        self.body.insert(0, Box(pos=newPos))
        self.lastPop = self.body[-1]
        self.body.pop(-1)
    
    def eat(self):
        self.body.append(self.lastPop)
    
    def checkCollision(self):
        for box in self.body:
            if self.body.count(box)>1:
                return True
        return False
        


def drawGrid(color):
    for i in range(mapSize + 1):
        pygame.draw.line(win, color, (margin + i*blockSize, margin), (margin + i*blockSize, winSize-margin), 1)
        pygame.draw.line(win, color, (margin, margin + i*blockSize), (winSize-margin, margin + i*blockSize), 1)


def foodCollision(snake, food):
    aux = False
    if food in snake.body:
        aux = True
        while food in snake.body:
            food.pos = [randint(0, mapSize-1), randint(0, mapSize-1)]
    return aux


def getMillis():
    return int(round(time() * 1000))


def game():
    pressedKeys = []
    snake = Snake()
    food = Box(pos=[4, 4], color=foodColor)
    lastDir = 'RIGHT'
    move = {'LEFT': [-1, 0], 'RIGHT': [1, 0], 'UP': [0, -1], 'DOWN': [0, 1]}
    lastMillis = getMillis()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'YOU QUIT'
            if event.type == pygame.KEYDOWN:
                pressedKeys.append(event.key)
            if event.type == pygame.KEYUP:
                try:
                    pressedKeys.remove(event.key)
                except:
                    pass
        if pressedKeys:
            if pressedKeys[-1] == pygame.K_LEFT:
                lastDir = 'LEFT'
            elif pressedKeys[-1] == pygame.K_RIGHT:
                lastDir = 'RIGHT'
            elif pressedKeys[-1] == pygame.K_UP:
                lastDir = 'UP'
            elif pressedKeys[-1] == pygame.K_DOWN:
                lastDir = 'DOWN'
                
        currentMillis = getMillis()
        if currentMillis - lastMillis >= delay:
            snake.move(move[lastDir])
    
            if foodCollision(snake, food):
                snake.eat()
            if snake.checkCollision():
                return 'YOU LOST\nYOU BIT YOURSELF'
            pos = snake.body[0].pos
            if 0 > pos[0] or pos[0] >= mapSize or  0 > pos[1] or pos[1] >= mapSize:
                return 'YOU LOST\nOUT OF BOUNDS'
            lastMillis = getMillis()
            
        win.fill(black)
        food.draw()
        snake.draw()
        drawGrid(white)
    
        pygame.display.update()

while True:
    status = game()
    if status == 'YOU QUIT':
        break
pygame.quit()