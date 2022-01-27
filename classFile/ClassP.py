import math
import pygame


class plt(object):
    # name为名称 st为图片文件名 pos为位置 vel为速度 mass为速度 acc为加速度
    # 其中pos,vel,acc均为二元向量
    def __init__(self, Name, imageFile, pos, vel, mass, acc):
        self.status = pygame.transform.scale(
            pygame.image.load("./resources/" + imageFile).convert(), (10, 10))
        self.name = Name
        self.imagefile = imageFile
        self.pos = pos
        self.acc = acc
        self.vel = vel
        self.mass = mass
        self.recordline = [[], []]
        self.recordspeed = [
            [1], [math.sqrt(self.vel[0] ** 2 + self.vel[1] ** 2)]]

