import pygame, sys
from settings import *

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        # creating display surface
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # creating clock
        self.clock = pygame.time.Clock()

    def run(self):
        # Checking if we're closing the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Filling the screen with black color
            self.screen.fill('black')
            # Updating the screen
            pygame.display.update()
            # setting the framerate
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()