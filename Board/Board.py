import os


from Evaluations.Evaluate import Evaluate


class Board:
    def __init__(self):
        self.evaluations = Evaluate()
        self.boards = []
        self.sibling_directory = os.path.join(os.path.dirname(__file__), 'Board_Configurations')
        for index in range(5):
            filepath = "\Sudoku" + str(index) + ".txt"
            self.boards.append(filepath)
        self.board = []
        self.prev_boards = []
        self.load_new_board(1)

    def load_new_board(self, board_state):
        file = open(str(self.sibling_directory + self.boards[board_state]), mode="r")
        lines = file.readlines()
        file.close()
        pre_board = []
        for index, line in enumerate(lines):
            pre_board.append([])
            for letter in line:
                if letter == '\n':
                    continue
                pre_board[index].append(int(letter))
        self.board = pre_board
        print(self.board)

    def make_move(self, move):
        # move = tuple(x, y, number)
        if not self.evaluations.check_valid_move(self.board, move):
            return
        self.board[move[0]][move[1]] = move[2]

    def return_board(self):
        return self.board
