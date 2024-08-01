import pygame
import os


# Load assets
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')
sonic_run_images = [pygame.image.load(os.path.join(image_path, f'sonic{i}.gif')) for i in range(1, 5)]
# sonic_stand_images = [pygame.image.load(os.path.join(image_path, f'sonicStanding{i}.gif')) for i in range(1, 3)]
sonic_jump_image = pygame.image.load(os.path.join(image_path, 'sonicJump.png'))
heart_image = pygame.image.load(os.path.join(image_path, 'heart.png'))
obstacle_image = pygame.image.load(os.path.join(image_path, 'spike.png'))
grass_image = pygame.image.load(os.path.join(image_path, 'grass.png'))
cloud_image = pygame.image.load(os.path.join(image_path, 'cloud.png'))
