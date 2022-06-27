import pygame

from pygame.locals import *
import time

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("img/apple.jpg").convert()   # load image with the apple
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("img/block.jpg").convert()  # print image(square) on the surface
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"


    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def walk(self):  # the block moves depending on the key we press

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE

        self.draw()


    def draw(self):
        self.parent_screen.fill((209, 202, 217))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()  # this is flip method

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((209, 202, 217))  # these values are collected from RGB color picker
        self.snake = Snake(self.surface, 6)  # the size of the snake
        self.snake.draw()
        self.apple = Apple(self.surface)  # initialize the apple in the game
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            self.play()

            time.sleep(0.3)  # after 0.2 sec, the block moves if we do not press any key


if __name__ == "__main__":  # used that method to initialize pygame library
    game = Game()
    game.run()