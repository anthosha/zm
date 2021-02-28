import random
import sys
import time

import pygame


class Process:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.FPS = 30

        self.black = pygame.Color(0, 0, 0)
        self.red = pygame.Color(rgbvalue=[255, 0, 0])
        self.blue = pygame.Color(65, 105, 255)

        self.fps = pygame.time.Clock()

        self.score = 0

    def born_n_checking(self):
        checking = pygame.init()
        if checking[1] > 0:
            sys.exit()
        else:
            print('OK')

    def layout(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("ZMIY")

    def events(self, step):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    step = 'RIGHT'
                elif event.key == pygame.K_LEFT:
                    step = 'LEFT'
                elif event.key == pygame.K_DOWN:
                    step = 'DOWN'
                elif event.key == pygame.K_UP:
                    step = 'UP'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return step

    def refresh(self):
        pygame.display.flip()
        process.fps.tick(32)

    def score(self, choice=1):
        score_font = pygame.font.SysFont('georgia', 32)
        score_surf = score_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        score_rect = score_surf.get_rect()

        if choice == 1:
            score_rect.midtop = (80, 10)
        else:
            score_rect.midtop = (360, 120)

        self.screen.blit(score_surf, score_rect)

    def gameover(self):
        gameover_font = pygame.font.SysFont('georgia', 83)
        gameover_surf = gameover_font.render('GAME OVER', True, self.red)
        gameover_rect = gameover_surf.get_rect()
        gameover_rect.midtop = (360, 15)
        self.screen.blit(gameover_surf, gameover_rect)
        self.score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake:
    def __init__(self, snake_color):
        self.snake_head = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        self.direction = 'RIGHT'
        self.step = self.direction

    def direction(self):
        if any([self.step == 'RIGHT' and not self.direction == 'LEFT',
                self.step == 'LEFT' and not self.direction == 'RIGHT',
                self.step == 'UP' and not self.direction == 'DOWN',
                self.step == 'DOWN' and not self.direction == 'UP']):
            self.direction = self.step

    def head(self):
        if self.direction == 'RIGHT':
            self.snake_head[0] += 10
        elif self.direction == 'LEFT':
            self.snake_head[0] -= 10
        elif self.direction == 'UP':
            self.snake_head[1] -= 10
        elif self.direction == 'DOWN':
            self.snake_head[1] += 10

    def body(self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head))
        # если съели еду
        if (self.snake_head[0] == food_pos[0] and
                self.snake_head[1] == food_pos[1]):
            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def snake_image(self, screen, surface_color):
        screen.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(screen, self.snake_color, pygame.Rect(
                pos[0], pos[1], 10, 10))

    def boundaries(self, gameover, WIDTH, HEIGHT):
        if any((
                self.snake_head[0] > WIDTH - 10
                or self.snake_head[0] < 0,
                self.snake_head[1] > HEIGHT - 10
                or self.snake_head[1] < 0
        )):
            gameover()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head[0] and
                    block[1] == self.snake_head[1]):
                gameover()


class Yummy:
    def __init__(self, yummy_color, screen_width, screen_height):
        self.yummy_color = yummy_color
        self.yummy_size_x = 10
        self.yummy_size_y = 10
        self.yummy_pos = [random.randrange(1, screen_width / 10) * 10,
                          random.randrange(1, screen_height / 10) * 10]

    def yummy_image(self, screen):
        pygame.draw.rect(screen, self.yummy_color, pygame.Rect(
            self.yummy_pos[0], self.yummy_pos[1],
            self.yummy_size_x, self.yummy_size_y
        ))


process = Process()
snake = Snake(process.red)
yummy = Yummy(process.blue, process.WIDTH, process.HEIGHT)

process.born_n_checking()
process.layout()

while True:
    snake.do = process.events(snake.do)
    snake.direction()
    snake.head()
    process.score, yummy.yummy_pos = snake.body(
        process.score, yummy.yummy_pos, process.WIDTH, process.HEIGHT)
    snake.snake_image(process.screen, process.red)
    yummy.yummy_image(process.screen)
    snake.boundaries(process.gameover, process.WIDTH, process.HEIGHT)
    process.score()
    process.refresh()
