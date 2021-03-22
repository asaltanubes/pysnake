import pygame
from pygame.locals import *
from game import Game
from snake import Snake as sn
from food import Food
pygame.init()

def reset():
    sn.tail = []
    sn.head.pos = [Game.cols//2, Game.rows//2]
    sn.head.looking_at = [0, -1]
    Food.place_again(sn)

def wait_reset():
    pygame.time.delay(700)
    reset()
    render()
    pygame.display.update()
    pygame.time.delay(500)
    # Evita que las teclas pulsadas durante la pausa se activen de golpe al reiniciar
    pygame.event.pump()


def render():
    window.fill((0, 180, 255))
    Game.draw_grid()
    sn.draw()
    Food.draw()

window = pygame.display.set_mode((750, 750))

clock = pygame.time.Clock()

reset()
tick = 0
while True:
    events = pygame.event.get()

    grid_area = Game.grid_area
    grid_percent =  (grid_area - len(sn.tail))/(grid_area)
    game_wait = max(int(10 * (grid_percent)**2), 5)
    if tick % game_wait == 0:
        sn.update()

    render()
    if len(sn.tail) + 1 == Game.cols*Game.rows or sn.head.pos in sn.tail_pos:
        wait_reset()
    for event in events:
        if event.type == KEYDOWN:
            # "Vector" entre la cabeza y la cola justo detras de esta, no se mira hacia ella porque sería instakill
            if len(sn.tail) > 0:
                dont_look_at = [sn.tail[0].pos[i] - sn.head.pos[i] for i in range(2)]
            else:
                dont_look_at = None
            if event.key == K_UP:
                if dont_look_at != [0, -1]:
                    sn.looking_at = [0, -1]
            elif event.key == K_DOWN:
                if dont_look_at != [0, 1]:
                    sn.looking_at = [0, 1]
            elif event.key == K_RIGHT:
                if dont_look_at != [1, 0]:
                    sn.looking_at = [1, 0]
            elif event.key == K_LEFT:
                if dont_look_at != [-1, 0]:
                    sn.looking_at = [-1, 0]
            elif event.key == K_ESCAPE:
                pygame.quit()
                quit()

        elif event.type == QUIT:
            pygame.quit()
            quit()



    pygame.display.update()
    clock.tick(60)
    tick += 1
