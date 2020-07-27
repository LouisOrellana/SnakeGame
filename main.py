import pygame

blockSize, mapSize, margin = 20, 600, 30

black, white, snakeColor = (0,0,0), (255,255,255), (255,0,255)

pygame.init()
win = pygame.display.set_mode((mapSize,mapSize))
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
        self.body = [Box(), Box([0,1]), Box([0,2])]
    
    def draw(self):
        for box in self.body:
            box.draw()
    
    def move(self, deltaX, deltaY):
        newPos = self.body[0].pos[:] # Deep copy of position
        newPos[0]+=deltaX
        newPos[1]+=deltaY
        self.body.insert(0, Box(pos=newPos))
        self.body.pop(-1)
        
       
def drawGrid(win, color):
    gridlineCount = (mapSize-(2*margin))//blockSize + 1
    for i in range(gridlineCount):
        pygame.draw.line(win, color, (margin + i*blockSize, margin), (margin + i*blockSize, mapSize-margin), 1)
        pygame.draw.line(win, color, (margin, margin + i*blockSize), (mapSize-margin, margin + i*blockSize), 1)



        
pressedKeys = []
snake = Snake()
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
            
    
    win.fill(black)    
    drawGrid(win, white)
    snake.draw()
    
    pygame.display.update()
    pygame.time.delay(70)

    
pygame.quit()