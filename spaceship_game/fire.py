import pygame
from settings import Settings


class Fire(pygame.sprite.Sprite):
    def __init__(self, location, direction,test_img):
        super().__init__()
        self.rect_x = location[0]
        self.rect_y = location[1]
        if test_img == 'spaceship':
            self.image = Settings.img_fire_spaceship
        if test_img == 'invaders':
            self.image = Settings.img_fire_invaders
        self.rect = self.image.get_rect(midbottom=(self.rect_x, self.rect_y))
        self.direction = direction

    def update(self):
        self.rect.top += 10 * self.direction

