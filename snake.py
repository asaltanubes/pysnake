from game import Game
import pygame
from copy import copy
from food import Food

class Snake_class:
    def __init__(self, pos):
        self.head = Snake_head(pos)
        self.tail = []

    @property
    def looking_at(self):
        return self.head.looking_at

    @looking_at.setter
    def looking_at(self, dir):
        anti_direction = [-i for i in self.looking_at]
        if dir != anti_direction:
            self.head.looking_at = dir

    @property
    def tail_pos(self):
        return [i.pos for i in self.tail]

    def update(self):
        for i, p in sorted(enumerate(self.tail), reverse = True):
            if i != 0:
                p.pos = copy(self.tail[i-1].pos)
            else:
                p.pos = copy(self.head.pos)
        self.head.update()

        if self.head.pos == Food.pos:
            self.tail.append(Snake_part())
            Food.place_again(self)


    def draw(self):
        [part.draw() for part in self.tail]
        self.head.draw()

class Snake_part:
    def __init__(self, pos = (-1, -1)):
        self.pos = list(pos)


    def draw(self):
        window = pygame.display.get_surface()
        pygame.draw.rect(window, (0, 255, 0),
                [self.pos[0] * Game.x_spacing, self.pos[1] * Game.y_spacing,
                Game.x_spacing+1, Game.y_spacing+1])

class Snake_head:
    def __init__(self, pos, looking_at = [-1, 0]):
        self.pos = list(pos)
        self.looking_at = list(looking_at)

    def update(self):
        self.pos[0] += self.looking_at[0]
        self.pos[1] += self.looking_at[1]
        if self.pos[0] < 0:
            self.pos[0] = Game.cols - 1
        elif self.pos[0] >= Game.cols:
            self.pos[0] = 0
        if self.pos[1] < 0:
            self.pos[1] = Game.rows - 1
        elif self.pos[1] >= Game.rows:
            self.pos[1] = 0

    def draw(self):
        window = pygame.display.get_surface()
        abs_pos = [self.pos[0] * Game.x_spacing, self.pos[1] * Game.y_spacing]
         # Head center
        pygame.draw.rect(window, (0, 255, 0),
                        [*abs_pos, Game.x_spacing+1, Game.y_spacing+1])

        # Eyes
        eye_rect = pygame.Rect(0, 0, Game.x_spacing/10, Game.y_spacing/10)
        abs_rect = pygame.Rect(*abs_pos, Game.x_spacing, Game.y_spacing)
        eye_rect.center = abs_rect.center
        eye_moving = [abs_rect.w/4, abs_rect.h/4]
        # looking up
        if self.looking_at == [0, -1]:
            # left eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(-eye_moving[0], -eye_moving[1]))
            # Right eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(eye_moving[0], -eye_moving[1]))
        # looking down
        if self.looking_at == [0, 1]:
            # left eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(-eye_moving[0], eye_moving[1]))
            # Right eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(eye_moving[0], eye_moving[1]))
        # looking rigt
        if self.looking_at == [1, 0]:
            # left eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(eye_moving[0], -eye_moving[1]))
            # Right eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(eye_moving[0], eye_moving[1]))
        # looking left
        if self.looking_at == [-1, 0]:
            # left eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(-eye_moving[0], eye_moving[1]))
            # Right eye
            pygame.draw.rect(window, (0, 0, 0), eye_rect.move(-eye_moving[0], -eye_moving[1]))

Snake = Snake_class((Game.cols//2, Game.rows//2))
