import pygame

from pygame.locals import *
import time

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("img/block.jpg").convert()  # print image(square) on the surface
        self.x = 100
        self.y = 100
        self.direction = "down"
    def draw(self):
        self.parent_screen.fill((209, 202, 217))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()  # this is flip method

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):  # the block moves depending on the key we press
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
            self.y += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((209, 202, 217))  # these values are collected from RGB color picker
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:  # with this loop you changing the direction
            for event in pygame.event.get():  # will give you all the keyboard/mouse events(actions)
                if event.type == KEYDOWN:  # came from pygame.locals import *
                    if event.key == K_ESCAPE:  # if the user clicks on esc key
                        running = False

                    if event.key == K_LEFT:  # for move the block using left key
                        self.snake.move_left()

                    if event.key == K_RIGHT:  # for move the block using right key
                        self.snake.move_right()

                    if event.key == K_UP:  # for move the block using up key
                        self.snake.move_up()

                    if event.key == K_DOWN:  # for move the block using down key
                        self.snake.move_down()

                elif event.type == QUIT:  # if the user click on cancel (X)
                    running = False

            self.snake.walk()
            time.sleep(0.2)  # after 0.2 sec, the block moves if we do not press any key


if __name__ == "__main__":  # used that method to initialize pygame library
    game = Game()
    game.run()