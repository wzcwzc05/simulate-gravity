import pygame
import os
import sys
import time
import random
import math
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

speed = float(1.0)


class plt(object):

    def __init__(self, st, pos, vel, mass, acc):
        self.status = pygame.transform.scale(
            pygame.image.load("./resources/" + st).convert(), (10, 10)) #加载图片
        screen.blit(self.status, (pos[0], pos[1]))                      #初始化在屏幕上
        self.rect = pygame.image.load("./resources/" + st).get_rect()   #图片矩形框（边界）
        self.pos = pos                                                  #位置
        self.acc = acc                                                  #加速度
        self.vel = vel                                                  #速度
        self.mass = mass                                                #质量
        self.recordline = [[], []]                                      #记录轨迹（二元组）
        self.recordspeed = [
            [1], [math.sqrt(self.vel[0] ** 2 + self.vel[1] ** 2)]]      #通过瞬时速度记录速度变化（二元组）


def cal(a, b):                                                          #计算plt a与plt b之间的万有引力作用力，返回到坐标轴方向
    x = b.pos[0]-a.pos[0]
    y = b.pos[1]-a.pos[1]
    dis = math.sqrt(x ** 2 + y ** 2)
    sin = x/dis
    cos = y/dis
    f = G*a.mass*b.mass/(dis ** 2)
    return f*sin, f*cos


def ClearRecordData():                                                  #清除记录
    for i in planet:
        i.recordline = [[], []]
        i.recordspeed = [[1], [math.sqrt(i.vel[0] ** 2 + i.vel[1] ** 2)]]


def Game_pause(TIME_STEP_, FPS, multiple):                              #游戏暂停
    choice = g.buttonbox(msg="游戏已暂停", title="暂停", choices=(
        "继续", "基本设置", "保存截图", "添加星球", "退出游戏"))

    if (choice == "添加星球"):
        title = "模拟宇宙 添加星球"
        msg = "设置"
        field = ["X轴位置", "Y轴位置", "X轴速度", "Y轴速度", "星球图片", "质量"]    #随机生成数据
        px = random.randint(10, WIDTH - 10)
        py = random.randint(10, HEIGHT - 10)
        vx = random.randint(-1, 1)/10
        vy = random.randint(-1, 1)/10
        m = random.randint(1, 25)
        ret = g.multenterbox(msg, title, field, values=[
                             px, py, vx, vy, "planet1.jpg", m])
        if ret is None:
            return 1, TIME_STEP_, FPS, multiple
        if (os.path.exists("./resources/" + ret[4]) == False):              #判定图片是否存在
            g.msgbox(msg="星球图片不存在！", title="Error", ok_button="OK")
            return 1, TIME_STEP_, FPS, multiple
        if (float(ret[5]) <= 0):                                            #判定数据合法性
            g.msgbox(msg="质量数值不合法！", title="Error", ok_button="OK")
            return 1, TIME_STEP_, FPS, multiple
        planet.append(plt(ret[4], [float(ret[0]), float(ret[1])], [
                      float(ret[2]), float(ret[3])], float(ret[5]), [0, 0]))    #加入planet
        planet[len(planet)-1] = Update_Record(planet[len(planet)-1])
        screen.blit(planet[len(planet)-1].status, planet[len(planet)-1].pos)
        pygame.display.flip()
        return 1, TIME_STEP_, FPS, multiple
    
    elif (choice == "修改游戏速度"):                            #修改速度
        title = "模拟宇宙 修改游戏速度"
        msg = "设置"
        field = ["游戏速度"]
        ret = g.multenterbox(msg, title, field, values=[tmp])
        if ret is None:
            return 1, TIME_STEP_, FPS, multiple
        if (float(ret[0]) <= 0):
            g.msgbox(msg="数值不合法！", title="Error", ok_button="OK")
            return 1, TIME_STEP_, FPS, multiple
        TIME_STEP_ = float(ret[0])
        pygame.display.flip()
        return 1, TIME_STEP_, FPS, multiple

    elif (choice == "实验性功能设置"):                  #碰撞
        title = "实验性功能设置"
        msg = "设置"
        field = ["开启碰撞模式", "碰撞后产生碎片个数"]
        ret = g.multenterbox(msg, title, field, values=["False", 0])
        if ret is None:
            return 1, TIME_STEP_, FPS, multiple
        if (ret[0] == "True" or ret[0] == "true"):
            HIT_ = True
        else:
            HIT_ = False
    
    elif (choice == "基本设置"):                #基本设置
        title = "模拟宇宙 基本设置"
        msg = "设置"
        field = ["FPS设置", "G值放大倍数", "清除记录数据"]

        ret = g.multenterbox(msg, title, field, values=[
                             FPS, multiple, "False"])
        if ret is None:
            return 1, TIME_STEP_, FPS, multiple
        if (int(ret[0]) <= 0) and (ret[2] != "True" or ret[2] != "true" or ret[2] != "False" or ret[2] != "false"):
            g.msgbox(msg="数值不合法！", title="Error", ok_button="OK")
            return 1, TIME_STEP_, FPS, multiple
        FPS = int(ret[0])
        multiple = float(ret[1])
        if (ret[2] == "true") or (ret[2] == "True"):
            ClearRecordData()
        return 1, TIME_STEP_, FPS, multiple
    
    elif (choice == "退出游戏"):
        return 0, TIME_STEP_, FPS, multiple

    elif (choice == "保存截图"):                            #将画面截图
        pygame.image.save(screen, "screenshot.jpg")

    return 1, TIME_STEP_, FPS, multiple


