"""
This class displays everything that needs to be displayed.
"""

import time
import pygame


class Display:
    def __init__(self, window_width, window_height, top_text_height, edge_thickness, board):
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.screen_divider = 900
        self.window_width = window_width
        self.window_height = window_height
        self.top_text_height = top_text_height
        self.edge_thickness = edge_thickness
        self.board_width = len(board[0])
        self.board_height = len(board)

        # fonts
        self.font_size = 40
        self.font_size_board = 80
        self.font = pygame.font.SysFont('arialbold', self.font_size)
        self.font_board = pygame.font.SysFont('arialbold', self.font_size_board)

        # text variables
        self.text_left_border = 20
        self.text_top_border = 20
        self.text_vertical_separation = self.font_size
        self.text_fields = ["Player: ", "Step: "]
        self.text_rect_previous = []
        # initialize text_rect_previous list
        for i in range(len(self.text_fields)):
            self.text_rect_previous.append(pygame.Rect(0, 0, 0, 0))

        # color variables
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (100, 100, 100)
        self.red = (200, 50, 50)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.background = self.black

    def draw_squares(self, board):
        """
        This method will display all the squares on the board.
        """
        squares = board.return_board()
        for row in squares:
            for square in row:
                square.display(self.screen, self.font_board)

    def draw_text(self, text_input):
        """
        This method will display all the necessary text on screen in the top-left corner.
        It does this by drawing a new background, then the text and then the screen, only at the coordinates directly around the text.
        To ensure that no white leftovers from previous text remain on the screen,
        if the previous text is physically bigger than the current text, the screen will be updated around the previous text.
        """
        update_rect = []
        for index in enumerate(text_input):
            text = self.text_fields[index[0]] + index[1]
            text_display = self.font.render(text, True, self.white)
            text_rect = text_display.get_rect()
            text_rect.topleft = (self.text_left_border, self.text_top_border + self.text_vertical_separation * index[0])
            if text_rect[2] > self.text_rect_previous[index[0]][2]:     # Compare whether current or previous text is bigger
                update_rect.append(text_rect)
            else:
                update_rect.append(self.text_rect_previous[index[0]])
            self.screen.fill(self.background, update_rect[index[0]])
            self.screen.blit(text_display, text_rect)
            self.text_rect_previous[index[0]] = text_rect
        pygame.display.update(update_rect)

    def reset_screen(self):
        """
        This method will reset the entire screen and create an empty background with the 9 areas.
        """
        self.screen.fill(self.background)
        range_y = self.window_height - self.top_text_height
        pygame.draw.line(self.screen, self.red, (0, 1/3 * range_y + self.top_text_height - 1),
                         (self.window_width, 1/3 * range_y + self.top_text_height - 1), self.edge_thickness)
        pygame.draw.line(self.screen, self.red, (0, 2/3 * range_y + self.top_text_height - 1),
                         (self.window_width, 2/3 * range_y + self.top_text_height - 1), self.edge_thickness)
        pygame.draw.line(self.screen, self.red, (1/3 * self.window_width - 1, self.top_text_height),
                         (1/3 * self.window_width - 1, self.window_height), self.edge_thickness)
        pygame.draw.line(self.screen, self.red, (2/3 * self.window_width - 1, self.top_text_height),
                         (2/3 * self.window_width - 1, self.window_height), self.edge_thickness)
        pygame.display.update()
