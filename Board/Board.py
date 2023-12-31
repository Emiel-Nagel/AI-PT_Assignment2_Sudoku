import os

from Board.Field import Field
from Evaluations.Evaluate import Evaluate


class Board:
    def __init__(self, window_width, window_height, top_text_height, edge_thickness):
        self.window_width = window_width
        self.window_height = window_height
        self.top_text_height = top_text_height
        self.edge_thickness = edge_thickness

        self.evaluations = Evaluate()
        self.boards = []    # All predefined boards

        self.sibling_directory = os.path.join(os.path.dirname(__file__), 'Board_Configurations')
        for index in range(5):
            filepath = "\Sudoku" + str(index + 1) + ".txt"
            self.boards.append(filepath)
        self.board = []
        self.prev_moves = []
        self.prev_mouse_coordinate = (0, 0)

    def load_new_board(self, board_state):
        """
        This method will load a new board.
        """
        file = open(str(self.sibling_directory + self.boards[board_state - 1]), mode="r")
        lines = file.readlines()
        file.close()
        self.board = []
        for y_index, line in enumerate(lines):
            self.board.append([])
            for x_index, letter in enumerate(line):
                if letter == '\n':
                    continue
                field = Field(self.window_width, self.window_height, self.top_text_height,
                                x_index, y_index, self.edge_thickness, int(letter))
                self.board[y_index].append(field)

    def update_board(self, mouse_coordinate):
        """
        This method will update the board.
        """
        mouse_x_board, mouse_y_board, prev_mouse_x_board, prev_mouse_y_board = mouse_coordinate
        self.board[mouse_y_board][mouse_x_board].hover(True)
        self.board[prev_mouse_y_board][prev_mouse_x_board].hover(False)

    def make_move(self, move):
        """
        This method will make a move on the board.
        """
        # move is a tuple: (x_coordinate, y_coordinate, value)
        if not self.evaluations.check_valid_move(self.board, move):
            return False
        board_x, board_y, value = move
        value += 1
        self.prev_moves.append(move)
        self.board[board_y][board_x].update_value(value)
        return True

    def reverse_move(self):
        """
        This method will reverse the last move.
        """
        if len(self.prev_moves) == 0:
            return False
        board_x, board_y, value = self.prev_moves.pop(-1)
        self.board[board_y][board_x].update_value(0)
        return True

    def settle_domains(self):
        """
        This method will settle the domains of the fields.
        """
        for row in self.board:
            for field in row:
                field.value = field.domain[0]

    def check_win(self):
        """
        This method will check if the game has been won.
        """
        return self.evaluations.valid_solution(self.board)

    def return_board(self):
        """
        This method will return the board.
        """
        return self.board

    def print_board(self):
        """
        This method will print the board.
        """
        for row in self.board:
            text = ""
            for field in row:
                text += str(field.domain)
            print(text)
