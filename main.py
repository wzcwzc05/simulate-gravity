from numpy.lib.shape_base import tile
import pygame
import os,sys,time,random,math
import numpy
import easygui as g

WIDTH=640
HEIGHT=640
G = 6.67408e-1
BLACK=0,0,0
FPS=120
NUM=5
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

def cal(a, b):
    x=b.pos[0]-a.pos[0]
    y=b.pos[1]-a.pos[1]
    dis=math.sqrt(x ** 2 + y ** 2)
    sin=x/dis
    cos=y/dis
    f=G*a.mass*b.mass/(dis ** 2)
    return f*sin,f*cos

def Game_pause(TIME_STEP_):
    choice=g.buttonbox(msg="游戏已暂停",title="暂停",choices=("继续","保存截图","添加星球","修改游戏速度","退出游戏"))    

    if (choice == "添加星球"):
        title="模拟宇宙 添加星球"
        msg="设置"
        field=["X轴位置","Y轴位置","X轴速度","Y轴速度","星球图片","质量"]
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        vx = random.randint(-1, 1)/10
        vy = random.randint(-1, 1)/10
        m = random.randint(1, 25)
        ret=g.multenterbox(msg,title,field,values=[px,py,vx,vy,"planet1.jpg",m])
        planet.append(plt(ret[4],[int(ret[0]),int(ret[1])],[float(ret[2]),float(ret[3])],int(ret[5]),[0,0]))
        screen.blit(planet[len(planet)-1].status, planet[len(planet)-1].pos)
        pygame.display.flip()
        return 1,TIME_STEP_
    elif (choice == "修改游戏速度"):
        title="模拟宇宙 修改游戏速度"
        msg="设置"
        field=["游戏速度"]
        print(TIME_STEP_)
        ret=g.multenterbox(msg,title,field,values=[tmp])
        TIME_STEP_=float(ret[0])
        pygame.display.flip()
        print(TIME_STEP_)
        return 1,TIME_STEP_
    elif (choice == "退出游戏"):
        return 0,TIME_STEP_
    elif (choice == "保存截图"):
        pygame.image.save(screen,"screenshot.jpg")

    return 1,TIME_STEP_
if __name__ == '__main__':
    title="模拟宇宙 欢迎"
    msg="设置"
    field=["X轴最大大小","Y轴最大大小","随机生成个数","FPS设置"]
    ret=g.multenterbox(msg,title,field,values=["640","640","5","60"])
    WIDTH=int(ret[0])
    HEIGHT=int(ret[1])
    NUM=int(ret[2])
    FPS=int(ret[3])

    g.msgbox(msg="在游戏中按下鼠标左键暂停，可修改参数，添加星球",title="提醒",ok_button="我明白了")
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption("模拟宇宙")

    clock = pygame.time.Clock() 
    planet = []

    for i in range(NUM):
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        vx = random.randint(-1, 1)/10
        vy = random.randint(-1, 1)/10
        m = random.randint(1, 25)
        planet.append(plt("planet1.jpg",[px,py],[vx,vy],m,[0,0]))
        screen.blit(planet[i].status, planet[i].pos)
        pygame.display.flip()
 
    while (1==1):
        clock.tick(FPS)
        event=pygame.event.get()
        for i in event:  
            if i.type == pygame.QUIT:  
                sys.exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                pos=i.pos
                tmp=i.button
                if tmp == 1:
                    ret=Game_pause(speed)
                    if (ret[0]==0):
                        sys.exit()
                    else:
                        speed=ret[1]
    
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
  #         print(j.pos)
            screen.blit(j.status,j.pos)
        pygame.display.flip()

pygame.quit()
