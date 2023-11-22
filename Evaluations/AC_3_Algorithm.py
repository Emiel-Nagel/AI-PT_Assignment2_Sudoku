from Evaluations.Constraints import Constraints
from Evaluations.Heuristics import Heuristics


class AC3:
    def __init__(self, heuristic):
        self.constraints = Constraints()
        self.heuristics = Heuristics(heuristic)
        self.queue = []
        self.evaluation_count = 0

    def establish_arcs(self, board):
        """
        This method will establish the arcs for the AC-3 algorithm.
        It loops over all fields in the sudoku where the value is 0.
        And for every arc it will find the constraining neighbours.
        """
        for y_coordinate, row in enumerate(board):
            for x_coordinate, square in enumerate(row):
                if square.value != 0:
                    continue
                first_variable = self.constraints.create_variable(board, x_coordinate, y_coordinate)
                for second_variable in self.find_neighbours(board, x_coordinate, y_coordinate):
                    board[x_coordinate][y_coordinate].neighbours.append(second_variable)
                    arc = first_variable + second_variable
                    if not self.check_for_duplicates(arc):
                        self.queue.append(arc)
                print(board[x_coordinate][y_coordinate].neighbours)

    def find_neighbours(self, board, x_coordinate, y_coordinate):
        """
        This method will find the neighbours of a given field.
        """
        neighbours = []
        neighbours += self.constraints.horizontal_neighbours(board, x_coordinate, y_coordinate)
        neighbours += self.constraints.vertical_neighbours(board, x_coordinate, y_coordinate)
        neighbours += self.constraints.area_neighbours(board, x_coordinate, y_coordinate)
        return neighbours

    def check_for_duplicates(self, current_arc):
        """
        This method will check if the arc has already been added to the queue.
        """
        for arc_index, arc in enumerate(self.queue):
            if arc == current_arc:
                return True
        return False

    def fit_constraints(self, board):
        """
        This method will solve the constraint problem following the AC-3 algorithm.
        """
        while len(self.queue) > 0:
            x_first, y_first, x_second, y_second = self.queue.pop()
            first_variable = board[x_first][y_first]
            second_variable = board[x_second][y_second]
            if self.revise(first_variable, second_variable):
                if len(first_variable.domain) == 0:
                    return False
                for neighbour in first_variable.neighbours:
                    if neighbour == (x_second, y_second):
                        continue
                    arc = (x_first, y_first) + neighbour
                    if not self.check_for_duplicates(arc):
                        self.queue.append(arc)
        return True

    def revise(self, first_variable, second_variable):
        """
        This method will resize the domains of the variables, based on the arc.
        """
        revised = False
        for value in first_variable.domain:
            if value in second_variable.domain:
                first_variable.domain.remove(value)
                revised = True
        self.evaluation_count += 1
        return revised
