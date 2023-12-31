class Evaluate:
    def __init__(self):
        self.areas = {
            1: ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
            2: ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)),
            3: ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)),
            4: ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)),
            5: ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)),
            6: ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)),
            7: ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)),
            8: ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)),
            9: ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8))
        }

    def check_valid_move(self, board, move):
        """
        This method will check if the move is valid.
        Rules: No duplicate numbers in the same row, column or domain.
        """
        board_x, board_y, value = move
        if board[board_y][board_x].value != 0:
            return False
        if not self.check_correspondence(board, move):
            return False
        return True

    def check_correspondence(self, board, move):
        """
        This method will check if the move is valid in all directions.
        Rules: No duplicate numbers in the same row, column or domain.
        """
        board_x, board_y, value = move
        value += 1
        for square_index in range(9):
            if square_index == board_x:
                continue
            if board[board_y][square_index].value == value:
                print(f"{board_x},{board_y},{value},Horizontal Lose!!")
                print(board[board_y][board_x].value)
                return False
        for square_index in range(9):
            if square_index == board_y:
                continue
            if board[square_index][board_x].value == value:
                print(f"{board_x},{board_y},Vertical Lose!!")
                return False
        for square_index in self.areas[(board_x // 3) + 3 * (board_y // 3) + 1]:
            if square_index[0] == board_x and square_index[1] == board_y:
                continue
            if board[square_index[0]][square_index[1]].value == value:
                print(f"{board_x},{board_y},Area Lose!!")
                return False
        return True

    def valid_solution(self, board):
        """
        This method will check if the game has been won/if a valid solution has been reached.
        """
        for row in board:
            for square in row:
                if square.value == 0:
                    return False
                move = (square.board_coordinate[0], square.board_coordinate[1], square.value)
                if not self.check_correspondence(board, move):
                    return False
        return True
