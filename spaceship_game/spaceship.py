from settings import Settings
from fire import Fire


class Spaceship:
    def __init__(self):
        self.image = Settings.img_spaceship
        self.rect_spaceship = self.image.get_rect(midbottom=(800, 750))
        self.speed_x_spaceShip = 0

    def fly(self, direction_spaceship):
        if direction_spaceship == 'right':
            self.rect_spaceship.x += 10
        if direction_spaceship == 'left':
            self.rect_spaceship.x -= 10
        if self.rect_spaceship.left <= 80:
            self.rect_spaceship.left = 80
        if self.rect_spaceship.right >= Settings.SCREEN_WIDTH - 80:
            self.rect_spaceship.right = Settings.SCREEN_WIDTH - 80

    def firing_spaceShip(self):
        return Fire(self.rect_spaceship.midtop, -1, 'spaceship')




