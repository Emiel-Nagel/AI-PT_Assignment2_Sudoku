from Evaluations.Constraints import Constraints


class AC3:
    def __init__(self):
        self.constraints = Constraints()
        self.queue = []
        self.evaluation_count = 0

    """
    class Arc:
        def __init__(self, first_variable, second_variable):
            self.first_variable_name, self.first_variable_domain = first_variable
            self.second_variable_name, self.second_variable_domain = second_variable
    """

    def establish_arcs(self, board):
        for y_coordinate, row in enumerate(board):
            for x_coordinate, square in enumerate(row):
                if square.value != [0]:
                    continue
                first_variable = self.constraints.create_variable(board, x_coordinate, y_coordinate)
                for second_variable in self.find_neighbours(board, x_coordinate, y_coordinate):
                    arc = first_variable + second_variable
                    if not self.check_for_duplicates(arc):
                        self.queue.append(arc)

    def find_neighbours(self, board, x_coordinate, y_coordinate):
        neighbours = []
        neighbours += self.constraints.horizontal_neighbours(board, x_coordinate, y_coordinate)
        neighbours += self.constraints.vertical_neighbours(board, x_coordinate, y_coordinate)
        neighbours += self.constraints.area_neighbours(board, x_coordinate, y_coordinate)
        return neighbours

    def check_for_duplicates(self, current_arc):
        for arc_index, arc in enumerate(self.queue):
            if arc == current_arc:
                return True
        return False

    def fit_constraints(self, board):
        while len(self.queue) > 0:
            x_first, y_first, x_second, y_second = self.queue.pop()
            has_been_changed = self.revise(board, x_first, y_first, x_second, y_second)
            if len(board[x_first][y_first].value) == 0:
                return False
            if not has_been_changed:
                continue
            for second_variable in self.find_neighbours(board, x_first, y_first):
                if second_variable == (x_second, y_second):
                    continue
                arc = (x_first, y_first) + second_variable
                if not self.check_for_duplicates(arc):
                    self.queue.append(arc)
        return True

    def revise(self, board, x_first, y_first, x_second, y_second):
        second_value = board[x_second][y_second].value
        if len(second_value) != 1:
            return False
        second_value = second_value[0]
        if second_value not in board[x_first][y_first].value:
            return False
        board[x_first][y_first].value.remove(second_value)
        self.evaluation_count += 1
        return True
