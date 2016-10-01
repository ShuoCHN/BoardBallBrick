

import pygame, sys, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class Board(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed  # only the x

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

class Brick(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



def animate():
    screen.fill([255, 255, 255])

    for ball in group_balls:
        ball.move()
    first_board.move()
    for ball in group_balls:
        if pygame.sprite.spritecollide(ball, group_boards, False):
            ball.speed[0] = -ball.speed[0]
            #ball.speed[1] = -ball.speed[1]

    for brick in group_bricks:
        for ball in group_balls:
            if pygame.sprite.spritecollide(ball, group_bricks, True):
                ball.speed[0] = -ball.speed[0]
                #ball.speed[1] = -ball.speed[1]

        screen.blit(ball.image, ball.rect)


        screen.blit(brick.image, brick.rect)
    screen.blit(first_board.image, first_board.rect)

    pygame.display.flip()
    pygame.time.delay(7)



size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])

ball_img = "Ball.png"
board_img = "Board.png"
brick_img = "Brick.png"

board_speed = [5,0]

group_bricks = pygame.sprite.Group()
group_balls = pygame.sprite.Group()
group_boards = pygame.sprite.Group()

first_board = Board(board_img,[540,600],board_speed)
group_boards.add(first_board)

for row in range(0,1):
    for column in range(0,1):
        location = [(row+1)*300 + 10,(column+1)*500 + 10]
        ball_speed = [4, 4]
        ball = Ball(ball_img,location,ball_speed)
        group_balls.add(ball)

for row in range(0,5):
    for column in range(0,5):
        location = [row*150+20*(row+1),column*50+20*(column+1)]
        brick = Brick(brick_img,location)
        group_bricks.add(brick)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    animate()










