import pygame

class Main_game:
    def __init__(self):
        self.cols = 7
        self.rows = 7


    @property
    def x_spacing(self):
        # window width/cols
        return pygame.display.get_window_size()[0]/self.cols

    @property
    def y_spacing(self):
        # window height/rows
        return pygame.display.get_window_size()[1]/self.rows

    @property
    def grid_area(self):
        return self.cols * self.rows

    def draw_grid(self):
        window = pygame.display.get_surface()
        width, height = window.get_size()

        for col in range(1, self.cols):
            x_pos = col * self.x_spacing
            pygame.draw.line(window, (255, 255, 255), (x_pos, 0), (x_pos, height))

        for row in range(1, self.rows):
            y_pos = row * self.y_spacing
            pygame.draw.line(window, (255, 255, 255), (0, y_pos), (width, y_pos))


Game = Main_game()
