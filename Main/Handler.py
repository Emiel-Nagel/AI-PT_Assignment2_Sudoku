"""
This class is an intermediate layer between main and the rest of the code and handles all the interactions between the classes.
"""


from Interaction.Display import Display
from Interaction.Keyboard import Keyboard
from Interaction.Mouse import Mouse
from Utilities.Enum_Variable import Enum_Variable
from Board.Board import Board


class Handler:
    def __init__(self, window_width, window_height, top_text_height):
        self.board = Board()
        self.display = Display(window_width, window_height, self.board.return_board())
        self.keyboard = Keyboard()
        self.mouse = Mouse(window_width, window_height, top_text_height)

        self.reset = True

        self.interaction_type = Enum_Variable(["Instant", "Step-by-Step", "Auto-run"])
        self.interaction_type.set_state("Step-by-Step")

        self.interaction_step = 0  # Useful for when you want to show step by step how the algorithm works, probably needs to be used in the self.interact class

        # for startup
        self.display.reset_screen()
        self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])

    def startup(self):
        """
        This method will start up the code
        """
        if not self.reset:
            return
        self.reset = False
        self.create_board()
        # self.display.draw_board(self.board.return_board())

    def create_board(self):
        """
        This method will call to create a new graph
        """
        self.board.load_new_board(1)

    def interact(self):
        """
        This method will handle all the interaction that happens between the user and the computer
        """
        pass
        #self.check_key_pressed()
        #print(self.mouse.)
        #print(self.mouse.return_mouse_coordinate())

    def check_key_pressed(self):
        """
        This method handles the interaction with the keyboard
        Space   = 44  Backspace = 42    Enter = 40
        """
        if 44 in self.keyboard.return_key():
            self.interaction_step += 1
            self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])
        if 42 in self.keyboard.return_key():
            self.interaction_step -= 1
            self.display.draw_text([self.interaction_type.return_state(), str(self.interaction_step)])
        if 40 in self.keyboard.return_key():
            self.reset = True

    def draw(self):
        """
        This method will call to display the program in a window
        """
        #self.display.display(self.interaction_type.return_state(), str(self.interaction_step))

