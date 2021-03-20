import pygame
from pygame.locals import *
from game import Game
import snake
pygame.init()


window = pygame.display.set_mode((750, 750))

clock = pygame.time.Clock()

Game.cols = 14
Game.rows = 14
sn = snake.Snake((5, 2))
sn.tail = [snake.Snake_part((-1, -1)) for i in range(5)]
tick = 0
while True:
    events = pygame.event.get()
    window.fill((0, 180, 255))

    Game.draw_grid()
    if tick % 10 == 0:
        sn.update()
    sn.draw()
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                sn.looking_at = [0, -1]
            elif event.key == K_DOWN:
                sn.looking_at = [0, 1]
            elif event.key == K_RIGHT:
                sn.looking_at = [1, 0]
            elif event.key == K_LEFT:
                sn.looking_at = [-1, 0]
        elif event.type == QUIT:
            pygame.quit()
            quit()



    pygame.display.update()
    clock.tick(60)
    tick += 1
