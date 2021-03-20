import pygame
import random
from game import Game

class Food_class:
    def __init__(self, pos = random.choice([[i,j] for i in range(Game.cols) for j in range(Game.rows)])):
        self.pos = list(pos)

    def place_again(self, snake):
        # Comprueba que haya algun hueco libre y si no lo hay resetea el juego
        all_places = [[i,j] for i in range(Game.cols) for j in range(Game.rows)]
        snake_places = [snake.head.pos, *snake.tail_pos]
        free_places = [place for place in all_places if not place in snake_places]
        if free_places == []:
            self.pos = [-1, -1]
        # Si hay hueco libre elige uno al azar y coloca la comida ahí
        else:
            self.pos = random.choice(free_places)

    def draw(self):
        window = pygame.display.get_surface()
        abs_pos = [self.pos[0] * Game.x_spacing, self.pos[1] * Game.y_spacing]
         # Head center
        pygame.draw.rect(window, (255, 0, 0),
                        [*abs_pos, Game.x_spacing+1, Game.y_spacing+1])


Food = Food_class()
