import pygame
import random

import constants
import sprites
import objects

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

pygame.display.set_caption("Sonic Dash")

# Clock
clock = pygame.time.Clock()

# Group setup
player = objects.Player()
player_group = pygame.sprite.Group()
player_group.add(player)

obstacle_group = pygame.sprite.Group()

cloud_group = pygame.sprite.Group()

# Main game loop
running = True
obstacle_timer = 0
obstacle_countdown = 200
cloud_timer = 0

while running:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if obstacle_timer > obstacle_countdown:
        obstacle = objects.Obstacle()
        obstacle_group.add(obstacle)
        obstacle_timer = 0
        obstacle_countdown = random.randint(60, 140)

    if cloud_timer > 50:
        cloud = objects.Cloud()
        cloud_group.add(cloud)
        cloud_timer = 0

    obstacle_timer += 1
    cloud_timer += 1

    # Collision detection
    if pygame.sprite.spritecollide(player, obstacle_group, True):
        player.hearts -= 1
        if player.hearts == 0:
            running = False

    # Update
    player_group.update()
    obstacle_group.update()
    cloud_group.update()

    # Drawing
    screen.fill(constants.SKY_BLUE)
    screen.blit(sprites.grass_image, (0, constants.SCREEN_HEIGHT - constants.GRASS_HEIGHT))
    player_group.draw(screen)
    obstacle_group.draw(screen)
    cloud_group.draw(screen)

    # Draw hearts
    for i in range(player.hearts):
        screen.blit(sprites.heart_image, (30 + i * 100, 30))

    pygame.display.flip()

pygame.quit()
