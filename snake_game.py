import pygame
import time

from pygame import display
from pygame.locals import *

def draw_block():
    surface.fill((209, 202, 217))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()  # this is flip method

if __name__ == "__main__":  # used that method to initialize pygame library
    pygame.init()

    surface = display.set_mode((500, 500))
    surface.fill((209, 202, 217))  # these values are collected from RGB color picker

    block = pygame.image.load("img/block.jpg").convert()  #print image(square) on the surface
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x,block_y))

    pygame.display.flip()  # for updating the screen
    #time.sleep(5)

    running = True

    while running:
        for event in pygame.event.get():  # will give you all the keyboard/mouse events(actions)
            if event.type == KEYDOWN:  # came from pygame.locals import *
                if event.key == K_ESCAPE:  # if the user clicks on esc key
                    running = False

                if event.key == K_UP:  # for move the block using up key
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:  # for move the block using down key
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:  # for move the block using left key
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:  # for move the block using right key
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:  # if the user click on cancel (X)
                running = False





