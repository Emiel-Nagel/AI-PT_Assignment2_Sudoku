import pygame


class Square:
    def __init__(self, window_width, window_height, top_text_height, board_x, board_y, edge_thickness, value):
        square_width = window_width / 9
        square_height = (window_height - top_text_height) / 9
        x_top_left = board_x * square_width + (edge_thickness / 2)
        y_top_left = board_y * square_height + (edge_thickness / 2) + top_text_height
        width = square_width - edge_thickness
        height = square_height - edge_thickness
        self.rect = pygame.Rect(x_top_left, y_top_left, width, height)
        self.board_coordinate = (board_x, board_y)

        self.value = value
        self.domain = [value]
        self.neighbours = []
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.colour = self.white
        self.update = True

    def update_value(self, value):
        """
        This method will update the value of the square.
        """
        self.value = value
        self.update = True

    def hover(self, hover):
        """
        This method will change the colour of the square when the mouse hovers over it.
        """
        if hover:
            self.colour = self.blue
        if not hover:
            self.colour = self.white
        self.update = True

    def display(self, screen, font):
        """
        This method will display the square on the screen.
        """
        if not self.update:
            return
        screen.fill(self.colour)
        text = str(self.value).replace("0", " ")
        text_display = font.render(text, True, self.black)
        text_rect = text_display.get_rect()
        text_rect.center = (self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2)
        screen.blit(text_display, text_rect)
        pygame.display.update(self.rect)
        self.update = False
