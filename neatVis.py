import pygame, sys, neat
import random as rand
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('neat')

n = neat.neat(3, 3, 5)

nodes = []
for a in n.nodes:
    nodes.append([a[0]*size[0]/n.layers, rand.randrange(0, size[1])])

while True:

    screen.fill((255, 255, 255))

    if len(n.nodes) > len(nodes):
        a = n.nodes[len(n.nodes)-1]
        nodes.append([a[0]*size[0]/n.layers, rand.randrange(0, size[1])])

    for a in n.connections:
        if a[3]:
            pygame.draw.line(screen, (0,0,0), nodes[a[0]], nodes[a[1]], 1)

    for a in nodes:
        pygame.draw.circle(screen, (255, 0, 0), [int(a[0]), int(a[1])], 5)





    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    n.mutate(1)

    pygame.display.update()
##    mainClock.tick(20)
