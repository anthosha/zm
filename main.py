import random
import sys
import time

import pygame


class Process:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.FPS = 30

        self.black = pygame.color(0, 0, 0)
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
        self.layout = pygame.display.set_mode(size = (self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("ZMIY")

    def loops(self, step):
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
        score_surf = score_font.render('Score: {0}'.format(self.score(), True, self.black))
        score_rect = score_surf.get_rect()

        if choice == 1:
            score_rect.midtop = (80, 10)
        else:
            score_rect.midtop = (360, 120)

        self.layout.blit((score_surf, score_rect))

    def gameover(self):
        gameover_font = pygame.font.SysFont('georgia', 83)
        gameover_surf = gameover_font.render('GAME OVER', True, self.red)
        gameover_rect = gameover_surf.get_rect()
        gameover_rect.midtop = (360, 15)
        self.layout.blit((gameover_surf, gameover_rect))
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
        if any(self.step == 'RIGHT' and not self.direction == 'LEFT',
               self.step == 'LEFT' and not self.direction == 'RIGHT',
               self.step == 'UP' and not self.direction == 'DOWN',
               self.step == 'DOWN' and not self.direction == 'UP'):
            self.direction = self.step

    def head(self):
        if

    def body(self):
        pass

    def snake_image(self):
        pass

    def boundaries(self):
        pass


class Yummy:
    def __init__(self):
        pass

    def yummy_image(self):
        pass


process = Process()
snake = Snake(process.red)
yummy = Yummy(process.blue, game.screen_width, game.screen_height)

process.born_n_checking()
process.layout()

while True:
    snake.do = process.loops(snake.do)
    snake.checking()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)
    food.draw_food(game.play_surface)
    snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)
    game.show_score()
    game.refresh_screen()

