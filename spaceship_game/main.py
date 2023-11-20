from settings import Settings
from spaceship import Spaceship
from fire import Fire
from manager import manager_game
import pygame


def next_game():
    game()


def game():
    clock = pygame.time.Clock()
    game = manager_game()
    game.start_game()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if not game.start and game.game_active:
            game.game_active = False
            game.run_game()
            game.spaceship_direction()
            game.fire_spaceship()
            game.fire_invaders()
            game.all_fire()
            game.all_invaders()
            game.collision()
            game.points_game()
            game.all_spaceship_life()
            game.levels()
        elif game.start and game.game_active:
            all_key = pygame.key.get_pressed()
            if all_key[pygame.K_SPACE]:
                game.start = False
        else:
            game.game_over()
            all_key = pygame.key.get_pressed()
            if all_key[pygame.K_SPACE] and game.game_active == False:
                next_game()
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    game()
