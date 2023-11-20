import pygame.display
import pygame



class Settings:
    img_background_number = 1
    img_spaceship = pygame.image.load("/home/mefathim-tech-56/spaceship_game/image/ship.bmp")
    img_background_1 = pygame.image.load(f"/home/mefathim-tech-56/spaceship_game/image/background_game_1.png")
    img_background_2 = pygame.image.load(f"/home/mefathim-tech-56/spaceship_game/image/background_game_2.png")
    img_background_3 = pygame.image.load(f"/home/mefathim-tech-56/spaceship_game/image/background_game_1.png")
    img_background_4 = pygame.image.load(f"/home/mefathim-tech-56/spaceship_game/image/background_game_4.png")
    img_fire_spaceship = pygame.image.load("/home/mefathim-tech-56/spaceship_game/image/racket.png")
    img_invader = pygame.image.load("/home/mefathim-tech-56/spaceship_game/image/alien.png")
    img_fire_invaders = pygame.image.load("/home/mefathim-tech-56/spaceship_game/image/fire_invaders.png")
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 800
    clock = pygame.time.Clock()

