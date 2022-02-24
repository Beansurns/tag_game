import pygame
from random import randint as rand

pygame.init()
s_width,s_height = 1900,950
screen = pygame.display.set_mode([s_width,s_height])

class Blocks:
    def __init__(self, width = rand(1,200), height = rand(1,200), colour = (rand(0,255),rand(0,255),rand(0,255)), pos = (rand(0,s_width),rand(0,s_height))):
        self.width = width
        self.height = height
        self.colour = colour
        self.pos = pos
        
    def update(self):
        self.draw()
        
    def draw(self):
        pygame.draw.rect(screen, self.colour, pygame.rect(self.width, self.height, self.pos))
            
            
            

block_num = 20
blocks = [Blocks(rand(1,200), rand(1,200), (rand(0,255),rand(0,255),rand(0,255)),(rand(0,s_width),rand(0,s_height))) for i in range(block_num)]

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))
    for block in blocks:
        block.update()
            
            
pygame.quit()
    

