"""
This is the main class from which the program runs.
The code is basically that you can close the program cleanly when you click on the cross button at the top-right corner of the pygame window.
"""


import pygame

from Handler import Handler

caption = "Graph Algorithm Visualizer"
window_width = 1000
window_height = 1000


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(caption)

        self.runBool = True

        self.handler = Handler(window_width, window_height)

    def run(self):
        """
        Main update loop, quits if the pygame window is closed
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runBool = False
            self.call()

    def call(self):
        """
        Method that calls the methods from other classes and handles the interaction
        """
        self.handler.create_graph()
        self.handler.interact()
        self.handler.draw()


# Starts and runs the game
if __name__ == "__main__":
    theMain = Main()
    theMain.run()
