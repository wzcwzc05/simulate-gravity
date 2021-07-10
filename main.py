import pygame
import os,sys,time,random,math
import numpy
import easygui as g
import matplotlib
from matplotlib import pyplot as plot

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
        if ret is None:
            return 1,TIME_STEP_
        planet.append(plt(ret[4],[float(ret[0]),float(ret[1])],[float(ret[2]),float(ret[3])],float(ret[5]),[0,0]))
        planet[len(planet)-1]=Update_Record(planet[len(planet)-1])
        screen.blit(planet[len(planet)-1].status, planet[len(planet)-1].pos)
        pygame.display.flip()
        return 1,TIME_STEP_
    elif (choice == "修改游戏速度"):
        title="模拟宇宙 修改游戏速度"
        msg="设置"
        field=["游戏速度"]
        ret=g.multenterbox(msg,title,field,values=[tmp])
        if ret is None:
            return 1,TIME_STEP_
        TIME_STEP_=float(ret[0])
        pygame.display.flip()
        return 1,TIME_STEP_
    elif (choice == "退出游戏"):
        return 0,TIME_STEP_
    elif (choice == "保存截图"):
        pygame.image.save(screen,"screenshot.jpg")

    return 1,TIME_STEP_

def Game_reject(position):
    mouse_x=position[0]
    mouse_y=position[1]
    flag=0
    for i in planet:
        x,y=i.pos[0],i.pos[1]
        dis=math.sqrt((mouse_x-x) ** 2 + (mouse_y-y) ** 2)
        if (dis<=10):
            ret=g.buttonbox(msg="你点击了星球，请选择操作:",title="模拟宇宙",choices=("查看运动轨迹","查看速度图像","修改星球"))
            if ret is None:
                flag=1
                break

            if ret == "查看运动轨迹":
                plot.plot(i.recordline[0],i.recordline[1])
                plot.show()
                flag=1
                break

            if ret == "查看速度图像":
                plot.plot(i.recordspeed[0],i.recordspeed[1])
                plot.show()
                flag=1
                break

            title="模拟宇宙 修改星球"
            msg="修改星球"
            field=["X轴位置","Y轴位置","X轴速度","Y轴速度","质量"]
            px = i.pos[0]
            py = i.pos[1]
            vx = i.vel[0]
            vy = i.vel[1]
            m = i.mass
            ret=g.multenterbox(msg,title,field,values=[px,py,vx,vy,m])

            if ret is None:
                flag=1
                break

            i.pos[0]=float(ret[0])
            i.pos[1]=float(ret[1])
            i.vel[0]=float(ret[2])
            i.vel[1]=float(ret[3])
            i.mass=float(ret[4])

            i=Update_Record(i)
            screen.blit(i.status, i.pos)
            pygame.display.flip()
            flag=1
            break
    if (flag==0):
        title="模拟宇宙 添加星球"
        msg="在鼠标点击坐标添加星球"
        field=["X轴位置","Y轴位置","X轴速度","Y轴速度","星球图片","质量"]
        px = mouse_x
        py = mouse_y
        vx = 0
        vy = 0
        m = random.randint(1, 25)
        ret=g.multenterbox(msg,title,field,values=[px,py,vx,vy,"planet1.jpg",m])
        if ret is None:
            return
        planet.append(plt(ret[4],[float(ret[0]),float(ret[1])],[float(ret[2]),float(ret[3])],float(ret[5]),[0,0]))
        planet[len(planet)-1]=Update_Record(planet[len(planet)-1])
        screen.blit(planet[len(planet)-1].status, planet[len(planet)-1].pos)
        pygame.display.flip()

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

    g.msgbox(msg="在游戏中按下鼠标左键暂停，可修改参数，添加星球\n鼠标右键可在指定坐标操作",title="提醒",ok_button="我明白了")
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
        planet[i-1]=Update_Record(planet[i-1])
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
                if tmp ==  3:
                    ret=Game_reject(pos)
    
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
            j=Update_Record(j)
            screen.blit(j.status,j.pos)
        pygame.display.flip()

pygame.quit()
