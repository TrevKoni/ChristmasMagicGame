import pygame

from player import Player


class Game:
    def __init__(self):
        # Initialize game state variables here
        self.player = Player()

    def update(self):
        # Update game logic here
        self.player.update()

    def draw(self, screen):
        # Draw game elements on screen here

        # Background Color
        screen.fill((0, 0, 0))
        self.player.draw(screen)

