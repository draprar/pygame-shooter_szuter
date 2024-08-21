import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen_fill_color = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien shooter game")

HERO_STEP = 1
hero_img = pygame.image.load('img/hero.png')
hero_width, hero_height = hero_img.get_size()
hero_x = screen_width / 2 - hero_width / 2
hero_y = screen_height - hero_height
hero_is_moving_left, hero_is_moving_right = False, False

BALL_STEP = 0.5
ball_img = pygame.image.load('img/ball.png')
ball_width, ball_height = ball_img.get_size()
ball_x, ball_y = 0, 0
ball_was_fired = False

ALIEN_STEP = 0.3
alien_img = pygame.image.load('img/alien.png')
alien_width, alien_height = alien_img.get_size()
alien_x = randint(9, screen_width - alien_width)
alien_y = 0

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                hero_is_moving_right = True
            if event.key == pygame.K_SPACE:
                ball_was_fired = True
                ball_x = hero_x + hero_width / 2 - ball_width / 2
                ball_y = hero_y - ball_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                hero_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                hero_is_moving_right = False

    if hero_is_moving_left and hero_x >= HERO_STEP:
        hero_x -= HERO_STEP
    if hero_is_moving_right and hero_x <= screen_width - hero_width - HERO_STEP:
        hero_x += HERO_STEP

    if ball_was_fired and ball_y + ball_height < 0:
        ball_was_fired = False
    if ball_was_fired:
        ball_y -= BALL_STEP

    alien_y += ALIEN_STEP
    if alien_y + alien_height > hero_y:
        game_is_running = False

    screen.fill(screen_fill_color)
    screen.blit(hero_img, (hero_x, hero_y))
    if ball_was_fired:
        screen.blit(ball_img, (ball_x, ball_y))
    screen.blit(alien_img, (alien_x, alien_y))

    pygame.display.update()

game_over_text = game_font.render("Game Over", True, 'black')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(500)

pygame.quit()
