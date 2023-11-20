import pygame
from settings import Settings
from fire import Fire


class Invaders(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.grop_invaders = pygame.sprite.Group()
        self.image = Settings.img_invader
        self.rect = self.image.get_rect(midbottom=(80, 160))
        self.speed_y = 25

    def all_invaders_grop(self):
        for row in range(3):
            for column in range(10):
                invader = Invaders()
                invader.rect.x = column * 120
                invader.rect.y = row * 60
                self.grop_invaders.add(invader)

    def update(self,speed,speed_y):
        self.rect.x += speed
        if speed_y == 1:
            self.rect.y += self.speed_y

