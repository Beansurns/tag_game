import pygame
from random import randint as rand

pygame.init()
s_width, s_height = 1900, 950
screen = pygame.display.set_mode([s_width, s_height])
drag = 9/10



g = 0.05

class Blocks:
    def __init__(self, width=rand(1, 200), height=rand(1, 200), colour=(rand(0, 255), rand(0, 255), rand(0, 255)),
                 pos=(rand(0, s_width), rand(0, s_height))):
        self.width = width
        self.height = height
        self.colour = colour
        self.pos = pos

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.pos[0], self.pos[1], self.width, self.height))


class Collisions:
    def __init__(self, c_width=1, c_height=1, c_pos=(0, 0)):
        self.width = c_width
        self.height = c_height
        self.pos = c_pos

    def update(self):
        self.draw()

    def draw(self):
        pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


class Player:
    def __init__(self, p_width=10, p_height=20, p_colour=(100, 100, 255), p_pos=(500, 500), vel=(0, 0), g_t=0):
        self.width = p_width
        self.height = p_height
        self.colour = p_colour
        self.pos = p_pos
        self.vel = vel
        self.jump = False
        self.g_t = g_t

    def update(self):
        if self.pos[1] >= 870:
            self.g_t = 0
        else:
            self.g_t += 1


        if (self.pos[1] + self.height) < 930:
            self.vel = (self.vel[0] * drag, self.vel[1] + g)
            self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        elif self.vel[1] <= 0 or self.jump == True:
            self.vel = (self.vel[0] * drag, self.vel[1])
            self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
            self.jump = False
        else:
            self.vel = (self.vel[0] * drag, 0)
            self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


        if (self.pos[1] + self.height) >= 930:
            self.vel = (self.vel[0], 0)


        self.draw()

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.pos[0], self.pos[1], self.width, self.height))


block_num = 20
blocks = [Blocks(rand(1, 200), rand(1, 200), (rand(0, 255), rand(0, 255), rand(0, 255)), (rand(0, s_width),
                                                                                          rand(0, s_height))) for i in
          range(block_num)]
collisions = [Collisions(1, 1, (-10, -10))]
players = [Player(30, 60, (255, 100, 100), (250, 870), (0, 0), 0), Player(30, 60, (100, 100, 255), (750, 870), (0, 0), 0)]


for i in range(block_num):
    for j in range(4):
        if j == 0:
            collisions.append(Collisions(blocks[i].width, 1, blocks[i].pos))

        elif j == 1:
            collisions.append(Collisions(blocks[i].width, 1, (blocks[i].pos[0], blocks[i].pos[1] + blocks[i].height)))

        elif j == 2:
            collisions.append(Collisions(1, blocks[i].height, blocks[i].pos))

        elif j == 3:
            collisions.append(Collisions(1, blocks[i].height, (blocks[i].pos[0] + blocks[i].width, blocks[i].pos[1])))

running = True
while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_j]:
        players[1].vel = (players[1].vel[0] - 0.1, players[1].vel[1])
    if keys[pygame.K_l]:
        players[1].vel = (players[1].vel[0] + 0.1, players[1].vel[1])
    if keys[pygame.K_i] and players[1].g_t <= 100:
        players[1].vel = (players[1].vel[0],  players[1].vel[1] - 0.08)
        players[1].jump = True
    if keys[pygame.K_k]:
        players[1].vel = (players[1].vel[0], players[1].vel[1] + 0.2)

    if keys[pygame.K_a]:
        players[0].vel = (players[0].vel[0] - 0.1, players[0].vel[1])
    if keys[pygame.K_d]:
        players[0].vel = (players[0].vel[0] + 0.1, players[0].vel[1])

    screen.fill((43, 45, 47))
    for block in blocks:
        block.update()

    for collision in collisions:
        collision.update()

    for player in players:
        player.update()

    pygame.draw.rect(screen, (223, 225, 227), (0, 930, 1900, 20))
    pygame.display.flip()

pygame.quit()
