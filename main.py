from classFile.ClassP import plt
import pygame
import configparser
import sys
import os
import easygui

planet = []

# 读取设置操作
RunningPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
ConfigFile = configparser.ConfigParser()
ConfigFile.read(RunningPath + "\\config.ini")
WIDTH = int(ConfigFile.get("Display", "Width"))
HEIGHT = int(ConfigFile.get("Display", "Height"))
FPS = int(ConfigFile.get("Display", "FPS"))
BackColor = int(ConfigFile.get("Display", "BackgroundColor"))
Font = ConfigFile.get("ResoucesFile", "Font")
G = float(ConfigFile.get("Calculation", "EnlargementFactor")) * 6.67408e-11


def Start_Screen():
    pass


def UpdateData():
    pass


def SaveGame():
    pass


def UpdateRecord():
    planet1 = planet
    for i in planet1:
        pos = i.pos
        m = i.mass
        xt = yt = 0

        for j in planet:
            if (j.pos != i.pos) and (j != i):
                x, y = plt.cal(i, j, G)
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


def GamePause():
    pass


if __name__ == '__main__':
    # 初始化
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("模拟宇宙")
    FontType = pygame.freetype.Font(Font, 36)
    clock = pygame.time.Clock()
    a = plt("Earth", "planet1.jpg", [200, 200], [0, 0], 10, [0, 0])
    planet.append(a)

    Start_Screen()

    InProcess = True  # 渲染过程开启
    while (InProcess == True):
        clock.tick(FPS)

        event = pygame.event.get()  # 获取键盘事件
        for i in event:
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.K_ESCAPE:
                GamePause()

        screen.fill(BackColor)
        screen.blit(planet[0].status, planet[0].pos)
        pygame.display.flip()

pygame.quit()
