import random
import pygame

import constants
import sprites


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_images = sprites.sonic_run_images
        self.jump_image = sprites.sonic_jump_image
        self.image = self.run_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (100, constants.SCREEN_HEIGHT - constants.GRASS_HEIGHT)
        self.vel_y = 0
        self.jumping = False
        self.hearts = constants.PLAYER_HEARTS
        self.frame_index = 0
        self.animation_counter = 0

    def update(self):
        self.vel_y += constants.PLAYER_GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = constants.JUMP_STRENGTH
            self.jumping = True

        self.rect.y += self.vel_y
        if self.rect.bottom >= constants.SCREEN_HEIGHT - constants.GRASS_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT - constants.GRASS_HEIGHT
            self.jumping = False

        self.animate()

    def animate(self):
        if self.jumping:
            self.image = self.jump_image
        else:
            self.animation_counter += constants.ANIMATION_SPEED
            if self.animation_counter >= len(self.run_images):
                self.animation_counter = 0
            self.image = self.run_images[int(self.animation_counter)]


# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprites.obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = constants.SCREEN_WIDTH
        self.rect.y = constants.SCREEN_HEIGHT - self.rect.height - constants.GRASS_HEIGHT

    def update(self):
        self.rect.x += constants.OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprites.cloud_image
        self.rect = self.image.get_rect()
        self.rect.x = constants.SCREEN_WIDTH
        self.rect.y = (constants.SCREEN_HEIGHT - constants.GRASS_HEIGHT - 100) // random.randint(2, 20)

    def update(self):
        self.rect.x += constants.OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()
