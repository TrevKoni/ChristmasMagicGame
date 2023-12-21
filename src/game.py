import pygame

from magicgenerator import MagicGenerator
from player import Player


class Game:
    def __init__(self):
        # Initialize game state variables here
        self.player = Player()
        self.magic_generators = []

    def update(self):
        # Update game logic here
        self.player.update(self.magic_generators)

        # Update Magic Generators
        for magic_generator in self.magic_generators:
            if magic_generator.can_generate_magic():
                magic_generated = magic_generator.generate_magic()
                self.player.christmas_magic += magic_generated
                magic_generator.update_last_generated_time()

        # Example: Check how much Christmas Magic the player currently has
        current_magic = self.player.get_christmas_magic()
        print("Current Christmas Magic:", current_magic)

    def draw(self, screen):
        # Draw game elements on screen here

        # Background Color
        screen.fill((0, 0, 0))

        # Player and objects
        self.player.draw(screen)

        for magic_generator in self.magic_generators:
            magic_generator.draw(screen)

