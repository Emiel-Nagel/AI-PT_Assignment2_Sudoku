import os

from Board.Square import Square
from Evaluations.Evaluate import Evaluate


class Board:
    def __init__(self, window_width, window_height, top_text_height, edge_thickness):
        self.window_width = window_width
        self.window_height = window_height
        self.top_text_height = top_text_height
        self.edge_thickness = edge_thickness

        self.evaluations = Evaluate()
        self.boards = []
        self.update_boards = {}

        self.sibling_directory = os.path.join(os.path.dirname(__file__), 'Board_Configurations')
        for index in range(5):
            filepath = "\Sudoku" + str(index) + ".txt"
            self.boards.append(filepath)
        self.board = []
        self.prev_boards = []
        self.prev_mouse_coordinate = (0, 0)
        self.load_new_board(1)

    def load_new_board(self, board_state):
        file = open(str(self.sibling_directory + self.boards[board_state]), mode="r")
        lines = file.readlines()
        file.close()
        self.board = []
        for y_index, line in enumerate(lines):
            self.board.append([])
            for x_index, letter in enumerate(line):
                if letter == '\n':
                    continue
                square = Square(self.window_width, self.window_height, self.top_text_height,
                                x_index, y_index, self.edge_thickness, int(letter))
                self.board[y_index].append(square)
                dict_name = str(y_index) + str(x_index)
                item = {dict_name: True}
                self.update_boards.update(item)

    def update_board(self, mouse_coordinate):
        if mouse_coordinate is not None:
            mouse_x_board, mouse_y_board, prev_mouse_x_board, prev_mouse_y_board = mouse_coordinate
            self.board[mouse_y_board][mouse_x_board].hover(True)
            self.board[prev_mouse_y_board][prev_mouse_x_board].hover(False)
            key = str(mouse_y_board) + str(mouse_x_board)
            self.update_boards[key] = True
            key = str(prev_mouse_x_board) + str(prev_mouse_y_board)
            self.update_boards[key] = True

    def make_move(self, move):
        # move = tuple(x, y, number)
        if not self.evaluations.check_valid_move(self.board, move):
            return
        board_x, board_y, value = move
        self.board[board_y][board_x].update_value(value)
        key = str(board_y) + str(board_x)
        self.update_boards[key] = True

    def return_relevant_squares(self):
        update_list = []
        for key, value in self.update_boards.items():
            if value is True:
                board_y = int(int(key) / 10)
                board_x = int(key) % 10
                square = self.board[board_y][board_x]
                update_list.append(square)
        return update_list

    def return_board(self):
        return self.board
