import pygame

from game import Game

pygame.init()

# Display Set Up
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The Christmas Magic")

# Creating Game Instance
game = Game()

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set frame rate
    clock.tick(60)

    # Update Game Logic
    game.update()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw game elements
    game.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit

