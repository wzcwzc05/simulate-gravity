import pygame
import sys
#Sprite class 
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = [0, 0, 0]
    size =[300, 300]
    screen = pygame.display.set_mode(size)
    player = Sprite([40, 50])
    # Define keys for player movement
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    wall = Sprite([100, 60])

main()
