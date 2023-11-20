from settings import Settings
from spaceship import Spaceship
from fire import Fire
from invaders import Invaders
import random
import pygame
import time


class manager_game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.game_active = True
        self.start = True
        self.spaceship = Spaceship()
        self.invaders = Invaders()
        self.grop_fire_invaders = pygame.sprite.Group()
        self.grop_fire_spaceship = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        self.space_pressed = 0
        self.test = 0
        self.speed_invaders = 5
        self.speed_invaders_y = False
        self.points = 0
        self.spaceship_life = 3
        self.screen_shift = 0
        self.number_levels = 1
        self.invaders_fire_speed = 40
        self.music = True

    def play_gunshot_sound(self, sound):
        if self.music:
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

    def start_game(self):
        pygame.init()
        font_start = pygame.font.Font(None, 100)
        text_start = font_start.render('to start the game press space', False, 'Green')
        text_start_rect = (text_start.get_rect(center=(780, 400)))
        self.screen.blit(Settings.img_background_1, (0, self.screen_shift))
        self.screen.blit(text_start, text_start_rect)
        player_stand_rect = Settings.img_spaceship.get_rect(center=(780, 550))
        self.screen.blit(Settings.img_spaceship, player_stand_rect)
        self.speed_invaders = 5
        sound_start_game = "/home/mefathim-tech-56/spaceship_game/MUSIK/background_music.mp3"
        sound = pygame.mixer.Sound(sound_start_game)
        sound.play()
        pygame.display.set_caption('DUDIS_INVADERS_SPACE')
        self.invaders.all_invaders_grop()

    def run_game(self):
        if Settings.img_background_number == 1:
            self.screen.blit(Settings.img_background_1, (0, self.screen_shift))
        if Settings.img_background_number == 2:
            self.screen.blit(Settings.img_background_2, (0, self.screen_shift))
        if Settings.img_background_number == 3:
            self.screen.blit(Settings.img_background_3, (0, self.screen_shift))
        if Settings.img_background_number == 4:
            self.screen.blit(Settings.img_background_4, (0, self.screen_shift))
        self.screen.blit(self.spaceship.image, self.spaceship.rect_spaceship)
        self.game_active = True
        self.screen_shift -= 1
        if self.screen_shift < -700:
            self.screen_shift = -1

    def spaceship_direction(self):
        all_key = pygame.key.get_pressed()
        if all_key[pygame.K_RIGHT]:
            self.spaceship.fly('right')
        if all_key[pygame.K_LEFT]:
            self.spaceship.fly('left')

    def fire_spaceship(self):
        all_key = pygame.key.get_pressed()
        if all_key[pygame.K_SPACE] and self.space_pressed <= 0:
            self.grop_fire_spaceship.add(self.spaceship.firing_spaceShip())
            self.space_pressed = 10
            sound_fire_spaceship = "/home/mefathim-tech-56/spaceship_game/MUSIK/shoot.mp3"
            self.play_gunshot_sound(sound_fire_spaceship)
        elif not all_key[pygame.K_SPACE]:
            self.space_pressed -= 1

    def fire_invaders(self):
        invaders_list = list(self.invaders.grop_invaders)
        if invaders_list:
            invader = random.choice(invaders_list)
            fire = Fire(invader.rect.midbottom, 1, 'invaders')
            if self.test == 0:
                self.grop_fire_invaders.add(fire)
                self.test = (self.test + 1) % self.invaders_fire_speed
            else:
                self.test = (self.test + 1) % self.invaders_fire_speed
        else:
            pass

    def all_fire(self):
        self.grop_fire_spaceship.draw(self.screen)
        self.grop_fire_invaders.draw(self.screen)
        self.grop_fire_spaceship.update()
        self.grop_fire_invaders.update()

    def invaders_direction(self):
        for invader in self.invaders.grop_invaders:
            if -1 >= invader.rect.left or invader.rect.right >= Settings.SCREEN_WIDTH:
                self.speed_invaders_y = True
                self.speed_invaders *= -1
                print(self.speed_invaders)
                break
            else:
                self.speed_invaders_y = False

    def all_invaders(self):
        self.invaders_direction()
        self.invaders.grop_invaders.draw(self.screen)
        self.invaders.grop_invaders.update(self.speed_invaders, self.speed_invaders_y)

    def collision(self):
        for invader in self.invaders.grop_invaders:
            if invader.rect.colliderect(self.spaceship.rect_spaceship):
                self.game_over()
            for fire in self.grop_fire_spaceship:
                if invader.rect.colliderect(fire.rect):
                    invader.kill()
                    fire.kill()
                    self.points += 10
                    sound_invaders = "/home/mefathim-tech-56/spaceship_game/MUSIK/smash.mpeg"
                    self.play_gunshot_sound(sound_invaders)
        for fire in self.grop_fire_spaceship:
            for fire_invader in self.grop_fire_invaders:
                if fire_invader.rect.colliderect(fire.rect):
                    fire.kill()
                    fire_invader.kill()
        for fire_invader in self.grop_fire_invaders:
            if self.spaceship.rect_spaceship.colliderect(fire_invader):
                fire_invader.kill()
                self.spaceship_life -= 1
                sound_spaceship_life = "/home/mefathim-tech-56/spaceship_game/MUSIK/hit.mp3"
                self.play_gunshot_sound(sound_spaceship_life)

    def points_game(self):
        font_points = pygame.font.Font(None, 50)
        text_points = font_points.render(f'points: {self.points}', False, 'Red')
        self.screen.blit(text_points, (20, 750))

    def all_spaceship_life(self):
        if self.spaceship_life == 0:
            self.game_active = False
        font_life = pygame.font.Font(None, 50)
        text_life = font_life.render(f'spaceship life: {self.spaceship_life}', False, 'Green')
        self.screen.blit(text_life, (1325, 750))

    def levels(self):
        font_levels = pygame.font.Font(None, 50)
        text_levels = font_levels.render(f' level: {self.number_levels}', False, 'yellow')
        self.screen.blit(text_levels, (730, 750))
        if len(self.invaders.grop_invaders) == 0:
            if self.number_levels < 4:
                self.number_levels += 1
                self.speed_invaders += 30
                self.invaders.speed_y += 20
                self.invaders_fire_speed -= 15
                Settings.img_background_number += 1
                font_game = pygame.font.Font(None, 100)
                text_level = font_game.render('to start the next level press space', False, 'Green')
                text_level_rect = text_level.get_rect(center=(780, 550))
                self.screen.blit(text_level, text_level_rect)
                self.start_game()


            else:
                sound_win = "/home/mefathim-tech-56/spaceship_game/MUSIK/shoot.mp3"
                self.play_gunshot_sound(sound_win)
                self.screen.blit(Settings.img_background_2, (0, self.screen_shift))
                font_win = pygame.font.Font(None, 300)
                text_win = font_win.render('you win', False, 'blue')
                text_win_rect = text_win.get_rect(center=(780, 380))
                self.screen.blit(text_win, text_win_rect)
                # font_points = pygame.font.Font(None, 120)
                # text_points = font_points.render(f'points: {self.points}', False, 'green')
                # text_points_rect = text_points.get_rect(center=(780, 600))
                # self.screen.blit(text_points, text_points_rect)

    def game_over(self):
        sound_game_over = "/home/mefathim-tech-56/spaceship_game/MUSIK/game over.mp3"
        self.play_gunshot_sound(sound_game_over)
        player_stand_rect = Settings.img_spaceship.get_rect(center=(780, 400))
        self.screen.blit(Settings.img_background_1, (0, 0))
        self.screen.blit(Settings.img_spaceship, player_stand_rect)
        font_game = pygame.font.Font(None, 100)
        text_name_game = font_game.render('game over ', False, 'Red')
        text_name_game_rect = text_name_game.get_rect(center=(780, 250))
        self.screen.blit(text_name_game, text_name_game_rect)
        text_message = font_game.render('to start the game again press space', False, 'Green')
        text_message_rect = text_message.get_rect(center=(780, 550))
        self.screen.blit(text_message, text_message_rect)
        self.number_levels = 1
        self.play_gunshot_sound(sound_game_over)
        self.music = False
