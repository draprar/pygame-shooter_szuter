import pygame
import sys
from random import randint, uniform
import math

pygame.init()

game_font = pygame.font.Font(None, 30)
game_score = 0

screen_width, screen_height = 800, 600
screen_fill_color = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien shooter game")

# ADD user input
HERO_STEP = 1
hero_img = pygame.image.load('img/hero.png')
hero_width, hero_height = hero_img.get_size()
hero_x = screen_width / 2 - hero_width / 2
hero_y = screen_height - hero_height
hero_is_moving_left, hero_is_moving_right = False, False
hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)

BALL_STEP = 0.5
ball_img = pygame.image.load('img/ball.png')
ball_width, ball_height = ball_img.get_size()
ball_x, ball_y = 0, 0
ball_was_fired = False
ball_rect = pygame.Rect(ball_x, ball_y, ball_width, ball_height)

ALIEN_SPEED = 0.2
alien_img = pygame.image.load('img/alien.png')
alien_width, alien_height = alien_img.get_size()
alien_x = randint(9, screen_width - alien_width)
alien_y = 0
alien_rect = pygame.Rect(alien_x, alien_y, alien_width, alien_height)
alien_angle = math.radians(uniform(0, 180))
alien_direction_x = ALIEN_SPEED * math.cos(alien_angle)
alien_direction_y = max(0, ALIEN_SPEED * math.sin(alien_angle))

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

    alien_x += alien_direction_x
    alien_y += alien_direction_y

    # ALIEN
    if alien_x < 0 or alien_x > screen_width - alien_width:
        alien_direction_x *= -1
        alien_x = max(0, min(alien_x, screen_width - alien_width))

    # DONE
    hero_rect.topleft = (hero_x, hero_y)
    alien_rect.topleft = (alien_x, alien_y)
    ball_rect.topleft = (ball_x, ball_y)

    # DONE
    if hero_rect.colliderect(alien_rect):
        game_is_running = False

    # DONE
    if ball_rect.colliderect(alien_rect):
        ball_was_fired = False
        alien_x = randint(9, screen_width - alien_width)
        alien_y = 0
        ALIEN_SPEED += 0.1
        alien_angle = math.radians(uniform(0, 180))
        alien_direction_x = ALIEN_SPEED * math.cos(alien_angle)
        alien_direction_y = max(0, ALIEN_SPEED * math.sin(alien_angle))
        game_score += 1

    # ALIEN
    if alien_y >= screen_height:
        alien_x = randint(9, screen_width - alien_width)
        alien_y = 0
        alien_angle = math.radians(uniform(0, 180))
        alien_direction_x = ALIEN_SPEED * math.cos(alien_angle)
        alien_direction_y = max(0, ALIEN_SPEED * math.sin(alien_angle))

    screen.fill(screen_fill_color)
    screen.blit(hero_img, (hero_x, hero_y))
    screen.blit(alien_img, (alien_x, alien_y))

    if ball_was_fired:
        screen.blit(ball_img, (ball_x, ball_y))

    game_score_text = game_font.render(f"Score: {game_score}", True, 'red')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

game_over_text = game_font.render("Game Over", True, 'black')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(500)

pygame.quit()
