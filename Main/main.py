"""
This is the main class from which the program runs.
The code is basically that you can close the program cleanly when you click on the cross button at the top-right corner of the pygame window.
"""


import pygame

from Handler import Handler

caption = "Sooodoookooo!!!"
window_width = 900
window_height = 1000
top_text_height = 100
edge_thickness = 6
#player = "Human"
player = "Algorithm"


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(caption)

        self.runBool = True

        self.handler = Handler(window_width, window_height, top_text_height, edge_thickness, player)

    def run(self):
        """
        Main update loop, quits if the pygame window is closed
        """
        while self.runBool:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runBool = False
            self.call()
        self.finish_game()

    def call(self):
        """
        Method that calls the methods from other classes and handles the interaction
        """
        if player == "Human":
            self.handler.interact()
        elif player == "Algorithm":
            self.handler.algorithm_solve()
        self.handler.draw()
        if self.handler.check_win():
            self.runBool = False

    def finish_game(self):
        """
        Method that finishes the game after a sudoku has been filled out
        """


# Starts and runs the game
if __name__ == "__main__":
    theMain = Main()
    theMain.run()
