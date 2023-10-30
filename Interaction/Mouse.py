import pygame


class Mouse:
    def __init__(self, window_width, window_height, top_text_height):
        self.window_width = window_width
        self.window_height = window_height
        self.top_text_height = top_text_height
        self.prev_board_coordinate = (0, 0)

    def get_mouse_on_board(self):
        """
        This method will return the mouse location on the board.
        """
        mouse_x_location, mouse_y_location = pygame.mouse.get_pos()
        if mouse_x_location < 0:
            mouse_x_location = 0
        if mouse_x_location > self.window_width:
            mouse_x_location = self.window_width
        if mouse_y_location < self.top_text_height:
            mouse_y_location = self.top_text_height
        if mouse_y_location > self.window_height:
            mouse_y_location = self.window_height
        return mouse_x_location, mouse_y_location

    def return_mouse_coordinate(self):
        """
        This method will return the mouse coordinate on the board, if it has changed.
        """
        mouse_x_board, mouse_y_board = self.get_mouse_on_board()
        mouse_x_board = int(mouse_x_board / (self.window_width / 9))
        mouse_y_board = int((mouse_y_board - self.top_text_height) / ((self.window_height - self.top_text_height) / 9))
        if self.prev_board_coordinate[0] != mouse_x_board or self.prev_board_coordinate[1] != mouse_y_board:
            prev_mouse_x_board, prev_mouse_y_board = self.prev_board_coordinate
            self.prev_board_coordinate = (mouse_x_board, mouse_y_board)
            return mouse_x_board, mouse_y_board, prev_mouse_x_board, prev_mouse_y_board
        else:
            return None
