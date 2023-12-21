import pygame


class MagicGenerator:
    def __init__(self, x, y, width=30, height=30, magic_generated=1):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)  # Green color for the magic generator
        self.magic_generated = magic_generated
        self.last_generated_time = (
            pygame.time.get_ticks()
        )  # Record the time when the MagicGenerator was created

    def draw(self, screen):
        # Draw the magic generator on the screen
        pygame.draw.rect(screen, self.color, self.rect)

    def generate_magic(self):
        # Function to simulate magic generation (e.g., called when the player interacts with the magic generator)
        return self.magic_generated

    def can_generate_magic(self):
        # Check if enough time has elapsed since the last magic generation
        current_time = pygame.time.get_ticks()
        return (
            current_time - self.last_generated_time >= 5000
        )  # 5000 milliseconds = 5 seconds

    def update_last_generated_time(self):
        # Update the time when magic was last generated
        self.last_generated_time = pygame.time.get_ticks()

