import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen_fill_color = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien shooter game")

hero_img = pygame.image.load('img/hero.png')
hero_width, hero_height = hero_img.get_size()
hero_x = screen_width / 2 - hero_width / 2
hero_y = screen_height - hero_height
HERO_STEP = 1
hero_is_moving_left, hero_is_moving_right = False, False

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                hero_is_moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                hero_is_moving_right = False

    if hero_is_moving_left and hero_x >= HERO_STEP:
        hero_x -= HERO_STEP
    if hero_is_moving_right and hero_x <= screen_width - hero_width - HERO_STEP:
        hero_x += HERO_STEP


    screen.fill(screen_fill_color)
    screen.blit(hero_img, (hero_x, hero_y))

    pygame.display.update()