"""
This is the main class from which the program runs.
The code is basically that you can close the program cleanly when you click on the cross button at the top-right corner of the pygame window.
"""


import pygame

from Handler import Handler
from Output.Excel_Writer import Excel_Writer

caption = "Sooodoookooo!!!"
window_width = 900
window_height = 1000
top_text_height = 100
edge_thickness = 6

board_tests = [1, 2, 3, 4, 5]
heuristic_tests = []
test = False

#player = "Human"
player = "Algorithm"

class Main:
    def __init__(self, sudoku_number=3, heuristic="None"):
        pygame.init()
        pygame.display.set_caption(caption)

        self.runBool = True

        self.handler = Handler(window_width, window_height, top_text_height, edge_thickness, player, sudoku_number, heuristic)

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
        if player == "Human":
            self.handler.interact()
            if self.handler.check_win():
                self.runBool = False
        elif player == "Algorithm":
            self.handler.algorithm_solve()
            self.runBool = False
        self.handler.draw()


# Starts and runs the game
if __name__ == "__main__":
    if test:
        writer = Excel_Writer()
        for board in board_tests:
            for heuristic in heuristic_tests:
                theMain = Main(board, heuristic)
                theMain.run()
                writer.append_data(theMain.handler.data)
        writer.fill_out_file()
    else:
        theMain = Main()
        theMain.run()
