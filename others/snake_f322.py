import pygame
import random

pygame.init()

Fuchsia = (255, 0, 255)  # цвета https://colorscheme.ru/html-colors.html
White = (255, 255, 255)
Chocolate = (210, 105, 30)
Black = (0, 0, 0)
Red = (255, 0, 0)
Lime = (0, 255, 0)
AliceBlue = (240, 248, 255)

dis_width = 800  # размеры интерфейса
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))  # создаем интерфейс
pygame.display.set_caption("Snake by fil322")  # название игры

clock = pygame.time.Clock()

snake_block = 10  # переменная для шага
snake_speed = 15  # скорость змейки

score_font = pygame.font.SysFont("yscore", 25)  # счет змейки


def Your_score(score):
    value = score_font.render("Твой счёт: " + str(score), True, Chocolate)
    dis.blit(value, [0, 0])


def snake(snake_block, snake_list):  # создание змейки
    for x in snake_list:
        pygame.draw.rect(dis, Black, [x[0], x[1], snake_block, snake_block])


def game():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    len_snake = 1

    eda_x = (random.randint(1, dis_width - 10) // 10) * 10
    eda_y = (random.randint(1, dis_height - 10) // 10) * 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(AliceBlue)
        pygame.draw.rect(dis, Lime, [eda_x, eda_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)

        if len(snake_List) > len_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_List)
        Your_score(len_snake - 1)

        pygame.display.update()

        if x1 == eda_x and y1 == eda_y:
            eda_x = (random.randint(1, dis_width - 10) // 10) * 10
            eda_y = (random.randint(1, dis_height - 10) // 10) * 10
            len_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
