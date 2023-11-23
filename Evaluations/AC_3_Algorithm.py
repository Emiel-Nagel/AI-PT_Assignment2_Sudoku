from Evaluations.Constraints import Constraints
from Evaluations.Heuristics import Heuristics


class AC3:
    def __init__(self, heuristic):
        self.constraints = Constraints()
        self.heuristics = Heuristics()
        self.used_heuristic = heuristic
        self.queue = []
        self.evaluation_count = 0

    class Arc:
        """
        This class will contain an arc between two variables.
        """
        def __init__(self, first_variable, second_variable):
            self.first_variable = first_variable
            self.second_variable = second_variable
            self.identity = f"{first_variable.board_coordinate}{second_variable.board_coordinate}"

    def establish_arcs(self, board):
        """
        This method will establish the arcs for the AC-3 algorithm.
        It loops over all fields in the sudoku where the value is 0.
        And for every arc it will find the constraining neighbours.
        """
        for y_coordinate, row in enumerate(board):
            for x_coordinate, first_variable in enumerate(row):
                self.constraints.create_domain(first_variable)
                for second_variable in self.find_neighbours(board, x_coordinate, y_coordinate):
                    first_variable.neighbours.append(second_variable)
                    arc = self.Arc(first_variable, second_variable)
                    if not self.check_for_duplicates(arc):
                        self.insert_by_heuristic(arc)

    def find_neighbours(self, board, x_coordinate, y_coordinate):
        """
        This method will find the neighbours of a given field.
        """
        pre_neighbours = self.constraints.horizontal_neighbours(board, x_coordinate, y_coordinate)
        pre_neighbours += self.constraints.vertical_neighbours(board, x_coordinate, y_coordinate)
        pre_neighbours += self.constraints.area_neighbours(board, x_coordinate, y_coordinate)
        neighbours = []
        [neighbours.append(variable) for variable in pre_neighbours if variable not in neighbours]  # Remove duplicates in neighbours
        return neighbours

    def check_for_duplicates(self, current_arc):
        """
        This method will check if the arc has already been added to the queue.
        """
        for arc_index, arc in enumerate(self.queue):
            if arc.identity == current_arc.identity:
                return True
        return False

    def insert_by_heuristic(self, insert_arc):
        """
        This method will insert the given arc into the queue following the heuristics.
        """
        match self.used_heuristic:
            case "None":
                self.queue.append(insert_arc)
            case "MRV":
                self.queue = self.heuristics.minimum_remaining_values(self.queue, insert_arc)
            case "PTFF":
                self.queue = self.heuristics.priority_to_filled_fields(self.queue, insert_arc)
            case "FNRA":
                self.queue = self.heuristics.filter_non_revisable_arcs(self.queue, insert_arc)
            case "MCV":
                self.queue = self.heuristics.most_constraining_variable(self.queue, insert_arc)

    def fit_constraints(self):
        """
        This method will solve the constraint problem following the AC-3 algorithm.
        """
        while len(self.queue) > 0:
            arc = self.queue.pop(0)
            if self.revise(arc):
                if len(arc.first_variable.domain) == 0:
                    return False
                for neighbour in arc.first_variable.neighbours:
                    if neighbour.board_coordinate == arc.second_variable.board_coordinate:
                        continue
                    new_arc = self.Arc(neighbour, arc.first_variable)
                    if not self.check_for_duplicates(new_arc):
                        self.insert_by_heuristic(new_arc)
        return True

    def revise(self, arc):
        """
        This method will resize the domains of the variables, based on the arc.
        """
        self.evaluation_count += 1
        if len(arc.second_variable.domain) > 1:
            return False
        for value in arc.first_variable.domain:
            if value in arc.second_variable.domain:
                arc.first_variable.domain.remove(value)
                return True
        return False
