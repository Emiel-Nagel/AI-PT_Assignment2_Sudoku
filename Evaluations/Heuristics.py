class Heuristics:
    @staticmethod
    def minimum_remaining_values(queue, insert_arc):
        """
        This method will insert the arc in the queue such that the domain sizes of the first variables are ordered from small to large.
        """
        for queue_index, arc in enumerate(queue):
            if len(insert_arc.first_variable.domain) <= len(arc.first_variable.domain):
                queue.insert(queue_index, insert_arc)
                return queue
        queue.append(insert_arc)
        return queue

    @staticmethod
    def priority_to_filled_fields(queue, insert_arc):
        """
        This method will insert the arc in the queue such that the queue is ordered based on the number of neighbours with single variable domains, from small to large.
        """
        def sum_small_domain_neighbours(arc):
            """
            This method counts the number neighbours with single-sized domains.
            """
            single_domain_count = 0
            for neighbour in arc.first_variable.neighbours:
                if len(neighbour.domain) == 1:
                    single_domain_count += 1
            return single_domain_count

        for queue_index, arc in enumerate(queue):
            if sum_small_domain_neighbours(insert_arc) <= sum_small_domain_neighbours(arc):
                queue.insert(queue_index, insert_arc)
                return queue
        queue.append(insert_arc)
        return queue

    @staticmethod
    def filter_non_revisable_arcs(queue, insert_arc):
        """
        This method will only insert an arc in the queue if the second field has a domain with length 1, aka, when the revise-function is able to perform the revision.
        """
        if len(insert_arc.second_variable.domain) == 1:
            queue.append(insert_arc)
        return queue

    @staticmethod
    def most_constraining_variable(queue, insert_arc):
        """
        This method will order the queue based to put the arcs with the field with the most neighbours with domain sizes larger than 1 first.
        """
        def sum_large_domain_neighbours(arc):
            """
            This method sums the domain sizes of the neighbours of the arc.
            """
            total_domain_size = 0
            for neighbour in arc.first_variable.neighbours:
                total_domain_size += len(neighbour.domain) == 1
            return total_domain_size

        for queue_index, arc in enumerate(queue):
            if sum_large_domain_neighbours(insert_arc) <= sum_large_domain_neighbours(arc):
                queue.insert(queue_index, insert_arc)
                return queue
        queue.append(insert_arc)
        return queue
