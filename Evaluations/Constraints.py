class Constraints:
    def __init__(self):
        self.areas = {
            1: ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
            2: ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)),
            3: ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)),
            4: ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)),
            5: ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)),
            6: ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)),
            7: ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)),
            8: ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)),
            9: ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8))
        }
        self.standard_domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def horizontal_neighbours(self, board, x_coordinate, y_coordinate):
        neighbours = []
        for board_x in range(9):
            if board_x == x_coordinate:
                continue
            neighbours.append(self.create_variable(board, board_x, y_coordinate))
        return neighbours

    def vertical_neighbours(self, board, x_coordinate, y_coordinate):
        neighbours = []
        for board_y in range(9):
            if board_y == y_coordinate:
                continue
            neighbours.append(self.create_variable(board, x_coordinate, board_y))
        return neighbours

    def area_neighbours(self, board, x_coordinate, y_coordinate):
        neighbours = []
        for board_x, board_y in self.areas[(x_coordinate // 3) + 3 * (y_coordinate // 3) + 1]:
            if board_x == x_coordinate and board_y == y_coordinate:
                continue
            neighbours.append(self.create_variable(board, board_x, board_y))
        return neighbours

    def create_variable(self, board, x_coordinate, y_coordinate):
        square = board[y_coordinate][x_coordinate]
        if square.value == [0]:
            square.value = self.standard_domain
        return x_coordinate, y_coordinate
