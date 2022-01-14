import pygame
import os,sys,time,random,math
import easygui as g
from matplotlib import pyplot as plot

global WIDTH
global HEIGHT
global multiple
global GO
global G 
global BLACK
global FPS
global NUM
NUM = 5
FPS = 120
BLACK = 0, 0, 0
WIDTH = 640
HEIGHT = 640
multiple = 1e10  # 在这里，为了保证演示效果，G扩大10的10次方倍
GO = 6.67408e-11
G = GO * multiple

speed=float(1.0)
class plt(object):

    def __init__(self,st ,pos, vel, mass, acc):
        self.status = pygame.transform.scale(pygame.image.load("./resources/" + st).convert(),(10,10)) 
        screen.blit(self.status, (pos[0],pos[1]))
        self.rect = pygame.image.load("./resources/" + st).get_rect() 
        self.pos = pos
        self.acc = acc
        self.vel = vel              
        self.mass = mass
        self.recordline = [[],[]]
        self.recordspeed = [[1],[math.sqrt(self.vel[0] ** 2 + self.vel[1] ** 2)]]

def cal(a, b):
    x=b.pos[0]-a.pos[0]
    y=b.pos[1]-a.pos[1]
    dis=math.sqrt(x ** 2 + y ** 2)
    sin=x/dis
    cos=y/dis
    f=G*a.mass*b.mass/(dis ** 2)
    return f*sin,f*cos

def ClearRecordData():
    for i in planet:
        i.recordline = [[],[]]
        i.recordspeed = [[1], [math.sqrt(i.vel[0] ** 2 + i.vel[1] ** 2)]]
        
def Update_Record(x):
    x.recordline[0].append(x.pos[0])
    x.recordline[1].append(x.pos[1])
    x.recordspeed[1].append(float(math.sqrt(x.vel[0] ** 2 + x.vel[1] ** 2)))
    x.recordspeed[0].append(int(x.recordspeed[0][len(x.recordspeed[0])-1]+1))
    return x

if __name__ == '__main__':
    title="模拟宇宙 欢迎"
    msg="设置"
    field=["X轴最大大小","Y轴最大大小","随机生成个数","FPS设置"]
    ret=g.multenterbox(msg,title,field,values=["640","640","5","60"])
    if ret is None:
        sys.exit()
    WIDTH=int(ret[0])
    HEIGHT=int(ret[1])
    NUM=int(ret[2])
    FPS=int(ret[3])

    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption("模拟宇宙")

    clock = pygame.time.Clock() 
    planet = []

    for i in range(NUM):    #随机生成NUM个星球
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        vx = random.randint(-1, 1)/10
        vy = random.randint(-1, 1)/10
        m = random.randint(1, 25)
        planet.append(plt("planet1.jpg",[px,py],[vx,vy],m,[0,0]))
        planet[i-1]=Update_Record(planet[i-1])
        screen.blit(planet[i].status, planet[i].pos)
        pygame.display.flip()
 
    while (1==1):       #渲染循环
        clock.tick(FPS)
        event=pygame.event.get()
        for i in event:  
            if i.type == pygame.QUIT:  
                sys.exit()
    
        planet1=planet
        for i in planet1:
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

            pos[0]=pos[0] + i.vel[0]*float(speed)
            pos[1]=pos[1] + i.vel[1]*float(speed)
            i.pos=pos
            i.rect=i.rect.move(i.vel[0],i.vel[1])
            
            for j in planet1:
                if (j.pos[0]>WIDTH) or (j.pos[0]<0) or (j.pos[1]>HEIGHT) or (j.pos[1]<0):
                    planet.remove(j)

        planet=planet1
        screen.fill(BLACK)
        for j in planet:
            j=Update_Record(j)
            screen.blit(j.status,j.pos)
        pygame.display.flip()

pygame.quit()
