import pygame
import numpy
import os
import sys
import random
import math
import time

global TIME_STEP
TIME_STEP=10
WIDTH=640
HEIGHT=640
G = 6.67408e-11

class plt(object):

    def __init__(self, pos, vel, mass, acc):
        self.pltstatus=pygame.image.load("./resources/planet1.jpg")  
        self.pos = pos
        self.acc = acc   
        self.vel = vel              
        self.mass = mass

if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size) 

    clock = pygame.time.Clock() 
    planet = []

    #测试用随机生成两个星球
    for i in range(1):
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        m = random.randint(1, 25)
        planet.append(plt([px,py],[0,0],[0,0],m))

    while (1==1):
        clock.tick(60)
        event=pygame.event.get()
        for i in event:  
            if i.type == pygame.QUIT:  
                sys.exit()
    
        pygame.display.flip()

pygame.quit()
