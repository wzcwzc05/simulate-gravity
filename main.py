from classFile.ClassP import plt
import pygame
import configparser
import sys,os
RunningPath = os.path.split(os.path.realpath(sys.argv[0]))[0]


pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("模拟宇宙")
a = plt("planet1.jpg",(200,200),(0,0),10,100)
