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
G = 6.67408e-1
BLACK=0,0,0
class plt(object):

    def __init__(self,st ,pos, vel, mass, acc):
        self.status = pygame.transform.scale(pygame.image.load("./resources/" + st).convert(),(10,10)) 
        screen.blit(self.status, (pos[0],pos[1]))
        self.rect = pygame.image.load("./resources/" + st).get_rect() 
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
    pygame.display.set_caption("模拟宇宙")

    clock = pygame.time.Clock() 
    planet = []

    for i in range(6):
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        vx = random.randint(-1, 1)/10
        vy = random.randint(-1, 1)/10
        m = random.randint(1, 25)
        planet.append(plt("planet1.jpg",[px,py],[vx,vy],m,[0,0]))
        screen.blit(planet[i].status, planet[i].pos)
        pygame.display.flip()
 
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
            accel=i.acc

            accel[0]=xt/m
            accel[1]=yt/m

            i.vel[0]+=accel[0]   
            i.vel[1]+=accel[1]  

            pos[0]+=i.vel[0]
            pos[1]+=i.vel[1]
            i.pos=pos
            i.rect=i.rect.move(i.vel[0],i.vel[1])
            
            screen.fill(BLACK)
            for j in planet:
                if (j.pos[0]>WIDTH) or (j.pos[0]<0) or (j.pos[1]>HEIGHT) or (j.pos[1]<0):
                    planet.remove(j)
            for j in planet:
                print(j.pos)
                screen.blit(j.status,j.pos)
            pygame.display.flip()

pygame.quit()
