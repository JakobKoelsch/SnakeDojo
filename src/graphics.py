import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

x_size = 500
y_size = 500


class GraphicsEngine:
    def __init__(self):
        pygame.init()
        #self.logo = pygame.image.load("logo32x32.png")
        #pygame.display.set_icon(logo)
        pygame.display.set_caption("Snake Dojo")
        self.screen = pygame.display.set_mode((x_size, y_size))
        self.running = True
        self.boardSize = 1


    def setSize(self, size):
        self.boardSize = size

    def update(self):
        #TODO: implement
        self.screen.fill((0xff, 0xff, 0xff))
        retValue = True
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                    retValue = False

        pygame.display.flip()
        return retValue
        
