import Board_Configurations


class Board:
    def __init__(self):
        self.boards = []
        for index in range(5):
            filepath = "Sudoku" + str(index) + ".txt"
            self.boards.append(filepath)
        self.board = self.load_new_board(1)

    def load_new_board(self, board_state):
        file = open(self.boards[board_state])
        print(file)


        return 1

    def return_board(self):
        return self.board
