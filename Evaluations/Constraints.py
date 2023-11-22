class Constraints:
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

    @staticmethod
    def create_domain(field):
        """
        This method will fill out the domain of a field for the AC-3 algorithm.
        """
        if field.domain == [0]:
            field.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @staticmethod
    def horizontal_neighbours(board, x_coordinate, y_coordinate):
        """
        This method will find the horizontal constraining neighbours of a given field.
        """
        neighbours = []
        for board_x in range(9):
            if board_x == x_coordinate:
                continue
            neighbours.append(board[y_coordinate][board_x])
        return neighbours

    @staticmethod
    def vertical_neighbours(board, x_coordinate, y_coordinate):
        """
        This method will find the vertical constraining neighbours of a given field.
        """
        neighbours = []
        for board_y in range(9):
            if board_y == y_coordinate:
                continue
            neighbours.append(board[board_y][x_coordinate])
        return neighbours

    def area_neighbours(self, board, x_coordinate, y_coordinate):
        """
        This method will find constraining neighbours of a given field in its 3x3 area.
        """
        neighbours = []
        for board_x, board_y in self.areas[(x_coordinate // 3) + 3 * (y_coordinate // 3) + 1]:
            if board_x == x_coordinate and board_y == y_coordinate:
                continue
            neighbours.append(board[board_y][board_x])
        return neighbours
