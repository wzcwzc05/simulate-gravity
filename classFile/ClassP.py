import pygame
import math
class plt(object):
    
    def __init__(self,st ,pos, vel, mass, acc):
        self.status = pygame.transform.scale(pygame.image.load("./resources/" + st).convert(),(10,10)) 
        pygame.screen.blit(self.status, (pos[0],pos[1]))
        self.rect = pygame.image.load("./resources/" + st).get_rect() 
        self.pos = pos
        self.acc = acc
        self.vel = vel              
        self.mass = mass
        self.recordline = [[],[]]
        self.recordspeed = [[1],[math.sqrt(self.vel[0] ** 2 + self.vel[1] ** 2)]]
        
    def Refresh_Screen(self):
        pygame.screen.blit(self.status, self.pos)


a = plt("planet1.jpg", (200, 200), (0, 0), 10, 100)
