import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        # Creating display surface
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Creating clock
        self.clock = pygame.time.Clock()
        # Setting the title of the game window
        pygame.display.set_caption('Legend Souls')
        # Creates an instance of the Level class
        self.level = Level()

    def run(self):
        # Checking if we're closing the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Filling the screen with black color
            self.screen.fill('black')
            # Runs the instance of the level class 
            self.level.run()
            # Updating the screen
            pygame.display.update()
            # setting the framerate
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()