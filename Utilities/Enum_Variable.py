"""
This class is just a simple enumerator variable. I wanted to make it cuz I thought it would be cool.
You can give it a list of possible states, then set a state and return which state it currently holds.
"""


class Enum_Variable:
    def __init__(self, given_states):
        self.states = []
        for state in given_states:
            self.states.append(state)
        self.state_number = 0

    def set_state(self, state_name):
        for state in enumerate(self.states):
            if state[1] is state_name:
                self.state_number = state[0]

    def return_state(self):
        return self.states[self.state_number]
