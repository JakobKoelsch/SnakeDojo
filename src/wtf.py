import pygame
import os

#os.environ["SDL_VIDEODRIVER"] = "svgalib"

pygame.init()
pygame.display.list_modes()

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


while True:
    pass