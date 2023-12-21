import pygame

from magicgenerator import MagicGenerator


class Player:
    def __init__(self, x=100, y=100, width=50, height=50, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.speed = speed
        self.christmas_magic = 10

    def update(self, magic_generators):
        # Player Movement and Actions
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Place a Magic Generator
        if keys[pygame.K_SPACE]:
            if self.spend_christmas_magic(5):
                magic_generator = MagicGenerator(self.rect.x + 50, self.rect.y)
                # Use self.magic_generators to access the list defined in the Game class
                magic_generators.append(magic_generator)

    def draw(self, screen):
        # Draw the player character on screen
        pygame.draw.rect(screen, self.color, self.rect)

    def spend_christmas_magic(self, amount):
        if self.christmas_magic >= amount:
            self.christmas_magic -= amount
            return True
        else:
            return False

    def get_christmas_magic(self):
        return self.christmas_magic

