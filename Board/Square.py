import pygame


class Square:
    def __init__(self, window_width, window_height, top_text_height, coordinate, edge_thickness, value):
        square_width = window_width / 9
        square_height = window_height - top_text_height / 9
        x_topleft = coordinate(0) * square_width + (edge_thickness / 2)
        y_topleft = coordinate(1) * square_height + (edge_thickness / 2)
        width = square_width - edge_thickness
        height = square_height - edge_thickness
        self.rect = pygame.Rect(x_topleft, y_topleft, width, height)
        self.value = value
        self.white = (255, 255, 255)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.colour = self.white

    def update_value(self, value):
        self.value = value

    def hover(self, hover=False):
        if hover:
            self.colour = self.blue
        if not hover:
            self.colour = self.white

    def display(self, screen, font):
        screen.fill(self.colour)
        text = self.value
        text_display = font.render(text, True, self.white)
        text_rect = text_display.get_rect()
        text_rect.center = (self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2)
        screen.blit(text_display, text_rect)
        pygame.display.update(self.rect)
