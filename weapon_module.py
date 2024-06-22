import pygame
import sys
import math
import bullets_module

class Weapon:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []

    def fire(self, x, y, angle):
        self.bullets.append(bullets_module.Bullet(self.screen, x, y, 4, 4, pygame.Color("Blue"), angle))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Player")
    screen = pygame.display.set_mode((640, 650))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        pygame.display.update()

if __name__ == "__main__":
    main()
