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

def cal(a, b):
    x=b.pos[0]-a.pos[0]
    y=b.pos[1]-a.pos[1]
    dis=math.sqrt(x ** 2 + y ** 2)
    sin=x/dis
    cos=y/dis
    f=G*a.mass*b.mass/(dis ** 2)
    return f*sin,f*cos
    
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
        for i in planet:
            pos=i.pos
            m=i.mass
            xt=yt=0

            for j in planet:
                if (j.pos!=i.pos) and (j!=i):
                    x,y=cal(i,j)
                    xt+=x
                    yt+=y
            accel=i.a

            accel[0]=xt/m
            accel[1]=yt/m

            i.vel[0]+=accel[0]   
            i.vel[1]+=accel[1]  

            pos[0]+=i.vel[0]
            pos[1]+=i.vel[1]

        pygame.display.flip()

pygame.quit()