def Game_reject(position):
    mouse_x = position[0]
    mouse_y = position[1]
    flag = 0
    for i in planet:
        x, y = i.pos[0], i.pos[1]
        dis = math.sqrt((mouse_x-x) ** 2 + (mouse_y-y) ** 2)
        if (dis <= 20):
            ret = g.buttonbox(msg="你点击了星球，请选择操作:", title="模拟宇宙",
                              choices=("查看运动轨迹", "查看速度图像", "修改星球"))
            if ret is None:
                flag = 1
                break

            if ret == "查看运动轨迹":                   #使用matplotlib绘制运动轨迹
                plot.plot(i.recordline[0], i.recordline[1])
                plot.show()
                flag = 1
                break

            if ret == "查看速度图像":                   #使用matplotlib绘制速度图像
                plot.plot(i.recordspeed[0], i.recordspeed[1])
                plot.show()
                flag = 1
                break

            title = "模拟宇宙 修改星球"             #修改星球数据
            msg = "修改星球"
            field = ["X轴位置", "Y轴位置", "X轴速度", "Y轴速度", "质量"]
            px = i.pos[0]
            py = i.pos[1]
            vx = i.vel[0]
            vy = i.vel[1]
            m = i.mass
            ret = g.multenterbox(msg, title, field, values=[px, py, vx, vy, m])

            if ret is None:
                flag = 1
                break

            if (float(ret[4]) <= 0):        #数据合法性检查
                g.msgbox(msg="质量数值不合法!", title="Error", ok_button="OK")
                break
            i.pos[0] = float(ret[0])
            i.pos[1] = float(ret[1])
            i.vel[0] = float(ret[2])
            i.vel[1] = float(ret[3])
            i.mass = float(ret[4])

            i = Update_Record(i)
            screen.blit(i.status, i.pos)
            pygame.display.flip()
            flag = 1
            break

    if (flag == 0):
        title = "模拟宇宙 添加星球"
        msg = "在鼠标点击坐标添加星球"
        field = ["X轴位置", "Y轴位置", "X轴速度", "Y轴速度", "星球图片", "质量"]
        px = mouse_x                        #在鼠标点击坐标上创建星球
        py = mouse_y
        vx = 0
        vy = 0
        m = random.randint(1, 25)
        ret = g.multenterbox(msg, title, field, values=[
                             px, py, vx, vy, "planet1.jpg", m])
        if ret is None:
            return
        if (os.path.exists("./resources/" + ret[4]) == False):
            g.msgbox(msg="星球图片不存在！", title="Error", ok_button="OK")
            return
        if (float(ret[5]) <= 0):
            g.msgbox(msg="质量数值不合法！", title="Error", ok_button="OK")
            return
        planet.append(plt(ret[4], [float(ret[0]), float(ret[1])], [
                      float(ret[2]), float(ret[3])], float(ret[5]), [0, 0]))
        planet[len(planet)-1] = Update_Record(planet[len(planet)-1])
        screen.blit(planet[len(planet)-1].status, planet[len(planet)-1].pos)
        pygame.display.flip()


def Update_Record(x):                           #更新数据记录
    x.recordline[0].append(x.pos[0])
    x.recordline[1].append(x.pos[1])
    x.recordspeed[1].append(float(math.sqrt(x.vel[0] ** 2 + x.vel[1] ** 2)))
    x.recordspeed[0].append(int(x.recordspeed[0][len(x.recordspeed[0])-1]+1))
    return x


if __name__ == '__main__':
    title = "模拟宇宙 欢迎"
    msg = "设置"
    field = ["X轴最大大小", "Y轴最大大小", "随机生成个数", "FPS设置"]
    ret = g.multenterbox(msg, title, field, values=["640", "640", "5", "60"])
    if ret is None:
        sys.exit()
    WIDTH = int(ret[0])
    HEIGHT = int(ret[1])
    NUM = int(ret[2])
    FPS = int(ret[3])

    g.msgbox(msg="在游戏中按下鼠标左键暂停，可修改参数，添加星球\n鼠标右键可在指定坐标操作",
             title="提醒", ok_button="我明白了")
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
        planet.append(plt("planet1.jpg", [px, py], [vx, vy], m, [0, 0]))
        planet[i-1] = Update_Record(planet[i-1])
        screen.blit(planet[i].status, planet[i].pos)
        pygame.display.flip()

    while (1 == 1):
        clock.tick(FPS)
        event = pygame.event.get()
        for i in event:
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                pos = i.pos
                tmp = i.button
                if tmp == 1:
                    ret = Game_pause(speed, FPS, multiple)
                    if (ret[0] == 0):
                        sys.exit()
                    else:
                        speed = ret[1]
                        FPS = ret[2]
                        multiple = ret[3]
                        G = GO * multiple
                if tmp == 3:
                    ret = Game_reject(pos)

        planet1 = planet
        for i in planet1:
            pos = i.pos
            m = i.mass
            xt = yt = 0

            for j in planet:
                if (j.pos != i.pos) and (j != i):
                    x, y = cal(i, j)
                    xt += x
                    yt += y
            accel = i.acc

            accel[0] = xt/m
            accel[1] = yt/m

            i.vel[0] += accel[0]
            i.vel[1] += accel[1]

            pos[0] = pos[0] + i.vel[0]*float(speed)
            pos[1] = pos[1] + i.vel[1]*float(speed)
            i.pos = pos
            i.rect = i.rect.move(i.vel[0], i.vel[1])

            for j in planet1:
                if (j.pos[0] > WIDTH) or (j.pos[0] < 0) or (j.pos[1] > HEIGHT) or (j.pos[1] < 0):
                    planet.remove(j)

        planet = planet1
        screen.fill(BLACK)
        for j in planet:
            j = Update_Record(j)
            screen.blit(j.status, j.pos)
        pygame.display.flip()

pygame.quit()
