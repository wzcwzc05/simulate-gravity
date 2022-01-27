from classFile.ClassP import plt
import pygame
import configparser
import sys
import os

# 读取设置操作
RunningPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
ConfigFile = configparser.ConfigParser()
ConfigFile.read(RunningPath + "\\config.ini")
WIDTH = int(ConfigFile.get("Display", "Width"))
HEIGHT = int(ConfigFile.get("Display", "Height"))
FPS = int(ConfigFile.get("Display", "FPS"))
BackColor = int(ConfigFile.get("Display", "BackgroundColor"))
Font = ConfigFile.get("ResoucesFile", "Font")
planet = []


def Start_Screen():
    pass


def UpdateData():
    pass


def SaveGame():
    pass


def UpdateRecord():
    pass


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
