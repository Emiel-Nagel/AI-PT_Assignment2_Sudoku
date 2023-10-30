"""
This class is an intermediate layer between main and the rest of the code and handles all the interactions between the classes.
"""


from Interaction.Display import Display
from Interaction.Keyboard import Keyboard
from Interaction.Mouse import Mouse
from Utilities.Enum_Variable import Enum_Variable
from Board.Board import Board


class Handler:
    def __init__(self, window_width, window_height, top_text_height, edge_thickness):
        self.board = Board(window_width, window_height, top_text_height, edge_thickness)
        self.board_index = 1
        self.board.load_new_board(self.board_index)
        self.display = Display(window_width, window_height, top_text_height, edge_thickness, self.board.return_board())
        self.keyboard = Keyboard()
        self.mouse = Mouse(window_width, window_height, top_text_height)
        self.mouse_coordinates = (0, 0, 0, 0)

        self.reset = False

        self.interaction_type = Enum_Variable(["Instant", "Step-by-Step", "Auto-run"])
        self.interaction_type.set_state("Step-by-Step")

        self.interaction_step = 0  # Useful for when you want to show step by step how the algorithm works, probably needs to be used in the self.interact class

        # for startup
        self.display.reset_screen()
        self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])

    def reset_game(self):
        """
        This method will start up the code.
        """
        self.board.load_new_board(self.board_index)
        self.interaction_step = 0
        # self.display.draw_board(self.board.return_board())

    def interact(self):
        """
        This method will handle all the interaction that happens between the user and the computer.
        """
        mouse_coordinates = self.mouse.return_mouse_coordinate()
        if mouse_coordinates is not None:
            self.mouse_coordinates = mouse_coordinates
        self.board.update_board(self.mouse_coordinates)
        self.check_key_pressed()

    def check_key_pressed(self):
        """
        This method handles the interaction with the keyboard.
        Space   = 44  Backspace = 42    Enter = 40
        """
        key = self.keyboard.return_key()
        if key is None:
            return
        if 44 in key:
            self.reset_game()
            self.board_index += 1
            if self.board_index == 5:
                self.board_index = 1
            self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])
        if 42 in key:
            if self.board.reverse_move():
                self.interaction_step -= 1
                self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])
        if 40 in key:
            self.reset_game()
        for key_value in range(9):
            if key_value + 30 in key:
                if self.board.make_move((self.mouse_coordinates[0], self.mouse_coordinates[1], key_value)):
                    self.interaction_step += 1
                    self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])

    def draw(self):
        """
        This method will call to display the program in a window.
        """
        self.display.draw_squares(self.board)

    def check_win(self):
        """
        This method will check if the game has been won.
        """
        if self.board.check_win():
            print("Congratulations, you win!")
            return True
        return False
