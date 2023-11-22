import heapq

class Heuristics:
    def __init__(self, heuristic):
        pass

    @staticmethod
    def minimum_remaining_values(queue):
        """
        This method will return the coordinate of a field with the smallest value.
        """
        min_arc = min(queue, key=lambda arc: len(arc.first_variable.domain))
        return min_arc

    @staticmethod
    def priority_to_filled_fields(queue):
        """
        This method will reorder the queue following the priority to filled fields principle.
        """
        queue_index = 0
        while queue_index < len(queue):
            if queue[queue_index].second_variable.domain == [0]:
                return queue[queue_index]
            queue_index += 1
        return queue[0]

    @staticmethod
    def forward_checking(queue):
        """
        This method will look through the cue to remove any arcs where the second variable has a domain size larger than 1.
        """
        for arc in queue:
            if len(arc.second_variable.domain) > 1:
                queue.remove(arc)
        return queue

    @staticmethod
    def most_constraining_variable(queue):
        """
        This method will order the queue based to put the arcs with the field with the most neighbours with domain sizes larger than 1 first.
        """
        return queue

